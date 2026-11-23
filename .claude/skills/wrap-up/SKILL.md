---
name: wrap-up
description: End-of-chat routine for the repair repo - check, commit, push, open PR, mark ready, merge into main with a merge commit, republish the checklists artifact if needed. Use at the end of any chat that changed repo files (owner's standing rule, no need to ask).
---

# Wrap up the chat

Owner's standing rule (CLAUDE.md, 2026-10-31): when a chat changed repo files, merge them
into `main` automatically. Don't ask first. Repo: `mikeygabmiller/repair`.

## 1. Check
```bash
python3 tools/check.py
python3 tools/checklists.py --check
python3 tools/due.py roadmap --check
```
- Fix every **ERROR** (broken link, unknown complaint number).
- Read every **WARN**: fix it, or be ready to say in one line why it's fine.
- `checklists.py --check` fails → run `python3 tools/checklists.py`.
- `roadmap --check` fails → run `python3 tools/due.py roadmap --write`.

## 2. Re-read the diff
`git diff origin/main...HEAD` and `git status`. Look for: a number with no source label,
a spec that disagrees with `specs.md`, personal details where they don't belong, stray
scratch files. Commit nothing with secrets.

## 3. Commit and push
- Message says what was learned or changed ("Add oil capacity from owner's manual p.215"),
  ending with the attribution lines the session gives.
- `git push -u origin <branch>`; retry network errors up to 4 times with backoff.
- Push rejected → `git fetch origin <branch> && git merge --no-edit FETCH_HEAD`, push again.

## 4. PR → ready → merge
With the GitHub MCP tools:
1. `create_pull_request` (draft) unless one is already open for this branch. Body: what
   changed and why, check.py result, ending with the session's PR attribution lines.
2. `update_pull_request` with `draft: false`.
3. `merge_pull_request` with `merge_method: "merge"` (**not squash**, so git sees the
   branch as merged and `tools/unmerged.py` stays quiet).

Conflict with `main` → merge `main` into the branch and resolve. **Stop and ask the
owner** if the merge is blocked or resolving would mean choosing between two different
facts (CLAUDE.md: conflicting sources, show both).

## 5. Republish the checklists page (only if procedures changed)
If any of `procedures/*.md`, `procedures/README.md` or `V/schedule.csv` changed:
`python3 tools/checklists.py`, then republish with the Artifact tool:
file `procedures/checklists.html`, url `https://claude.ai/artifact/4aED2sm2MyWmr8QqBR8YgL`.

## 6. Tell the owner
One line: what merged, with the PR link (`[mikeygabmiller/repair#N](url)`).
