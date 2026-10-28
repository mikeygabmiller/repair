# Chilton Library checklist: 2005 Accord EX 2.4 L, automatic

Written 2026-10-27 for one big library session. Everything here is something the repo
still marks UNVERIFIED or doesn't have at all. Things the owner's manual already gave us
(fluid types and capacities, lug nuts, maintenance schedule, alignment angles, fuses,
bulbs) are in `specs.md` and are left out.

**How:** library website → online resources/databases → Chilton Library → log in with
the library card → 2005 Honda Accord, **2.4L 4-cyl** (not the V6) → automatic.
**Screenshot each item with the section title visible.** Each confirmed value goes into
`specs.md` with its section and date; tick it off here.

## Progress

- **Pack F (2026-10-27)**: `sources/chilton-pack-F-2026-10-27.md`. Results are in `specs.md`.
  It refers to an earlier **pack A–E** that isn't in the repo yet: upload it.
- **Report A–I (2026-10-27)**: `sources/chilton-report-A-I-2026-10-27.md`. Results are in
  `specs.md` and `open-issues.md`. Ticked below = found for this car (or settled);
  "Hybrid/V6 only" = found, but not usable as 4-cyl data.
- Chilton's 2005 coverage often lists only Hybrid, V6 or Acura TSX for an article. When
  that happens, try the same article under **2006 or 2007 Accord 2.4 L** (same generation)
  and label anything found that way "2006–07 article", not 2005 data. Or try ALLDATA if the
  library has it.
- **Not found in Chilton for the 2.4 L (pack F):** oil change steps, front/rear rotor
  specs, engine air filter steps, cabin filter (Hybrid only), coolant drain/fill, drive
  belt replacement (V6 only for 2005), struts (Hybrid only), alternator and starter R&I,
  battery spec, wiper size, bulbs (Hybrid only).

## A. Right front and ABS (the car right now)
- [ ] 1. (A–I: Hybrid only, 181 lbf·ft for a 24 mm nut. Owner closed the axle nut question 2026-10-28; reference only) Front axle (spindle) nut torque, 4-cyl. Also: tighten with the wheel on or off the ground, and how to stake the nut
- [ ] 2. (A–I: Hybrid only, 0–0.05 mm) Front wheel bearing axial play limit (proves "no play" with a number)
- [x] 3. (A–I: code 12 = RF sensor noise/intermittent; 61 = low voltage; V6 articles) ABS trouble code chart: 12-1, 61-1 and any new code Ben read
- [ ] 4. (A–I: V6 only) ABS wheel speed sensor test procedure, right front (resistance/voltage check, air gap if listed)
- [x] 5. (A–I: L4 ABS schematic, ETM p.44) Wiring diagram: right front wheel speed sensor → ABS modulator, with connector locations
- [x] 6. (A–I: C616, FR+B 2, FR-GND 18) ABS modulator connector pin numbers for the right front sensor (for a continuity test)
- [ ] 7. (A–I: Hybrid only — needs Honda scan tool; battery disconnect doesn't clear) How to clear ABS codes on this car (scan tool required or not)
- [ ] 8. (A–I: Hybrid only — press-in, snap ring, brown side in) Front hub bearing: confirm press-in, confirm magnetic encoder and which way it faces, removal/install steps, snap ring
- [ ] 9. (A–I: V6 only, 7.2 lbf·ft) ABS sensor bolt torque
- [ ] 10. (A–I: Hybrid only) Lower ball joint castle nut torque + cotter pin (check Ben's work)
- [ ] 11. Tie rod end nut torque
- [ ] 12. Sway bar link nut torque (touched in October)
- [ ] 13. Knuckle-to-upper-arm ball joint nut torque
- [ ] 14. Lower arm and damper fork bolt torques, and whether they're tightened at ride height
- [ ] 15. CV axle install: how to confirm the inner joint's clip is locked into the transmission

## B. Brakes
- [ ] 16. (A–I: runout 0.004 in found; min thickness 0.830 in TENTATIVE) Front rotor minimum thickness, runout limit, thickness variation limit (decides if the grooved rotor can be resurfaced)
- [x] 17. (A–I: 0.060 in) Front pad minimum thickness
- [x] 18. (A–I: 80 lbf·ft) Front caliper bracket bolt torque
- [ ] 19. (A–I: 26 lbf·ft TENTATIVE) Front caliper slide pin bolt torque
- [ ] 20. Rotor retaining screws: torque (pack F: screws are in the procedure; no torque shown)
- [ ] 21. (A–I: rear row TENTATIVE; look at the car) Rear brakes (pack F found a rear disc procedure, but doesn't tie it to the EX; just look through the rear wheel): disc or drum on this car, minimum thickness, bracket/slide bolt torques
- [x] 22. (A–I: FL, FR, RR, RL; no scan tool unless the modulator was opened) Brake bleed order, and whether the ABS unit needs a scan-tool bleed
- [ ] 23. How much fluid a full flush takes
- [ ] 24. (A–I: Hybrid only) Parking brake adjustment

## C. Shake under hard acceleration, steering
- [ ] 25. Engine and transmission mount inspection procedure
- [ ] 26. Each mount's bolt torques
- [ ] 27. Power steering fluid level check and bleed procedure
- [ ] 28. (A–I: Hybrid shows −1°; 4-cyl not found) Alignment camber sign: is rear camber 1° negative? (`specs.md` has the angle without a sign)

## D. Engine
- [x] 29. Oil drain plug torque: **33 lbf·ft** (pack F02, citing A–E)
- [x] 30. Spark plug torque and gap: 13 lbf·ft, 1.0–1.1 mm (pack F04, general article)
- [ ] 31. (A–I: K24A4 table found but exhaust conflicts with TSX article — see `specs.md`) Valve clearance, intake and exhaust, cold; adjustment procedure
- [ ] 32. Valve cover bolt torque and order; whether the gasket is reusable
- [ ] 33. Compression test spec: minimum and maximum spread between cylinders (health check before selling)
- [ ] 34. Timing chain: how to check for stretch, tensioner service limit
- [ ] 35. VTC actuator: diagnosing the cold-start rattle, replacement procedure and bolt torque
- [ ] 36. Throttle body cleaning procedure and any idle relearn afterward
- [ ] 37. Idle relearn after a battery disconnect
- [ ] 38. Engine trouble code chart (P0507 and others)
- [ ] 39. (Pack F: replacement article is V6-only for 2005) Drive belt: auto-tensioner indicator range, belt routing diagram
- [ ] 40. Coolant bleeding procedure, radiator cap pressure, thermostat opening temperature
- [ ] 41. PCV valve location and test

## E. Transmission
- [x] 42. ATF drain plug: 36 lbf·ft, 18 × 1.5 mm thread, new washer (A–I). Socket size still unknown
- [x] 43. (A–I: check within 60–90 s of shutoff) ATF level check procedure (compare with OM p.219)
- [ ] 44. (A–I: Hybrid only) Is there a serviceable ATF filter or strainer, and its service interval
- [ ] 45. Transmission trouble code chart

## F. Electrical and the battery drain
- [ ] 46. Parasitic draw test procedure and the maximum allowed draw
- [ ] 47. Charging system specs: alternator output voltage and amps
- [ ] 48. Fuse/relay chart showing what each circuit powers (more detail than the owner's manual)
- [ ] 49. Head unit connector pinout (Bluetooth adapter power)
- [x] 50. (A–I: fuse 21, ETM p.110-10; re-check routing before tapping) Reverse light circuit: wire color and where to tap it (backup camera, no cutting)
- [ ] 51. Power window and moonroof reset after a battery disconnect

## G. Airbags (SRS): read only, never DIY
- [x] 52. (A–I: Hybrid articles; 61-10 = driver buckle switch open) SRS code chart: 61-10, E2-11, F1-11
- [ ] 53. Passenger seat removal and install: SRS connectors and occupant sensor warnings (so you know what a shop will do)

## H. Body and interior
- [ ] 54. Front bumper cover removal: fastener and clip locations
- [ ] 55. Rear door panel removal (tint redo)
- [ ] 56. Dash trim removal around the center vents (broken vane)

## I. Bulletins
- [x] 57. TSB list: 92 entries, 12 recalls (pack F10). Recalls match `recalls.md`. Worth reading in full: A06-087 front brake judder, A07-045 low/soft pedal, A03-036 drifts right, A14-001 DTC P0139 (L4), A05-062 no upshift to 4th, A05-071 DTC P0973.
- Was: Honda service bulletin (TSB) list for this car, if Chilton has one. Free copy of the list is also on nhtsa.gov → Manufacturer Communications
