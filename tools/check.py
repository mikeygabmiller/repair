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

    if not quiet:
        for e in errors:
            print("ERROR", e)
        for w in warns:
            print("WARN ", w)
    print(f"check.py: {len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
