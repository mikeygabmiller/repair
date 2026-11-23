#!/usr/bin/env python3
"""Stop hook: don't let a chat end with broken notes or notes that never reach main.

When Claude is about to finish a turn:
  - tools/check.py has any ERROR  -> Claude must fix it first;
  - repo files changed but aren't on origin/main -> Claude is reminded of the owner's
    standing rule (CLAUDE.md: commit, PR, merge at the end of every chat; /wrap-up).
It blocks at most once per turn (stop_hook_active), so Claude can still stop to ask the
owner a question, e.g. for the odometer reading, mid-job.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def sh(*args, timeout=30):
    try:
        return subprocess.run(list(args), cwd=ROOT, capture_output=True, text=True,
                              errors="replace", timeout=timeout).stdout
    except Exception:
        return ""


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    if data.get("stop_hook_active"):
        return

    reasons = []
    errors = [l for l in sh(sys.executable, "tools/check.py", timeout=60).splitlines()
              if l.startswith("ERROR")]
    if errors:
        reasons.append("tools/check.py has ERRORs; fix them:\n" + "\n".join(errors))

    dirty = [l for l in sh("git", "status", "--porcelain").splitlines()
             if "__pycache__" not in l]
    sh("git", "fetch", "--quiet", "origin", "main", timeout=15)
    ahead = sh("git", "rev-list", "--count", "origin/main..HEAD").strip()
    if dirty or (ahead.isdigit() and int(ahead) > 0):
        what = []
        if dirty:
            what.append(f"{len(dirty)} uncommitted file(s)")
        if ahead.isdigit() and int(ahead) > 0:
            what.append(f"{ahead} commit(s) not on main")
        reasons.append(
            "Repo changes are not on main yet (" + ", ".join(what) + "). Owner's standing rule: "
            "follow the /wrap-up skill (check, commit, PR, ready, merge-commit) now. "
            "If you're stopping to wait for the owner's answer mid-job, say so and stop.")

    if reasons:
        print(json.dumps({"decision": "block", "reason": "\n\n".join(reasons)}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # a broken guard must never trap the chat
