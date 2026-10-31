# Plan: Eonon head unit install (bought 2026-10-26)

Written 2026-10-26 from the purchase chat. This is a **checklist and wiring sheet**, not a
procedure. Once it's installed, the job goes in `log.md` and anything worth reusing goes
in `procedures/`.

## What was bought

- **Eonon HAC1X7A**, 10.1" Android 14, wired + wireless CarPlay / Android Auto, made for
  2003–2007 Accord. Bundle **with a backup camera**, about **$200** (owner, 2026-10-26).
  Tax, seller (eonon.com or other) and order number: not recorded yet.
- Eonon's page lists 4 GB RAM / 64 GB, RK3562 4-core, built-in DSP, **90-day returns**
  (eonon.com product page, read 2026-10-26). Third-party listings say 3 GB / 32 GB:
  check the label on the unit.
- Why this one over the $139 Amazon "SailingTravel" unit: known brand, more memory, 90-day
  returns, and the wiring diagram shows it plugs into the factory climate panel with a
  single-zone adapter (below).

## Before installing

1. **Climate panel type** (decides harness #29). The owner's manual says automatic dual-zone
   climate is only on EX-L and EX-V6 (VERIFIED: OM p.106). The VIN decodes as plain "EX"
   (OFFICIAL RECORD: NHTSA vPIC, 2026-10-26), but `profile.md` says "auto climate".
   Look at the panel: two dials + AUTO / DUAL / OFF = dual-zone; three plain dials = single-zone.
2. **Ask Eonon's chat** (get answers in writing):
   - Photo of the climate panel: should #29 be connected, and does climate info show on screen?
   - Does the factory FM antenna plug fit, or is an adapter needed (which one)?
   - Is the dash frame built onto the unit?
   - Does the CAN decoder read reverse on a 2005 Accord, or must #2 go to the reverse lights?
   - Does it ship with the Google Play Store?
3. **Parasitic draw test with the old setup first** (`open-issues.md` item 5), so a later
   drain can be pinned on the right thing.
4. Plan a full day, not the night before work. **No defrost until the radio/climate pod is
   back in**, so the car can't be driven safely mid-job.

## Wiring sheet (from Eonon's wiring diagram, product page, 2026-10-26)

| # | Wire | Plan |
|---|---|---|
| 6 + 1 | Power cable (blue plug) + box | Plugs into the factory radio connectors. Compare plugs before anything else |
| 30 | Air conditioning panel interface | Factory climate panel plugs in here. Eonon warns a wrong connection causes "malfunction or inoperability" |
| 4 | Air conditioning plug | To #30, per diagram |
| 29 | Single-zone conditioner adapter | **Dual-zone car: do not connect** (Eonon's note). Single-zone: use it |
| 5 → 19 | RX/TX | Connect to each other, per diagram |
| 2 | Reverse trigger | +12 V only in reverse. The factory radio plug likely has no reverse signal (UNVERIFIED: Chilton Library wiring diagram). Run to the reverse-light feed in the trunk; check whether the camera cable has a bundled red trigger wire |
| 22 / 24 | Backup camera input / +12 V for camera | Bundled camera. Mount must be no-drill (plate frame or plate screws) |
| 8 | External mic | Route along the steering column cover, not the A-pillar (curtain airbags) |
| 28 | GPS antenna | Under the dash top or behind trim, away from metal |
| 7 | AMP | Leave capped unless the car has a factory amp (UNVERIFIED) |
| 3 | Steering wheel control 2 | Likely unused; set up buttons in the unit's settings |
| 23 | Brake/shift control | Follow Eonon's manual |
| 9–18 | Sub, front camera, AUX, audio outs | Unused; cap with heat shrink |

Splices: soldered and heat-shrunk, or Posi-Tap at the reverse light. No cutting factory wiring.

## Install notes from the Sep 7–8 Bluetooth job (`log.md`)

- Disconnect the battery. Coin tray (12 V socket) screws first; pocket pushes in at the
  bottom and pulls out at the top; radio and climate come out as one pod.
- **The SRS unit is on the floor tunnel under the console.** Keep knees and tools off its
  three yellow connectors.
- **Test everything before trim goes back:** defrost and climate display, steering buttons,
  FM, Bluetooth calls, camera in reverse, boot time. Then repeat the draw test.

## Keep for resale

Factory radio, the B08JQ9G2LP Bluetooth adapter, the old plate-frame camera and its 4.3"
monitor: box them and keep them with the car.
