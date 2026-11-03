# Plan: catch up the maintenance nobody recorded (November 2026)

Rewritten 2026-11-03 (first version 2026-10-25, then `plan-maintenance-catchup.md`). Covers
every **"No record → Now"** row in `maintenance.md`. Fluid types, amounts and torques are
copied from `specs.md`, which cites the owner's manual (OM) page or Chilton. Severe
schedule applies (OM p.199, `specs.md`). The right front job this plan used to wait for
is done (Ben's Auto Care, 2026-10-27).

## The split

| Job | Who | Why |
|---|---|---|
| Oil + filter | **DIY** | Easy, ~1 h, procedure already written: `procedures/accord-2005-oil-change.md` |
| Engine air filter | **DIY** | Clips on the airbox, no tools or a screwdriver, ~10 min |
| Cabin (dust and pollen) filter | **DIY** | Behind the glovebox, ~10 min (OM p.235) |
| Drive belt: inspect | **DIY, look only** | Cracks, glazing, missing chunks. Replace only if it fails the look |
| ATF drain and refill | **DIY recommended**, shop if you'd rather | Same kind of job as an oil change (drain plug, refill through the dipstick tube). A full change is **3 drain-and-refills with a short drive between, then a final one** (VERIFIED: OM p.220). A shop "transmission service" is usually priced as one visit, so DIY is the only cheap way to do the full change |
| Brake fluid | **Shop** | Bleeding all four wheels is a two-person job, and an air bubble left in is a brake you can't trust. Ask for a full brake inspection at the same visit (right front rotor is grooved, `open-issues.md` item 5) |
| Coolant | **Shop** (least urgent) | Needs the air bled out of the system and the old coolant disposed of properly. Check the level and colour first: if it looks right, this can wait for a later month |
| Tire rotation | **Wait** | Not until the 60 mph shake is diagnosed: moving wheels around muddies the test (`maintenance.md`) |
| Valve clearance | **Listen** | Shop job only if it ticks (`maintenance.md`) |

Nothing here needs the battery disconnected. If a shop does disconnect it, re-check that
both terminals are tight afterward: a loose one is the leading suspect for P0685
(`open-issues.md` item 2).

## DIY shopping list

Prices: HondaPartsNow, looked up 2026-11-03, **before shipping** (shipping can cost more
than the small parts: a Honda dealer parts counter in person avoids that). Budget prices:
eBay and ShopSavvy listings, same date. Filters aren't safety-critical, so the choice is
yours.

| Item | Buy | Honda (OEM) | Budget option | Status |
|---|---|---|---|---|
| Engine oil | **5 qt** API Premium **5W-20** (Honda preferred, synthetic OK). Change takes **4.4 US qt** with filter | any brand meeting the spec | same | VERIFIED: OM p.213, p.274 |
| Oil filter | 1 | **15400-PLM-A02**, $6.87. HondaPartsNow: A01 and A02 are interchangeable; no 2005 row shown on its page | Fram TG7317, ~$10 (eBay) | UNVERIFIED for this VIN. The Honda filter is cheaper than the budget one here, so buy Honda |
| Drain plug washer | 1, new every change (OM p.215) | **94109-14000**, $0.46 ("on oil pan drain plug", 14 mm) | none worth it | UNVERIFIED for this VIN |
| Engine air filter | 1 | **17220-RAA-A00**, $22.30. HondaPartsNow lists it for **2005 4-door EX, KA 5AT** | cross-reference the Honda number in a parts-store app (price not looked up) | Listing matches the trim; HondaPartsNow isn't clearly a dealer, so confirm by VIN |
| Cabin filter | 1 | **80292-SDA-407**, $20.19. HondaPartsNow says it replaces SDA-406 and SDA-A01 | Fram CF10134, ~$10–13 (ShopSavvy / Amazon) | UNVERIFIED for this VIN |
| ATF | **3 qt per drain-and-refill** (3.0 US qt, VERIFIED: OM p.274 and Chilton). Full change = 4 rounds = **12 qt** | Manual says **ATF-Z1** (OM p.219). Z1 is discontinued; **DW-1** (08200-9008, $10.75/qt, out of stock at HondaPartsNow 2026-11-03) is sold as its replacement | **Honda fluid only** (standing rule). DEXRON III is temporary only (OM p.219) | DW-1 replacing Z1: COMMUNITY (forum posts and a parts retailer), not a Honda document. Ask the Honda counter with the VIN |
| ATF drain plug washer | 1 per drain (Chilton: new sealing washer) | number never found | none | Ask the Honda counter |

Torques, from `specs.md`: oil drain plug **33 lbf·ft** with a new washer (OM p.215 and
Chilton; 29 is the V6 figure, never use it). ATF drain plug **36 lbf·ft (49 N·m)**, new
washer (Chilton). ATF level: engine hot (radiator fan has come on), level ground, engine
off, read within 60–90 s (Chilton), between the marks on the yellow-loop dipstick (OM
p.219). Never read it cold and overfill.

**One call does all the checks for free:** a Honda dealer parts counter with the VIN
(it's in `vehicle.json`). Ask for: oil filter, drain washer, air filter, cabin filter,
whether DW-1 replaces Z1, and the ATF drain plug washer number. Put the answers in
`parts.md`.

## Shop list (order of priority)

| # | Ask for | Rough price | Notes |
|---|---|---|---|
| 1 | **Brake fluid exchange with Honda Heavy Duty DOT 3** (DOT 3 or DOT 4 only as a temporary replacement, VERIFIED: OM Service Information Summary) + full brake inspection | No free estimate found for a 2005 Accord: get a quote | Every 3 years regardless of miles; no record (`maintenance.md`) |
| 2 | Only if you skip DIY ATF: **ATF drain-and-refill with Honda ATF (DW-1 or Z1)**, "the drain and refill the owner's manual describes (p.220), not a machine flush" | $221–273 (KBB, 2005 Accord, ZIP 51501 Iowa, 2026-11-03); $172–206 (RepairPal national). Expect more around Snohomish | Drain-and-refill instead of a flush machine: COMMUNITY (common Honda forum advice). That the manual's method is drain-and-refill: VERIFIED, OM p.220. A shop that only has a flush machine and generic "multi-vehicle" fluid: walk away |
| 3 | **Coolant change with Honda Type 2, premixed 50/50** (never plain water or straight antifreeze, VERIFIED: OM p.217). Change amount 1.32 US gal (OM p.274) | $201–248 (KBB, 2005 Accord, ZIP 51501, 2026-11-03); $242–390 (KBB, **2008** Accord, ZIP 98020 Edmonds) | Honda Type 2 part OL999-9001 is from Chilton's V6 article: confirm at the counter (`parts.md`). Lowest priority if level and colour look right |

The 60 mph shake: do the first ATF drain-and-refill **before** paying for mounts, and note
whether the shake changes after it (`open-issues.md` item 3, step 5).

## The day (Sunday, with Monday as the buffer)

Saturday is a work day for you and Sunday isn't, so the DIY day is **Sunday**. That also
leaves Monday spare if a part turns out wrong. No step leaves the car undrivable for
longer than the step itself, as long as **every part is bought before you start**.

| When | Job | Time (estimate, UNVERIFIED) | Undrivable? |
|---|---|---|---|
| Before Sunday | One call to the Honda counter (above); buy everything on the DIY list, incl. 12 qt ATF if you'll do all four rounds | — | No |
| Sun morning | Look at coolant (reserve tank level, colour) and brake fluid (level, colour); write it down | 5 min | No |
| | Drive belt look | 10 min | No |
| | Engine air filter, cabin filter | 20 min | No |
| | Drive 10–15 min to warm up, then oil + filter (`procedures/accord-2005-oil-change.md`) | ~1 h | Only while it's drained |
| | ATF drain-and-refill **round 1** (needs the engine warm for the level check after) | ~1 h | Only while it's drained |
| Sun–next week | ATF rounds **2, 3 and 4**, each after a short drive, one per day or two (OM p.220) | ~45 min each | Only while it's drained |
| Mon or later (weekday) | Shop: brake fluid + brake inspection; coolant if it's due | drop-off, ~1–2 h | Yes, while it's there: book a morning you don't need it |

Log every job in `log.md` with the **odometer reading**, and update its row in
`maintenance.md`. Write the drain plug socket size into the oil procedure once you know it.

## What I couldn't verify

- **Every part number above for this exact VIN**: free at a Honda dealer parts counter.
  The air filter listing matches a 2005 4-door EX KA 5AT, but HondaPartsNow isn't
  clearly a dealer.
- **DW-1 as Z1's replacement**: forum and retailer only. Same Honda counter call.
- **ATF drain plug washer part number**: never found. Same call.
- **Job times**: estimates, not from a manual.
- **Brake fluid exchange price** for this car: no free estimate found. Ask the shop.
- **Shop prices**: KBB's 2005 figures are for an Iowa ZIP. Put your own ZIP into
  kbb.com's repair estimator (free) for a local number.
- **Drain-and-refill instead of a machine flush**: COMMUNITY advice. The manual's own
  method is drain-and-refill (OM p.220).
