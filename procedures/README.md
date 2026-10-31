# Procedures

One file per job, e.g. `accord-2005-oil-change.md`. Only write one after the steps are
sourced (library service manual or owner's manual) or the job was actually done and
logged. Every step that has a number cites `specs.md` or its source.

Exception: a job the owner asks for before the manual has been read can be written as a
**DRAFT**: say so at the top, label every unsourced step, give no torque specs, and end
with a "Still needed from the FSM" list. Remove the DRAFT label once those are filled.

Current procedures:
- `accord-2005-oil-change.md`: oil and filter (owner's manual pp.214–215)
- `accord-2005-wheel-alignment-diy.md`: string-method toe, camber check (DRAFT)

Template:

```markdown
# <Job>: <vehicle>

Sources: <manual + section/page>, <other>
Difficulty: easy / moderate / hard · Time: ~X h

## Tools and parts
- ...

## Safety
- ...

## Steps
1. ... (torque: see specs.md → <item>)

## Gotchas
- COMMUNITY: ... (where from)
```
