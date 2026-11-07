# Long-term plan: keep it as long as possible, sale-ready at any time

**Owner's rule, 2026-11-07:** the default is to keep the car as long as possible, while
keeping it in a state that gets the most money back if the owner decides to sell at any
point. (This replaces "sell around 170k".) Apply this to every recommendation.

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
