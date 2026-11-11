# Procedures

One file per job, e.g. `accord-2005-oil-change.md`. Only write one after the steps are
sourced (library service manual or owner's manual) or the job was actually done and
logged. Every step that has a number cites `specs.md` or its source.

Exception: a job the owner asks for before the manual has been read can be written as a
**DRAFT**: say so at the top, label every unsourced step, give no torque specs, and end
with a "Still needed from the FSM" list. Remove the DRAFT label once those are filled.

Every procedure gives: the proper shop method first, then a labeled `COMMUNITY` backyard
method with why it works; real time estimates (labeled as estimates); whether the car is
left undrivable (it's the only car); tools; and a "What I couldn't verify" list.

Current procedures (by job):

| Job | File | Status |
|---|---|---|
| Oil and filter | `accord-2005-oil-change.md` | Sourced (OM pp.214–215) |
| Automatic transmission fluid, drain and refill | `accord-2005-atf-drain-refill.md` | Sourced (OM pp.219–221, Chilton) |
| Brake fluid exchange; coolant change | `accord-2005-brake-fluid-coolant.md` | Brake: sourced; coolant DIY steps from a V6 article (labeled) |
| Engine air filter, cabin filter | `accord-2005-filters-air-cabin.md` | DRAFT (no manual steps exist) |
| Spark plugs | `accord-2005-spark-plugs.md` | Sourced (Chilton K24A4 rows) |
| Tire rotation | `accord-2005-tire-rotation.md` | Sourced (OM p.239, p.250) |
| Routine checks, 10k/20k inspection, wipers, hinge lube | `accord-2005-routine-checks.md` | Sourced (OM pp.201–203, 233–235) |
| Front brake pads and rotors | `accord-2005-front-brakes.md` | Sourced (Chilton F03 + spec table; two TENTATIVE values flagged) |
| Drive belt inspect / replace | `accord-2005-drive-belt.md` | Inspect sourced; replace DRAFT |
| Battery, charging, parasitic draw tests | `accord-2005-battery-charging-tests.md` | Partly sourced (charging limits from a TSX article, labeled) |
| Exterior bulbs | `accord-2005-bulbs.md` | Sourced (OM pp.226–232) |
| Roadside: flat, jump, overheating, warning lights, towing | `accord-2005-roadside.md` | Sourced (OM pp.245–264) |
| Wheel alignment (string method) | `accord-2005-wheel-alignment-diy.md` | DRAFT |

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
