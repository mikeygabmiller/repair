#!/usr/bin/env python3
"""PostToolUse hook: keep the notes honest the moment Claude edits them.

After an Edit/Write to a repo notes file:
  - runs tools/check.py and shows Claude every ERROR, plus any WARN on the edited file;
  - procedure, procedures/README.md or schedule.csv edited: regenerates
    procedures/checklists.html (tools/checklists.py) and reminds Claude to republish it;
  - ledger.csv or schedule.csv edited: rewrites the 500k roadmap table
    (tools/due.py roadmap --write).
Edits made through Bash (sed, heredocs) don't trigger this; the Stop hook still runs
check.py before Claude finishes.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WATCHED = ("vehicles/", "procedures/", "mods/", "INDEX.md", "CLAUDE.md", "README.md")


def run(*args):
    r = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True,
                       errors="replace", timeout=60)
    return r.returncode, (r.stdout + r.stderr).strip()


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    path = (data.get("tool_input") or {}).get("file_path") or ""
    if not path:
        return
    try:
        rel = Path(path).resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return  # outside the repo (scratchpad etc.)
    if not rel.startswith(WATCHED):
        return

    problems, notes = [], []

    _, out = run("tools/check.py")
    for line in out.splitlines():
        if line.startswith("ERROR") or (line.startswith("WARN") and f" {rel}:" in line):
            problems.append(line)

    if (rel.startswith("procedures/") and rel.endswith(".md")) or rel.endswith("schedule.csv"):
        page = ROOT / "procedures" / "checklists.html"
        before = page.read_bytes() if page.exists() else b""
        code, out = run("tools/checklists.py")
        if code != 0:
            notes.append(f"tools/checklists.py FAILED:\n{out}")
        elif page.read_bytes() != before:
            notes.append("procedures/checklists.html regenerated (tools/checklists.py). Republish "
                         "the 'Accord Garage Checklists' artifact before the chat ends (/wrap-up step 5).")

    if rel.endswith(("ledger.csv", "schedule.csv")):
        roadmap = ROOT / "vehicles" / "2005-accord-ex-i4-at" / "plans" / "roadmap-500k.md"
        before = roadmap.read_bytes() if roadmap.exists() else b""
        code, out = run("tools/due.py", "roadmap", "--write")
        if code != 0:
            notes.append(f"tools/due.py roadmap --write FAILED:\n{out}")
        elif roadmap.exists() and roadmap.read_bytes() != before:
            notes.append("plans/roadmap-500k.md table rewritten (tools/due.py roadmap --write).")

    if problems:
        reason = (f"tools/check.py after editing {rel}:\n" + "\n".join(problems)
                  + "\nFix every ERROR. For each WARN on this file, fix it or say why it's fine.")
        if notes:
            reason += "\n" + "\n".join(notes)
        print(json.dumps({"decision": "block", "reason": reason}))
    elif notes:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                                 "additionalContext": "\n".join(notes)}}))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # never break an edit; just say so
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
              "additionalContext": f"after-edit hook failed ({e}); run tools/check.py by hand."}}))
