# Issue history: 2005 Accord EX

Background for `open-issues.md`. Read this when an open item needs its back story, or when
the owner asks what happened. **Don't** use it for the current status: `open-issues.md` is
the current status, and newer notes there win over anything here.

Two parts:
1. The full `open-issues.md` as it stood on 2026-10-28, before it was cut down to current
   items only (copied word for word).
2. Notes that sat on unmerged branches (draft PRs #1–#14 and #22, 2026-10-22 to 10-28) and
   were folded in on 2026-10-28, copied word for word with their dates. Some were
   overtaken by later events; the current status is in `open-issues.md`.

---

# Part 1. `open-issues.md` as of 2026-10-28


Most urgent first. Update or close an item whenever something changes. Background is in
`log.md` and `sources/project-history-2026-10-21.md`.

**Status 2026-10-27 (owner): car back from Ben's and drivable.** Right front has a new
axle, new axle nut (owner) and new lower ball joint (Ben's). Still open on the right front:
the ABS (item 3: Ben found the bearing's tone ring damaged; **owner deferred the fix,
2026-10-28**) and the grooved rotor/pads. Background: `plan-right-front-2026-10.md`.

### 0. RESOLVED 2026-10-27: right front grinding, loose bearing, stripped axle nut
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

### 1. RESOLVED 2026-10-27: front axle nut
- **Owner, 2026-10-28: the axle nut is fine; closed. Don't raise it again** unless the owner asks or a new symptom points at it (clunk, wheel play, noise from the right front).
- **Owner, 2026-10-27: fixed. New axle nut on the new axle; car drivable.** Only loose end: the torque number used and its source weren't recorded (`log.md`). If it came from Chilton, add it to `specs.md`.

History:
- The owner torqued the right front axle nut to **181 lb-ft** when the old axle went back in (Oct 19).
- Past chats gave both 181 and 134 lb-ft (134 lb-ft = 181 N·m, so one is probably a unit mix-up). The owner's manual has no axle nut spec.
- Safety-critical spec: the real 4-cylinder number belongs in `specs.md` with its Chilton citation.
- **Chilton A–I report (2026-10-27): 4-cyl axle nut torque NOT FOUND.** The only figure, 181 lbf·ft (245 N·m), is from the Accord **Hybrid** article for a **24 × 1.5 mm** nut. This car's Honda nut (90305-692-010) is the **22 mm** nut, so that figure is for a different nut. The Hybrid article also says: new nut every time, oil its seating face, stake the shoulder into the driveshaft slot after tightening.
- (Closed by owner 2026-10-28) What torque went on the new nut last week? If it was 181 lb-ft, that is the 24 mm nut's number. Get the 4-cyl figure from Ben (shop software, free to ask), a Honda dealer service desk, or Chilton's 2006–07 Accord 2.4 article, and re-torque if it differs.

### 2. Right front: steering shake under hard acceleration + torn lower ball joint boot
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

### 3. ABS light, code 12-1 (since Oct 20)
- **DEFERRED by owner, 2026-10-28:** living with the ABS light for now; will fix later. When it's picked back up: Ben's quote ($544.04, NSK bearing) vs Les Schwab (≈$516 incl. new hub, valid to 2026-11-20, bearing brand unknown) are below. Best done in the same visit as the right front rotor/pads (rotor comes off for the bearing anyway).
- **Chilton backs Ben's diagnosis (A–I report, 2026-10-27; V6 and Hybrid articles, not 4-cyl-specific):** code **12** = right front wheel sensor electrical noise / intermittent signal. Honda's fix order: check the sensor and the **front magnetic encoder**; if the encoder is bad, **replace the front wheel bearing** (the encoder is part of it). Bearing goes in with the brown encoder side toward the inside of the knuckle; keep metal debris and magnetic tools off it. Codes are stored in memory and are **not** cleared by disconnecting the battery; code 12-type faults stay on until the system is normal and the car is driven (Hybrid article). V6 sensor air gap 0.5–1.2 mm (V6 only). L4 wiring pins are in `specs.md`.
- **2026-10-27, Ben's diagnosis (owner relaying):** the ABS fault is the **tone ring on the right front wheel bearing, damaged**. Ben compared it with the left side; the right one is "definitely damaged".
- **Ben's quote (Tekmetric, 2026-10-27, tech "B Ieremie"):** R&R front wheel bearing, one side, labor **$404.25** · NSK wheel bearing ×1 **$93.04** · subtotal $497.29 · est. tax $46.75 · **total $544.04**. No hub, alignment, rotor or pads on it.
- Compare: Les Schwab quote (item 0, valid to 2026-11-20) bearing $128.48 + hub $110.11 + hub/bearing labor w/ press off rotor $232.99 = $471.58 + tax ≈ $516, **includes a new hub**; brand not shown. Honda bearing 44300-TR4-A51 $119.63 (catalog, 2026-10-25). NSK makes Honda's original bearing (`plan-right-front-2026-10.md`).
- Past-chat reading: right front wheel speed sensor, noisy or intermittent signal, likely damaged by hammering on the knuckle. Meaning of 12-1 is UNVERIFIED; a library service manual has the Honda code chart.
- Normal brakes work; no anti-lock until fixed.
- Part from past chats: Honda 57450-SDA-A11 (UNVERIFIED; confirm by VIN at a Honda parts counter).
- **2026-10-27 (owner, relaying Ben's Auto Care):** Ben replaced the right front ABS sensor. ABS light still on; on a test drive the sensor "isn't getting a read" from the wheel. Ben suspects the tone ring. Still unknown: new code number, how "no read" was judged (live data?), sensor brand/part number, whether Ben has already replaced the hub bearing.
- **The "tone ring" on this car is most likely part of the hub bearing, not the axle.** MOTOR Magazine, "Foreign Service", Aug 2013, pp.12–16 (trade press, read 2026-10-27; not a Honda document): 2003-and-newer Accords usually use a wheel bearing with a built-in **magnetic encoder** (a flat brown ring on the bearing's inboard face) instead of a toothed tone ring. Brown side faces in toward the sensor, black rubbery seal faces out; the encoder holds a paper clip; installed backwards = no signal, and the bearing is usually ruined getting it back out. SKF also lists its 2003–07 Accord front bearing (FW48) as having an integrated tone ring (search listing only, article not opened). Confirm the design in Chilton.
- So "bad tone ring" = new hub bearing, which is already on the list (item 0). Suspects, cheapest to check first: (a) if Ben already put in a new bearing, was it installed brown side in, and does it have an encoder at all; (b) old bearing: play changes the sensor gap, and steel dust from the caliper grinding the rotor sticks to a magnetic encoder; (c) sensor wiring/connector damaged by the October hammering; (d) wrong or bad new sensor (Japan-built 57450-SDC-013 / SDH-003 said not to fit).

### 4. SRS (airbag) light on
- Was on before the passenger seat was removed; removing the seat adds codes of its own.
- Codes read with a MADDOX MRBT: SRS 61-10, E2-11, F1-11; ABS 61-1. Meanings from past chats are guesses (UNVERIFIED).
- Lead to check (free): recall **07V001000** (Honda A07-002, driver's seat position sensor harness) says a broken sensor wire turns the SRS light on. Whether that recall was done on this VIN, and whether it matches these codes, is unknown. Check the VIN at nhtsa.gov/recalls or ask a Honda dealer's service desk; open recalls are fixed free.
- **With the SRS light on, the airbags may not deploy in a crash.**
- Not known: whether the light was on before Sep 7, when the console came apart over the SRS unit.
- Plan from past chats: reinstall the passenger seat, clear codes, see which come back.
- Recalls: project history says no open recalls on the VIN. Confirm at <https://www.nhtsa.gov/recalls>.
- **Chilton A–I report (2026-10-27), Hybrid-only SRS articles (code meanings are probably shared, not confirmed for this car):** **61-10 = open in the driver's seat belt buckle switch.** **E2-11 / F1-11** sit in one combined article about airbags, side airbags, curtain airbags and seat belt tensioners; its description was cut off, and it links a note that the SRS unit must be replaced after any deployment. Have a Honda dealer or SRS-capable shop read these with Honda's scan tool before assuming anything.
- Bulletins worth asking the shop about: **A02-052 "Initializing the OPDS Unit"** (the passenger seat's occupant sensor; the passenger seat was removed), **A07-002** seat position sensor harness recall (above), **A20-010 / A20-015** warranty extensions for the driver's and passenger's airbag inflators on 2003–07 Accords.

### 5. Battery drain (status unknown)
- See `log.md` (Sep 8). 12.6 V at rest proves nothing on its own.
- Next: load test (free at many parts stores) and a parasitic draw test. Suspects: Bluetooth adapter, camera wiring.
- Battery: EverStart Maxx, made May 2025 (under warranty per owner).
- **Link (Chilton V6 ABS article, A–I report):** ABS code **61 = low +B-FSR voltage** at the ABS unit; Honda's fix is "check the charging system". So the ABS **61-1** read earlier points at low voltage: battery or charging, not the wheel sensor.
- Bulletins: A88-023 Battery Testing and Replacement, A10-054 Alternator and Regulator Circuit Troubleshooting, A12-002 Alternator Testing (titles only; Chilton Bulletins tab).

### 6. Maintenance with no record (treat as overdue)
Order, shopping list and quantities: plan-maintenance-catchup.md (old file, 2026-10-25; rewritten 2026-11-03 as `plans/2026-11-catch-up-maintenance.md`).
Intervals are from the manual (`specs.md`, OM pp.202–203). Severe schedule likely applies (short local trips).
- ATF: no record. Honda drain-and-refill method (OM p.220).
- Engine coolant: no record (120k mi / 10 yr first change).
- Brake fluid: no record (every 3 years).
- Drive belt: inspect (every 30k mi / 2 yr).
- Valve clearance: inspect at 110k mi, otherwise adjust only if noisy. Car is ~139k.
- Cabin and engine air filters: no record.
- Oil change: last one not recorded. Log the next one with mileage.
- Throttle body cleaning: unknown whether done.

### 7. Body and interior (not urgent)
- Front bumper cover cracked. Rear bumper divot and clear-coat crack. Hood rock chips to primer (check whether any reach bare metal before winter). Peeling clear coat in spots.
- Rear road noise since the deadener was lost.
- Tint: right rear door piece needs replacing.
- Backup camera monitor adhesive lets go in heat; keep it out of the passenger airbag zone.
- Center vent vane broken. Leather worn in areas.
- VTC actuator cold-start rattle (known K24 issue per past chats; UNVERIFIED). Not urgent.

---

# Part 2. Notes folded in from unmerged branches (2026-10-28)

## Right front, 2026-10-22: axle installed, ball joint boot gone (branch brave-bell, PR #1)

- **2026-10-22 (owner): new axle installed, "in and working."** Not yet recorded: new axle nut or reused, torque used, whether the screech/rubbing is gone, whether the bearing still has play now the nut is tight, whether the bearing/hub or rotor/pads were replaced. Until those are answered, this item stays open.
- **2026-10-22 (owner, follow-up):** screech/rubbing **gone**; shake under acceleration **gone**. Owner plans to keep the rotor and pads. Owner's voice-to-text reply on the nut reads "new axle not talk to spec": most likely "new axle nut torqued to spec", but the number used and its source are **not confirmed**.
- Still to do: rock the wheel at 12 and 6 o'clock (wheel off the ground) to confirm no bearing play; measure the grooved right rotor against the minimum thickness cast/stamped on the rotor itself (Tier 1); check pad thickness.
### 2. Right front lower ball joint: boot completely gone (axle now done)
- **2026-10-22 (owner): the lower ball joint boot is completely gone.** Torn by the pickle fork on Oct 19; now missing entirely. The joint has no seal: water and grit get straight into it and it wears from here on. New Moog K80228 is already on hand.
- A lower ball joint carries the car's weight; if it separates, the wheel folds under (UNVERIFIED: general knowledge, not from a manual). Replace soon, not "someday". Watch for clunks over bumps or wandering steering.
- 2026-10-22: new axle installed (see `log.md`); owner says the hard-acceleration shake is **gone**.
- **Tools, 2026-10-22:** owner's O'Reilly does **not** have the Honda Ball Joint Adapter Set (67049) the poster lists.
  - OTC sells a separate adapter kit for this generation: OTC 6734, "Honda/Acura Ball Joint Adapter Update", 3 pieces, used with OTC C-frame 7248; covers Accord sedan/coupe 2003–2007 and TSX 2004–2007 (VERIFIED: otctools.com product page, read 2026-10-22). ~$246, so not a buy. Implication: a generic "Honda" adapter set may be for older Hondas and not fit this car. Ask any loaner counter whether their set covers a 2003–2007 Accord.
  - Fallback that needs no adapter: remove the knuckle and have a shop press the old joint out and the new one in on a hydraulic press. Needs another new axle nut (it is staked). Car is undrivable while the knuckle is out.
  - Joint is held by a circlip (52226-SL0-003 in `parts.md`, UNVERIFIED): snap ring pliers needed.
### Background (from before the axle was installed)

## Right front and SRS, 2026-10-23: Chilton pull, "fixed everything" report (branch serene-mendel, PR #4)

- **2026-10-23 (owner): "fixed everything."** Who did the work, date, mileage, parts (axle brand/number, bearing/hub, ball joint, ABS sensor?, rotor/pads), axle nut torque used and alignment: **not recorded yet**. Close this item and log the job once those are in.
- **Chilton (2026-10-23):** only the **Hybrid** version has the spindle nut: 24 × 1.5 mm, 245 N·m (181 lbf·ft). The 4-cyl parts catalog lists a **22 mm** nut, and the owner's 32 mm socket fits (36 mm too big). So the Hybrid number is probably for a different nut. UNVERIFIED (Claude's math): 181 N·m = 134 lbf·ft, which would fit the "unit mix-up" theory. If the 4-cyl spec is lower than 181 lbf·ft, the Oct 19 nut was over-tightened. That nut has since been called stripped/cross-threaded by Les Schwab anyway.
- **Safety-critical. Still need the real 4-cylinder spec.** Free: a Honda dealer service desk (read from Honda service info by VIN), or the Chilton halfshaft or torque-spec pages that name the 4-cylinder. New nut every time (Chilton, Hybrid article).
- Code meaning (Chilton, **V6** version; Chilton writes "12", not "12-1"): right front wheel sensor, **electrical noise or intermittent interruption**. Fixes it lists: wheel sensor, the magnetic encoder, or **the front wheel bearing**. That fits the loose bearing Les Schwab found.
- The tone ring on this car is the **magnetic encoder inside the front wheel bearing**, not a ring on the axle (Chilton bearing article + parts catalog, `specs.md`). A new bearing must go in with the **brown encoder side facing the inside of the knuckle**, or the sensor can't read it.
- 2026-10-23 (owner): repairs done, code cleared with the MADDOX, rescan shows no ABS codes, but **the light stays on**.
- What Chilton says (V6 version): the light stays on until the fault is gone **and the car is driven**; noise faults clear on a test drive at **19 mph (30 km/h)**; codes survive a battery disconnect.
- MADDOX MRBT: Harbor Freight's coverage tool showed nothing for this car, and the product page only promises reading/clearing **engine** codes. So "no ABS codes" may mean it never reached the ABS unit. Check: does ABS live data show four wheel speeds?
- Next, in order: (1) drive over 19 mph, then restart; (2) MADDOX ABS live data, right front vs the others; (3) fuses #17 (30 A) and #18 (20 A) under the hood; (4) battery/charging test, since earlier ABS code 61 = low voltage (Chilton V6: "Check the charging system"); (5) if a new bearing went in, confirm the encoder faces inward, plus the sensor plug, seating and wire routing.
- Normal brakes work; no anti-lock until fixed (OM p.185).
- RF sensor part 57450-SDA-A11 confirmed by VIN (`parts.md`). Sensor bolt 9.8 N·m (7.2 lbf·ft) (`specs.md`).
- NHTSA service bulletins: none about code 12/61, wheel sensors or the ABS light (all 190 read 2026-10-23).
- Codes read with a MADDOX MRBT: SRS 61-10, E2-11, F1-11; ABS 61-1.
- Meanings from Chilton (**Hybrid** version, not confirmed for this car, 2026-10-23):
  - 61-10: open in the driver's seat belt buckle switch circuit.
  - **E2-11 / F1-11: in a group meaning an airbag, side airbag, curtain airbag or seat belt tensioner has DEPLOYED.** Chilton says the SRS unit must be replaced after a deployment. This could mean a past crash or a fired belt tensioner. **Dealer job, never DIY.**
- Recalls: NHTSA VIN check shows **0 unrepaired recalls** (OFFICIAL RECORD, data refreshed 2026-10-22, checked 2026-10-23).

## Alignment pointer, 2026-10-24 (branch compassionate-dirac, PR #5)

- Alignment after this job: DIY string method in `procedures/accord-2005-wheel-alignment-diy.md` (DRAFT; needs FSM tolerances and torques first). Ben's scope doesn't include an alignment yet.

## OBD port, 2026-10-24 (branch intelligent-thompson, PR #7)

### 4b. NEW 2026-10-24: O'Reilly scan tool would not connect to the OBD port
- Owner report: employee tried ~5 min, said it might be a wiring problem. Reason for the scan, ignition position and mileage not recorded.
- The port worked in Oct 2026: the owner's MADDOX MRBT read SRS/ABS codes (project history). So something changed recently, or the store's tool/procedure was the problem.
- Owner's manual fuse charts (OM pp.268–269) do **not** name a fuse for the diagnostic connector. Which fuse feeds it: UNVERIFIED; get it from the Chilton Library wiring diagram (free with a library card).
- Free test order: own MADDOX with ignition ON (II) → check every fuse visually and with a test light → test light / meter on the port's power and ground pins → battery voltage (item 5).

## SRS light, 2026-10-23 to 10-26 (branch compassionate-euler, PR #2)

- **Owner, 2026-10-24: the light came on when the passenger seat was removed** (Aug 2026, ~137k, right after purchase). This replaces the earlier note, carried over from past chats (`sources/project-history-2026-10-21.md` §C), that it was on before the seat came out.
- **The light cannot go off while the passenger seat is out.** That seat carries the passenger weight sensors (VERIFIED: OM pp.23–24, 27), and the system monitors front passenger seat belt use (OM p.24). The manual says not to remove a front seat without consulting the dealer, because it makes the weight sensors ineffective (OM p.33). Any fix starts with the seat going back in.
- Reconnecting the seat's yellow SRS connectors is airbag work: shop or dealer, not DIY. Easiest: have the shop reinstall the seat while the car is in for the axle job.
- Known pattern on 2005 Accords (COMMUNITY: NHTSA complaints, several naming code 71-10 and/or 61-10): broken driver seat position sensor harness or driver buckle switch. Recall 07V001000 replaced that harness only on some VINs; many 2005 owners were told their VIN was outside it.
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
- **2026-10-26 result:** seat reinstalled (owner did the connectors). The Side Airbag Off indicator now does its normal brief key-on check (OM p.31). Codes cleared with the MADDOX; the **same three came back**. So the seat wasn't what's keeping these codes, and the "seat explains it" theory is out for these codes. Next: a Honda dealer (or a shop with a Honda-level scan tool) reads the SRS system, and checks that the front airbags and driver tensioner are genuine and never fired. Fix 61-10 (driver buckle switch) whatever the crash codes turn out to be.
- **Unresolved conflict (2026-10-26):** if E2-11/F1-11 were real, the light should have been on since the crash, but it was off at purchase and still works now (so it wasn't a pulled bulb). That points to the MADDOX misreading the codes; codes returning after a clear doesn't rule that out. Settle it with a Honda-level read or a second, different SRS-capable scanner. Free: look for purchase-listing photos or videos showing the dash with the engine running. Ask the owner whether anything under the **driver** seat or the console was touched (61-10 is the driver buckle).
- Free checks before paying for a dealer scan (2026-10-26): call Honda (1-888-234-2138, from `recalls.md`) or a Honda dealer with the VIN and ask which airbag recalls were done on this car, when and where. Takata inflator work means a dealer had both front airbags apart, and a date or part record may show a replacement. Also check: does the driver belt pull out and retract normally (a fired tensioner may lock it; UNVERIFIED); compare the date on the driver belt webbing label with the door-jamb build date; look for a replaced or mismatched dash top / steering wheel cover. None of these is proof; only a Honda-level SRS read is.
- Seat bolts also anchor the passenger seat belt buckle: torque spec from Chilton Library, not from memory.
- Recalls: **confirmed 2026-10-26, 0 open recalls on the VIN** (OFFICIAL RECORD: NHTSA VIN lookup; Honda MyGarage agrees). Completed-recall history (which airbag work was done, when) is still unknown: call Honda 1-888-234-2138.

## Battery drain, 2026-10-26 (branch practical-heisenberg, PR #10)

### 5. Battery drain: not happening now (owner, 2026-10-26)
- **2026-10-26 (owner): no battery drain currently.** The September episodes are in `log.md` (Sep 8). Cause was never pinned down.
- If it comes back: load test (free at many parts stores), then a parasitic draw test. Old suspects: Bluetooth adapter, camera wiring.
- Keep new add-ons on key-on power anyway, so a stuck accessory can't flatten the only car.

## Head unit, 2026-10-26 (branch admiring-cannon, PR #12)

### 8. Head unit install pending (bought 2026-10-26)
- Eonon HAC1X7A + camera ordered. Checklist, questions for Eonon and wiring: `plan-head-unit-2026-10.md`.
- Before install: check climate panel type (single vs dual zone), and do the parasitic draw test (item 5) on the old setup.
- 90-day return window: install and test inside it.

## Ben's Auto Care, 2026-10-27 (branch upbeat-heisenberg, PR #14)

- **2026-10-27 (owner): car dropped off at Ben's Auto Care for the lower ball joint; work still being done today.** Two add-ons per Ben (verbal, owner's summary):
  - Waiting on a **grease fitting (zerk)** for the lower ball joint. Open question: our notes say Moog K80228 is *not* greaseable (seller listings, COMMUNITY), so ask whether Ben used the owner's K80228 or a different joint, and if the car leaves before the fitting arrives, whether the hole is plugged and the joint already greased.
  - **Right front ABS sensor snapped** while pressing the ball joint out of the knuckle. Ben is ordering one: **$40, at his cost (no markup) per Ben**. Brand/part number not given yet. That sensor was already suspected bad (item 3), so this is a part that was on the list anyway.
  - Still to confirm with Ben: full scope today (axle? bearing/hub? axle nut torque source?), alignment, warranty, and whether the car is safe to drive until the parts arrive (ABS stays off until the sensor is in).
- 2026-10-27: old sensor snapped at Ben's during the ball joint press; Ben ordering a replacement ($40). Ask for the brand and part number (cross-check against 57450-SDA-A11) and clear the code after install.

## Shake around 60 mph, 2026-10-28 (branch funny-feynman, PR #22)

- **2026-10-28 (owner): "car is pretty shaky around 60 mph."** Not yet known: whether this is the old hard-acceleration shake or a new one since the right front work; steering wheel vs seat; whether it stays when coasting or changes when braking; whether lug nuts were re-checked after the wheel went back on. Triage order given: lug nuts (80 lbf·ft, OM p.250) → coast/brake test → wheel balance and tire check → axle/bearing → ATF/torque converter shudder (complaints 10299703, 11076272: 55–65 mph under light throttle).
- **2026-10-28 (owner, coast test):** coasting at ~60 is "kind of shaky", **much worse on the gas**. So two parts: a mild rotating shake (wheel/tire/bearing) plus a bigger load shake (torque converter shudder, inner CV on either axle, mounts). The hard-acceleration shake was not fixed by the new right axle, or the new axle brought its own. Next: speed-band and throttle test, check the new axle is fully seated, lug nuts + balance, ATF drain-and-refill (overdue anyway), then brake-torque mount test. No torque-converter or driveline-vibration bulletin among the TSB titles saved in `sources/chilton-pack-F-2026-10-27.md` (only part of the 92-entry list was saved).

