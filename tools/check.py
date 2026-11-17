#!/usr/bin/env python3
"""Catch drift in the repair notes before it reaches an answer.

  python3 tools/check.py            # all checks, exit 1 if any ERROR
  python3 tools/check.py --quiet    # only the summary line

Checks (each finding is ERROR or WARN):
  links     ERROR  a `path.md` (or .py/.txt/.json/.pdf) named in backticks that doesn't exist
  torque    WARN   an lbf·ft value in procedures/ or plans/ that specs.md doesn't contain
  labels    WARN   a line in procedures/ with a torque, pressure or capacity number but no
                   source label (VERIFIED, OM p., Chilton, COMMUNITY, UNVERIFIED, TENTATIVE,
                   specs.md, NOT FOUND, estimate)
  partnos   WARN   a Honda part number (12345-ABC-A01 form) outside parts.md that parts.md
                   doesn't list
  odi       ERROR  an NHTSA complaint/communication number (10xxxxxx / 11xxxxxx) cited
                   that isn't in complaints-all.md or tsbs.md
  ledger    WARN   a log.md job dated 2026-11-17 or later with no ledger.csv row that day, or a
                   ledger.csv item kind/key the tools don't know
  odometer  WARN   maintenance.md's "Last known odometer" is behind the newest ledger.csv reading
  generated WARN   procedures/checklists.html or the roadmap table is out of date
  size      WARN   a tracked file over 5 MB (big files bloat every clone, and stay in history)

Run it after editing notes and before merging (CLAUDE.md, "Keeping the repo current").
It can't tell whether a number is *right*, only whether it drifted from specs.md or lost
its label.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAR = ROOT / "vehicles" / "2005-accord-ex-i4-at"
SKIP_DIRS = {".git", "switch-slot-ideas"}  # research dump with its own link style
SKIP_FILES = {"complaints-all.md", "recalls.md", "tsbs.md"}  # generated

LABEL = re.compile(r"VERIFIED|OFFICIAL RECORD|OM p|OM pp|Chilton|COMMUNITY|UNVERIFIED|"
                   r"TENTATIVE|specs\.md|NOT FOUND|not found|estimate|DRAFT|parts\.md|"
                   r"Not found|owner|Owner", re.I)
NUM_UNIT = re.compile(r"\b\d+(?:\.\d+)?\s*(?:lbf·ft|lb-ft|ft\. lbs|N·m|psi|US qt|qt\b|US gal)")
TORQUE = re.compile(r"\b(\d+(?:\.\d+)?)\s*(?:lbf·ft|lb-ft)")
PARTNO = re.compile(r"\b\d{5}-[A-Z0-9]{3}-[A-Z0-9]{3,4}\b")
ODI = re.compile(r"\b1[01]\d{6}\b")
BACKTICK = re.compile(r"`([^`\s]+\.(?:md|py|txt|json|pdf|html))`")


def md_files():
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def resolve(ref, src):
    ref = ref.split("#")[0]
    if ref.startswith("V/"):  # INDEX.md shorthand for the vehicle folder
        ref = str(CAR.relative_to(ROOT) / ref[2:])
    if "<" in ref or "*" in ref or ref.startswith("YYYY"):
        return True  # template placeholder
    bases = [src.parent, ROOT, CAR, ROOT / "procedures", ROOT / "mods", ROOT / "sources",
             ROOT / "tools", ROOT / "prompts", CAR / "plans",
             ROOT / "mods" / "switch-slot-ideas"]
    return any((b / ref).exists() for b in bases)


def main():
    quiet = "--quiet" in sys.argv
    errors, warns = [], []
    specs = (CAR / "specs.md").read_text()
    spec_torques = set(TORQUE.findall(specs))
    parts = (CAR / "parts.md").read_text()
    odi_known = set(ODI.findall((CAR / "complaints-all.md").read_text()))
    if (CAR / "tsbs.md").exists():
        odi_known |= set(ODI.findall((CAR / "tsbs.md").read_text()))

    for f in md_files():
        rel = f.relative_to(ROOT)
        text = f.read_text(errors="replace")
        lines = text.splitlines()
        generated = f.name in SKIP_FILES
        in_proc = rel.parts[0] == "procedures" or "plans" in rel.parts
        for n, line in enumerate(lines, 1):
            where = f"{rel}:{n}"
            if not generated:
                for ref in BACKTICK.findall(line):
                    if not resolve(ref, f):
                        errors.append(f"links   {where}: `{ref}` not found")
                for odi in ODI.findall(line):
                    if odi not in odi_known and "VIN" not in line:
                        errors.append(f"odi     {where}: {odi} not in complaints-all.md or tsbs.md")
            if in_proc:
                for t in TORQUE.findall(line):
                    if t not in spec_torques:
                        warns.append(f"torque  {where}: {t} lbf·ft not in specs.md")
                if NUM_UNIT.search(line) and not LABEL.search(line):
                    # look one line up and down for the label (tables wrap)
                    ctx = " ".join(lines[max(0, n - 2):n + 1])
                    if not LABEL.search(ctx):
                        warns.append(f"labels  {where}: number without a source label")
            if f.name != "parts.md" and not generated:
                for pn in PARTNO.findall(line):
                    if pn not in parts:
                        warns.append(f"partnos {where}: {pn} not in parts.md")

    warns += extra_checks()

    if not quiet:
        for e in errors:
            print("ERROR", e)
        for w in warns:
            print("WARN ", w)
    print(f"check.py: {len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


def extra_checks():
    import csv
    import subprocess
    sys.path.insert(0, str(ROOT / "tools"))
    out = []
    with open(CAR / "ledger.csv", newline="") as fh:
        ledger = list(csv.DictReader(fh))
    with open(CAR / "schedule.csv", newline="") as fh:
        keys = {r["key"] for r in csv.DictReader(fh)}
    kinds = {"purchase", "maintenance", "repair", "mod", "tool", "inspection"}
    dates = {r["date"] for r in ledger}
    for n, r in enumerate(ledger, 2):
        if r["kind"] not in kinds:
            out.append(f"ledger  ledger.csv:{n}: kind '{r['kind']}' not one of {sorted(kinds)}")
        if r["kind"] == "maintenance" and r["item"] not in keys:
            out.append(f"ledger  ledger.csv:{n}: maintenance item '{r['item']}' not a schedule.csv key")
    log = (CAR / "log.md").read_text().splitlines()
    for n, line in enumerate(log, 1):
        m = re.match(r"## (?:~|Reported )?(\d{4}-\d{2}-\d{2})\b", line)
        # Older entries were back-filled by hand when the ledger started; symptom reports
        # and lookups aren't jobs, so they don't need a row.
        if (m and m.group(1) >= "2026-11-17" and m.group(1) not in dates
                and not re.search(r"report|symptom|lookup|no work on the car", line, re.I)):
            out.append(f"ledger  log.md:{n}: {m.group(1)} entry has no ledger.csv row "
                       "(add one, with the cost if known)")
    odos = [float(r["odometer"]) for r in ledger if r["odometer"].strip()]
    m = re.search(r"Last known odometer: \*\*([\d,]+) mi", (CAR / "maintenance.md").read_text())
    if odos and m and float(m.group(1).replace(",", "")) < max(odos):
        out.append(f"odometer maintenance.md: last known odometer {m.group(1)} is behind "
                   f"ledger.csv ({max(odos):,.0f})")
    import checklists
    if not checklists.OUT.exists() or checklists.OUT.read_text() != checklists.build():
        out.append("generated procedures/checklists.html is stale: run python3 tools/checklists.py")
    import due
    if due.roadmap_stale(CAR):
        out.append("generated plans/roadmap-500k.md table is stale: run python3 tools/due.py roadmap --write")
    try:
        files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    except OSError:
        files = []
    for f in files:
        p = ROOT / f
        if p.exists() and p.stat().st_size > 5_000_000:
            out.append(f"size    {f}: {p.stat().st_size / 1e6:.0f} MB tracked file")
    return out


if __name__ == "__main__":
    main()
