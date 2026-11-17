# Repair

A private, source-checked car repair knowledge base. Connect it to Claude and ask repair
questions: Claude checks this repo and official free sources first and labels every fact
(VERIFIED, OFFICIAL RECORD, COMMUNITY or UNVERIFIED). The rules are in `CLAUDE.md`.

```
CLAUDE.md                  rules Claude follows every chat
vehicles/<car>/            profile, open issues, maintenance tracker, verified specs,
                           parts, log, issue history, recalls, complaints
procedures/                step-by-step jobs, sourced
mods/                      upgrades and accessories (same rules, kept apart from repairs)
receipts/                  invoices, quotes, inspection sheets (private)
sources/                   owner's manual PDF, Chilton pulls, photos of labels
prompts/                   prompts for pulling Chilton data with another AI
tools/lookup.py            pulls NHTSA recalls/complaints, EPA data, VIN decode
tools/unmerged.py          lists chat notes that never reached main
tools/due.py               what's due, cost per mile, the 500k roadmap table
tools/checklists.py        builds procedures/checklists.html (phone checklists)
tools/check.py             drift checker, run before every merge
```

After each chat that changed notes, Claude merges its PR into `main` automatically
(owner's rule, 2026-10-31), or the next chat won't see them.
