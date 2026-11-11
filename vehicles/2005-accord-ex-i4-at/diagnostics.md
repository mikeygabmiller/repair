# Diagnostic trees for the open issues

One tree per item in `open-issues.md`. `open-issues.md` holds the **status**; this file holds
the **decision path**, so a future chat can say "you're at step B3" instead of starting over.
Each branch ends in a result to write back into `open-issues.md`.

Labels: steps marked (OM)/(Chilton) come from those sources (`specs.md`); everything else is
standard diagnostic order, **UNVERIFIED reasoning** unless labeled. Specs are never invented:
where a number is needed and missing, the tree says so.

---

## Item 1. SRS light (61-10, E2-11, F1-11): shop only

Not a DIY tree. The owner's part is getting the facts a shop needs, for free:

1. Call Honda (1-888-234-2138) with the VIN: which airbag recalls were done, when, where.
2. Door jamb label: build month (also settles 11V395000).
3. Driver's belt: pulls out and retracts smoothly? Buckle clicks firmly? (Looking only; no
   connector touching.)
4. Book a Honda dealer or SRS-capable shop. Bring: the three codes, "light came back after
   clearing", "passenger seat was removed and reinstalled ~10-24", bulletins **A02-052,
   A07-002, A20-010, A20-015** (`tsb-guide.md`). Ask them to check the passenger seat bolt
   torque while there.
   - Shop reads the same codes with a Honda tool → their repair.
   - Shop reads different codes → the MADDOX was misreading; write both into open issue 1.

---

## Item 2. P0685 (ECM/PCM power relay control circuit)

What the code means: the engine computer powers PGM-FI main relay 1 and watches its own
power feed; the feed dropped or sagged while commanded on (COMMUNITY: Honda job aid quoted on
two repair sites; not yet checked in Chilton).

```
A. Before anything: screenshot Freeze Frame (rpm, temp, speed when it set).
B. Battery and connections (free, 10 min)
   B1. Both clamps: try to turn by hand. Any movement → clean, tighten, B4.
   B2. Ring terminals stacked on a post (light harness, head unit)? Move them on top
       of the clamp, never between post and clamp.
   B3. Ground strap engine→body and battery−→body: tight, no corrosion.
   B4. Clear the code. Drive 3–5 days normally. Rescan.
       → Gone: close item 2 (log the date and odometer).
       → Back: C.
C. Fuses and what the light install touched (free)
   C1. Interior #23 IGP 7.5 A and under-hood #8 FI ECU 15 A (OM pp.268–269): in, not
       tapped, not swapped. Add-a-circuit taps on neither.
   C2. Aux-light relay harness: fused at the battery; its ground on bare metal; nothing
       shares the ECM's ground.
D. Battery and charging test, free at a parts store
   (`procedures/accord-2005-battery-charging-tests.md`).
   → Battery fails: warranty replacement (EverStart, May 2025), then B4.
   → Charging out of range: alternator diagnosis (bulletin A10-054), then B4.
E. Still coming back with everything above good
   → Test PGM-FI main relay 1 with the factory procedure (Chilton through the library:
     relay location, pins, test). Don't buy a relay on the app's guess.
   → Intermittent wiring at the relay/ECM: shop with a Honda-capable scanner.
```

Tie-in: if the USB drop (item 9) stops at the same time P0685 stops, they shared a cause.

---

## Item 3. Shake around 60 mph, worse on the gas

Two symptoms are probably two causes: mild shake when coasting (rotating parts) + bigger
shake under throttle (drivetrain under load). Re-baseline after item 11 is fixed.

```
A. Free
   A1. Lug nuts 80 lbf·ft crisscross, all four (OM p.250).
   A2. Pressures 32/30 cold (OM p.237).
   A3. Drive test, write the answers in open issue 3:
       - speed it starts / stops?
       - felt in the steering wheel (front) or seat (rear/drivetrain)?
       - coasting in N at 60: shake there? (engine out of the equation)
       - light throttle vs hard throttle?
       - steady cruise 55–65 with light throttle: a buzz/shudder like rumble strips?
B. Coasting shake present (in N too) → wheels/tires
   B1. Tire shop: balance all four (Honda weights, OM p.238); ask for road-force if offered.
   B2. Look for bulges, flat spots, the bent rim from item 11.
   → Gone: done. → Still there: bearing (item 4) or bent part (item 11).
C. Shake only on throttle → drivetrain
   C1. Light-throttle shudder at 55–65 that feels like rumble strips: torque converter
       lock-up pattern (COMMUNITY: complaints 10299703, 11076272).
       → ATF drain and refill round 1 (`procedures/accord-2005-atf-drain-refill.md`),
         re-test; finish all 4 rounds; re-test.
   C2. Heavy throttle shake/clunk: inner CV joint or mounts.
       → Shop: confirm the new right axle's inner joint is fully seated (circlip locked,
         Chilton A02 says pull straight out/push straight in); inspect the left axle.
       → Mounts: with a helper holding the brake, light D↔R shifts while watching the
         engine: big lurch = mount (COMMUNITY test). Torques: TSX values only so far
         (`specs.md`): get the 2.4 L ones from Chilton before any mount work.
```

---

## Item 4. ABS light: right front bearing encoder

Diagnosis is done (Ben's, 2026-10-27). Remaining tree is about doing it once:

```
A. Bundle with item 5 (rotor/pads) and item 11 (ditch inspection) in one shop visit.
B. Part: OEM Honda 44300-TR4-A51 (NSK) or name-brand with the magnetic encoder
   (SKF FW48 / Timken 510073 candidates: confirm cross-ref, `parts.md`).
   Safety-critical: OEM or name-brand only.
C. After the job: ABS light should go out after a test drive at ~19 mph (Chilton, V6
   article). Still on → read ABS codes with an ABS-capable tool; check the new sensor
   connector at the knuckle; old code 61 (low voltage) → battery/charging (item 6).
```

Quotes in open issue 4 (Les Schwab ≈$516 valid to **2026-11-20**).

---

## Item 5. Right front rotor grooved

```
A. Free: read the minimum thickness cast/stamped on the rotor (Tier 1).
B. Measure at the deepest groove with a micrometer (parts-store loaner or ~$20).
   Below the stamped minimum, or deep grooves → new rotor (pair recommended, COMMUNITY:
   even braking left/right). Above → pads only, or resurface if the shop's lathe leaves
   it above minimum (Honda prefers on-car refinishing, bulletin A00-088).
C. Pads: lining under 0.060 in (Chilton) → replace as a front pair.
```
Procedure: `procedures/accord-2005-front-brakes.md`.

---

## Item 6. Battery drain (none since 2026-10-26)

```
A. Battery and charging test at a parts store (free). Battery made May 2025.
B. If it drains again: parasitic draw test
   (`procedures/accord-2005-battery-charging-tests.md`).
   High draw → pull fuses one at a time with the meter connected, note which fuse drops it.
   Suspects: Eonon head unit (new 2026-11-03), Bluetooth adapter (removed?), camera wiring,
   aux-light relay harness (pin 30 is live all the time, `log.md` 2026-10-29).
C. The maximum normal draw for this car: **not found yet** (Chilton checklist 46).
```

---

## Item 8. Cold-start rattle (UNVERIFIED as VTC)

```
A. Record it: cold engine (sat overnight), video with sound, how many seconds it lasts.
B. Oil level and age: low or old oil makes chain/VTC noise worse. Fresh 5W-20 first.
C. 1–2 s rattle at cold start that stops: commonly blamed on the VTC actuator on K24s
   (COMMUNITY). Longer, or at idle warm → timing chain tensioner/chain (shop).
D. No check engine light and only at cold start: not urgent. Watch for codes P0341/
   P0011-type cam timing faults (any code: read and look up before parts).
```
Chilton items still needed: 34 (chain stretch check), 35 (VTC diagnosis).

---

## Item 9. Phone USB drops when the aux lights switch

The three-step split test in open issue 9 is the tree; result paths:
- Drops with the aux fuse pulled → not the aux lights → battery clamp / Eonon power and
  ground → same as item 2 B.
- Drops only with the relay connected, lights unplugged → relay coil spike → relay with a
  suppression diode or a diode across the coil (stripe toward pin 86 / +).
- Drops only with lights plugged in → current dip → light ground at battery negative or bare
  metal, not shared with the head unit; wire gauge adequate.

---

## Item 10. Backup camera

Trigger confirmed (+12 V only in R at the Eonon reverse wire, owner 2026-11-05). Tree:
```
A. Eonon support with photos + video (in progress since 2026-11-06).
B. Confirm the wire used is "F5" in Eonon's picture.
C. Camera format setting (AHD vs CVBS, NTSC/PAL) matches the A0125 camera.
D. Meter in R: +12 V at camera power; camera ground to body; video continuity.
E. Unit fault → return/exchange inside the 90 days (~2027-01-24).
```

---

## Item 11. Ditch slide: wobble, alignment worse, left front bead leak

```
A. Spare on for any driving (50 mph max, OM p.246) until the left front is checked.
B. Free look, front on stands: rim lips dented? Spin each wheel against a fixed pointer:
   rim wobble vs tread wobble. Compare left/right tie rods and lower arms for bends/scrapes.
C. Tire shop: dismount left front, clean bead, check rim runout and the inside of the tire.
   → Rim bent: straighten (wheel repair shop) or replace with the same 16 x 6 1/2 JJ
     (OM p.240). Tire damaged inside: replace (pair on the front if wear differs a lot,
     OM p.239).
D. Shop: steering and suspension inspection (tell them "ditch"). Replace bent parts
   (OEM/name-brand), do the item 4 bearing in the same visit, align **last**, get the
   before/after printout. Ask them to follow bulletin A06-068 for pull/drift.
E. Re-test item 3.
```
