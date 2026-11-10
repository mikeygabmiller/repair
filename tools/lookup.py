#!/usr/bin/env python3
"""Pull official, free vehicle data and write it as Markdown.

Sources (all U.S. government, no key needed):
  NHTSA recalls     https://api.nhtsa.gov/recalls/recallsByVehicle
  NHTSA complaints  https://api.nhtsa.gov/complaints/complaintsByVehicle
  NHTSA VIN decode  https://vpic.nhtsa.dot.gov/api/
  EPA vehicle data  https://www.fueleconomy.gov/ws/rest/

Usage:
  python3 tools/lookup.py refresh vehicles/2005-accord-ex-i4-at
  python3 tools/lookup.py vin <17-char VIN>
  python3 tools/lookup.py tsbs vehicles/2005-accord-ex-i4-at   (slow: ~75 MB download)

The tsbs command reads NHTSA's "Manufacturer Communications" flat files
(https://static.nhtsa.gov/odi/ffdd/tsbs/, field list in TSBS.txt there) and writes
tsbs.md: every Honda service bulletin NHTSA holds for this model and year. NHTSA only
stores a short summary of each bulletin; the bulletin's own text (the fix, the parts) is a
PDF on nhtsa.gov under the vehicle's "Manufacturer Communications" tab.
"""
import collections
import datetime
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "repair-kb"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def q(**params):
    return urllib.parse.urlencode(params)


def today():
    return datetime.date.today().isoformat()


def recalls(v):
    url = "https://api.nhtsa.gov/recalls/recallsByVehicle?" + q(
        make=v["make"], model=v["nhtsa_model"], modelYear=v["year"])
    rows = json.loads(get(url))["results"]
    rows.sort(key=lambda r: datetime.datetime.strptime(r["ReportReceivedDate"], "%d/%m/%Y"), reverse=True)
    out = [
        f"# Recalls: {v['year']} {v['make']} {v['nhtsa_model']}",
        "",
        f"Label: **OFFICIAL RECORD** (NHTSA). Pulled {today()} from <{url}>.",
        "",
        "These cover every {year} {model} variant (4-cyl, V6, coupe, hybrid). "
        "Whether a recall applies to *this* car, and whether it was already done, "
        "is only known by checking the VIN at <https://www.nhtsa.gov/recalls> "
        "(free). Open recalls are repaired free at a Honda dealer.".format(
            year=v["year"], model=v["nhtsa_model"]),
        "",
        f"Total campaigns: {len(rows)}",
        "",
    ]
    for r in rows:
        out += [
            f"## {r['NHTSACampaignNumber']}: {r['Component']}",
            "",
            f"- Reported: {r['ReportReceivedDate']}",
            f"- Park it: {'YES' if r.get('parkIt') else 'no'}",
            f"- Problem: {r['Summary'].strip()}",
            f"- Risk: {r['Consequence'].strip()}",
            f"- Fix: {r['Remedy'].strip()}",
            "",
        ]
    return "\n".join(out)


def complaints(v):
    url = "https://api.nhtsa.gov/complaints/complaintsByVehicle?" + q(
        make=v["make"], model=v["nhtsa_model"], modelYear=v["year"])
    rows = json.loads(get(url))["results"]
    # Names like "SERVICE BRAKES, HYDRAULIC" contain ", "; the list separator is a bare ",".
    by_comp = collections.defaultdict(list)
    for r in rows:
        for c in re.split(r",(?! )", r["components"]):
            by_comp[c.strip()].append(r)
    out = [
        f"# Owner complaints: {v['year']} {v['make']} {v['nhtsa_model']}",
        "",
        f"Label: **COMMUNITY** (owner reports filed with NHTSA, not checked by anyone). "
        f"Pulled {today()} from <{url}>.",
        "",
        "Use these to spot patterns (\"lots of people report X\"), never as a spec or a diagnosis.",
        "",
        f"Total complaints: {len(rows)}",
        "",
        "| Component | Complaints |",
        "|---|---|",
    ]
    ranked = sorted(by_comp.items(), key=lambda kv: -len(kv[1]))
    out += [f"| {c} | {len(rs)} |" for c, rs in ranked]
    out += ["", "Full text of every complaint, grouped by component: `complaints-all.md`.", ""]
    full = [f"# All owner complaints: {v['year']} {v['make']} {v['nhtsa_model']}", "",
            f"Label: **COMMUNITY**. Pulled {today()} from <{url}>. Newest first in each section.", ""]
    filed = lambda r: datetime.datetime.strptime(r["dateComplaintFiled"], "%m/%d/%Y")
    for c, rs in ranked:
        full += [f"## {c} ({len(rs)})", ""]
        for r in sorted(rs, key=filed, reverse=True):
            full.append(f"- **{r['odiNumber']}** ({r['dateComplaintFiled']}): {' '.join(r['summary'].split())}")
        full.append("")
    return "\n".join(out), "\n".join(full)


def epa(v):
    base = "https://www.fueleconomy.gov/ws/rest/vehicle/"
    menu = ET.fromstring(get(base + "menu/options?" + q(
        year=v["year"], make=v["make"], model=v["epa_model"])))
    match = [m for m in menu.iter("menuItem") if m.findtext("text") == v["epa_option"]]
    if not match:
        options = [m.findtext("text") for m in menu.iter("menuItem")]
        sys.exit(f"EPA option {v['epa_option']!r} not found. Options: {options}")
    vid = match[0].findtext("value")
    url = base + vid
    d = ET.fromstring(get(url))
    f = lambda k: d.findtext(k) or "—"
    return "\n".join([
        f"# EPA record: {v['year']} {v['make']} {v['epa_model']} ({v['epa_option']})",
        "",
        f"Label: **OFFICIAL RECORD** (U.S. EPA). Pulled {today()} from <{url}>.",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Engine | {f('cylinders')} cyl, {f('displ')} L |",
        f"| Transmission | {f('trany')} |",
        f"| Drive | {f('drive')} |",
        f"| Fuel | {f('fuelType1')} |",
        f"| MPG city / hwy / combined | {f('city08')} / {f('highway08')} / {f('comb08')} |",
        "",
    ])


def vin(code):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{code}?format=json"
    r = json.loads(get(url))["Results"][0]
    keys = ["ModelYear", "Make", "Model", "Trim", "Series", "BodyClass", "DisplacementL",
            "EngineCylinders", "EngineModel", "EngineHP", "TransmissionStyle",
            "TransmissionSpeeds", "DriveType", "PlantCity", "PlantCountry", "ErrorText"]
    lines = [f"VIN decode (NHTSA vPIC, OFFICIAL RECORD, {today()}): {url}"]
    lines += [f"  {k}: {r.get(k) or '—'}" for k in keys]
    return "\n".join(lines)


TSB_RANGES = ["1995-1999", "2000-2004", "2005-2009", "2010-2014", "2015-2019",
              "2020-2024", "2025-2025", "2025-2029", "2026-2026"]


def tsb_rows(v):
    """Yield one dict per bulletin (rows for the same NHTSA ID merged)."""
    import io
    import zipfile
    make, model, year = v["make"].upper(), v["nhtsa_model"].upper(), str(v["year"])
    found = {}
    for rng in TSB_RANGES:
        url = f"https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS_RECEIVED_{rng}.zip"
        try:
            blob = get(url)
        except Exception:
            continue  # NHTSA renames the newest file from time to time
        with zipfile.ZipFile(io.BytesIO(blob)) as z:
            for name in z.namelist():
                with z.open(name) as fh:
                    for raw in fh:
                        line = raw.decode("latin-1")
                        if make not in line:
                            continue
                        f = line.rstrip("\r\n").split("\t")
                        if len(f) < 14 or f[7] != make or f[9] != year:
                            continue
                        if f[8] != model:  # skips e.g. ACCORD HYBRID
                            continue
                        r = found.setdefault(f[0], {
                            "id": f[0], "doc": f[3].strip(), "date": f[4], "added": f[2],
                            "type": f[6], "components": set(), "summary": " ".join(f[13].split())})
                        r["components"].update(c.strip() for c in f[10].split(",") if c.strip())
    return sorted(found.values(), key=lambda r: (r["date"], r["id"]), reverse=True)


def tsbs(v):
    rows = tsb_rows(v)
    d = lambda s: f"{s[:4]}-{s[4:6]}-{s[6:]}" if len(s) == 8 and s.isdigit() else (s or "—")
    out = [
        f"# Honda service bulletins on file at NHTSA: {v['year']} {v['make']} {v['nhtsa_model']}",
        "",
        f"Label: **OFFICIAL RECORD** (NHTSA Manufacturer Communications flat files, "
        f"<https://static.nhtsa.gov/odi/ffdd/tsbs/>). Pulled {today()} by `tools/lookup.py tsbs`.",
        "",
        "What this is: NHTSA's one-line summary of every communication Honda filed that names the "
        f"{v['year']} {v['nhtsa_model']} (all engines, sedan and coupe; hybrid rows are left out). "
        "**The summary is NHTSA's, not the bulletin's text.** It tells you a bulletin exists and what "
        "it is about; the actual fix, part numbers and VIN ranges are only in the bulletin PDF, free "
        "on nhtsa.gov: search the car, open \"Manufacturer Communications\", find the NHTSA ID. "
        "Many bulletins are V6-, coupe- or other-year-only even though NHTSA lists them here.",
        "",
        "Hand-sorted reading of these for this car (what applies to the 2.4 L automatic sedan, by "
        "symptom): `tsb-guide.md`.",
        "",
        f"Total bulletins: {len(rows)}",
        "",
        "| Bulletin date | Honda doc ID | NHTSA ID | NHTSA component | NHTSA summary |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        comp = "; ".join(sorted(r["components"])).replace("|", "/")
        summ = re.sub(r"\s*\*\w+\s*$", "", r["summary"]).replace("|", "/")
        out.append(f"| {d(r['date'])} | {r['doc'] or '—'} | {r['id']} | {comp} | {summ} |")
    out.append("")
    return "\n".join(out)


def refresh(folder):
    folder = Path(folder)
    v = json.loads((folder / "vehicle.json").read_text())
    (folder / "recalls.md").write_text(recalls(v))
    summary, full = complaints(v)
    (folder / "complaints.md").write_text(summary)
    (folder / "complaints-all.md").write_text(full)
    (folder / "epa.md").write_text(epa(v))
    print(f"Wrote recalls.md, complaints.md, complaints-all.md, epa.md in {folder}")
    if v.get("vin"):
        print(vin(v["vin"]))


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "refresh":
        refresh(sys.argv[2])
    elif len(sys.argv) == 3 and sys.argv[1] == "tsbs":
        folder = Path(sys.argv[2])
        (folder / "tsbs.md").write_text(tsbs(json.loads((folder / "vehicle.json").read_text())))
        print(f"Wrote tsbs.md in {folder}")
    elif len(sys.argv) == 3 and sys.argv[1] == "vin":
        print(vin(sys.argv[2]))
    else:
        sys.exit(__doc__)
