# Mods: 2005 Accord EX

Upgrades and accessories, kept apart from repairs so repair answers stay easy to find.
Same rules as the rest of the repo (`CLAUDE.md`): every spec and part number sourced,
**reversible installs only, no cutting factory wiring, no drilling** (if drilling is the
only way, say so up front), soldered and heat-shrunk connections, keep the OEM parts.
Repairs and safety items come first: don't start a mod while `open-issues.md` has a
safety item the mod would delay.

Vehicle files referred to below (`log.md`, `open-issues.md`, `parts.md`, `specs.md`,
`profile.md`) are in `vehicles/2005-accord-ex-i4-at/`.

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
- **12 V accessories:** sockets are limited to 120 W / 10 A combined, fuse #9 (`specs.md`).
  Keep add-ons on key-on power (`open-issues.md`, battery item).
