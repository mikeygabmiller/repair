#!/usr/bin/env python3
"""What's due, what the car has cost, and the scheduled work between here and 500,000 mi.

  python3 tools/due.py                      # what's due now + cost so far
  python3 tools/due.py --odo 141250         # same, at a given odometer reading
  python3 tools/due.py --date 2027-03-01    # same, on a given date
  python3 tools/due.py roadmap              # print the scheduled-work table to 500k
  python3 tools/due.py roadmap --write      # rewrite that table inside plans/roadmap-500k.md
  python3 tools/due.py roadmap --check      # exit 1 if the table in the file is out of date

Reads two files in the vehicle folder:
  schedule.csv   Honda's severe schedule (owner's manual p.203), one row per item
  ledger.csv     one row per job, purchase or inspection: date, odometer, kind, item, cost

A `maintenance` row in ledger.csv whose `item` matches a schedule.csv `key` counts as that
item being done. The narrative for every job stays in log.md; the ledger is the part a
script can add up. This tool does arithmetic only: every interval comes from schedule.csv
(which cites its source) and every cost from ledger.csv.
"""
import csv
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = 500_000
BAND = 30_000
SOON_MILES = 1_000
SOON_DAYS = 30
START = "<!-- roadmap:start"
END = "<!-- roadmap:end -->"
# Roadmap table columns: schedule key -> short heading
COLS = [("oil", "Oil"), ("oil-filter", "Oil filter"), ("tire-rotation", "Tire rotation"),
        ("air-filter", "Air filter"), ("cabin-filter", "Cabin filter"), ("atf", "ATF"),
        ("brake-fluid", "Brake fluid"), ("coolant", "Coolant"), ("spark-plugs", "Spark plugs")]


def car_dir(arg=None):
    if arg:
        return (ROOT / arg) if not Path(arg).is_absolute() else Path(arg)
    cars = [p for p in (ROOT / "vehicles").iterdir() if p.is_dir()]
    if len(cars) != 1:
        sys.exit("More than one vehicle folder: name one, e.g. tools/due.py vehicles/<car>")
    return cars[0]


def parse_date(s):
    s = s.strip()
    if re.fullmatch(r"\d{4}-\d{2}", s):  # month only: call it mid-month
        s += "-15"
    return dt.date.fromisoformat(s)


def num(s):
    s = (s or "").strip().replace(",", "")
    return float(s) if s else None


def add_months(d, months):
    y, m = divmod(d.month - 1 + int(months), 12)
    y += d.year
    m += 1
    last = [31, 29 if y % 4 == 0 and (y % 100 or y % 400 == 0) else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
    return dt.date(y, m, min(d.day, last))


def load(car):
    with open(car / "schedule.csv", newline="") as f:
        sched = list(csv.DictReader(f))
    for r in sched:
        for k in ("first_miles", "first_months", "every_miles", "every_months", "parts_cost"):
            r[k] = num(r[k])
    with open(car / "ledger.csv", newline="") as f:
        ledger = list(csv.DictReader(f))
    for r in ledger:
        r["when"] = parse_date(r["date"])
        r["odo"] = num(r["odometer"])
        r["usd"] = num(r["cost"])
    ledger.sort(key=lambda r: r["when"])
    return sched, ledger


def last_done(ledger):
    last = {}
    for r in ledger:  # sorted oldest first, so the newest wins
        if r["kind"] == "maintenance":
            last[r["item"]] = r
    return last


def as_of(ledger):
    """Newest odometer reading in the ledger and the date it was read."""
    rows = [r for r in ledger if r["odo"] is not None]
    newest = max(rows, key=lambda r: (r["odo"], r["when"]))
    return int(newest["odo"]), newest["when"]


def fmt_mi(n):
    return f"{int(round(n)):,} mi"


def due_rows(sched, ledger, odo, today):
    last = last_done(ledger)
    out = []
    for s in sched:
        done = last.get(s["key"])
        next_mi = next_date = None
        note = ""
        if done:
            last_txt = done["date"] + (f", {fmt_mi(done['odo'])}" if done["odo"] is not None
                                       else ", odometer not recorded")
            if s["every_miles"] is None and s["every_months"] is None:
                out.append(("OK", s, last_txt, "No repeat interval (" + s["source"] + ")"))
                continue
            if s["every_miles"] is not None:
                if done["odo"] is not None:
                    next_mi = done["odo"] + s["every_miles"]
                else:
                    note = " (miles unknown: last odometer not recorded)"
            if s["every_months"] is not None:
                next_date = add_months(done["when"], s["every_months"])
        else:
            last_txt = "No record"
            first_mi = s["first_miles"] if s["first_miles"] is not None else s["every_miles"]
            if s["first_months"] is not None or s["every_months"] is not None:
                # A 2005 car is past every time limit in the schedule, so with no dated
                # record the item is due (specs.md, maintenance schedule note).
                out.append(("DUE", s, last_txt, "Now (no record; past the time limit)"))
                continue
            next_mi = first_mi
        over = (next_mi is not None and odo >= next_mi) or (next_date and today >= next_date)
        soon = ((next_mi is not None and odo >= next_mi - SOON_MILES)
                or (next_date and today >= next_date - dt.timedelta(days=SOON_DAYS)))
        status = "DUE" if over else "SOON" if soon else "OK"
        bits = []
        if next_mi is not None:
            bits.append(fmt_mi(next_mi))
        if next_date:
            bits.append(next_date.strftime("%Y-%m"))
        when = " or ".join(bits) + (", whichever comes first" if len(bits) == 2 else "") + note
        if status == "DUE":
            when = "Now (was due " + when + ")" if done else "Now (no record; past " + when + ")"
        out.append((status, s, last_txt, when))
    order = {"DUE": 0, "SOON": 1, "OK": 2}
    out.sort(key=lambda r: order[r[0]])
    return out


def print_due(sched, ledger, odo, today):
    print(f"What's due at {fmt_mi(odo)} on {today}  (severe schedule, schedule.csv)\n")
    rows = due_rows(sched, ledger, odo, today)
    for status, s, last_txt, when in rows:
        print(f"  {status:<5} {s['item']}")
        print(f"        last: {last_txt}")
        print(f"        next: {when}")
        print(f"        how:  {s['procedure']}")
    n = sum(1 for r in rows if r[0] == "DUE")
    print(f"\n  {n} due now, {sum(1 for r in rows if r[0] == 'SOON')} due soon "
          f"(within {SOON_MILES:,} mi or {SOON_DAYS} days), "
          f"{sum(1 for r in rows if r[0] == 'OK')} not yet due.")


def print_costs(ledger, odo):
    print("\nCost so far (ledger.csv)\n")
    kinds = ["maintenance", "repair", "mod", "tool", "inspection"]
    total = {k: 0.0 for k in kinds}
    blank = {k: [] for k in kinds}
    for r in ledger:
        if r["kind"] not in total:
            continue
        if r["usd"] is None:
            blank[r["kind"]].append(r)
        else:
            total[r["kind"]] += r["usd"]
    for k in kinds:
        n = sum(1 for r in ledger if r["kind"] == k)
        if n:
            miss = f"  + {len(blank[k])} with no cost recorded" if blank[k] else ""
            print(f"  {k:<12} ${total[k]:>9,.2f}  ({n} row{'s' if n != 1 else ''}){miss}")
    buy = next((r for r in ledger if r["kind"] == "purchase" and r["odo"] is not None), None)
    if not buy:
        print("\n  No purchase row with an odometer reading: cost per mile can't be worked out.")
        return
    miles = odo - buy["odo"]
    running = total["maintenance"] + total["repair"]
    print(f"\n  Miles since purchase: {miles:,.0f}  ({fmt_mi(buy['odo'])} on {buy['date']} "
          f"to {fmt_mi(odo)})")
    if buy["note"]:
        print(f"    purchase row note: {buy['note']}")
    if miles > 0:
        print(f"  Keeping it running (maintenance + repair): ${running:,.2f} "
              f"= ${running / miles:.2f} per mile")
        allin = running + total["mod"]
        print(f"  With mods:                                 ${allin:,.2f} "
              f"= ${allin / miles:.2f} per mile")
    missing = [r for k in kinds for r in blank[k]]
    if missing:
        print(f"\n  These are floors, not totals: {len(missing)} rows have no cost. Fill them in "
              "ledger.csv:")
        for r in missing:
            print(f"    {r['date']}  {r['what']}")
    print("  Not counted: fuel, insurance, registration, tires, the purchase price, and "
          "tools\n  (tools outlive the car: see mods/tools-owned.md).")


def simulate(sched, ledger, rate):
    """Scheduled services from the newest odometer reading to TARGET, at `rate` mi/yr.

    Each item repeats at whichever comes first: its mileage interval, or its time interval
    turned into miles at `rate`. It starts from its last recorded service; with no usable
    record it's due now, so it starts from the current odometer. An item with no time limit
    that isn't due yet (idle speed) starts from zero.
    """
    odo, when = as_of(ledger)
    last = last_done(ledger)
    events = {}
    for s in sched:
        steps = []
        if s["every_miles"] is not None:
            steps.append(s["every_miles"])
        if s["every_months"] is not None:
            steps.append(s["every_months"] / 12 * rate)
        if not steps:
            continue
        step = min(steps)
        done = last.get(s["key"])
        if done and done["odo"] is not None:
            base = done["odo"]
        elif done:  # done, odometer not recorded: place it by date
            base = odo - (when - done["when"]).days / 365.25 * rate
        elif s["every_months"] is None and s["first_months"] is None and odo < step:
            base = 0
        else:
            base = odo - step  # no record: due now
        at, hits = base + step, []
        while at <= TARGET:
            hits.append(max(at, odo))
            at += step
        events[s["key"]] = hits
    return odo, when, events


def roadmap_table(sched, ledger, rate):
    odo, when, events = simulate(sched, ledger, rate)
    by_key = {s["key"]: s for s in sched}
    edges = [odo] + [e for e in range(170_000, TARGET + 1, BAND) if e > odo]
    year0 = when.year + (when.timetuple().tm_yday - 1) / 365.25
    lines = [f"{START} miles-per-year={int(rate)} -->",
             f"Generated by `tools/due.py roadmap --write` from `schedule.csv` and `ledger.csv`. "
             f"Starts at {odo:,} mi ({when}), at {int(rate):,} mi a year. Don't edit by hand.",
             "",
             "| Miles | Years (about) | " + " | ".join(h for _, h in COLS)
             + " | Parts at today's prices |",
             "|---|---|" + "---|" * (len(COLS) + 1)]
    tot = {k: 0 for k, _ in COLS}
    tot_cost = 0.0
    for lo, hi in zip(edges, edges[1:]):
        first = lo == odo
        counts, cost = [], 0.0
        for key, _ in COLS:
            n = sum(1 for e in events.get(key, []) if (lo <= e <= hi if first else lo < e <= hi))
            tot[key] += n
            counts.append(str(n) if n else "–")
            cost += n * (by_key[key]["parts_cost"] or 0)
        tot_cost += cost
        y1, y2 = year0 + (lo - odo) / rate, year0 + (hi - odo) / rate
        lines.append(f"| {lo:,}–{hi:,} | {int(y1)}–{int(y2)} | " + " | ".join(counts)
                     + f" | ${cost:,.0f} |")
    lines.append("| **Total** | | " + " | ".join(f"**{tot[k]}**" for k, _ in COLS)
                 + f" | **${tot_cost:,.0f}** |")
    lines.append("")
    one_off = []
    for key in ("idle-speed",):
        for e in events.get(key, []):
            one_off.append(f"{by_key[key]['item']} at {fmt_mi(e)} "
                           f"(about {int(year0 + (e - odo) / rate)})")
    if one_off:
        lines.append("Also on the schedule: " + "; ".join(one_off) + ".")
    priced = [f"{h.lower()} ${by_key[k]['parts_cost']:.2f} ({by_key[k]['parts_cost_source']})"
              for k, h in COLS if by_key[k]["parts_cost"]]
    lines.append("")
    lines.append("What the parts column counts, per service: " + "; ".join(priced) + ". "
                 "Tire rotation, brake fluid and coolant have no price on file, so they add $0 "
                 "here.")
    lines.append(END)
    return "\n".join(lines)


def roadmap(car, argv):
    sched, ledger = load(car)
    path = car / "plans" / "roadmap-500k.md"
    text = path.read_text() if path.exists() else ""
    rate = None
    if "--miles-per-year" in argv:
        rate = float(argv[argv.index("--miles-per-year") + 1])
    else:
        m = re.search(re.escape(START) + r" miles-per-year=(\d+)", text)
        rate = float(m.group(1)) if m else 11_000.0
    table = roadmap_table(sched, ledger, rate)
    if "--write" in argv or "--check" in argv:
        if START not in text or END not in text:
            sys.exit(f"{path.relative_to(ROOT)} has no roadmap markers")
        a, b = text.index(START), text.index(END) + len(END)
        if "--check" in argv:
            if text[a:b] != table:
                print(f"{path.relative_to(ROOT)}: scheduled-work table is out of date. "
                      "Run: python3 tools/due.py roadmap --write")
                sys.exit(1)
            return
        path.write_text(text[:a] + table + text[b:])
        print(f"Wrote the table into {path.relative_to(ROOT)}")
    else:
        print(table)


def roadmap_stale(car=None):
    """For tools/check.py: True if the table in roadmap-500k.md no longer matches the data."""
    car = car or car_dir()
    path = car / "plans" / "roadmap-500k.md"
    if not path.exists():
        return False
    text = path.read_text()
    m = re.search(re.escape(START) + r" miles-per-year=(\d+)", text)
    if not m or END not in text:
        return True
    sched, ledger = load(car)
    a, b = text.index(START), text.index(END) + len(END)
    return text[a:b] != roadmap_table(sched, ledger, float(m.group(1)))


def main():
    argv = sys.argv[1:]
    if "-h" in argv or "--help" in argv:
        print(__doc__)
        return
    flags_with_value = {"--odo", "--date", "--miles-per-year"}
    pos, skip = [], False
    for i, a in enumerate(argv):
        if skip:
            skip = False
        elif a in flags_with_value:
            skip = True
        elif not a.startswith("--"):
            pos.append(a)
    if pos and pos[0] == "roadmap":
        roadmap(car_dir(pos[1] if len(pos) > 1 else None), argv)
        return
    car = car_dir(pos[0] if pos else None)
    sched, ledger = load(car)
    odo, _ = as_of(ledger)
    if "--odo" in argv:
        odo = int(num(argv[argv.index("--odo") + 1]))
    today = dt.date.today()
    if "--date" in argv:
        today = parse_date(argv[argv.index("--date") + 1])
    print_due(sched, ledger, odo, today)
    print_costs(ledger, odo)


if __name__ == "__main__":
    main()
