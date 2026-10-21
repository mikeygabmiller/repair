# Repair

A private, source-checked car repair knowledge base. Connect it to Claude and ask repair
questions: Claude checks this repo and official free sources first and labels every fact
(VERIFIED, OFFICIAL RECORD, COMMUNITY or UNVERIFIED). The rules are in `CLAUDE.md`.

```
CLAUDE.md                  rules Claude follows every session
vehicles/<car>/            profile, verified specs, parts, log, recalls, complaints
procedures/                step-by-step jobs, sourced
sources/                   owner's manual PDF, photos of labels
tools/lookup.py            pulls NHTSA recalls/complaints, EPA data, VIN decode
```
