# Automatic transmission fluid: drain and refill, 2005 Accord EX-L 2.4 L, 5-speed automatic

Sources: Honda owner's manual (OM) "Transmission Fluid", pp.219–221 (read 2026-11-10);
capacities OM p.274; Chilton A/T Fluid Replacement and A/T Fluid Level Check, applicability
"2003–04 Accord V6 A/T and 2005–07 Accord" (engine not split), report E in
`sources/chilton-report-A-I-2026-10-27.md`; numbers copied in `specs.md`.
Difficulty: easy–moderate (an oil change with a different plug and a funnel in a dipstick
tube). Time: ~45–60 min per round (estimate, not from a manual).
**Undrivable?** Only between pulling the plug and finishing the refill (~30 min), as long as
the fluid and a washer are bought first.

## Why it matters on this car
The automatic is the part most likely to end this car (`plans/long-term-ownership.md`), the
fluid has no service record (`maintenance.md`), and the 60 mph shake (open issue 3) has a
light-throttle shudder pattern in NHTSA complaints that fresh fluid sometimes helps
(COMMUNITY). Severe-schedule interval: 60,000 mi or 3 yr, then every 30,000 mi or 2 yr
(VERIFIED: OM p.203).

## Tools and parts

| Item | Spec | Source |
|---|---|---|
| Fluid | **Honda ATF-Z1**; DEXRON III only as a temporary replacement. Z1 is discontinued; Honda DW-1 is sold as its replacement (COMMUNITY + parts retailer; **ask the Honda parts counter with the VIN**, `parts.md`). No Honda fluid locally: order DW-1 online, or see the MaxLife note in `parts.md` (not Honda, not OEM licensed) | VERIFIED: OM p.219 |
| Amount per round | **3.0 US qt (2.8 L)**. Buy 4 qt per round so a spill doesn't stop you | VERIFIED: OM p.274; Chilton K24A4 capacities row agrees (6.0 pt) |
| Scheduled service | **One drain-and-refill** ("drained and refilled with new fluid according to the… maintenance schedule") | VERIFIED: OM p.220 |
| Thorough flush (optional) | 3 drain-and-refills with a short drive after each, then a final drain-and-refill = **4 rounds, 12 qt**. Worth it here (no fluid record at ~139k), but rounds can be spread out as budget allows | VERIFIED: OM p.220 ("To thoroughly flush the transmission…") |
| Drain plug | Thread 18 × 1.5 mm, **36 lbf·ft (49 N·m)**, **new sealing washer** every time | VERIFIED: Chilton report E (`specs.md`) |
| Drain plug washer | Lead: 90471-PX4-000 (COMMUNITY, YouTube description). **Confirm by VIN** before buying | `parts.md` |
| Filler bolt (only if you use it) | 24 × 1.5 mm, 33 lbf·ft (44 N·m), new washer | VERIFIED: Chilton report E |
| Socket / drive for the drain plug | **Not recorded.** Many Honda ATF drain plugs take a 3/8-in square drive (ratchet straight in) (COMMUNITY, UNVERIFIED for this car): look before buying anything | Write it here after the job |
| Also | Torque wrench that reads 36 lbf·ft, drain pan (≥5 qt), long-neck funnel that fits the dipstick tube, rags, gloves, ramps or jack + **two jack stands** | — |

## Safety
- Never under the car on a jack alone. Ramps, or stands at the factory jacking points, on
  level ground, wheels chocked (jack points: OM p.248 picture; stand points: Chilton, not
  pulled yet).
- Hot fluid. Warm is what you want for draining; let it sit a few minutes if it was just
  driven hard.
- The level check needs the car **level**. Checking on ramps gives a wrong reading: drive
  it off first.

## Steps
1. **Warm it up**: drive until the engine is at normal temperature (the radiator fan has
   cycled) (Chilton C01). Park level, engine off.
2. Raise the front on ramps or stands. Find the drain plug on the bottom of the
   transmission (driver's side, below the engine oil pan area; look for the square-drive
   or hex plug on the transmission case, not the engine oil pan). If unsure, **don't pull
   anything**: ask, or compare with the oil drain bolt you already know.
3. Pan under it, remove the plug, let it drain until it only drips. Look at the plug's
   magnet: fine grey paste is normal wear; chunks or flakes are not (COMMUNITY): photo it.
4. New washer on the plug, thread in by hand, torque **36 lbf·ft** (Chilton).
5. Lower the car to level ground. Pull the **yellow-loop dipstick** (OM p.219; location
   OM p.210). Funnel in **3.0 US qt** through the dipstick tube, slowly (OM p.219: clean
   spills right away).
6. Start the engine, run it to normal temperature, shift slowly through each gear with
   your foot on the brake, back to P.
7. **Check the level** (OM p.219 + Chilton): level ground, engine **off**, within **60–90 s**
   of shutting off. Wipe the dipstick, push it **all the way in** with the rubber cap
   seated, pull and read. Between the upper and lower marks. Low: add a little and recheck.
   **Never overfill.**
8. Rounds 2–4 (optional thorough flush; can be weeks apart): drive a short distance (OM p.220 says "a short distance"; 10–20 min of normal
   driving is the usual reading, COMMUNITY), then repeat steps 1–7. Rounds can be a day or
   two apart; the car is drivable between them.

## Backyard method (COMMUNITY)
- **Measure what came out** in a marked jug and put back the same amount, then fine-tune on
  the dipstick. Why it works: a drain only empties what's in the case (about 3 of the
  ~6.9 qt total, OM p.274); the rest stays in the torque converter and lines. Matching in
  to out keeps you from guessing at the level while the fluid is cold.
- **Free loaner tools**: chain parts stores loan torque wrenches and fluid pumps against a
  refundable deposit (AutoZone "Loan-A-Tool", O'Reilly, Advance; COMMUNITY, check your
  local store).
- **Why not a flush machine**: Honda's own method is drain-and-refill (OM p.220). Shop
  machines push generic "multi-vehicle" fluid; Honda wants Honda fluid (OM p.219). If a
  shop offers only a machine flush with generic fluid, walk away (COMMUNITY, common Honda
  forum advice).

## Gotchas
- **No pan, gasket or filter in this job.** The OM (pp.219–220) and Chilton's A/T Fluid
  Replacement use only the drain plug and the dipstick tube; Chilton's only ATF filter
  article is Hybrid-only (report E, G27). AutoZone's "complete the job" add-ons for this car
  (Duralast filter kit TF534, Fel-Pro pan gasket 2304, Lubegard Shudder Fixx; seen
  2026-11-14) are not part of Honda's procedure: skip them. Additives also break the
  Honda-fluid rule and would muddy the 60 mph shake test.
- **Price check (2026-11-14):** AutoZone MaxLife Multi-Vehicle 1 gal $45.99 = ~$11.50/qt,
  more than Honda DW-1 at $10.75/qt (`next-steps.md`). One gallon covers one round only.
- One round replaces only part of the fluid: about 3.0 of 6.9 qt (OM p.274), ~43%. Estimated
  new-fluid share, assuming the old and new mix fully: 1 round ~43%, 2 ~68%, 3 ~82%, 4 ~90%
  (Claude's arithmetic from the OM numbers, not a Honda figure). The manual's routine service
  is one round; the 4-round flush is its "thorough" option (OM p.220).
- Honda bulletin list on NHTSA includes **A89-022 "Using the ATF DW-1 Cooler Cleaner"**
  (Chilton bulletin list item 24): a shop item tied to transmission replacement, not this
  job. Not read in full.
- If the fluid comes out **burnt-smelling and dark brown with grit**, still do the change,
  but log it: it changes the walk-away math for this car (`plans/long-term-ownership.md`).

## After the job
- `log.md`: date, **odometer**, fluid brand/part number, quarts per round, drain plug drive
  size, what the magnet looked like.
- `maintenance.md`: ATF row. Next: 30,000 mi or 2 yr (severe, OM p.203).
- Re-test the 60 mph shake after round 1 and round 4; write what changed in
  `open-issues.md` item 3.

## What I couldn't verify
- DW-1 replacing Z1 and the drain washer number: Honda parts counter, free, with the VIN.
- Drain plug drive size and exact location photo: look under the car once.
- Jack stand points: Chilton (library) → "Jacking" section; or the OM p.248 jack points are
  the safe lift points, stands go next to them on the pinch weld (COMMUNITY, UNVERIFIED).
- "Short distance" between rounds: the manual gives no number.
