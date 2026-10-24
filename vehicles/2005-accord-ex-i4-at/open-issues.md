# Open issues: 2005 Accord EX

Most urgent first. Update or close an item whenever something changes. Background is in
`log.md` and `sources/project-history-2026-10-21.md`.

## 0. NEW 2026-10-21: loud screech/grinding from the front in a turn while stopping
- Owner report: took a turn, came to a stop, loud screeching/grinding from the front. Details pending (which side, did the car stop on its own, does it repeat).
- Right front was apart on Oct 19 (ball joint separated, axle out and back in, sway bar link, ABS sensor area hammered); mudflaps recently added.
- **Do not drive until the right front is inspected.**
- **Les Schwab inspection 2026-10-21, 139,032 mi (free suspension check, written notes):** "Recommend replace front right bearing because of movement and recommend replace CV axle due to CV axle not being tight and looks cross threaded." Owner declined and signed their waiver.
  - Owner's verbal summary: axle worn; bearing very loose, play lets the caliper rub the rotor (the noise); axle nut under-torqued and stripped.
  - Quote (valid to 2026-11-20): front bearing PRB510073 $128.48 · front hub MPB63085 $110.11 · right CV axle HO8176 $157.74 · axle install labor $148.99 · hub assembly replacement w/ press off rotor $232.99 · thrust-angle alignment $119.99 · tax $84.45 · **total $982.75**. Lower ball joint is **not** on the quote. Bearing/hub brand not shown.
- Likely link (UNVERIFIED): on this design the axle nut clamps the hub bearing, so a loose/stripped nut alone can cause bearing play. Driving on it may also have damaged the bearing. Ask whether play was judged with the nut loose.
- Loaner on the poster if DIY: Master Wheel Hub & Bearing Remover & Installer Kit 67213 (select stores). Bearing is believed press-in (UNVERIFIED: Chilton).
- **Do not drive: stripped, loose axle nut plus a loose bearing. Tow.**
- 2026-10-22 (owner): Ben's Auto Care will install customer-supplied parts for **$275 labor**. Scope (axle, bearing/hub press, ball joint, rotor/pads?), alignment and warranty not confirmed yet.
- 2026-10-21 (owner): the rubbing is cutting **deep grooves into the right front rotor**. Rotor and the right-side pads likely need replacing; the rotor and pads are not on the Les Schwab quote.

- **2026-10-23 (owner): "fixed everything."** Who did the work, date, mileage, parts (axle brand/number, bearing/hub, ball joint, ABS sensor?, rotor/pads), axle nut torque used and alignment: **not recorded yet**. Close this item and log the job once those are in.

## 1. Front axle nut torque is unverified, and the car is being driven on it
- The owner torqued the right front axle nut to **181 lb-ft** when the old axle went back in (Oct 19).
- Past chats gave both 181 and 134 lb-ft (134 lb-ft = 181 N·m, so one is probably a unit mix-up). The owner's manual has no axle nut spec.
- **Chilton (2026-10-23):** only the **Hybrid** version has the spindle nut: 24 × 1.5 mm, 245 N·m (181 lbf·ft). The 4-cyl parts catalog lists a **22 mm** nut, and the owner's 32 mm socket fits (36 mm too big). So the Hybrid number is probably for a different nut. UNVERIFIED (Claude's math): 181 N·m = 134 lbf·ft, which would fit the "unit mix-up" theory. If the 4-cyl spec is lower than 181 lbf·ft, the Oct 19 nut was over-tightened. That nut has since been called stripped/cross-threaded by Les Schwab anyway.
- **Safety-critical. Still need the real 4-cylinder spec.** Free: a Honda dealer service desk (read from Honda service info by VIN), or the Chilton halfshaft or torque-spec pages that name the 4-cylinder. New nut every time (Chilton, Hybrid article).

## 2. Right front: steering shake under hard acceleration + torn lower ball joint boot
- Symptom: shake only under hard acceleration, gone when coasting, no clunk. Suspect: inner CV joint; engine/transmission mounts second.
- 2026-10-21: owner says the shake is the same.
- New axle on hand, not installed: Parts Geek order #31-12567661, placed 2026-10-10, delivered 2026-10-19, $83.74 total. The emails say only "2005 Honda Accord CV Axle Assembly": **brand, part number and side (right/passenger) are not in them**. Read the box label before the job.
- New Moog K80228 lower ball joint on hand (owner, 2026-10-21). Press-in joint: plan is an O'Reilly loaner press kit.
- Seller listings (COMMUNITY): K80228 is press-in, not greaseable, has a cotter pin hole, "includes mounting hardware", no instructions included.
- Do the ABS sensor (item 3) in the same job.
- Loaner tools (O'Reilly EverTough free loaner poster, photo 2026-10-21; numbers read from a worn photo, confirm at the counter): Ball Joint/U-Joint Press Set 67045 + **Honda Ball Joint Adapter Set 67049**; Master Ball Joint Installer/Remover Adapter Set 67310 (select stores); Axle Puller 67030 + Slide Hammer 67031; FWD Axle Puller Adapter 67102; Pitman Arm/Tie Rod Puller 67028; Tie Rod End Remover (non-damaging) 67008; 1/2" click torque wrench 67075 (range not on poster); axle nut sockets 30/32/34/36 mm (67038–67041).
- Worth knowing (UNVERIFIED, past chats): old ATF can also cause a shudder that feels like a CV problem. ATF change history is unknown (item 6).
- If the shake remains after the new axle: check the mounts.

## 3. ABS light, code 12-1 (since Oct 20)
- Code meaning (Chilton, **V6** version; Chilton writes "12", not "12-1"): right front wheel sensor, **electrical noise or intermittent interruption**. Fixes it lists: wheel sensor, the magnetic encoder, or **the front wheel bearing**. That fits the loose bearing Les Schwab found.
- The tone ring on this car is the **magnetic encoder inside the front wheel bearing**, not a ring on the axle (Chilton bearing article + parts catalog, `specs.md`). A new bearing must go in with the **brown encoder side facing the inside of the knuckle**, or the sensor can't read it.
- 2026-10-23 (owner): repairs done, code cleared with the MADDOX, rescan shows no ABS codes, but **the light stays on**.
- What Chilton says (V6 version): the light stays on until the fault is gone **and the car is driven**; noise faults clear on a test drive at **19 mph (30 km/h)**; codes survive a battery disconnect.
- MADDOX MRBT: Harbor Freight's coverage tool showed nothing for this car, and the product page only promises reading/clearing **engine** codes. So "no ABS codes" may mean it never reached the ABS unit. Check: does ABS live data show four wheel speeds?
- Next, in order: (1) drive over 19 mph, then restart; (2) MADDOX ABS live data, right front vs the others; (3) fuses #17 (30 A) and #18 (20 A) under the hood; (4) battery/charging test, since earlier ABS code 61 = low voltage (Chilton V6: "Check the charging system"); (5) if a new bearing went in, confirm the encoder faces inward, plus the sensor plug, seating and wire routing.
- Normal brakes work; no anti-lock until fixed (OM p.185).
- RF sensor part 57450-SDA-A11 confirmed by VIN (`parts.md`). Sensor bolt 9.8 N·m (7.2 lbf·ft) (`specs.md`).
- NHTSA service bulletins: none about code 12/61, wheel sensors or the ABS light (all 190 read 2026-10-23).

## 4. SRS (airbag) light on
- Was on before the passenger seat was removed; removing the seat adds codes of its own.
- Codes read with a MADDOX MRBT: SRS 61-10, E2-11, F1-11; ABS 61-1.
- Meanings from Chilton (**Hybrid** version, not confirmed for this car, 2026-10-23):
  - 61-10: open in the driver's seat belt buckle switch circuit.
  - **E2-11 / F1-11: in a group meaning an airbag, side airbag, curtain airbag or seat belt tensioner has DEPLOYED.** Chilton says the SRS unit must be replaced after a deployment. This could mean a past crash or a fired belt tensioner. **Dealer job, never DIY.**
- **With the SRS light on, the airbags may not deploy in a crash.**
- Not known: whether the light was on before Sep 7, when the console came apart over the SRS unit.
- Plan from past chats: reinstall the passenger seat, clear codes, see which come back.
- Recalls: NHTSA VIN check shows **0 unrepaired recalls** (OFFICIAL RECORD, data refreshed 2026-10-22, checked 2026-10-23).

## 5. Battery drain (status unknown)
- See `log.md` (Sep 8). 12.6 V at rest proves nothing on its own.
- Next: load test (free at many parts stores) and a parasitic draw test. Suspects: Bluetooth adapter, camera wiring.
- Battery: EverStart Maxx, made May 2025 (under warranty per owner).

## 6. Maintenance with no record (treat as overdue)
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
