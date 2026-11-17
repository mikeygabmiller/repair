# Maintenance tracker: 2005 Accord EX 2.4 L automatic

What's due, at a glance. **Update the row every time a maintenance job is done** (date and
odometer), and put the job in `log.md` too. Order and shopping list for the catch-up:
`plans/2026-11-catch-up-maintenance.md`.

Intervals are Honda's **severe** schedule (OM p.203, copied in `specs.md`), because the
car does short local trips and winter roads (OM p.199). "No record" = treat as due now.
Whichever comes first, miles or time.

Last known odometer: **139,781 mi** (2026-11-15, owner, ATF round 1).

Quick answer from the data: `python3 tools/due.py` (reads `schedule.csv` and `ledger.csv`).
This table stays the human-readable version with notes; if the two disagree, fix the ledger.

| Item | Interval (severe, OM p.203) | Last done | Next due |
|---|---|---|---|
| Engine oil | 5,000 mi or 6 months | **No record** | **Now.** Procedure: `procedures/accord-2005-oil-change.md` |
| Oil filter | 10,000 mi or 1 yr (change it with the oil anyway: the 4.4 qt capacity assumes a new filter, OM p.215) | **No record** | **Now** |
| Brake fluid | Every 3 years | **No record** | **Now.** Shop recommended; what to ask for: `procedures/accord-2005-brake-fluid-coolant.md` |
| Automatic transmission fluid | 60,000 mi or 3 yr, then every 30,000 mi or 2 yr | 2026-11-15, 139,781 mi: round 1 of 4 (Valvoline, `log.md`) | Rounds 2–4 of the thorough flush (OM p.220), each after a short drive. Then 169,781 mi or 2028-11 (severe, OM p.203). Procedure: `procedures/accord-2005-atf-drain-refill.md` |
| Engine coolant | 120,000 mi or 10 yr, then every 60,000 mi or 5 yr | **No record** | **Now** (car is past 120k and 10 yr). Same file as brake fluid |
| Drive belt: inspect | 30,000 mi or 2 yr | **No record** | **Now** (look only) |
| Air cleaner element | 15,000 mi in dusty conditions (normal 30,000) | **No record** | **Now.** `procedures/accord-2005-filters-air-cabin.md` |
| Dust and pollen (cabin) filter | 30,000 mi or 2 yr; 15,000 mi if urban soot or weak airflow (OM p.233) | **No record** | **Now.** Same file |
| Tire rotation | 10,000 mi | **No record** | **Now**, after the item 11 inspection. Chalk each tire's old spot (LF, RF, LR, RR) first so a wobble that follows a wheel shows. Pattern and steps: `procedures/accord-2005-tire-rotation.md` |
| Brakes, steering, suspension, boots: inspect | 10,000 mi or 1 yr | Partial: Les Schwab free suspension check, 2026-10-21, 139,032 mi (written notes cover the right front) | Full inspection with the next brake job. Checklist: `procedures/accord-2005-routine-checks.md` |
| Valve clearance | Inspect at 110,000 mi, otherwise adjust only if noisy | **No record** (car is past 110k) | Listen for ticking; shop job. Exhaust spec is unsettled (`specs.md`) |
| Spark plugs | 110,000 mi | **2026-10-18, 138,943 mi** (Bosch 9614, `log.md`) | ~248,900 mi |
| Idle speed: inspect | 160,000 mi | No record | 160,000 mi |
| Lubricate all hinges, locks and latches | 10,000 mi or 1 yr (OM p.203) | **No record** | **Now** (5 min, `procedures/accord-2005-routine-checks.md`) |
| Parking brake adjustment: check | 20,000 mi or 1 yr (OM p.203) | **No record** | **Now**, with the brake inspection |
| Brake hoses and lines (incl. ABS), exhaust, fuel lines, lights and controls, underbody: inspect | 20,000 mi or 1 yr (OM p.203) | **No record** | **Now**: underbody especially after the ditch slide (open issue 11) |
| Oil and coolant level | Every fuel stop (OM p.203) | — | Habit: `procedures/accord-2005-routine-checks.md` |
| Tire pressure and condition; ATF level; brake fluid level; lights | Monthly (OM p.201) | — | Same file |
| Wiper blades: inspect | Every 6 months (OM p.234) | 2026-09 (new blades) | ~2027-03 |

## Parts with a known age (repairs, not scheduled items)

Useful when something acts up again, and for the buyer when the car is sold.

| Part | Installed | Mileage | By | Record |
|---|---|---|---|---|
| Right front lower ball joint (Moog K80228, to confirm on invoice) | 2026-10-27 (reported) | not recorded | Ben's Auto Care | `log.md`; invoice → `receipts/` |
| Right front ABS wheel speed sensor | 2026-10-27 (reported) | not recorded | Ben's Auto Care | `log.md`; invoice → `receipts/` |
| Right front CV axle + new axle nut | ~2026-10-22 | not recorded | Owner | `log.md` (Parts Geek order #31-12567661) |
| Battery (EverStart Maxx) | before purchase | — | — | Made May 2025 (label) |
| Front wiper blades (BFGoodrich Beam 26"/18") | 2026-09 | not recorded | Owner | `log.md` |

## Mileage habit

Every job, inspection or symptom report needs the odometer reading. A photo of the
dashboard is enough. Most entries in `log.md` say "mileage not recorded", and a dated,
mileage-stamped history is what makes the car worth more whenever it's sold, and what the
500k plan (`plans/roadmap-500k.md`) runs on.
