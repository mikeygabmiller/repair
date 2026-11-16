# What only the owner can check: one trip to the car, two phone calls, one library session

Every item here clears an UNVERIFIED or "not recorded" entry somewhere in the repo. Grouped
so each trip clears as many as possible. Tick it, send the photo or answer to Claude, and the
chat files it (photos → `sources/photos/`, paperwork → `receipts/`).

## 1. One trip to the car (~30 min, phone camera, flashlight)

**Without tools**
- [ ] **Odometer** (dash photo). Last recorded: 139,032 on 2026-10-21. Needed by every
      maintenance row and the ditch/shake entries.
- [ ] **Driver door-jamb label(s)**, sharp enough to read: **build month** (decides recall
      11V395000 coverage), tire size and cold pressures (settles OM vs Chilton, `specs.md`),
      GVWR/GAWR, paint code.
- [ ] **Under-hood emissions label** (underside of the hood or radiator support): does it
      say **SULEV**? Decides the plug gap and -11 vs -13 plug (`specs.md`). Also look for a
      **belt routing sticker** nearby.
- [ ] **Battery label**: group size (51R unverified), date code.
- [ ] **Both fuse box lids** (interior: driver's lower dash; under-hood: driver's side rear).
      Settles which rows apply to this car: under-hood #11 (20 vs 30 A), #17, #18, #22, and
      the back-up light fuse number (`quick-reference.md`).
- [ ] **Coolant reserve tank**, engine cold: level and colour. **Brake fluid**: level and
      colour. **ATF** dipstick (engine hot): level, colour, smell. Photos. (Decides how
      urgent the shop fluid jobs are.)
- [ ] **Drive belt** close-up of the ribbed side + the tensioner's indicator marks
      (`procedures/accord-2005-drive-belt.md`).
- [ ] **Airbox**: how the cover is fastened (clips or screws), and the intake tube between
      airbox and throttle body: is there a **sensor plugged into it** (MAF)? Decides which
      intake kit could even fit (`mods/README.md`). Photo the sensor and any number on it,
      and the under-hood emissions label (does it say SULEV?).
- [ ] **Rear brakes**: disc or drum? (Look through the rear wheel spokes.)
- [ ] **Front rotors**: any minimum thickness cast/stamped on the rotor hat (visible
      through the spokes on some wheels).
- [ ] **Tires**: DOT date code on each (4 digits, week+year), tread depth or wear bars,
      brand and model. Plus the left front rim lips (open issue 11).
- [ ] **Lug nut socket size** (try 19 mm and 21 mm).
- [ ] Center console: **heated seat switches** next to the shifter? (`profile.md`)
- [ ] **Keys**: how many, and do they all start the car?
- [ ] Map light bulb and trunk bulb: pull one, read the number (`parts.md`).
- [ ] Bulbs bought 2026-10-27: did the 168s and the two LED DE3175s go in, and where? Are the
      old low-beam bulbs kept (for resale)? (`log.md`, 2026-10-27)
- [ ] Driver's seat belt: pulls out and retracts smoothly; label date (look only, open
      issue 1).

**With the front on ramps (only if it's already up for the oil change)**
- [ ] ATF drain plug: what drive it takes (3/8-in square or hex, size).
- [ ] Oil drain bolt socket size (lead: 17 mm, COMMUNITY; test-fit, record in the oil change procedure).
- [ ] Right axle: brand/part number on the tag or boot clamp; right axle seal dry?

## 2. Phone call A: Honda dealer **parts counter**, with the VIN (`vehicle.json`), ~15 min
Ask for the part number **for this VIN** and the price of each:
- [ ] Oil filter (15400-PLM-A02?) and drain bolt washer (94109-14000?)
- [ ] Engine air filter (17220-RAA-A00?) and cabin filter (80292-SDA-407?)
- [ ] ATF: is **DW-1 (08200-9008)** the replacement for ATF-Z1 on this car? ATF drain plug
      washer number (90471-PX4-000?)
- [ ] Front brake pad set number; which front rotor (45251-TA0-A02 or 45251-TA5-A00)
- [ ] Front hub bearing (44300-TR4-A51?) and front hub (44600-SDA-A00?)
- [ ] Serpentine belt (31110-RAA-A02?)
- [ ] Type 2 coolant premixed (OL999-9001?) and M-77 paste (08798-9010?)
- [ ] **Trim by VIN: EX or EX-L?** (`profile.md` conflict)
Answers → `parts.md` "Confirmed" table.

## 3. Phone call B: Honda customer service **1-888-234-2138**, with the VIN, ~10 min
- [ ] Which recall campaigns were done on this car, when, at which dealer (Takata
      inflators, 11V395000 transmission software, 07V097000 fuel pump relay, 05V132000
      fuse box, 07V001000 seat position sensor). → `profile.md`, open issue 1, sale file.

## 4. Free, from a computer (~30 min)
- [ ] nhtsa.gov → 2005 Honda Accord → **Manufacturer Communications**: open and save the
      PDFs for **A06-087, A03-036, A06-068, A07-045, A05-034, A10-054** (`tsb-guide.md`,
      "Next step"). Upload them; Claude writes Honda's fix into `tsb-guide.md`.
- [ ] Kelley Blue Book or Edmunds: private-party value, 2005 Accord EX-L sedan, real
      mileage → walk-away worksheet in `plans/long-term-ownership.md`.

## 5. One library session (Chilton, through the county library)
- [ ] Run **`prompts/muse-chilton-pull-3.md`** with Muse (≈25 items: brake table
      footnotes, front suspension torques, valve clearance, filter/coolant/belt articles,
      P0685 and main relay test, parasitic draw limit, back-up light fuse). It's built to
      clear the TENTATIVE brake values and most DRAFT labels in `procedures/`.
- [ ] Later: `prompts/muse-chilton-maintenance.md` Part 2, one session at a time.

## 6. Paperwork to photograph (→ `receipts/`)
- [ ] Ben's Auto Care invoice, 2026-10-27 (ABS sensor brand/number, which ball joint, mileage)
- [ ] Les Schwab inspection sheet and quote, 2026-10-21 (bearing quote valid to **2026-11-20**)
- [ ] Parts Geek axle order #31-12567661 or the axle box label
