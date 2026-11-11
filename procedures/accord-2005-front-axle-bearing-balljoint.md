# Right/left front: CV axle, wheel bearing, lower ball joint. 2005 Accord EX-L 2.4 L AT

**Shop recommended. This file is for ordering the job right and checking the work.** The
owner's October attempt shows how these jobs strand the only car (`log.md` 2026-10-19: ball
joint taper wouldn't separate, inner CV wouldn't pop, old axle went back in). Safety-critical:
OEM or name-brand parts only.

Sources: Chilton halfshaft R&I summary (A02, article covers this vehicle), hub/bearing
(A03, **Hybrid** article), lower ball joint (A04) in `sources/chilton-2026-10-23.md`; bearing
facts in `issues-history.md`; part numbers `parts.md`.

## What's known for this car
| Item | Value | Status |
|---|---|---|
| Axle nut | Honda 90305-692-010, 22 mm thread, **32 mm socket** (test-fit) | Part: listing; socket: confirmed by fit |
| Axle nut torque, 4-cyl | **NOT FOUND.** The 181 lbf·ft figure is the Hybrid article's 24 mm nut | Owner closed this question 2026-10-28. For the bearing job the shop torques the new nut from its own data |
| Wheel bearing | Press-in, with a **magnetic ABS encoder**; brown encoder side faces **inward** (Hybrid article) | Hybrid article; same design per MOTOR Aug 2013 (`issues-history.md`) |
| Bearing part | Honda 44300-TR4-A51 (NSK) | Listing |
| Lower ball joint | Honda 51220-SDA-A02 → -305; Moog K80228 reported installed right side (confirm on Ben's invoice) | Listing |
| Tie rod end nut | Castle 29–35 lbf·ft, non-castle 32, new cotter pin | VERIFIED: Chilton R2 A05 |
| ABS sensor bolt | 7.2 lbf·ft (9.8 N·m) | VERIFIED: Chilton, drawing labeled 4-cylinder |
| Strut (damper) fork through-bolt nut | 47 lbf·ft, wheels on the ground, new self-locking bolt | VERIFIED: Chilton R2 A05 |
| Caliper bracket bolts | 80 lbf·ft | VERIFIED: Chilton spec table |
| Lug nuts | 80 lbf·ft crisscross | VERIFIED: OM p.250 |

## Ordering the bearing job (open issue 4)
Ask for: "Right front hub bearing, OEM Honda/NSK or SKF/Timken with the **magnetic ABS
encoder**, encoder side facing inward, new axle nut staked, new cotter pins, all suspension
fasteners to Honda spec, ABS light cleared with a scanner and a test drive." Do it in the
same visit as the rotor (issue 5) and the ditch inspection (issue 11), **alignment last**.
Les Schwab's quote (≈$516 incl. hub) is valid to **2026-11-20**.

## Checking the work afterwards (free)
- ABS light goes out after a test drive (~19 mph, Chilton V6 article).
- No hum or growl that changes with speed; no play rocking the wheel at 12/6 o'clock.
- Axle nut staked into the spindle notch; cotter pins in the castle nuts.
- Invoice lists brand and part number of the bearing → `parts.md`, `log.md` with mileage.

## Chilton steps (summaries, for reference)
- **Axle (A02):** raise the nut's stake, remove the nut; drain the transmission (it loses
  fluid with the right axle out: refill with Honda ATF, `specs.md`); disconnect the
  stabilizer link (hold the pin with a hex key) and the lower ball joint; pull the knuckle
  out, tap the outer joint out of the hub with a plastic hammer; pry the inner joint out of
  the differential. **Never pull on the shaft** (the inner joint comes apart). Reverse;
  check the inner clip is locked (Part 3 prompt R07 asks how); refill the transmission;
  check alignment.
- **Bearing (A03, Hybrid):** knuckle off the car; press the hub out, press the bearing out;
  press the new bearing in **brown encoder side inward**; snap ring; press the hub in. Needs
  a press and Honda's adapters (07GAF-SD40100 etc.).
- **Ball joint (A04):** cotter pin and nut off; ball joint remover on the stud threads;
  **never hit the joint itself.**

## Backyard notes (COMMUNITY, from the October attempt)
- A stuck taper: put a screw-type puller under tension, then one sharp hit on the knuckle
  where the stud passes. Why: the tension does the work; the hit only breaks the taper's
  grip. Hammering without tension wedges it tighter.
- Keep heat away from the ABS wire, brake hose and boots.
- The ABS sensor can snap when the knuckle is worked on (it did at Ben's): budget for one.
- Don't start this the night before a work day.
