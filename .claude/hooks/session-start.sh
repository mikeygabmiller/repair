#!/bin/bash
# Start-of-chat check (CLAUDE.md "Start and end of every chat").
# Runs tools/unmerged.py so Claude sees stranded notes before it answers, instead of
# relying on Claude to remember. Stdout from a SessionStart hook goes into Claude's context.
# Skipped on resume/compact: the chat already ran it when it started.
set -uo pipefail
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

source=$(python3 -c 'import json,sys
try: print(json.load(sys.stdin).get("source",""))
except Exception: print("")' 2>/dev/null)
case "$source" in resume|compact) exit 0 ;; esac

echo "Start-of-chat check, tools/unmerged.py (run by the session-start hook):"
timeout 60 python3 tools/unmerged.py || echo "WARNING: tools/unmerged.py did not finish. Run it by hand."
exit 0
