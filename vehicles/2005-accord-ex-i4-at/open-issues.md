# Open issues: 2005 Accord EX

Most urgent first. Update or close an item whenever something changes. Background is in
`log.md` and `sources/project-history-2026-10-21.md`.

**Status 2026-10-27 (owner): the car is drivable.** New right axle + new axle nut (owner,
last week) and new lower ball joint (Ben's) are in. Still open on the right front: the ABS
signal (item 3) and the grooved rotor/pads. Background: `plan-right-front-2026-10.md`.

## 0. RESOLVED 2026-10-27: right front grinding, loose bearing, stripped axle nut
- **Owner, 2026-10-27: car is drivable; the axle and axle nut issue is fixed** (new axle and new axle nut, installed by the owner the week of Oct 19–26; bearing play gone). The "do not drive / tow" warnings below are history, no longer in force.
- Still open from this item: the right front rotor was being grooved by the caliper; check the rotor and pads (not yet inspected after the fix). Optional: free re-check of bearing play at a shop.

History:
- Owner report: took a turn, came to a stop, loud screeching/grinding from the front. Details pending (which side, did the car stop on its own, does it repeat).
- Right front was apart on Oct 19 (ball joint separated, axle out and back in, sway bar link, ABS sensor area hammered); mudflaps recently added.
- (Was, until 2026-10-27) Do not drive until the right front is inspected.
- **Les Schwab inspection 2026-10-21, 139,032 mi (free suspension check, written notes):** "Recommend replace front right bearing because of movement and recommend replace CV axle due to CV axle not being tight and looks cross threaded." Owner declined and signed their waiver.
  - Owner's verbal summary: axle worn; bearing very loose, play lets the caliper rub the rotor (the noise); axle nut under-torqued and stripped.
  - Quote (valid to 2026-11-20): front bearing PRB510073 $128.48 · front hub MPB63085 $110.11 · right CV axle HO8176 $157.74 · axle install labor $148.99 · hub assembly replacement w/ press off rotor $232.99 · thrust-angle alignment $119.99 · tax $84.45 · **total $982.75**. Lower ball joint is **not** on the quote. Bearing/hub brand not shown.
- Likely link (UNVERIFIED): on this design the axle nut clamps the hub bearing, so a loose/stripped nut alone can cause bearing play. Driving on it may also have damaged the bearing. Ask whether play was judged with the nut loose.
- Loaner on the poster if DIY: Master Wheel Hub & Bearing Remover & Installer Kit 67213 (select stores). Bearing is believed press-in (UNVERIFIED: Chilton).
- (Was, until 2026-10-27) Do not drive: stripped, loose axle nut plus a loose bearing.
- 2026-10-27 (owner): new axle and new axle nut installed last week; owner reports no bearing play. If a re-check (wheel off the ground, rock it at 12 and 6 o'clock) confirms that, Les Schwab's "movement" was likely the loose nut and the bearing may not need replacing for play. It may still need replacing if its ABS magnetic ring is damaged (item 3).
- 2026-10-22 (owner): Ben's Auto Care will install customer-supplied parts for **$275 labor**. Scope (axle, bearing/hub press, ball joint, rotor/pads?), alignment and warranty not confirmed yet.
- 2026-10-27 (owner): that $275 turned out to be for the **lower ball joint only** (done). Axle and nut were done by the owner (above).
- 2026-10-21 (owner): the rubbing is cutting **deep grooves into the right front rotor**. Rotor and the right-side pads likely need replacing; the rotor and pads are not on the Les Schwab quote.

## 1. RESOLVED 2026-10-27: front axle nut
- **Owner, 2026-10-27: fixed. New axle nut on the new axle; car drivable.** Only loose end: the torque number used and its source weren't recorded (`log.md`). If it came from Chilton, add it to `specs.md`.

History:
- The owner torqued the right front axle nut to **181 lb-ft** when the old axle went back in (Oct 19).
- Past chats gave both 181 and 134 lb-ft (134 lb-ft = 181 N·m, so one is probably a unit mix-up). The owner's manual has no axle nut spec.
- Safety-critical spec: the real 4-cylinder number belongs in `specs.md` with its Chilton citation.

## 2. Right front: steering shake under hard acceleration + torn lower ball joint boot
- Symptom: shake only under hard acceleration, gone when coasting, no clunk. Suspect: inner CV joint; engine/transmission mounts second.
- 2026-10-21: owner says the shake is the same.
- New axle on hand, not installed: Parts Geek order #31-12567661, placed 2026-10-10, delivered 2026-10-19, $83.74 total. The emails say only "2005 Honda Accord CV Axle Assembly": **brand, part number and side (right/passenger) are not in them**. Read the box label before the job.
- **2026-10-27: lower ball joint replaced by Ben's Auto Care** with the owner's Moog K80228, $275 labor (`log.md`). Torn-boot part of this item is done; the shake and the axle are not.
- New Moog K80228 lower ball joint on hand (owner, 2026-10-21). Press-in joint: plan is an O'Reilly loaner press kit.
- Seller listings (COMMUNITY): K80228 is press-in, not greaseable, has a cotter pin hole, "includes mounting hardware", no instructions included.
- Do the ABS sensor (item 3) in the same job.
- Loaner tools (O'Reilly EverTough free loaner poster, photo 2026-10-21; numbers read from a worn photo, confirm at the counter): Ball Joint/U-Joint Press Set 67045 + **Honda Ball Joint Adapter Set 67049**; Master Ball Joint Installer/Remover Adapter Set 67310 (select stores); Axle Puller 67030 + Slide Hammer 67031; FWD Axle Puller Adapter 67102; Pitman Arm/Tie Rod Puller 67028; Tie Rod End Remover (non-damaging) 67008; 1/2" click torque wrench 67075 (range not on poster); axle nut sockets 30/32/34/36 mm (67038–67041).
- Worth knowing (UNVERIFIED, past chats): old ATF can also cause a shudder that feels like a CV problem. ATF change history is unknown (item 6).
- If the shake remains after the new axle: check the mounts.

## 3. ABS light, code 12-1 (since Oct 20)
- Past-chat reading: right front wheel speed sensor, noisy or intermittent signal, likely damaged by hammering on the knuckle. Meaning of 12-1 is UNVERIFIED; a library service manual has the Honda code chart.
- Normal brakes work; no anti-lock until fixed.
- Part from past chats: Honda 57450-SDA-A11 (UNVERIFIED; confirm by VIN at a Honda parts counter).
- **2026-10-27 (owner, relaying Ben's Auto Care):** Ben replaced the right front ABS sensor. ABS light still on; on a test drive the sensor "isn't getting a read" from the wheel. Ben suspects the tone ring. Still unknown: new code number, how "no read" was judged (live data?), sensor brand/part number, whether Ben has already replaced the hub bearing.
- **The "tone ring" on this car is most likely part of the hub bearing, not the axle.** MOTOR Magazine, "Foreign Service", Aug 2013, pp.12–16 (trade press, read 2026-10-27; not a Honda document): 2003-and-newer Accords usually use a wheel bearing with a built-in **magnetic encoder** (a flat brown ring on the bearing's inboard face) instead of a toothed tone ring. Brown side faces in toward the sensor, black rubbery seal faces out; the encoder holds a paper clip; installed backwards = no signal, and the bearing is usually ruined getting it back out. SKF also lists its 2003–07 Accord front bearing (FW48) as having an integrated tone ring (search listing only, article not opened). Confirm the design in Chilton.
- So "bad tone ring" = new hub bearing, which is already on the list (item 0). Suspects, cheapest to check first: (a) if Ben already put in a new bearing, was it installed brown side in, and does it have an encoder at all; (b) old bearing: play changes the sensor gap, and steel dust from the caliper grinding the rotor sticks to a magnetic encoder; (c) sensor wiring/connector damaged by the October hammering; (d) wrong or bad new sensor (Japan-built 57450-SDC-013 / SDH-003 said not to fit).

## 4. SRS (airbag) light on
- Was on before the passenger seat was removed; removing the seat adds codes of its own.
- Codes read with a MADDOX MRBT: SRS 61-10, E2-11, F1-11; ABS 61-1. Meanings from past chats are guesses (UNVERIFIED).
- Lead to check (free): recall **07V001000** (Honda A07-002, driver's seat position sensor harness) says a broken sensor wire turns the SRS light on. Whether that recall was done on this VIN, and whether it matches these codes, is unknown. Check the VIN at nhtsa.gov/recalls or ask a Honda dealer's service desk; open recalls are fixed free.
- **With the SRS light on, the airbags may not deploy in a crash.**
- Not known: whether the light was on before Sep 7, when the console came apart over the SRS unit.
- Plan from past chats: reinstall the passenger seat, clear codes, see which come back.
- Recalls: project history says no open recalls on the VIN. Confirm at <https://www.nhtsa.gov/recalls>.

## 5. Battery drain (status unknown)
- See `log.md` (Sep 8). 12.6 V at rest proves nothing on its own.
- Next: load test (free at many parts stores) and a parasitic draw test. Suspects: Bluetooth adapter, camera wiring.
- Battery: EverStart Maxx, made May 2025 (under warranty per owner).

## 6. Maintenance with no record (treat as overdue)
Order, shopping list and quantities: `plan-maintenance-catchup.md` (2026-10-25).
Intervals are from the manual (`specs.md`, OM pp.202–203). Severe schedule likely applies (short local trips).
- ATF: no record. Honda drain-and-refill method (OM p.220).
- Engine coolant: no record (120k mi / 10 yr first change).
- Brake fluid: no record (every 3 years).
- Drive belt: inspect (every 30k mi / 2 yr).
- Valve clearance: inspect at 110k mi, otherwise adjust only if noisy. Car is ~139k.
- Cabin and engine air filters: no record.
- Oil change: last one not recorded. Log the next one with mileage.
- Throttle body cleaning: unknown whether done.

## 7. Body and interior (not urgent)
- Front bumper cover cracked. Rear bumper divot and clear-coat crack. Hood rock chips to primer (check whether any reach bare metal before winter). Peeling clear coat in spots.
- Rear road noise since the deadener was lost.
- Tint: right rear door piece needs replacing.
- Backup camera monitor adhesive lets go in heat; keep it out of the passenger airbag zone.
- Center vent vane broken. Leather worn in areas.
- VTC actuator cold-start rattle (known K24 issue per past chats; UNVERIFIED). Not urgent.
