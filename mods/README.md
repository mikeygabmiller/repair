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
- `tool-tray-print/README.md`: 3D-printed bottom layer of the toolbox (2026-11-18): what goes
  in it, the photo scan sheet, and the print phases.
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
- **Front speakers + door deadening (2026-11-16):** `plan-front-speakers-2026-11.md`.
  6-1/2" doors + dash tweeters. DIY ~$105–130 budget coaxial, ~$175–205 with Kilmat,
  ~$240–285 Alpine component + Kilmat; shop labor $100–150 extra. Pick by sensitivity, not watts.
- **Used 10" sub on Marketplace (asked 2026-11-18): fair price, not a steal; not bought.**
  Pioneer "TS-W251F", $50, Monroe, driver + grille only (no box, no amp). "TS-W251F" not
  found anywhere; probably the TS-W251R, which a retailer lists as 10", single 4 Ω,
  120 W RMS / 600 W peak, 90 dB (COMMUNITY: Sonic Electronix search snippet, 2026-11-18),
  not the listing's "300 W". Ask the seller for a photo of the magnet label. Pioneer's box
  volume not found. A bare driver also needs a sealed box, a mono amp (~120–150 W RMS at
  4 Ω) and a copper (not CCA) 8 AWG kit; the Eonon has a sub output (wiring sheet,
  `plan-head-unit-2026-10.md`), so no line-output converter. Before any amp: fix the loose
  battery-terminal / USB-dropout item and repeat the draw test after (`open-issues.md`).
  Firewall pass-through without drilling not confirmed. Front speakers still the first
  upgrade; a sub then lets the doors be high-passed so they play louder and cleaner.
- **Used JL sub + JD500/1 on Marketplace (asked 2026-11-24): good gear, worth it if it
  tests good; not bought.** $250 (was $350), Monroe. Box reads "Slot-Ported BassWedge";
  JL sells that as the **CP-series with a W0v3 driver** (CP110-W0v3 10", CP112-W0v3 12"),
  CP112-W0v3 listed 300 W RMS, 4 Ω (COMMUNITY: retailer listings, abt.com, 2026-11-24).
  Exact model and size: read the box label. **JD500/1:** 250 W RMS at 4 Ω, 500 W at 2 Ω
  (14.4 V), **no onboard fuse; JL calls for 4 AWG power and ground and a 50 A fuse near the
  battery** (COMMUNITY: Crutchfield JD500/1 FAQ, 2026-11-24; confirm in the JL manual).
  So this setup **cannot** use the fuse-tap / no-firewall route: it needs a battery run
  through a firewall grommet (location still not confirmed; no drilling). 4 Ω sub on a
  250 W-at-4 Ω amp is a good match. Before buying: meter the sub's voice coil (DM500 on Ω;
  a few ohms = OK, near 0 or OL = bad), check the surround and push the cone evenly for
  scraping, and hear it play off a battery. Same order as below: power items
  (`open-issues.md` 2, 6, 9) closed first.
  **Follow-up (2026-11-24):** new prices seen (retail listings, recheck): CP110-W0v3
  $199.99–249.99 (Car Toys), CP112-W0v3 $249.99–279.99 (Car Toys, Sound of Tristate,
  Online Car Stereo); JD500/1 ~$330–410 base (Sonic Electronix, JBS Power Centre). New pair
  ≈ $530–690, so $250 used is about 40–45% of new. Listed 5 weeks with one drop already, so
  an offer under asking is reasonable. **Power with the Hertz HCP 4 already on the Scosche
  KPA8CC 8 AWG run:** the 8 AWG run can't also feed a 50 A amp. Plan: one 4 AWG power and
  ground run, a main fuse at the battery sized for that wire, a fused distribution block at
  the amps (40 A Hertz branch, 50 A JL branch); the old 8 AWG can be reused as the short
  block-to-Hertz branch because the 40 A branch fuse protects it (COMMUNITY: standard
  distribution-block practice). Main fuse size: from the 4 AWG kit's own rating, not chosen
  yet. Finish Hertz session 2 first so the signal path is proven.
  **Seller offered $100 (2026-11-24)**, ~15–20% of new. Confirm it's sub + amp, test both
  before paying, cash in person, no deposit.
  **Simplest route (2026-11-24): skip the JD500/1, run the sub off the Hertz's unused rear
  channels bridged.** Hertz 3-ch mode gives 170 W × 1 at 4 Ω, min bridged load 4 Ω (VERIFIED:
  Hertz HCP 4 tech sheet, `plan-front-speakers-2026-11.md`). 250 W vs 170 W is about 1.7 dB
  (10·log10 of the power ratio), a small difference. Uses the existing 8 AWG run and fuse; no new
  power wire, block or firewall pass. Needs: sub meters about 3–4 Ω (a 4 Ω coil; if it reads
  ~2 Ω, it can't be bridged on the Hertz), Eonon "Subwoofer Out" RCA → Hertz REAR IN (Y-adapter
  to both rear inputs, COMMUNITY), REAR MONO on, REAR LPF ~80 Hz, FRONT HPF 80 Hz, boost 0,
  speaker wire from the bridged terminals (read the amp's label) to the box. Rear speakers stay
  on the Eonon. JD route instead: KnuKonceptz Kolossus 4 AWG OFC kit $71.99–79.99
  (knukonceptz.com, eBay) + fused block (Scosche PDM482 $11.56, Stinger SPD5622 $42.95,
  Walmart listings, 2026-11-24, recheck) ≈ $85–125 and a second firewall run.
  **Fell through (owner, 2026-11-24).**
- **Used Kicker VCWR122 (48VCWR122) on Marketplace (asked 2026-11-24): pass unless it can be
  made 4 Ω; not bought.** $200, Monroe pickup, box only (no amp). CompR 12" ported,
  500 W RMS, **2 Ω final** (COMMUNITY: Sonic Electronix, Worldwide Stereo, AutoPro listings),
  18-3/8" L × 16" H × 11-1/4"/14-7/16" W (listing). New $259–350 (eBay, Worldwide Stereo,
  Car Toys, 2026-11-24), so $200 is ~57–77% of new. **The Hertz can't bridge 2 Ω (min 4 Ω,
  tech sheet)**; one Hertz channel at 2 Ω gives 85 W. Works on the Hertz only if the driver is
  dual 2 Ω and gets rewired in series (= 4 Ω); whether the loaded box uses a DVC driver is not
  confirmed (the bare 48CWR122 driver is DVC 2 Ω). Check: unscrew the driver, count terminal
  pairs (2 = dual coil). Otherwise it needs a 2 Ω mono amp plus the 4 AWG route. Look for 4 Ω
  boxes instead.
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
- **Aftermarket exhaust (asked 2026-11-16): not recommended until 2030.** Washington law
  bans modifying the exhaust to be louder than the original muffler and bans cutouts or
  bypasses; vehicles 25 or more years old are exempt (OFFICIAL RECORD: RCW 46.37.390(1),(3),
  last amended 2006, read 2026-11-16; no decibel number in the current text, the old 95 dB
  rule is gone). This car (2005) reaches 25 around 2030; whether that counts from model
  year is UNVERIFIED. Removing or hollowing the catalytic converter is federal tampering:
  never. A louder system also cuts against the sale-ready rule (most buyers of a stock
  Accord see it as a minus) and drones at highway cruise. **When the stock exhaust rusts
  out**, the stock-sound bolt-on replacement is MagnaFlow BRExhaust **106-0585**
  (~$223; listing says 2003–07 Accord 2.4 L, interchanges with Honda 18030-SDN-A00 /
  -A01 / -A10; COMMUNITY: retailer listing nahrods.com, 2026-11-16, confirm against the
  Honda catalog by VIN). Before any exhaust work: inspect for damage from the ditch slide
  (open issue 11). Flange bolt torque is not in `specs.md`: pull it from Chilton.
  **Looks-only option (owner, 2026-11-16): clamp-on dual-outlet tip** on the stock
  tailpipe. Bolts on after the muffler, so it doesn't make the car louder (COMMUNITY;
  the law targets louder, `RCW 46.37.390(3)`) and comes off for resale. Pick: 304
  stainless, double wall, side-specific for the exit side. Name-brand: Flowmaster
  **15390** (2.5 in inlet, dual 3 in angle-cut, polished 304, **left** side, clamp-on;
  ~$120–165, retailer listings 2026-11-16); Mishimoto, MBRP, Takeda make similar 2.5 in
  inlet tips. Budget no-name tips: price and steel grade not checked (avoid chrome-plated
  mild steel and "201" stainless: they rust). **Blocker: stock tailpipe size unknown.**
  Most name-brand clamp-on tips are 2.5 in inlet; if the pipe is smaller, a muffler shop
  expands the pipe end or an adapter sleeve is needed. Measure first (owner checklist).
  A true dual exit (one each side) means custom pipe work and cutting the rear bumper
  cover: not reversible, rejected.
- **Subwoofer, $100 budget (asked 2026-11-16):** $100 new only buys an all-in-one
  powered sub (amp built in). Seen 2026-11-16 (retail listings, recheck): Rockville SS8P,
  8" slim, 100 W RMS / 400 W peak, $99.95 (rockvilleaudio.com, Walmart); BOSS BAB10, 10",
  ~$97 (Walmart), listed "600 W RMS" but buyer reviews dispute it: treat as marketing.
  Name-brand powered subs (Rockford, Kicker, Pioneer) run ~$200–300 new; a used one is
  the best value at $100. Add ~$20–40 for a power wire kit (most don't include one).
  Hookup: Eonon sub RCA out + its AMP remote lead (#7) to the sub's REM, so it shuts off
  with the radio (battery item, `open-issues.md` 6); power wire fused near the battery,
  through an existing firewall grommet (location on this car not confirmed; no drilling);
  ground to a factory body bolt, **never a seat-belt anchor**. Fix the quiet Bluetooth
  level first (`log.md` 2026-11-05) or the sub's gain gets set too high.
  **No-firewall route (2026-11-16):** small sub only. Power from the front accessory-socket
  circuit (interior fuse #9, 15 A; sockets 120 W / 10 A combined, VERIFIED: OM p.103/269,
  `specs.md`) via a hardwired fuse tap, not a cigarette plug. OK only if the sub's own fuse
  is 10 A or less (SS8P fuse rating not found yet: read it off the unit or manual). It
  shares a cabin circuit, so watch for head-unit or USB dropouts on bass hits (ties to
  open items 2 and 9). The BAB10 or anything bigger needs a battery run through a grommet.
  In a sedan the cabin is a better spot than the trunk (COMMUNITY); keep it off the seat
  rails and seat wiring (SRS light on).
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
  **Budget set to $80 (owner, 2026-11-16).** Name brands are all over it (Injen black
  $239.97, Revlinekc $185.47, AEM $293.99, Injen polished $305.02; listings 2026-11-16).
  Only new kit found under $80: ProTuningLab aluminum short ram, $71.99 sale (reg. $110.30),
  2003–2006 Accord 2.4, **non-MAF only, excludes SULEV/LEV2** (search summary; the product
  page didn't load, so confirm fitment and what's included). Other route: a used name-brand
  kit for the right MAF version, plus a new filter. Generic risks: filter quality (dust
  past a poor filter wears the engine, which matters for 500k), loose couplers, no CARB EO.
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
  **Speakers already owned (owner, 2026-11-16): Kenwood KFC-1666S**, 6.5" 2-way coaxial,
  pulled from the Saturn's front doors (used; they were spliced to the Saturn's wires with no
  harness). Retailer specs: 4 ohm, 90 dB (Newegg, mobilespecs.net), top-mount depth 1-11/16"
  (Newegg) to 1-3/4" (mobilespecs.net), 30 W RMS (mobilespecs.net). No Kenwood sheet found.
  Same sensitivity as the Stage2 65C and shallower, so they are the **front-door candidate**
  if the measured depth allows (~2" reported). Use the Metra 82-7806 bracket and a speaker
  harness, not splices (harness fit for the front doors not confirmed). Inspect surrounds and
  check for cone rub before installing; test them on the harness before the panel goes back on.
  **One is damaged (owner photo, 2026-11-22):** a crack runs across the cone from the tweeter
  post out to the surround (about 2"), the surround is wrinkled at that spot, and the frame lip
  is bent near the leads. Claude advised a new pair; **owner chose to use them anyway
  (2026-11-22)**: patch the crack with a flexible glue, straighten the rim, and buzz-test before
  the panel goes on. If it buzzes, replace the pair.
  **Prices seen 2026-11-16:** Metra 82-7806 $12.99 (Sonic Electronix) to $19.95; Metra
  72-7800 (pair) $7.99 (Quality Mobile Video) to $15.51; 80 mil 36 sq ft butyl: VEVOR $53.90
  (Walmart), Kilmat $86.22 (eBay), Noico sold out in the US listings found. JBL Club 6500C
  $179.95 (out of stock) to $319 (Sonic Electronix), so not worth it over the free Kenwoods
  for 2 dB. Front doors with the Kenwoods: about $75-120 all in.
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
