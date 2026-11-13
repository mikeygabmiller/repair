# Repair and maintenance log: 2005 Accord EX

Newest first. One entry per job, problem or inspection.

Entries before 2026-10-21 come from the owner's project history
(`sources/project-history-2026-10-21.md`, compiled from past chats). What was done is the
owner's record. Specs used in those jobs came from past chats and are **not** verified
unless `specs.md` lists them.

## 2026-11-06 (reported): slid into a small ditch (date and mileage not recorded)
- Owner: braking while turning at the bottom of a steep hill, slid into a small ditch, came back onto the road. Since then a low-speed back-and-forth wheel shake and worse alignment. ABS was out at the time (`open-issues.md` item 4). Triage: `open-issues.md`, item 11.

## 2026-11-05: Bluetooth (Spotify) max volume too quiet on the Eonon (reported; mileage not recorded)
- Owner: Spotify over Bluetooth is not very loud even at max volume. Looked in the unit's sound settings, no fix; couldn't find an adjustable EQ.
- Eonon lists a 48-band graphic EQ for this unit (`mods/plan-head-unit-2026-10.md`), so it should exist; menu location not confirmed.
- Next: FM-vs-Bluetooth split test, phone/Spotify volume settings, find the EQ/DSP app, ask Eonon support for the menu path. Not known yet: whether the factory radio was louder.

## 2026-11-04: phone USB drops when aux lights switch (reported; mileage not recorded)
- Owner: turning the aux high beams on or off (high-beam stalk) briefly disconnects the phone's USB connection to the Eonon head unit. Started the day after the Eonon install. Triage: `open-issues.md`, item 9.

## 2026-11-03: Eonon HAC1X7A head unit installed (owner; mileage not recorded)
- Owner: installed. Plan and wiring sheet: `mods/plan-head-unit-2026-10.md`.
- Not recorded yet: mileage, harness #29 (single-zone adapter) used or not, how reverse trigger (#2) and the camera were wired, results of the plan's test list (climate, defrost, wheel buttons, FM, calls, camera, boot time), post-install draw test. Factory radio and climate panel kept for resale?

## 2026-10-31: check engine light, code P0685 (mileage not recorded)
- MADDOX: MIL on, P0685 "ECM/PCM Power Relay Control Circuit/Open", stored/confirmed. App suggests "replace main relay" (not a diagnosis).
- Came on right after the aux-light install (entries below). Triage: `open-issues.md`, P0685 item.
- Same day: owner found **one battery terminal loose** (which one not recorded). Tighten, clear, rescan after a few days of driving.

## Reported 2026-10-31: auxiliary driving lights installed (owner; mileage not recorded)
- Owner: "I added these to my car." Which lights is not confirmed: the last ones discussed were Nilight 18 W 4" spot pods, 2-pack with harness (Amazon B00Q8CF7DE; listing: 18 W / 1.5 A each).
- Not recorded yet: exact light model, mount location and bracket (hood-gap clamp Nilight B0824RPMDB was in the cart), mounted height (WA maximum 42 in. for auxiliary driving lamps, RCW 46.37.180(4)), which harness feeds them (the installed HF 64330 kit or the Nilight harness), fuse rating (HF manual 64330 p.4: two lights of 17–24 W each = 7.5 A), trigger (high beams or a switch), tethers.
- Re-check mount screws, tethers and aim after the first ~10 miles.

## Reported 2026-10-29: aux-light relay harness installed, light returned (owner; mileage not recorded)
- Owner test-fit a Harbor Freight Roadshock 6" LED spot (1,050 lm claimed), triggered by the high beams through a Harbor Freight Roadshock Light Bar Wiring Kit (item 64330). Result: "not a big difference"; the light went back to the store.
- Relay in the kit: RAYFIRE JD1912, 12 V coil, 40 A NO / 30 A NC (read off the relay, owner photo). 4-pin or 5-pin not confirmed.
- The relay harness is still installed with nothing on its output. Not recorded yet: which wire was tapped for the trigger (likely WHT/RED at the HB3 high-beam plug; meter-test result not reported), Y-adapter or Posi-Tap, fuse rating in the holder, ground point, wire gauge.
- Until a light is attached: the power lead to relay pin 30 is live at all times, and the output lead (pin 87) goes live with the high beams. Pull the fuse and keep the open ends insulated.

## 2026-10-28: shake around 60 mph reported (mileage not recorded)
- Owner: "car is pretty shaky around 60 mph." Coast test the same day: coasting at ~60 is "kind of shaky", **much worse on the gas**.
- Triage plan: `open-issues.md`, shake item.

## Reported 2026-10-27: low-beam bulbs replaced (owner; mileage not recorded)
- Owner put in **Sylvania SilverStar Ultra 9006** low beams, bought at O'Reilly ("$35 each"). Pack: 2 halogen lamps, 12.8 V 55 W (photo: `sources/photos/2026-10-27-bulb-purchase.jpg`). The manual rates the low beam HB4, 12 V 51 W (VERIFIED: OM p.275); 9006 is HB4, rated at a different test voltage.
- Result (owner, same day): "I don't notice a very big lighting difference." That chat sent him to check, cheapest first: bulb fully twisted in, lens haze, aim, voltage at the headlight plug. The Nov 12 plan in `mods/lighting-upgrades.md` picks it up from there.
- Bought on the same trip, **install not recorded**: Sylvania SilverStar 168 2-pack (14 V 4.9 W; license plate / trunk) and two Sylvania LED DE3175 cool white festoons (12.8 V 0.5 W; dome / map). The dome bulb was measured the day before as a 31 mm festoon (`parts.md`), so the DE3175 size fits it.
- Not recorded: mileage, whether the old low beams were kept (resale rule), where the 168s and LEDs went.
- Filed 2026-11-13 from the Oct 27 chat, which said it would log the install and never did.

## Reported 2026-10-27: Ben's Auto Care, right front lower ball joint + ABS sensor (mileage not recorded)
- **Lower ball joint replaced** with the owner's Moog K80228: **$275 labor**, about 1.5 hours by Ben's estimate (owner, 2026-10-27).
- **Right front ABS sensor replaced.** The old sensor **snapped while the ball joint was being pressed** out of the knuckle; Ben ordered a replacement for **$40, at his cost (no markup)** per Ben. Brand/part number not recorded yet (cross-check against 57450-SDA-A11).
- Ben was waiting on a **grease fitting (zerk)** for the ball joint. Seller listings say K80228 isn't greaseable (COMMUNITY): ask whether the K80228 went in, and whether the fitting hole is plugged.
- Date of work not recorded. Not known yet: whether the axle, the stripped axle nut or the loose bearing were touched.
- Result: ABS light still on. Ben: on a test drive the sensor isn't getting a reading from the wheel; suspects the tone ring. See `open-issues.md`, ABS item.
- 2026-10-27: car picked up. Ben's final word: ABS fault is the damaged tone ring on the right front wheel bearing (compared with the left side). Quoted $544.04 for an NSK bearing installed (`open-issues.md`, ABS item). Owner's status summary listed axle, axle nut and ball joint as new; **ABS sensor replacement to be confirmed** against the invoice. Invoice goes in `receipts/`.

## ~2026-10-24 to 10-26: front passenger seat reinstalled by owner (mileage not recorded)
- All yellow SRS connectors plugged back in by the owner. Unknown whether the battery was disconnected first. Seat bolt torque not recorded (spec must come from the service manual).
- Afterward the Side Airbag Off indicator lights briefly at start, then goes out. That's the normal key-on check (VERIFIED: OM p.31).
- Cleared SRS codes with the MADDOX. Rescan shows the same codes: 61-10, E2-11, F1-11. See `open-issues.md`, SRS item.

## 2026-10-24: O'Reilly scan tool would not connect to the OBD port (mileage not recorded)
- Employee tried ~5 min, said it might be a wiring problem. The owner's MADDOX read codes through the same port before and after (Oct 2026), so the store's tool is the likelier problem.

## ~2026-10-23: right front repair reported finished; ABS light stays on (mileage not recorded)
- Owner: "fixed everything" (axle/bearing/ball joint work). Later reports (10-27) show the ball joint was done at Ben's on 10-27, so this referred to the axle job below.
- ABS code cleared with the MADDOX MRBT; rescan showed no ABS codes, but the light stayed on. The MADDOX may not reach the ABS unit at all (Harbor Freight's coverage tool showed nothing for this car).

## 2026-10-23: Chilton Library lookups (no work on the car)
- Claude in Chrome pulled specs, ABS/SRS code meanings, parts numbers and the NHTSA VIN recall check. Record: `sources/chilton-2026-10-23.md`; numbers in `specs.md` and `parts.md`.

## 2026-10-22 (reported): right front CV axle replaced, new axle nut (owner; mileage not recorded)
- Owner, 2026-10-22: new axle "in and working." Axle is the Parts Geek order #31-12567661 (brand, part number not recorded; read from the box or the axle tag).
- Same day (owner): screech/rubbing gone, shake under acceleration gone; keeping the rotor and pads. Nut reply was voice-to-text ("new axle not talk to spec").
- Owner, 2026-10-27: confirmed new axle and new axle nut; says the bearing now has no play.
- Lower ball joint was **not** replaced in this job (its boot was completely gone by 10-22); Ben's replaced it 10-27 (above).
- Not recorded: mileage, axle brand/part number, nut part number, torque used and its source, whether the nut was staked. (Owner closed the torque question 2026-10-28.)
- 2026-10-28: the shake is back, or a new one started (entry above).

## Date unknown: mudflaps / splash guards installed
- Owner confirmed installed (2026-10-21). Brand, part number, date and mileage not recorded yet.
- Past-chat pick was A-Premium SG023; OEM numbers never confirmed (see `parts.md`).

## 2026-10-20: window tint, in progress (~138.9k)
- 35% pre-cut kit, all 4 doors (PrecutAutoTint, $28.99), Black Magic install kit.
- Front window good using the heat-shrink method. Right rear piece creased: needs a replacement piece.
- Lesson: shrink fingers with heat before squeegeeing; creases are permanent.

## 2026-10-20: ABS light on, code 12-1 (~138.9k)
- Came on the day after the axle attempt; came back after clearing. See `open-issues.md`.

## 2026-10: right front lower sway bar work
- Done around the axle job. ABS light came on afterward.

## 2026-10-19: right front CV axle replacement attempt, failed (~138.9k)
- Lower ball joint taper would not separate (penetrant, pickle fork, hammer). Inner CV would not pop out of the transmission.
- Old axle reinstalled. Owner torqued the axle nut to 181 lb-ft. **That number is unverified; see `open-issues.md`.**
- Pickle fork tore the lower ball joint boot → whole ball joint to be replaced (Moog K80228 ordered, due Oct 23).
- Tools bought: 32 mm socket (test-fit confirmed), EverTough torque wrench, 18" pry bar, 2 lb dead blow, PB Blaster, magnetic tray. McGraw 70479 air hammer chosen.
- Lessons (COMMUNITY/past chats): hammering a taper wedges it; use a screw-type puller under tension plus a sharp hit on the knuckle where the stud passes, heat as backup (keep flame off the ABS wire, brake hose, boots). Free the ball joint and hub before popping the inner CV. Hitting near the knuckle can damage the ABS sensor. Don't start this job the night before a work day.

## 2026-10-18: spark plugs (138,943 mi)
- Installed Bosch 9614 Double Iridium (FR6LII330X), $60 AutoZone. Pre-gapped. Torqued 13 lb-ft, cold engine, no anti-seize (torque from past chats: UNVERIFIED).
- Old plugs looked healthy.
- Manual's factory plug: NGK IZFR6K-11 / DENSO SKJ20DR-M11 (OM p.275). If misfires or rough idle appear, go back to the NGK.

## 2026-10: P0507 (idle higher than commanded) no longer an issue
- Came with the car. Throttle body cleaning status still unknown (see `open-issues.md`).

## 2026-10: gas spill cleanup
- Fuel can leaked in the cabin and dissolved the asphalt deadener under the rear seat; scraped out. Road noise up since.

## 2026-09 (mid): front wiper blades
- Costco BFGoodrich Beam, 26" driver, 18" passenger (sizes confirmed by fit).

## 2026-09-08: battery drain episodes
- After a jump it died ~5 min after shutoff. After a long key-on session: too weak to crank, radio still lit, 12.6 V at rest.
- Earlier: 10.9 V after a failed crank, 11.8 V after rest, 14 V charging at idle and under load.
- Load test and parasitic draw test never done. See `open-issues.md`.
- 2026-10-26: owner reports no drain currently.

## 2026-09-07 to 09-08: 14-pin Bluetooth adapter (mileage not recorded)
- Amazon B08JQ9G2LP, $53.94, plugged into the factory head unit in place of XM. Working Sep 8.
- Dash access: remove the center holder (coin tray / 12 V socket) screws first; pocket pushes in at the bottom and pulls at the top. Radio/climate come out as one pod (upper vent panel, 3 screws behind it, 2 bottom screws).
- Center console came apart and exposed the SRS control unit on the floor tunnel (three yellow connectors).
- That night the adapter lost power after the mic install; fix not recorded. Head unit only detects the adapter at power-up.

## ~2026-09-07: center vent vane removed
- Left center vent (left of the hazard button): broken vane with the slider tab removed; other half lost.

## 2026-08-26: throttle body cleaning, **status unknown**
- Planned to clean in place with CRC Throttle Body cleaner. No record it was done; other notes say never cleaned.

## 2026-08-24: rear bumper first repair try
- Sanding the divot didn't work (low spots get filled, not sanded). Damage is paint only: cracked clear and a divot, plastic not torn.

## 2026-08 (~137k): purchase and first changes
- Bought at ~137,000 mi with code P0507.
- Backup camera kit installed (plate-frame camera + 4.3" monitor, no drilling).
- Front passenger seat and rear seatbacks removed for gear space.
- Wheels/tires deep-cleaned.

## 2026-08 to 2026-10: paint correction, ceramic coating, trim restoration
- Coating on the car: **CarPro CQuartz Lite** (owner confirmed 2026-10-21; settles the CanCoat vs CQuartz question). Use the same product on any resprayed panel.
