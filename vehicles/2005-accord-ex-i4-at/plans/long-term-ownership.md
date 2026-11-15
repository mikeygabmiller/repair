# Long-term plan: keep it as long as possible, sale-ready at any time

**Owner's rule, 2026-11-07:** the default is to keep the car as long as possible, while
keeping it in a state that gets the most money back if the owner decides to sell at any
point. (This replaces "sell around 170k".) Apply this to every recommendation.

**Target (owner, 2026-11-15): 500,000 miles.** That's ~361,000 more miles. Pace so far is
roughly 2,000 mi from purchase (Aug 2026, ~137,000) to 139,032 (2026-10-21), about 10,000 mi
a year if it holds (rough: purchase date and mileage are approximate). At that pace 500k is
decades away, so **age (rust, rubber, plastic, wiring) is as big a threat as miles.**

Mileage when this was written: last known 139,032 (2026-10-21).

## How the two goals fit together

Most spending serves both: a car that's maintained on schedule, with dated receipts and no
warning lights, lasts longer **and** sells for more. Where they pull apart, judge each spend
by two questions:

1. Does it keep the car safe and running longer?
2. Would a buyer pay for it, or mark the car down without it?

| Spend | Keeps it running | Buyer pays for it | Default |
|---|---|---|---|
| Scheduled maintenance, logged with mileage and receipt | Yes | Yes (records) | Always |
| Clearing warning lights (SRS, ABS, check engine) | Yes | Yes: a lit light gets a lowball or a walk-away (COMMUNITY, buyer behaviour) | Always, high priority |
| Safety repairs (brakes, steering, suspension, tires) | Yes | Yes (inspection) | Always, OEM or name-brand |
| Rust prevention, chip touch-up, detailing (owner does these himself) | Yes (rust) | Yes | Always: cheap for this owner |
| Body shop work (cracked bumper cover, clear coat) | No | Partly | Decide at sale time, against a quote |
| Mods and accessories | Rarely | Rarely | Reversible only; OEM parts boxed and kept |
| Big repair (transmission, engine) | Yes | Only if it saves the car | Walk-away worksheet below |

## Walk-away worksheet (any repair over about the price of a month's car payment)

Do this before saying yes to a big repair. Values come from free sites (Kelley Blue Book or
Edmunds, private-party value, 2005 Accord **EX-L** sedan, real mileage and condition).
Update the value once a year and write it here with the date.

1. Repair cost (written quote).
2. Value of the car **after** the repair.
3. Value of the car **as-is**, broken (what it would sell for unfixed).
4. Cost of a replacement car that's no worse, plus tax, title and fees.

Fix it if the repair costs less than (4) minus (3) **and** the rest of the car is sound.
It's a bad bet when the body is rusting through or a second major system is also failing.
The owner decides; the worksheet just puts the numbers side by side.

| Date | Mileage | Private-party value | Source |
|---|---|---|---|
| (not checked yet) | | | |

## What keeps it running (the order to do things)

1. **Now: safe and caught up.** Ditch damage (open issue 11), right front bearing and rotor
   (4, 5), SRS light (1), then every "No record" row in `maintenance.md` using
   `2026-11-catch-up-maintenance.md`.
2. **Transmission: the most likely thing to end this car.** Full ATF change per the owner's
   manual: drain and refill, drive a short distance, three times, then a final drain and
   refill (VERIFIED: OM p.220). Then every 30,000 mi or 2 yr (VERIFIED: OM p.203, severe).
   Honda fluid only (`specs.md`; Z1 vs DW-1 still to confirm at a Honda parts counter).
   Gentle launches; D3 when hauling or on long climbs (VERIFIED: OM p.195).
3. **Engine habits.** Oil and filter every 5,000 mi or 6 months, 5W-20 (VERIFIED: OM pp.203,
   213). Dipstick every other fill-up: running it low is how high-mileage engines die.
   Valve clearance check (overdue since 110k, shop job). Listen for cold-start chain or
   VTC rattle (open issue 8).
4. **Rust.** Rinse the underbody every couple of weeks in winter (road sand and de-icer).
   Look at the rear wheel arches and subframe once a year (COMMUNITY: known rust spots on
   this generation, UNVERIFIED).
5. **Parts that will fail along the way.** Water pump, radiator, alternator, starter, A/C
   compressor, mounts, bushings, brakes. Replace on failure; safety-critical parts OEM or
   name-brand.

## Extra habits for the 500k target (added 2026-11-15)

- **Transmission fund.** Set aside money every month toward a transmission replacement or
  rebuild. Fluid care lowers the odds but doesn't make a 2005 automatic last 500k
  (COMMUNITY/UNVERIFIED: the automatic is widely seen as this generation's weak point).
  When it comes, the walk-away worksheet decides.
- **ATF every 30,000 mi or 2 yr** after the catch-up (VERIFIED: OM p.203, severe), and the
  inline filter decision (`parts.md`, 25430-PLR-003) once the 4-cyl Chilton steps are pulled.
- **Oil top-up log.** Write every quart added, with the odometer, in `log.md`. A rising
  rate is the earliest warning of engine wear (COMMUNITY reasoning).
- **Valve clearance** on a regular cycle once the spec conflict is settled (`specs.md`):
  tight exhaust valves on high-mileage K24s can burn (COMMUNITY, UNVERIFIED).
- **Timing chain / VTC.** No replacement interval; listen. A cold-start rattle that gets
  longer (open issue 8) goes to `symptom-index.md` before it becomes a chain job.
- **Rust is what usually ends a long-life car in a salt state.** Winter underbody rinses
  (above); consider a yearly oil-based undercoat spray (COMMUNITY: e.g. Fluid Film; washes
  off, doesn't hurt resale). Fix rock chips to bare metal before winter (open issue 8).
- **Rubber and cooling parts age out.** Look at hoses, mounts, bushings and the radiator's
  plastic tanks once a year; coolant on schedule (Honda Type 2).

## Interior: keep it from wearing out (added 2026-11-15)

Over decades the interior dies from **water, sun and wear points**, in that order of
damage. Cleaning products are the owner's own field; this is the repair side.

- **Water first.** A wet floor rots carpet padding, rusts the floor pan and smells, and the
  driver's seat position sensor and passenger weight sensors sit under the front seats
  (VERIFIED: OM p.27, "do not spill any liquids on or under the seats"). Spills also damage
  wiring (OM p.103). Twice a year, and after any musty smell: press the carpet in each
  footwell and the trunk/spare well for damp. Common leak paths: clogged moonroof drains,
  door seals, a door's plastic water shield left loose after panel work (COMMUNITY,
  UNVERIFIED for this car). Bulletin A05-012 covers a damaged moonroof glass weatherstrip
  (title only, `tsb-guide.md`). Don't run the moonroof when frozen or snow-covered (VERIFIED:
  OM p.99). Silicone spray on door and trunk seals keeps them from sticking and tearing
  (VERIFIED: OM p.244, storage section). Cabin filter on schedule (OM p.233).
- **Nothing liquid loose in the cabin.** The fuel-can spill already cost the rear deadener
  (`log.md`). Chemicals and fuel ride in sealed bins in the trunk, never under the seats.
- **Sun.** Doors are tinted (`log.md`, right rear piece still to redo). A fitted reflective
  windshield shade when parked does the most for the dash and front leather (COMMUNITY).
- **Mats.** Custom-fit all-weather mats that hook on the factory anchors; never a mat on top
  of the anchored mat (VERIFIED: OM p.233). Box the OEM carpet mats for the sale.
- **Leather.** Worn spots (open issue 8): repair early with a color-matched leather
  repair/dye kit before cracks spread (COMMUNITY). **Fitted seat covers: front seats have
  side airbags; don't cover the front seat-backs without consulting the dealer** (VERIFIED:
  OM p.33). Rear seats and bottoms are fine.
- **Seat belts:** mild soap and warm water only, no bleach or solvents; wipe the loops so
  they retract freely (VERIFIED: OM p.233). Nothing clipped to belts (OM p.19).
- **Headliner and pillars:** no wet cleaning (glue lets go and it sags, COMMUNITY); nothing
  mounted there, curtain airbags above the side windows (VERIFIED: OM p.23).
- **Wear parts that will fail by 500k:** door lock actuators, window regulators/motors
  (both common in NHTSA complaint text for 2005 Accords, COMMUNITY). Replace on failure.
- **Cheap replacement trim:** same-color pieces from a salvage yard Accord of the same
  generation; match the interior color code ("Type B", door jamb) and the OEM part number
  (COMMUNITY).
- **Yearly photo set** of seats, dash, door panels and headliner, kept with the sale file.

## Sale-ready checklist (keep these true at all times)

- [ ] No warning lights on the dash.
- [ ] Every job in `log.md` with date and mileage; paperwork in `receipts/`.
- [ ] Factory parts removed for mods are boxed and kept with the car (list:
      `mods/plan-head-unit-2026-10.md`, "Keep for resale"). Mods come out cleanly.
- [ ] Passenger seat and rear seatbacks in place (rear seatbacks are out for cargo now).
- [ ] Trim confirmed as EX-L with a Honda dealer's VIN lookup, so the listing can say so.
- [ ] Honda's record of which recalls were done (Honda customer service, 1-888-234-2138).
      A buyer of a Takata-era Honda will ask.
- [ ] Owner's manual in the glovebox. Number of keys: not recorded yet.

At sale time, not before: decide on body shop work, print `log.md` and the receipts as a
binder, detail it, and remove personal items and any device paired to the head unit.
