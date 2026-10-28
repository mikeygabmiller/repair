# Wheel alignment (DIY string method): 2005 Accord EX sedan, 2.4 L, automatic

**Status: DRAFT.** Not done on this car yet, and the steps are not checked against the
factory service manual. Targets are from the owner's manual; tolerances, torque specs and
wrench sizes are not. Before the first real use, read the FSM wheel alignment section in
Chilton Library (free with a library card) and fill in the "Still needed" list at the end.

Sources: owner's manual p.275 (targets, via `specs.md`) · OM p.250 (lug nuts) · OM p.276
(tire pressure) · DIY method write-ups and DriveAccord threads (COMMUNITY, linked inline)
Difficulty: moderate · Time: ~3–4 h the first time, mostly setup (estimate, not sourced);
~1–1.5 h once you've done it

## What DIY can and can't do on this car

| Angle | Adjustable from the factory? | DIY? |
|---|---|---|
| Front toe | Yes, at the tie rods | **Yes.** This is the one that matters most for tire wear and the one you'll adjust most often |
| Rear toe | Yes, cam (eccentric) bolts on the rear toe arms. COMMUNITY: [DriveAccord, rear toe arm thread](https://www.driveaccord.net/threads/rear-control-arm-toe-arm-q.540259/) | Yes, if the cam bolts aren't seized |
| Thrust angle | Follows from rear toe | Yes: make the two rear wheels' toe equal |
| Front camber | No. COMMUNITY: [DriveAccord, "Is camber adjustable on these cars? No"](https://www.driveaccord.net/threads/is-camber-adjustable-on-these-cars-no.560015/). Correcting it needs an aftermarket adjustable upper arm or similar | **Measure only.** A reading off spec or different side to side points to a bent or worn part |
| Front caster | No. COMMUNITY: [DriveAccord, front caster thread](https://www.driveaccord.net/threads/alignment-questions-front-caster.35276/) | Measure only (optional, fiddly) |
| Rear camber | Small range at most. COMMUNITY reports differ; adjustable rear arms exist for more | Measure only |

Honest call: for **toe**, a careful string setup is the standard home method. For
**camber/caster diagnosis** after a crash, a curb strike or hammering on the knuckle, a
shop's printout is more trustworthy than a phone-sized angle gauge. One paid printout
also documents the car for resale.

Aftermarket camber arms are bolt-on and reversible (owner's rules allow that), but they
replace OEM parts: keep the originals if you ever fit them.

## When to align

- **Only after worn parts are fixed.** Aligning with a loose wheel bearing, a bad ball
  joint or a worn tie rod end gives meaningless numbers. On this car right now: do the
  right-front axle/bearing/ball joint job first (`open-issues.md` item 0 and 2).
- After replacing tie rods, tie rod ends, struts, control arms, or the rack.
- When the steering wheel is off-center driving straight, the car pulls, or tires wear
  on one edge.
- Replacing a hub bearing or the lower ball joint doesn't touch an adjustment point, so
  it should not change alignment by itself (UNVERIFIED reasoning, not from the FSM). If
  numbers are off afterward with nothing adjusted, suspect a part bent during the job.

## Targets

From `specs.md` (VERIFIED: OM p.275):

| | Front | Rear |
|---|---|---|
| Toe-in | 0.00 in (0.0 mm) | 0.08 in (2.0 mm) |
| Camber | 0° | 1° (sign not printed; very likely negative, UNVERIFIED) |
| Caster | 3°15′ | — |

Not in the owner's manual (need the FSM): the **tolerance** (± range) on each value,
whether the toe figures are **total** (both wheels added) or per wheel, the **diameter**
the toe is measured at, and the vehicle condition (load, fuel) for measuring.

What that means in practice:
- **Front toe target is zero**, so it reads the same at any diameter and whether total
  or per wheel. Set the front to zero, equal side to side.
- **Rear toe is tiny.** If 2.0 mm is total toe measured at the tire tread (~652 mm for a
  P205/60R16: 406 mm wheel + 2 × 123 mm sidewall), then across ~430 mm of rim lip it's
  about 1.3 mm total, ~0.7 mm per wheel. That's about the limit of reading a tape. So for
  the rear, aim for: slight toe-in, **never toe-out**, and **both sides equal**.
  To convert any linear toe to your measuring span: `spec × (your span ÷ spec diameter)`.

## Tools and parts

- Level floor (garage slab or a flat driveway). Check with a long level; shim tires
  with plywood or tile if needed and keep the shims for every visit.
- 4 jack stands (or any 4 stable stands/boxes ~hub height) to hold the strings. They
  don't carry the car.
- Low-stretch string: braided mason's line.
- Steel ruler with mm marks (more readable than a tape at this scale), a tape measure.
- Digital angle gauge (for camber; zero it on the floor at each wheel spot).
- Front "turn plates" so the front tires can move while you adjust with the car on the
  ground: two squares of vinyl floor tile or plastic cutting board per tire with grease
  between (COMMUNITY trick).
- Steering wheel holder: a bar or strap to hold the wheel centered.
- Wrenches for the tie rod jam nuts and a wrench or locking pliers for the inner tie rod
  flats; wrenches for the rear cam bolt nuts. **Sizes not verified**: check the FSM or
  test-fit.
- Penetrating oil, applied a day or two before (tie rod threads, rear cam bolts).
- Torque wrench.
- Masking tape and a marker (mark tie rod and cam bolt start positions).

## Safety

- The car sits on its tires for measuring. If you raise it to reach a cam bolt: jack
  stands, never just the jack. Wheels chocked.
- Tie rod jam nuts and rear toe arm nuts are **steering/suspension fasteners**: torque
  must come from the factory service manual (Chilton Library). No number here on purpose.
- Lug nuts if a wheel comes off: 80 lbf·ft (108 N·m), crisscross (VERIFIED: OM p.250).
- Road-test gently before normal driving.

## Steps

### Prep (~30 min)
1. Tire pressures cold: front 32 psi, rear 30 psi (VERIFIED: OM p.276, see `specs.md`).
2. Load as you normally drive it. Note: the front passenger seat and rear seatbacks are
   out (`profile.md`). Honda's spec condition is unverified (FSM). Either put them back
   first or note in the log that they were out.
3. Check for play: grab each front wheel at 9 and 3 o'clock and rock it (tie rod end /
   rack), then at 12 and 6 (bearing / ball joint). Any play → fix that first.
4. Roll the car straight forward and back about a car length to settle the suspension,
   ending rolling **forward**. Bounce each corner.
5. Steering wheel straight, front wheels straight. Hold the wheel with the bar/strap.
6. Put the front tires on the turn plates (or roll onto them before step 4).

### Set up the strings (~45 min the first time)
7. One string down each side of the car, at hub-center height, a few inches outside the
   tires so nothing touches it. Tie to a stand at each end, pulled tight.
8. Make the two strings **parallel**: the distance between them is the same at the front
   stands and the rear stands.
9. Make them **centered on the car**: string-to-center-cap distance equal on the left and
   right front hubs. Then check the rear hubs are equal too. Adjust the stands, recheck
   step 8. Repeat until both hold. Now each string is parallel to the car's centerline.
   (COMMUNITY: [Rob Robinette's DIY alignment calculator](https://robrobinette.com/DIYAlignmentCalculator.htm)
   describes a version that only needs the strings parallel to each other.)
10. Don't bump the stands from here on. Mark their feet with tape.

### Measure toe (~20 min)
11. At each wheel, measure from the string to the **rim lip** (not the tire: sidewalls
    bulge) at the **front** edge and the **rear** edge of the rim, both at hub height.
    Same spot on the lip each time. Write it down.
12. Per wheel: **rear reading − front reading**. Positive = toe-in, negative = toe-out.
    Total toe for an axle = left + right.
13. Measure your span: the distance between the two points on the rim lip (front to
    back). Needed for the conversion above and to turn it into degrees:
    `angle ≈ (difference ÷ span) × 57.3°`.
14. Optional, for bent/out-of-round rims: roll the car exactly half a wheel turn, repeat,
    and average.

### Adjust front toe (~30–45 min)
15. Mark the tie rod's starting position with tape/marker so you can always go back.
16. Loosen the outer tie rod jam nut. Turn the inner tie rod by its flats a small amount
    (start with 1/8 turn). Watch the rack boot: it should not twist with the rod; loosen
    its small outer clamp if it does (general practice, UNVERIFIED for this car).
17. Re-measure that wheel. This tells you which direction moves toe-in on this car.
    Repeat until that wheel is at zero.
18. Do the other side. Both wheels at zero = front total toe zero.
19. **Steering wheel off-center?** Toe right but wheel crooked means one tie rod is
    long and one short. Lengthen one and shorten the other by the same amount (same
    number of flats), re-check the wheel and the toe.
20. Tighten the jam nuts to the FSM spec while holding the inner rod so it doesn't turn.
21. Remove the steering holder, roll forward/back again, re-measure. Toe often moves a
    little when the jam nuts tighten; adjust again if needed.

### Rear toe (only if it's off; ~30–60 min)
22. Rear wheels unequal, or toe-out → adjust. Equal and slightly toe-in → leave it.
23. Mark the cam bolt position. Loosen the nut (bolt head turns the cam). COMMUNITY:
    the nut has to be loosened before the cam will turn; seized cam bolts are common and
    some have had to be cut out ([DriveAccord](https://www.driveaccord.net/threads/rear-control-arm-toe-arm-q.540259/)).
    **If it won't turn with normal force, stop.** A broken cam bolt leaves the car
    undrivable; get the replacement bolts in hand first (part numbers: Honda parts
    catalog by VIN).
24. Turn the cam a little, re-measure, set both sides equal and slightly toe-in.
    COMMUNITY: turning the cam can shift rear camber a little.
25. Torque the nut to the FSM spec, settle the car, re-measure.

### Camber check (~15 min)
26. Zero the angle gauge on the floor where the wheel sits (or on the turn plate).
27. Hold the gauge vertically against the rim lip at the top and bottom (a straight bar
    across the rim helps), wheel straight ahead. Read the angle.
28. Compare to the targets and side to side. Tolerance unverified (FSM). A big
    difference side to side with nothing adjustable is a parts problem (bent knuckle,
    arm, strut, worn bushing), not an alignment adjustment.

### Caster (optional)
29. Needs the turn plates marked in degrees: camber read with the wheel turned 20°
    left and 20° right. Caster ≈ 1.46 × the camber change (general geometry, UNVERIFIED
    against the FSM; the factor is 1 ÷ (2 × sin 20°)). Since it isn't adjustable, what
    matters is left vs right being close. If you want a caster number, a shop printout
    is easier.

### Finish
30. Road test on a straight, level road: wheel centered, no pull. A pull with good toe
    and even camber can be a tire: swap the two front tires side to side and see if the
    pull changes side (general practice).
31. Re-check lug nuts if a wheel came off (80 lbf·ft, OM p.250).
32. Log it in `log.md`: date, mileage, before and after toe per wheel, camber per wheel,
    span used, what was turned and how much, and whether the seats were in.

## Gotchas
- COMMUNITY: reading a tape to 1 mm reliably is hard, and a string a hair off parallel
  shows up as fake toe. Recheck string parallel/centering before believing a reading
  ([Garage Journal thread](https://www.garagejournal.com/forum/threads/how-do-i-do-a-diy-alignment-with-toe-plates.557650/)).
- COMMUNITY: measure on the wheel, not the tire ([The Mustang Source, DIY toe](https://themustangsource.com/?p=10027)).
- Front toe moves when the car sits up or down: always settle the car before measuring
  (general practice).
- Doesn't leave the car undrivable if you only touch toe and mark start positions,
  **except** a seized rear cam bolt or a stripped tie rod thread. Do the first one on a
  day off.

## Still needed from the FSM (Chilton Library, free with a library card)
- Toe, camber, caster **tolerances**.
- Whether toe is total or per wheel, and at what diameter.
- Rear camber sign (expected −1°).
- Vehicle condition for measuring (load, fuel, spare).
- Torque: outer tie rod jam nut, rear toe arm (cam bolt) nut.
- Wrench sizes for both.
- Honda's own alignment procedure, to replace or confirm steps 15–25.
