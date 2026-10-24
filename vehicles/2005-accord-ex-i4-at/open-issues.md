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
- **Owner, 2026-10-24: the light came on when the passenger seat was removed** (Aug 2026, ~137k, right after purchase). This replaces the earlier note, carried over from past chats (`sources/project-history-2026-10-21.md` §C), that it was on before the seat came out.
- **The light cannot go off while the passenger seat is out.** That seat carries the passenger weight sensors (VERIFIED: OM pp.23–24, 27), and the system monitors front passenger seat belt use (OM p.24). The manual says not to remove a front seat without consulting the dealer, because it makes the weight sensors ineffective (OM p.33). Any fix starts with the seat going back in.
- Reconnecting the seat's yellow SRS connectors is airbag work: shop or dealer, not DIY. Easiest: have the shop reinstall the seat while the car is in for the axle job.
- Known pattern on 2005 Accords (COMMUNITY: NHTSA complaints, several naming code 71-10 and/or 61-10): broken driver seat position sensor harness or driver buckle switch. Recall 07V001000 replaced that harness only on some VINs; many 2005 owners were told their VIN was outside it.
- Codes read with a MADDOX MRBT: SRS 61-10, E2-11, F1-11; ABS 61-1. Meanings from past chats are guesses (UNVERIFIED).
- **2026-10-23 code meanings (COMMUNITY: two Honda SRS code lists, ramblerdan.com/e/srs_codes.htm and safetyrestore.com's "Honda (2002-2011) SRS Airbag Module DTC Codes"; neither is Honda's manual):**
  - 61-1x = open circuit in the driver's seat belt buckle switch.
  - **E2-11 = passenger front airbag deployed. F1-11 = driver airbag and driver seat belt tensioner deployed.** These are crash records. A scan tool can't clear them; the SRS unit has to be replaced or reset, and every deployed part replaced.
  - If that's right, this car was in a frontal crash and the front airbags went off at some point. Unknown whether the airbags and tensioner were replaced with real Honda parts, or replaced at all.
  - Must be confirmed against the factory manual's SRS code chart (Chilton Library; or charm.li, which was down 2026-10-23), then a Honda dealer inspection.
  - The pasted Google AI code list (2026-10-23) doesn't include any of these codes and mixes in older-model codes. Don't use it.
  - Owner, 2026-10-23: the MADDOX app's own code descriptions match. That's the same tool that read the codes, not an independent check.
- **Owner facts (2026-10-23):** the SRS light was **not on when the car was bought** (Aug 2026). Prior owner (Chuck) said the front end had a minor accident before he got it (bumper only, no insurance claim). The owner had a low-speed bump with another car (paint transfer only, date not recorded). No airbag has deployed while the owner has had the car.
- Since the light started with the seat removal and no airbag has deployed, the likeliest story is: the seat removal set the light, and E2-11/F1-11 are misread or mislabeled by the MADDOX (none of the three codes is a passenger-seat code on the community lists). Not proven. Test: seat back in (shop), clear codes, see what returns. If E2-11/F1-11 come back, a Honda dealer reads them with Honda's own scan tool.
- Earlier reasoning: deployment codes should keep the light on from the day of the crash. Open possibilities: the codes are misread; the light was disabled or the airbag computer reset or swapped before the sale; or something else. Tests are in order of cost, cheapest first: when the light first came on; whether it lights briefly at key-on; airbag covers checked for signs of replacement; whether the MADDOX "clear" removes E2-11/F1-11; ask Chuck; a Honda dealer reading with Honda's own scan tool.
- **With the SRS light on, the airbags may not deploy in a crash.**
- Not known: whether the light was on before Sep 7, when the console came apart over the SRS unit.
- Plan from past chats: reinstall the passenger seat, clear codes, see which come back.
- Recalls: project history says no open recalls on the VIN. Confirm at <https://www.nhtsa.gov/recalls>.

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
