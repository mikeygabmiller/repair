# Mods: 2005 Accord EX

Upgrades and accessories, kept apart from repairs so repair answers stay easy to find.
Same rules as the rest of the repo (`CLAUDE.md`): every spec and part number sourced,
**reversible installs only, no cutting factory wiring, no drilling** (if drilling is the
only way, say so up front), soldered and heat-shrunk connections, keep the OEM parts.
Repairs and safety items come first: don't start a mod while `open-issues.md` has a
safety item the mod would delay.

Vehicle files referred to below (`log.md`, `open-issues.md`, `parts.md`, `specs.md`,
`profile.md`) are in `vehicles/2005-accord-ex-i4-at/`.

## Research files
- `tools-plan.md`: staged tool-buying plan, budget vs name-brand, loaner tools, the 2020
  Harbor Freight jack stand recall.
- `lighting-upgrades.md`: what's legal and worth it (halogen upgrades yes; LED/HID retrofits
  in halogen headlights no, per NHTSA letters).

## Current
- `plan-head-unit-2026-10.md`: Eonon HAC1X7A head unit + camera, **bought 2026-10-26**,
  not installed. 90-day return window: install and test inside it. Before installing,
  check the climate panel type (single vs dual zone; `profile.md`) and do the parasitic
  draw test on the old setup (`open-issues.md`, battery item).
- `switch-slot-ideas/`: research on what to put in the two blank dash switch slots
  (2026-10-26). `report.md` is the summary (`report.html` is the same as a phone page);
  `research/` holds the notes behind it.

## Ideas noted
- **Hitch for storage (2026-10-31):** `plan-hitch-storage-2026-10.md`. Draw-Tite 24787 is
  the no-drill hitch (~$200–270). The car's ~100 lb tongue limit makes a hitch carrier a
  weak deal; a small trailer uses the 1,000 lb tow rating instead.
- **Roof storage for towels and cords (2026-10-31):** roof limit is 165 lb rack + load
  (VERIFIED: OM p.172, `specs.md`). Bare roof, so a rack needs clamp feet with a
  vehicle-specific fit kit (Thule Evo Clamp or Yakima BaseLine + BaseClip); kit number
  for a 2005 sedan **not confirmed** (Rack Warehouse lists a "guaranteed fit" Evo Clamp
  bundle for 2005 Accord without the kit number). Earlier pick was a soft roof bag
  (`sources/project-history-2026-10-21.md`). **Cabin is full (owner, 2026-10-31)**, so
  the pick is a hard, locking, side-opening box on a name-brand clamp rack: it keeps towels
  dry and frees cabin space for heavy gear. A soft bag leaks at zippers and can mark the paint.
  Prices seen 2026-10-31 (retail listings, recheck): Thule Evo Clamp feet $264.95, WingBar
  Evo 135 pair $279.95, Evo Clamp fit kit $159.95 (~$705 rack); Yakima BaseLine towers
  $219.95–275, JetStream bars $216–270, BaseClip $59.95–75 (~$500–620); universal bare-roof
  bars $54–67 (Accord fit unconfirmed). Boxes: Thule Force XT $600–750, Yakima SkyBox 16
  $719, SportRack Vista XL ~$350, Jegs 18 $290. FIVKLEMNZ soft bag $28–110. Sterilite 54 qt
  gasket tote $22.99; HDX 27 gal tote $44.65.
  **Budget set to $150 (owner, 2026-10-31):** no new hard box plus rack fits (cheapest US
  hard box seen: Jegs $199.99). Plan: budget bare-roof bars ($54–67) + soft bag strapped to
  the bars ($28–110 depending on sale), towels in a dry bag inside it. Used hard box only
  if one turns up cheap with keys.
- **Short ram intake (sound mod, 2026-10-26):** Injen IS1680P / IS1680BLK, $305.02
  (Modbargains, KamiSpeed), **no-MAF cars only**, CARB EO D-476-5. K&N Typhoon
  69-1209TS, $419.99 (Velocity Shop), lists 2004–07 EX, says it keeps the factory mass
  air sensor. AEM 22-511 install sheet covers 2003–04 only, no MAF. Which kit fits
  depends on whether the car has a MAF sensor: check before buying. Keep the stock airbox
  and resonator (Honda 17230-RAA-A00, $186 to replace, `parts.md`).
  **2026-11-16 lookup:** listings split by MAF too: HPS 827-737 "2003–2006 Accord 2.4L
  without MAF" (includes 2005 EX), HPS 827-173R "2003–2007 2.4L with MAF"; some sellers
  list separate "SULEV" kits. COMMUNITY (Honda-Tech thread): SULEV cars carry a MAF/IAT
  combo sensor, non-SULEV don't. So the under-hood emissions label (SULEV or not) plus a
  look at the intake tube settles which kit fits. Before buying: true cold-air kits put
  the filter low in the fender, so a deep puddle can pull in water (hydrolock); short ram
  avoids that but breathes hotter under-hood air. Expect sound, not a real power gain
  (gains quoted are maker dyno claims). Oiled filters: oil lightly if the car has a MAF.
  Install after the P0685 check-engine item closes, so a new code isn't mixed up with it.
- **Truck-bed LED strip kit as a cargo light (2026-10-31):** owner found a Temu 3-strip
  kit (with an inline switch; lengths, current draw and its yellow lead not confirmed). Best use: inside
  only, lighting the trunk and the rear-seat cargo area (seatbacks are out). Strip under the
  rear package shelf, one along the cabin side of the pass-through; zip ties or adhesive on
  clean painted metal, never on trunk carpet. Nothing on the headliner or pillar trims: side
  curtain airbags sit in the ceiling above the side windows (VERIFIED: OM p.23). Power:
  key-on only, either an add-a-circuit on fuse #9 (OM p.269) or, with no tapping at all,
  a 12 V plug into the front accessory socket (key-on per OM p.78). Not outside the car
  (WAC 204-21-230; resale). Matches switch-slot ideas #7/#17.
  **Owner wants them on with the trunk lid (2026-10-31):** doable. Shop method: a relay with
  a suppression diode, its coil across the trunk-lamp terminals and its load side fused
  (5 A) to the strips, so the trunk latch switch only carries the coil. That switch also
  feeds the dash's door-and-trunk-open monitor (OM p.60), and its rating isn't known, so
  don't load it past the stock 5 W lamp (OM p.275). Tap with Posi-Taps, no cutting. Before
  wiring: meter which lamp side is constant +12 V and which side is switched, and pull the
  Interior Lights schematic (`chilton-checklist.md` 51a). Drain risk only if the lid is
  left open or ajar; the kit's own switch is the off switch. Backyard: swap the stock bulb
  for one strip that draws no more than the bulb (bag the bulb for resale).
  **Plan changed (owner, 2026-10-31): one strip in the trunk, one in each front footwell.**
  Two circuits: trunk strip on the trunk relay; footwells on key-on fuse #9 with the kit
  switch. Footwell strips go under the lower dash edge, aimed at the carpet, never under the
  seats: the driver's seat position sensor and passenger weight sensors are there (OM p.23),
  and the manual says no objects under the front seats (OM p.27). No knee airbag is listed
  (OM p.23). Driver side tied off clear of the pedals. Bed strips may be too long and too
  bright for a footwell: check lengths and cut marks; add a dimmer or a short footwell kit.
- **White tire lettering (2026-11-06):** paint pen on the raised sidewall letters; wears
  off or scuffs off, so fully reversible. Maker's method (Tire Penz instructions PDF,
  RevZilla): scrub with soap and water, strip all tire shine (paint won't stick over it),
  rubbing alcohol wipe, lightly scuff the letters with a wire brush (scour pad on new
  tires), shake pen, thin coats, **12 h dry**, dressing OK only after that. Pens: Uni-Paint
  PX-30 white (oil-based, broad chisel) ~$9–11 (Staples $9.19, Quill $10.59, seen
  2026-11-06), PX-20 is the finer tip; Coker Tire white pen $15; Tire Penz kit (pen +
  brush) price/availability not confirmed (RevZilla shows closeouts). Hold until the
  sidewall check in `open-issues.md` item 11: a tire damaged in the ditch gets replaced.
- **Dash cam (2026-11-09):** researched, nothing bought. **Pick: a standalone camera, not
  one run through the Eonon.** Eonon's HAC1X7A page shows only one dash cam for the unit, the
  **A100** USB camera ("not included"; 1280×720, 120°, playback on the screen; eonon.com
  product image, read 2026-11-09), about $34–59 on eBay. Against it: 720p is weak for
  plates; it records only while the head unit is booted; it would sit on the unit's second
  USB port (#21 "USB Port"; #20 is CarPlay, Eonon wiring diagram) and the USB link already
  drops with the high beams (`open-issues.md` item 9). Where it stores video and whether
  it loops properly: not confirmed. The unit's #10 "Front Camera Input" is a live view
  only, not a recorder (UNVERIFIED: ask Eonon). Standalone lead: **VIOFO A119 Mini 2**
  (2K, Sony Starvis 2, supercapacitor, Wi-Fi app, 5 V / 1 A, −20 to 65 °C; viofo.com,
  read 2026-11-09), $159.99 on viofo.com, $120–130 seen on Amazon/eBay trackers (recheck).
  Budget: 70mai M310, about $33–53 (review sites; battery vs capacitor not confirmed).
  Plus a high-endurance microSD. Power: key-on only. No-tap way is the front accessory
  socket (key-on, OM p.78; fuse #9 15 A, `specs.md`); cleaner is VIOFO's HK4 hardwire kit
  ($17.99, viofo.com) on an add-a-circuit, both leads on a key-on fuse so there is no
  parking mode and no drain (`open-issues.md` item 6). Routing: behind the mirror, along
  the headliner edge, down the passenger A-pillar tucked in the door weatherstrip, never
  across the pillar trim face or behind it (side curtain airbags, OM p.23; SRS light is
  on, item 1). Stick the mount to the glass behind the mirror, out of the driver's view
  (RCW 46.37.410(2), read 2026-11-09). WA needs consent to record conversations (RCW
  9.73.030 per recordinglaw.com; statute not read): turn the mic off or tell passengers.
  **Update 2026-11-15 (owner wants one):** A119 Mini 2 deals: $100 at Best Buy (Slickdeals,
  2026-09-07, was $140); viofo.com $109.99 sale / $149.99 regular (undated). Buy-now line
  about $100 or less; Black Friday is 2026-11-27. Front + rear option: **VIOFO A229 Plus 2CH**,
  2K + 2K STARVIS 2, $209.99 sale / $249.99 regular (viofo.com), refurb $139.99
  (BlackboxMyCar). Rear cable: run it along the floor under the door-sill trims and up through
  the cargo area to the back glass, not along the headliner past the curtain airbags.
  Plan: start on the 12 V socket plug (no install), hardwire later with HK4 on key-on only.
  **$60 budget (owner, 2026-11-15):** only the **70mai M310** fits with a card: 2304x1296,
  130 deg, no GPS, no HDR, **battery not supercapacitor** (DashCamTalk forum), $32.99-40
  (DashCamTalk), rated 6.3/10, weak at night. Vantrue E1 Lite (supercapacitor, GPS, 1080p) is
  $89.99 (Best Buy), over budget. Pick: M310 + 64 GB high-endurance card if $60 is firm;
  otherwise watch Black Friday for the A119 Mini 2 near $85-100.
- **Audio: deadening vs speakers vs sub, which first (2026-11-15):** nothing bought.
  Order: (1) free: sort out the quiet Bluetooth and find the EQ (`log.md` 2026-11-05);
  louder speakers can't fix a weak signal. (2) Rear floor deadener: this is a **repair**,
  replacing what the gas spill dissolved (`log.md`); butyl only (gasoline dissolved the
  asphalt kind), on fully clean, dry metal. (3) Front doors: deaden + new speakers in **one**
  panel-off session, because a door speaker's bass depends on a sealed, damped door. Keep the
  factory speakers for resale. (4) Sub last, and only after the power items are closed
  (`open-issues.md` 2, 6, 9): an amp is the biggest current draw in this list, and a supply
  dip already drops the USB link. **The old "LC2i / speaker-level input" note is out of
  date:** the Eonon has a sub output among its unused leads #9–18 (Eonon wiring diagram,
  `plan-head-unit-2026-10.md`), so a powered sub can run from that; which lead is the sub
  out is not confirmed.
  **Factory speakers (Crutchfield Research Garage, "2003-2007 Honda Accord", read
  2026-11-15):** front doors 6-1/2" in plastic frames; **aftermarket door speakers need
  adapter brackets and new screw holes drilled in the door steel** (conflicts with the
  no-drill rule; a bracket that uses the factory clip holes is not confirmed). Rear deck
  6"x9", "much easier", no drilling listed (panel tool, 8 mm socket); Crutchfield says to
  deaden the deck if subs go there. Two tweeters in the upper dash corners with the crossover
  built in; no tweeter harness, so Posi-Products connectors. Speaker harnesses exist for
  every other spot. No outboard factory amp; factory radio "roughly 10 watts RMS x 4".
  Mounting depths not on that page.
  **$100 plan (2026-11-15):** free tuning first, then high-sensitivity rear 6x9s (no drill)
  and/or built-in-crossover dash tweeters. Front doors wait for the owner's call on drilling.
  **6x9 picks for bass (2026-11-15, retailer specs, nothing bought):** Kicker DSC6930,
  92 dB, 4 ohm, top-mount depth 3-3/16" (Kicker page via search) or 3-1/4" (Sonic
  Electronix), $119.99 a pair at Sonic Electronix. Budget: Pioneer TS-A6990F, 90 dB
  (Crutchfield, onlinecarstereo), 3-3/8" depth, $89.99 seen, discontinued. Harness: Metra
  72-7800 (Honda, lists Accord; owners report it fits the Accord rear deck), replaced by NVX
  NSH-7800. No official rear-deck depth limit found; 2003-07 Accord rear kits ship speakers of
  3" to 3.83". **With the rear seatbacks out, the trunk no longer seals off the back of the
  cone, so some deep bass cancels** (acoustics, UNVERIFIED how much in this car). Free test:
  cover the seatback opening with a heavy blanket or cardboard and listen for the bass change.
  **Under-seat sub: ruled out (2026-11-15).** The manual says not to "put any cargo or metal
  objects under the front seats" (VERIFIED: OM p.27); the driver's seat position sensor and
  passenger weight sensors are there, and the SRS light is already on (`open-issues.md` 1).
  Same compact powered sub goes on the rear cargo floor or in the trunk instead, strapped
  down: with the seatbacks out it plays straight into the cabin, and its own sealed box means
  the open seatbacks don't cancel it. Wiring: fused battery lead, chassis ground, Eonon sub
  out (#9-18) and remote lead (#7 "AMP", UNVERIFIED that it's a remote turn-on). Firewall
  pass through an existing grommet (location not confirmed; if drilling is the only way, stop).
  After `open-issues.md` 2, 6 and 9 are closed.
  **Front door speakers (2026-11-15):** drilling conflict. Crutchfield says new screw holes
  in the door steel; **Metra 82-7806** (pair, 6.5" and most 6.75") says "mount directly into
  the factory location, so no drilling is required" (metraonline.com, read 2026-11-15) and
  Sonic Electronix lists it for 1998-2007 Accord. Metra's own Accord fit not read (fit
  guide). Metra outranks Crutchfield on its own part; confirm with the bracket in hand.
  **Depth is the limit:** owners report about 2" from the door's mounting surface to the
  window track (2005 sedan and 2001, forum posts; no official figure). Measure with the glass
  down before buying. Candidate: JBL Club 6500C component set, 92 dB at 2.83 V, 3 ohm,
  woofer top-mount depth 1-13/16" (Electronic Express, Sonic Electronix), $179.95 seen
  (Sound of Tri-State, out of stock). Its tweeter goes in the factory dash-corner spot,
  crossovers behind the radio (Crutchfield method). Door butyl with the same panel-off.
  Owner found **JBL Stage2 65C** (Sonic Electronix, 2026-11-15; price not read, page blocks
  bots): 90 dB, 4 ohm (retailer listings); depth 2-3/16" (eBay) to 6.06 cm / 2.39" (most
  retailers), no JBL sheet found. Likely ~1/4-3/8" deeper than the ~2" owners report: fits
  only if the measured door depth allows. Club 6500C is 2 dB more sensitive and shallower.
  Stage2 65C launch price **$69.95** (JBL/HARMAN Gen 2 announcement); eBay new $59.99-87.99
  (2026-11-15). Buy-now line: $60 or less; fair up to ~$70 (MSRP); skip above $75.
- **12 V accessories:** sockets are limited to 120 W / 10 A combined, fuse #9 (`specs.md`).
  Keep add-ons on key-on power (`open-issues.md`, battery item).
