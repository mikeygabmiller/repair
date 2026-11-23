---
name: log-job
description: Record a finished job, purchase, mod or inspection on the Accord - log.md entry, ledger.csv row, maintenance.md row, roadmap refresh. Use whenever the owner reports work done on the car or pastes a log box from the checklists page.
argument-hint: "[what was done, odometer, cost]"
---

# Log a job

The owner reported work on the car: $ARGUMENTS

Vehicle folder: `vehicles/2005-accord-ex-i4-at/` (`V/` below).

## 1. Get the facts first
Ask only for what's missing, in one message:
- **Odometer reading** (CLAUDE.md rule: always ask; a dash photo is fine). Write
  "not recorded" only if the owner doesn't know.
- **Date** (default: today), **cost** (blank if unknown; say "Cost not recorded" in `note`),
  **parts and fluids used** (brand and part number if known), **who** did it (owner or shop).
- Anything the job revealed: leaks, wear, a bolt that seized, a reading.

If the owner pasted the checklists page's log box, use its ledger row **exactly as given**.

## 2. `V/log.md`
Add an entry at the **top** (newest first), in the existing style:
`## YYYY-MM-DD, NNN,NNN mi: <job> (<who>)` then bullets: what was done, parts and fluids,
torque used, what was found, what's next. Label specs: a torque or capacity cites
`specs.md` or its source; a value the owner used that `specs.md` doesn't have is marked
as the owner's value, not VERIFIED.

## 3. `V/ledger.csv`
Append one row: `date,odometer,kind,item,cost,by,what,note`
- `kind`: purchase, maintenance, repair, mod, tool or inspection.
- `maintenance` row: `item` **must be** the matching `key` in `V/schedule.csv` (e.g. `oil`,
  `oil-filter`, `tire-rotation`), or `tools/due.py` won't count it as done.
  One row per schedule key (an oil change with a filter = two rows: `oil` and `oil-filter`).
- Quote any field containing a comma.

## 4. `V/maintenance.md` (maintenance jobs only)
Update that item's row: "Last done" = date, mileage, short note with a `log.md` pointer;
"Next due" = from `python3 tools/due.py --odo <reading>`, not your own arithmetic.

## 5. Other files the job may change
- Closes or changes an open problem → rewrite its status in `V/open-issues.md`
  (current state only; history goes to `V/issues-history.md` when it closes).
- New part number confirmed from the part or a receipt → `V/parts.md`.
- A value read off the car or a manual → `V/specs.md` with source and date.
- Receipt or invoice photo → `receipts/`.

## 6. Refresh and check
```bash
python3 tools/due.py roadmap --write
python3 tools/due.py --odo <reading>
python3 tools/check.py
```
Fix every ERROR. Tell the owner in 2-3 lines what was logged and what's due next.
Then follow `/wrap-up` (owner's standing rule: merge at the end of the chat).
