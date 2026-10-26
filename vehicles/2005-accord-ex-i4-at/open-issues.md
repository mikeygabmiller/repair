# Open issues: 2005 Accord EX

Most urgent first. Update or close an item whenever something changes. Background is in
`log.md` and `sources/project-history-2026-10-21.md`.

**Items 0–3 are one job.** Options, parts list with Honda numbers, questions for Ben's and
the Chilton spec checklist: `plan-right-front-2026-10.md` (2026-10-25).

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

## 1. Front axle nut torque is unverified, and the car is being driven on it
- The owner torqued the right front axle nut to **181 lb-ft** when the old axle went back in (Oct 19).
- Past chats gave both 181 and 134 lb-ft (134 lb-ft = 181 N·m, so one is probably a unit mix-up). The owner's manual has no axle nut spec.
- **Safety-critical. Get the real 4-cylinder spec from Chilton Library (free through a public library) before the axle job, and use a new nut.**

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
- Past-chat reading: right front wheel speed sensor, noisy or intermittent signal, likely damaged by hammering on the knuckle. Meaning of 12-1 is UNVERIFIED; a library service manual has the Honda code chart.
- Normal brakes work; no anti-lock until fixed.
- Part from past chats: Honda 57450-SDA-A11 (UNVERIFIED; confirm by VIN at a Honda parts counter).

## 4. SRS (airbag) light on
- Was on before the passenger seat was removed; removing the seat adds codes of its own.
- Codes read with a MADDOX MRBT: SRS 61-10, E2-11, F1-11; ABS 61-1. Meanings from past chats are guesses (UNVERIFIED).
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

## 8. Head unit install pending (bought 2026-10-26)
- Eonon HAC1X7A + camera ordered. Checklist, questions for Eonon and wiring: `plan-head-unit-2026-10.md`.
- Before install: check climate panel type (single vs dual zone), and do the parasitic draw test (item 5) on the old setup.
- 90-day return window: install and test inside it.
