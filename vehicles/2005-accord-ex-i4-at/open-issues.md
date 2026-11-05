# Open issues: 2005 Accord EX

**Only what is broken or unfinished now**, most urgent first. Each item gives its status,
what's known and the next steps, cheapest first. When an item closes, move it to
"Closed recently" with the date, put the job in `log.md`, and put its details in
`issues-history.md`. Back story for every item: `issues-history.md`. Files written
before 2026-10-28 cite "item 0–6" by the old numbering, which is in `issues-history.md`
Part 1.

Last updated 2026-11-05. **The car is drivable.** Last known mileage: 139,032 (2026-10-21).

## 1. SRS (airbag) light: codes 61-10, E2-11, F1-11. Dealer or SRS shop only, never DIY
- **With the SRS light on, the airbags may not deploy in a crash.** This is the most
  important safety item even though the car drives normally.
- **2026-10-26:** passenger seat reinstalled (owner plugged the connectors), codes cleared
  with the MADDOX, **the same three came back**. So the missing seat isn't what sets these
  codes.
- What the codes may mean (none confirmed for this exact car):
  - 61-10: open circuit in the **driver's** seat belt buckle switch. Chilton (Hybrid
    article) and two community code lists agree.
  - E2-11 / F1-11: community code lists say "passenger airbag deployed" and "driver airbag
    plus driver belt tensioner deployed". Chilton (Hybrid article) puts them in a group
    about deployed airbags and tensioners.
  - **Conflict:** if they were real crash records, the light would have been on since the
    crash. It was **off when the car was bought** (owner) and no airbag has gone off while
    the owner has had it. So the MADDOX may be misreading the codes. Only a Honda-level
    scan settles it.
- Recalls: **0 open recalls on this VIN** (OFFICIAL RECORD: nhtsa.gov/recalls, checked
  2026-10-23 and 2026-10-26; Honda MyGarage agrees). That doesn't show which airbag
  recalls were *done*, or when.
- Next, cheapest first:
  1. Free: call Honda (1-888-234-2138) with the VIN and ask which airbag recalls were done
     on this car, when and where. Takata work means a dealer had both front airbags apart.
  2. Free look: does the driver's belt pull out and retract normally? Does the date on the
     driver belt's label make sense next to the build date on the door jamb?
  3. A Honda dealer or SRS-capable shop reads the codes with a Honda-level tool. Ask them
     about bulletins A02-052 (OPDS initialization), A07-002 (seat position sensor harness)
     and A20-010 / A20-015 (inflator warranty extensions).
  4. While it's there: the passenger seat bolts also anchor that seat's belt buckle, and
     the torque used when it went back in wasn't recorded. Have the shop check them.

## 2. Check engine light: P0685, ECM/PCM power relay control circuit (2026-10-31)
- **2026-10-31 (owner, MADDOX screenshot):** MIL on, P0685 stored/confirmed. The app's
  "most likely fix: replace main relay" is the app's guess, not a diagnosis. Mileage,
  freeze frame and any symptoms (stall, hard start, cut-out) not recorded yet.
- What it means on this car (COMMUNITY: Honda job aid quoted by ricksfreeautorepairadvice.com
  and iamcarhacker.com, covers 2003–12 Accord; not yet checked in Chilton): the engine
  computer turns on PGM-FI main relay 1 and watches its own power feed (IGP). If that feed
  drops out or sags too low while the relay is commanded on, the code sets. Shops report a
  weak battery or bad charging as the most common cause, then the main relay (cracked
  solder joints inside), then fuses/wiring/grounds.
- **Timing:** it showed up right after the aux-light relay harness (2026-10-29) and the aux
  lights (2026-10-31) went in (`log.md`). A loose battery terminal, a ring terminal stacked
  on a battery post, a disturbed ground or a tapped fuse can drop the computer's power for
  a moment and set exactly this code (UNVERIFIED reasoning; check below).
- **2026-10-31 (owner): one battery terminal found loose** (which one, and whether it was
  the one the light harness connects to, not recorded). Leading suspect now. Next: tighten,
  clear the code, drive a few days, rescan. If P0685 stays away, close this item.
- **2026-11-04:** the phone's USB link to the head unit drops each time the aux lights switch on or off (item 9). Same kind of momentary power/ground dip; check the two together.
- Recall 07V097000 (fuel pump relay = PGM-FI main relay 2) shows **not open** on this VIN.
- Next, cheapest first:
  1. Screenshot the **Freeze Frame** before erasing anything (shows rpm, temp, speed when
     it set).
  2. Battery terminals: tight, clean, nothing loose under the clamps. Wiggle each clamp by
     hand; it must not turn. Check the new harness's power and ground connections.
  3. Confirm no fuse was pulled or tapped for the lights, and that nothing touches the
     interior **#23 IGP (PGM-FI ECU) 7.5 A** fuse (VERIFIED: OM p.269) or the under-hood
     main fuses (OM p.268).
  4. Free battery + charging test at a parts store (battery under warranty, item 6).
  5. Clear the code and drive normally for a few days. Comes back with everything tight →
     test the main relay with the factory procedure (Chilton through the library), not by
     guessing.

## 3. Shake around 60 mph, much worse on the gas (reported 2026-10-28)
- **2026-10-28 (owner, coast test):** coasting at ~60 is "kind of shaky"; **much worse on
  the gas**.
- Owner reports conflict over time: shake under hard acceleration before Oct 21 → "gone"
  after the new right axle went in (2026-10-22) → shaky at 60 now (2026-10-28). So either
  the new axle didn't fix it, or something new started.
- Reading (UNVERIFIED, Claude's reasoning): two separate things. A mild shake that's there
  when coasting points at something that turns with the wheels (tire, wheel balance,
  bearing). The bigger shake under throttle points at the drivetrain under load
  (transmission torque converter shudder, an inner CV joint on either axle, engine or
  transmission mounts).
- Next, cheapest first:
  1. Lug nuts: re-torque to **80 lbf·ft, crisscross** (VERIFIED: OM p.250). The right
     front wheel has been off several times.
  2. Narrow it down on a drive: at what speeds it starts and stops; steering wheel or seat;
     light vs hard throttle. Write the answers here.
  3. Have a shop confirm the new right axle's inner joint is fully seated in the
     transmission (Chilton checklist item 15).
  4. Tires: look for bulges and uneven wear; get a wheel balance at a tire shop.
  5. **ATF drain and refill**: overdue anyway (`maintenance.md`). NHTSA complaints
     10299703 and 11076272 describe a 55–65 mph light-throttle shudder on this model
     (COMMUNITY). Honda ATF only (`specs.md`).
  6. Engine and transmission mounts (shop).
- No Honda bulletin about this found yet. Only part of the bulletin title list is saved
  (`sources/chilton-pack-F-2026-10-27.md`); the free full list is on nhtsa.gov under the
  car's "Manufacturer Communications".

## 4. ABS light: right front wheel bearing's encoder is damaged. DEFERRED by owner, 2026-10-28
- Normal brakes work; anti-lock doesn't until this is fixed.
- **Diagnosis (Ben's Auto Care, 2026-10-27):** the "tone ring" on the right front wheel
  bearing is damaged (compared with the left). On this car the tone ring is the bearing's
  built-in **magnetic encoder**, so the fix is a new **wheel bearing** (Chilton V6/Hybrid
  articles; MOTOR Magazine Aug 2013; details in `issues-history.md`).
- Already done: right front ABS sensor replaced at Ben's (the old one snapped while the
  ball joint was being pressed; $40 at Ben's cost). Brand and part number: on the invoice,
  not recorded yet.
- Quotes: **Ben's $544.04** (NSK bearing, labor $404.25) · **Les Schwab ≈$516** incl. a
  new hub, valid to **2026-11-20**, bearing brand not shown. Honda bearing 44300-TR4-A51
  (`parts.md`).
- When it's picked back up: do it in the same visit as item 5 (the rotor comes off for the
  bearing anyway). The bearing's brown encoder side faces the inside of the knuckle; keep
  metal debris and magnetic tools off it (Chilton, Hybrid article).
- Separate lead: the old ABS code 61-1 means low voltage at the ABS unit (Chilton, V6
  article). See item 6.

## 5. Right front rotor and pads: grooved, not checked since the repair
- The loose bearing let the caliper cut **deep grooves** into the right front rotor
  (owner, 2026-10-21). Owner planned to keep the rotor and pads (2026-10-22).
- Next (free): measure the rotor's thickness at the grooves. The minimum is usually cast or
  stamped on the rotor itself (Tier 1; read it). Chilton gives **0.830 in** minimum, but
  two readings of that table disagree on whether that row is the 4-cylinder (`specs.md`).
  Pads: minimum lining **0.060 in** (VERIFIED: Chilton). Replace pads as a front pair.

## 6. Battery and charging: no drain since 2026-10-26, cause never found
- **2026-10-26 (owner): no battery drain now.** The September episodes are in `log.md`.
- If it comes back: free load test and charging test at a parts store, then a parasitic
  draw test. Old suspects: the Bluetooth adapter, the camera wiring.
- Keep new add-ons on key-on power, so a stuck accessory can't flatten the only car.
- Battery: EverStart Maxx, made May 2025 (under warranty per owner).

## 7. Maintenance with no record
Everything with no dated record counts as overdue. Status, intervals and what's due next:
`maintenance.md`. Order, shopping list and the day plan: `plans/2026-11-catch-up-maintenance.md`. First job:
oil and filter (`procedures/accord-2005-oil-change.md`).

## 8. Body and interior (not urgent)
- Front bumper cover cracked. Rear bumper divot and clear-coat crack. Hood rock chips to
  primer (check whether any reach bare metal before winter). Peeling clear coat in spots.
- Rear road noise since the deadener was lost.
- Tint: right rear door piece needs replacing.
- Backup camera monitor adhesive lets go in heat; keep it out of the passenger airbag zone.
- Center vent vane broken. Leather worn in areas.
- VTC actuator cold-start rattle (known K24 issue per past chats; UNVERIFIED). Not urgent.

## 9. Phone USB connection drops when the aux lights switch on or off (reported 2026-11-04)
- **Owner, 2026-11-04:** turning the aux high beams on *or* off briefly disconnects the
  phone's USB connection; the USB plug is wired into the head unit.
- Head unit is the **Eonon HAC1X7A, installed 2026-11-03** (owner). Aux lights come on
  with the **high-beam stalk** (no cabin switch), so the factory high beams switch at the
  same moment. Started the day after the install, so the Eonon's own power/ground hookup
  is a suspect too. Lights' ground point: not recorded yet.
- Two likely causes (UNVERIFIED, Claude's reasoning): (a) a supply or ground dip when the
  light current switches (fits the loose battery terminal and P0685, item 2); (b) the
  relay coil's turn-off spike (RAYFIRE JD1912; diode inside not confirmed) coupling into
  the head unit or the USB cable through wiring routed behind the dash.
- Next, cheapest first:
  1. Battery clamps tight (must not turn by hand); light harness ring terminal on top of
     the clamp, not between post and clamp. Lights grounded at battery negative or bare
     body metal, not shared with the head unit ground.
  2. Three-step split test, flashing the high beams each time:
     a. Aux fuse pulled (relay and lights dead). Still drops → not the aux lights; it's
        the factory high-beam load plus a weak connection: battery clamp, or the Eonon's
        power/ground (connectors fully latched, any splices).
     b. Fuse in, lights unplugged at the DT plug. Drops → relay coil spike.
     c. Drops only with lights plugged in → light current (supply/ground).
  3. Try the CarPlay/AA USB cable from the Eonon box and a short good phone cable.
  4. Relay cause: diode-suppressed relay, or a diode across the coil on the aftermarket
     harness (stripe to the + / pin-86 side; check the relay's printed diagram). Backwards,
     it shorts the high-beam trigger and can blow the high-beam fuse.
  5. Workarounds: wireless CarPlay/AA; ferrite clamp on the USB cable (COMMUNITY).

## 10. Backup camera not showing on the Eonon (reported 2026-11-05)
- **Owner, 2026-11-05:** "all the wires are confirmed connected right, it's still not
  coming on." Not recorded yet: whether the screen switches at all in reverse (black/blue/
  "no signal") or stays on the normal screen; which camera (new Eonon bundle or the old
  plate-frame one); where the trigger (#2) and camera power are tapped; mileage.
- Owner is buying a multimeter (2026-11-05) for this.
- Next, cheapest first (Claude's diagnostic order, UNVERIFIED for this unit):
  1. Reverse lights actually light in R (key on). If not, the tapped feed is dead.
  2. Does the screen switch in R at all? No → trigger side (#2 voltage, Eonon reverse
     setting, CAN decoder). Yes but black → camera power, ground, video, or format setting.
  3. Eonon camera settings: camera format (AHD 720p/1080p vs CVBS, NTSC/PAL) must match
     the camera; check the camera cable for an AHD/CVBS select loop (COMMUNITY).
  4. Meter, in R: +12 V at Eonon #2 and at camera power; power off: camera ground to body,
     video cable end to end.
  5. Ask Eonon's chat (written answer) with the camera model and a photo of the settings.

## Loose ends to record (no action needed, just write them down when known)
- From Ben's invoice (2026-10-27): date, mileage, ABS sensor brand and part number,
  whether the owner's Moog K80228 went in. Ben was waiting on a **grease fitting** for
  the ball joint, but seller listings say K80228 isn't greaseable (COMMUNITY): ask which
  joint went in, and whether the fitting hole is plugged.
- From the axle job (~2026-10-22): axle brand and part number (box label or axle tag),
  mileage.
- O'Reilly's scan tool wouldn't connect to the OBD port (2026-10-24). Probably their tool:
  the owner's MADDOX worked through the same port on ~2026-10-26. If another tool fails,
  check the fuses (OM pp.268–269 don't name one for the port; Chilton wiring diagram does).

- Eonon install (2026-11-03): mileage; harness #29 used or not; reverse trigger and camera
  wiring (spliced where?); whether everything in the plan's test list works.

## Closed recently (details in `issues-history.md`)
- **2026-10-28: front axle nut torque. Closed by the owner; don't raise it again** unless
  the owner asks or a new symptom points at it (clunk, wheel play, noise from the right
  front).
- **2026-10-27: right front grinding, loose bearing, stripped axle nut.** New right axle
  and new axle nut (owner, ~2026-10-22); bearing play gone (owner).
- **2026-10-27: torn lower ball joint boot.** Lower ball joint replaced at Ben's.
