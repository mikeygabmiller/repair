# Overnight session summary: 2026-11-10 (finished 2026-11-11)

Plain version of what changed, how much of it is checked, and what's next. All of it is on
`main` (PRs #62–#67, merge commits).

## What was built
- **17 procedures** (was 2). Each gives the shop method first, a labeled backyard method
  with why it works, time, and whether the car is left undrivable. List:
  `procedures/README.md`.
  - **Sourced from the owner's manual and/or Chilton (10):** oil change, ATF drain-and-refill,
    brake fluid + coolant (coolant DIY steps from a V6 article, labeled), spark plugs, tire
    rotation, routine checks + 10k/20k inspection + wipers, bulbs, roadside (flat, jump,
    overheating, warning lights, towing), front brakes, winter prep.
  - **Partly sourced (3):** battery/charging/parasitic draw tests (charging limits from a TSX
    article), drive belt (inspection sourced, replacement DRAFT), front axle/bearing/ball
    joint (shop-first; how to order and check the job).
  - **DRAFT (4):** air + cabin filters (the manual has no steps), valve clearance (exhaust
    spec in conflict), throttle body + idle relearn, string alignment.
- **Diagnostics:** `symptom-index.md` (every common symptom → cheap-first path → matching
  bulletins, recalls, complaints), `diagnostics.md` (a decision tree for every open issue),
  `tsb-guide.md` (bulletins that can apply to a 2.4 L automatic sedan, by symptom).
- **Official data:** `tsbs.md`, all **183** Honda communications NHTSA holds for the 2005
  Accord, from a new `tools/lookup.py tsbs` command. Recalls/complaints refreshed (no change:
  24 recalls, 686 complaints, VIN decode still says EX).
- **Quick reference** from ~60 owner's manual pages read as images: fluids, tires, **both
  fuse charts in full**, bulbs, roadside (`quick-reference.md`).
- **Planning:** `next-steps.md` (prioritized, with cost, time, off-road per row),
  `owner-checklist.md` (one car trip, two calls, one library session),
  `prompts/muse-chilton-pull-3.md` (≈25 Chilton items that unblock procedures).
- **Research (`mods/`):** `tools-plan.md` (staged tool buying, budget vs name brand, free
  loaners, the 2020 Harbor Freight jack stand recall item numbers), `lighting-upgrades.md`
  (halogen upgrades yes; LED/HID retrofits in halogen housings no, per NHTSA letters).
  `parts.md` gained a **catalog by system** (30 parts with status).
- **Repo tools:** `INDEX.md` (find anything fast), `tools/check.py` (broken links, torques
  that drifted from `specs.md`, unlabeled numbers, unknown part numbers, bad complaint
  numbers). First run found 7 broken links; now 0 errors, 0 warnings. `CLAUDE.md` got
  workflow hooks only (INDEX, run check.py before merging); **your standing rules weren't
  touched**.

## Things found and fixed
- **Chilton's 30/29 psi tire pressure is the LX row** (OM p.237 prints 30/29 for the LX
  only). This car (EX-L) is **32 front / 30 rear**. Door-jamb sticker still has the last word.
- `maintenance.md` was missing **six severe-schedule items** (hinge/lock lube, parking brake
  check, brake lines/exhaust/fuel lines/underbody, fuel-stop and monthly checks, wiper
  inspection). Added.
- Back-up light fuse conflict found: the manual says interior **#7 (10 A)**, an earlier
  Chilton read said **#21**. Recorded in `specs.md`; check before tapping for the camera.
- The axle-nut torque question stays closed, as you asked on 2026-10-28.

## How much is checked
| | VERIFIED / confirmed | Not yet |
|---|---|---|
| Specs (`specs.md`, ~150 rows) | ~95 rows carry a VERIFIED source (owner's manual page or Chilton 2.4 L row) | 5 TENTATIVE (two brake torques/limits, rear brake row), 8 rows from Hybrid/V6/TSX only, a few open conflicts (valve exhaust spec, rear camber sign, back-up fuse) |
| Part numbers | 7 confirmed by fit or the manual | 8 "listing" (parts site lists it for this trim), 13 "lead", 4+ unknown. **None confirmed by a dealer VIN lookup yet** |
| Bulletins | 183 exist (OFFICIAL RECORD) | **Honda's fixes not read for any of them**: only titles and NHTSA one-liners |
| Prices | Dated snapshots with links | Most tool prices are old coupon/deal pages; recheck |

## How to check the rest for free
1. **One trip to the car** (30 min, phone): odometer, door-jamb label, emissions label
   (SULEV?), battery label, both fuse-box lids, rear brakes disc/drum, fluids' colour.
2. **Honda parts counter call with the VIN**: every part number in `owner-checklist.md` §2,
   plus DW-1 vs Z1 and EX vs EX-L.
3. **Honda customer service 1-888-234-2138**: which recalls were done.
4. **nhtsa.gov** Manufacturer Communications: download six bulletin PDFs (list in
   `tsb-guide.md`).
5. **Library**: run `prompts/muse-chilton-pull-3.md` in Muse.

## Next biggest improvements, ranked
1. **Front-end shop visit before 2026-11-20** (Les Schwab bearing quote expires): left front
   bead/rim, bearing, rotor, ditch inspection, alignment last. Safety, and it fixes the ABS.
2. **The parts-counter call**: turns ~25 part numbers from "lead" to confirmed in 15 min.
3. **Chilton Part 3 pull**: removes the TENTATIVE brake torques and most DRAFT labels.
4. **Read the six bulletins** and write Honda's fixes into `tsb-guide.md`.
5. **Sunday catch-up maintenance** (oil, filters, ATF round 1) with the new procedures.
6. Next session for Claude: product research for name-brand pads/rotors/bearings once the
   Honda numbers are confirmed (cross-referencing needs those numbers first), and the
   Part 2 Chilton import.

## What I couldn't do or confirm
- Web search hit its weekly limit for part of the night, so product research is thinner
  than planned (tools and lighting done; brake/bearing/mount brand cross-references are
  leads only).
- NHTSA, AutoZone and some parts sites refused direct page loads (403); facts from those are
  quoted from search results and say so.
- Nothing was bought, and nothing about the airbags was touched or advised beyond "dealer or
  SRS shop".
