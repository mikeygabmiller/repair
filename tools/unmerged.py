#!/usr/bin/env python3
"""List branches holding repo notes that never reached main.

Each Claude chat saves its notes on its own branch. A new chat only sees main, so a
branch that was never merged means notes the next chat can't see. Claude runs this at
the start of every chat (CLAUDE.md); it can also be run by hand:

  python3 tools/unmerged.py

A branch is skipped when git counts it as merged, when it's listed in
tools/folded-branches.txt (reviewed and folded in by hand), or when every line it adds is
already on main (squash-merged). Never fails: any error just prints nothing.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git(*args, timeout=30):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          timeout=timeout).stdout


def main():
    try:
        git("fetch", "--quiet", "origin", timeout=20)
    except subprocess.TimeoutExpired:
        pass
    current = git("rev-parse", "--abbrev-ref", "HEAD").strip()
    folded = set()
    listed = ROOT / "tools" / "folded-branches.txt"
    if listed.exists():
        folded = {l.strip() for l in listed.read_text().splitlines()
                  if l.strip() and not l.startswith("#")}
    branches = [b.strip() for b in git("branch", "-r", "--no-merged", "origin/main").splitlines()]
    branches = [b for b in branches if b and "->" not in b and b != f"origin/{current}"
                and b.removeprefix("origin/") not in folded]
    if not branches:
        print("No unmerged repo notes.")
        return
    main_text = git("grep", "-h", "-I", "-e", "", "origin/main")
    found = []
    for b in branches:
        added = [l[1:].strip() for l in git("diff", f"origin/main...{b}").splitlines()
                 if l.startswith("+") and not l.startswith("+++")]
        missing = [l for l in added if len(l) >= 25 and l not in main_text]
        if missing:
            date, subject = git("log", "-1", "--format=%cd%x09%s", "--date=short", b).strip().split("\t", 1)
            found.append(f"- {b} ({date}, {len(missing)} lines not on main): {subject}")
    if not found:
        print("No unmerged repo notes.")
        return
    print("UNMERGED REPO NOTES: these branches hold notes that are not on main, so this "
          "chat can't see them unless they're folded in:")
    print("\n".join(found))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
