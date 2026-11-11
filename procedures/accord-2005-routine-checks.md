# Routine owner checks and the 10,000-mile inspection: 2005 Accord EX-L 2.4 L AT

Sources: Honda owner's manual (OM) "Owner's Maintenance Checks" p.201 and the severe
schedule p.203 (page images read 2026-11-10); level checks OM pp.212–224; tires OM
pp.236–239; battery OM p.242. Steps without an OM page are labeled.
Difficulty: easy. The car stays drivable.

## Every fuel stop (~2 min) (OM pp.201, 203)
- [ ] **Engine oil**: dipstick (orange handle), car level, engine off a few minutes. Between
      the marks; never above the upper mark (OM p.212).
- [ ] **Coolant**: reserve tank between MIN and MAX (OM p.217). Never open the radiator cap
      hot.

## Monthly (~10 min) (OM p.201)
- [ ] **Tire pressure, cold**, all four + spare: 32 front / 30 rear / spare 60 psi
      (OM pp.237, 246). Look at the tread and sidewalls for wear, nails, bulges (OM p.238).
- [ ] **ATF level** (yellow loop): engine hot, level, engine off, within 60–90 s
      (OM p.219; time window Chilton). Steps: `accord-2005-atf-drain-refill.md` step 7.
- [ ] **Brake fluid**: between MIN and MAX (OM p.223). Dropping = pads wearing or a leak.
- [ ] **Lights**: headlights low/high, parking, tail, brake (incl. high-mount), license
      plate, turn signals, back-up (OM p.201). A helper or a reflection in a window works.
- [ ] **Washer fluid** (OM p.216). **Power steering** level, engine cold (OM p.224).
- [ ] **Battery**: look at the test window; terminals tight and clean (OM p.242). On this
      car also: **clamps must not turn by hand** (open issue 2, P0685).

## Every 6 months
- [ ] **Wiper blades**: cracks, hardening, streaks → replace (OM p.234). Steps below.

## Every 10,000 mi or 1 year (severe schedule, OM p.203) (~45 min DIY look-over)
Do this on jack stands with the wheels off, or ask for it with any tire rotation or
brake job. Write what you find in `log.md` with the odometer.

| Check | What "bad" looks like | Source of the item | How to look |
|---|---|---|---|
| Front and rear brakes | Pad lining under **0.060 in** (front, Chilton); rotor grooves, lip, blue spots; leaks at calipers | OM p.203 (item); min lining: Chilton, `specs.md` | Look through the wheel or wheel off; measure the thinnest pad end |
| Tie-rod ends, steering gearbox, boots | Torn boot, grease flung out, play | OM p.203 | Grab the tire at 3 and 9 o'clock, push-pull: any clunk (COMMUNITY method) |
| Suspension components | Torn ball-joint boots, cracked bushings, leaking struts, broken links | OM p.203 | Wheel at 12 and 6 o'clock: clunk = bearing or ball joint (COMMUNITY method). Honda bulletin **A05-021 "Rear Stabilizer Link Is Broken"** exists for this model (`tsbs.md`) |
| Driveshaft (CV) boots | Split, grease on the inside of the wheel or the subframe | OM p.203 | Turn the steering to full lock, rotate the tire, look all the way around both inner and outer boots |
| Lubricate hinges, locks and latches | Squeaky doors, sticky trunk/hood latch | OM p.203 | Hood latch: clean, then multipurpose grease on moving parts and pivots (OM p.225). Doors: same idea |
| Oil filter | With every oil change | OM p.203 | `accord-2005-oil-change.md` |

## Every 20,000 mi or 1 year (severe, OM p.203)
| Check | What to look for |
|---|---|
| Parking brake adjustment | Lever travel and hold on a slope. Adjustment procedure: Chilton (Hybrid-only so far, `chilton-checklist.md` 24): shop if it needs adjusting |
| Brake hoses and lines (incl. ABS) | Cracked/bulging rubber hoses, rusty steel lines, wet fittings |
| All fluid levels and condition | Dark/burnt ATF, rusty coolant, dark brake fluid |
| Exhaust system | Rust-through, loose hangers, rattling heat shields, black soot at joints |
| Fuel lines and connections | Wet spots, fuel smell |
| Lights and controls; vehicle underbody | Everything works; underbody rust, damage, loose shields. After the ditch slide (open issue 11), check the underbody now |

## Wiper blades (OM pp.234–235, ~10 min)
1. Lift the **driver's** arm first, then the passenger's. **Never open the hood with the arms
   raised** (damages hood and arms) (OM p.234).
2. Push the lock tab in, slide the blade assembly toward the base of the arm, off.
3. Factory-style refills: pull the blade out of its holder by the tabbed end; move the metal
   reinforcement strips to the new blade if it has none; slide it in until the tabs lock.
4. Slide the assembly onto the arm until it locks. Lower the **passenger's** arm first,
   then the driver's (OM p.235).
Sizes on the car now: 26 in driver / 18 in passenger (BFGoodrich Beam, fit confirmed,
`parts.md`). When filling the washer, wipe the blade edges with washer fluid (OM p.216).

## Seat belts and floor mats (OM p.233)
- Belts that retract slowly: wipe the inside of the loops with mild soap and warm water or
  isopropyl alcohol. No bleach or solvents.
- Driver's mat must hook over its floor anchors; never stack mats (pedal interference).
  (SRS note: the passenger seat sensors are why the manual warns about marking the front
  passenger's weight sensors; open issue 1.)
