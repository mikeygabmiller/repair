# Accessory ideas for the blank dash switch slots (2005 Accord EX sedan, I4, AT): what to put there and how to wire it with no cuts

Vehicle context, from the repo (`vehicles/2005-accord-ex-i4-at/`): daily driver and work car. Passenger seat and rear seatbacks removed for cargo. Backup camera kit already installed (plate-frame camera + 4.3" monitor). 14-pin Bluetooth adapter (Amazon B08JQ9G2LP) plugged into the factory radio in place of XM. **Battery drain is unresolved.** No parasitic draw test has been done yet (`open-issues.md` #5, `log.md` 2026-09-08). The SRS light is on (`open-issues.md` #4). Battery rated 38 AH/5 HR (OM p.275, per `specs.md`).

Page-number convention: "OM p.X" is the **printed** page number of `/home/user/repair/sources/2005-accord-owners-manual.pdf`. The PDF page index is printed page + 1. The text was extracted with `pdftotext -layout` and read directly (Tier 1, VERIFIED).

Labels follow the repo's CLAUDE.md: VERIFIED (Tier 1–2, read), OFFICIAL RECORD, COMMUNITY (forums), MANUFACTURER/RETAILER (listing), UNVERIFIED (my estimate).

---

## Q1. What can a blank switch slot control or hold? (70 candidates, to be narrowed to 50)

### Takeaway
Most ideas fall into four groups: (a) **switched low-current loads** (≤ ~5 A: LEDs, USB, cameras, bass knob, amp remote) fed from an ACC-switched fuse tap; (b) **relay-driven loads** (fog lights, horns, inverter, compressor socket) where the dash switch only drives a relay coil and the load gets a fused feed from the battery; (c) **battery-protection and diagnostic items** (master accessory switch, low-voltage cutoff, push-to-read voltmeter, Bluetooth shunt monitor), which matter most for this car while the drain is unresolved; and (d) **passive uses** (OEM blank, coin/SD holder, mic or garage-remote mount). Several popular ideas are bad or illegal on this car: strobes, red/blue/green exterior light, anything that runs key-off without a cutoff, and seat heaters near side-airbag seams.

### Cited Findings

**Prices and specs that have a source (2025–2026 listings unless noted).** All prices are retailer snapshots and change often.

| Product | Price found | What the source says | Source |
|---|---|---|---|
| Genuine Honda fog kit 08V31-SDA-101 | **Discontinued**, no price | Fitment 2003–2005 Accord 4-door | [HondaPartsNow](https://www.hondapartsnow.com/genuine/honda~foglight~kit~08v31-sda-101.html) |
| Honda individual fog lamp 08V31-S5D-1M101 | $114.58 (MSRP $162.00) | Single lamp, not the SDA kit. Fitment to the SDA car not confirmed | [HondaPartsNow](https://www.hondapartsnow.com/oem-2005-honda-accord-fog_light.html) |
| Aftermarket passenger fog lamp (Go-Parts AC2593106) | $88.95 | "ONLY fits vehicles where the fog lights were Dealer Installed" | [Go-Parts](https://www.go-parts.com/ac2593106-2003-2007-honda-accord-fog-light-lamp-right-passenger-side.html) |
| Aftermarket 03–07 Accord fog switch | not captured | Listing says it plugs into the factory harness and mounts at the factory dash location | [FI Performance](https://fiperformance.com/products/2003-2007-honda-accord-fog-light-switch) |
| Viofo HK4 USB-C hardwire kit | $17.99 | ACC detection for parking mode. Low-voltage cutoff selectable at 11.8 / 12.0 / 12.2 / 12.4 V. Fuse taps not included by default. Listings on the same site disagree on red vs yellow wire = ACC vs constant | [BlackboxMyCar](https://www.blackboxmycar.com/products/viofo-type-c-hk4-hardwire-kit), [Viofo](https://www.viofo.com/products/viofo-6m-19-68fttype-c-hk4-hardwire-kit-for-a119-mini-2-a229-duo-a229-plus-a229-pro-t130-wm1-a329) |
| Viofo A229 Pro 2-channel dash cam | $289.99–$359.99 (list $359.99) | 4K front / 2K rear, buffered parking mode, time-lapse, low-bitrate modes | [BlackboxMyCar](https://www.blackboxmycar.com/products/viofo-a229-pro-4k-uhd-2-channel-dash-cam) |
| BlackVue Power Magic Pro | $17.54 (MSRP $25.99) | **Discontinued Jan 2023.** Users measured a BlackVue 550 at ~250 mA, ~420 mA with a rear camera, about the same in parking mode. Needs ≥12.25 V to switch on at the 12 V setting | [Subispeed](https://www.subispeed.com/products/pmp-blackvue-power-magic-pro), [BlackVue](https://blackvue.com/product-tag/parking-mode/), [DashCamTalk (COMMUNITY)](https://dashcamtalk.com/forum/threads/how-power-magic-pro-works.35038/post-431468) |
| Rockford Fosgate Punch PEQ (bass/treble remote) | $49.99 | For select 2007–2025 Punch/Power amps | [Sonic Electronix](https://www.sonicelectronix.com/item_8773_Rockford-Fosgate-Punch-PEQ.html) |
| Kicker CXARC (46CXARCT) bass remote | $39.99 | Wired. For CX amps, plus DX/PX with a remote bass jack. 19.5 ft cable. Replaces the discontinued 43CXARC | [Sonic Electronix](https://www.sonicelectronix.com/item_107707_Kicker-Bass-Remote-Control-Knob-CXARC-43CXARC.html) |
| Rockford PLC2 / JL Audio RBC-1 | $49.99 / $59.99 | Alternative bass remotes | [Sonic Electronix](https://www.sonicelectronix.com/item_8773_Rockford-Fosgate-Punch-PEQ.html) |
| Victron SmartShunt 500A (Bluetooth battery monitor) | $100.30–$105.55 US | Standby draw ~1 mA, or "<1 mA, ~0.7 Ah/month". The phone app is the display | [Solar-Electric](https://www.solar-electric.com/victron-energy-smartshunt-500a-50mv-battery-shunt.html), [Freeport Marine](https://www.freeportmarine.com/products/victron-smartshunt-500a50mv-bluetooth-battery-monitor-84027), [Bimble](https://www.bimblesolar.com/V-Smart-Shunt-500A-IP65), [Solacity](https://www.solacity.com/product/victron-smartshunt/) |
| Blue Sea 1830 M2 DC SoC monitor | $294.99 (from $499.99) | Blue Sea's plain DC voltmeter in this line is PN 1833 (price not found) | [DRSA](https://www.drsa.com/collections/electrical-meters-monitoring?page=1), [Blue Sea](https://www.bluesea.com/products/category/6/112/Meters/OLED_Digital_Monitors) |
| Victron BatteryProtect 65A (low-voltage disconnect) | $36.55–$68.20; $58.65 at eMarine | Disconnects non-essential loads before the battery is too low to crank. Draw ~1.5 mA on / 0.6 mA off (standard). Smart version 1.2–1.4 mA on, 0.6–0.9 mA off (listings conflict) | [eMarine](https://emarineinc.com/Victron-Energy-BP-65-BatteryProtect-12-24V-65A), [Bimble](https://www.bimblesolar.com/BatteryProtect65A), [InvertersRUs](https://invertersrus.com/product/victron-smart-battery-protect/) |
| Blue Sea ML-RBS 7700100 remote battery switch, 12 V | $195.09–$233.99 (MSRP $310.68–$347.33) | 500 A magnetic-latching, remote or manual, manual override knob, optional state LED | [Blue Sea](https://www.bluesea.com/products/7700100/ML-RBS_Remote_Battery_Switch_12V), [Freeport Marine](https://www.freeportmarine.com/products/blue-sea-7700100-ml-solenoid-12v-500a-wmanual-control-amp-deutsch-connector), [Klizer](https://mps.klizer.co/marine-parts/electrical-systems/battery-systems/remote-battery-management) |
| Hella Supertone horn kit 003399801 | $35.99–$50.00 | 118 dB, 300/500 Hz, ~5.5 A per horn. A relay is included. Harness sold separately per reviews | [FTSpeed](https://www.ftspeed.com/products/hel-003399801-hella-supertone-horn-kit-pair), [Subispeed](https://www.subispeed.com/products/hel-003399801-hella-supertone-horn-kit-pair), [Subimods](https://subimods.com/collections/2002-2003-wrx/products/hella-supertone-horn-kit-003399801) |
| Blue Sea 1016 dual USB socket | $25.98–$29.99 | 2.1 A max, **not** USB-C PD | [Hardin Marine](https://www.hardin-marine.com/c-2245-accessory-power-and-usb-power-ports.aspx), [Klizer](https://mps.klizer.co/12v-dual-usb-charger-socket-blue-sea-1016) |
| Blue Sea 1045 dual USB fast charger | $45.95–$74.99 US | 4.8 A total, USB-A, 1-1/8" socket hole. No Blue Sea USB-C PD model found | [NavStore](https://navstore.com/products/blue-sea-1045-12-24v-dual-usb-charger-1-1-8-socket-mount-1045), [Nautasea](https://nautasea.com/?p=46492), [Blue Sea](https://www.bluesea.com/products/category/30/USB_Chargers) |
| Blue Sea 1011 12 V dash socket | $9.95–$16.99 | Plain 12 V socket | [NavStore](https://navstore.com/products/blue-sea-12v-dash-socket-white-1011200), [DRSA](https://www.drsa.com/products/blue-sea-12v-dash-socket-white-1011200) |
| Honda-style square flush USB port (Anina) | price not captured | 44 × 26 mm cutout. Listing says to measure the blank first; blank can be trimmed | [Amazon](https://www.amazon.com/Anina-Charger-Adapter-Extension-Odyssey/dp/B0CDWSN719) |
| Nilight LED rocker switches, 5-pack (3-pin SPST) | $9.99 | Lighted on/off. Not Honda-styled | [Walmart](https://www.walmart.com/ip/Nilight-5PCS-Led-Lighted-Rocker-Switch-12V-Red-Illuminated-ON-Off-Toggle-30A-3Pin-SPST-Oval-Shaped-12mm-Hole-Automotive-Car-Truck-RV-Motorcycles-Mari/9318709059) |
| 5-pin rocker + relay + fuse harness (non-Nilight seller) | $17.99 | Generic. Nilight 10013W harness has no price captured | [eBay](https://www.ebay.com/p/2184686348) |
| LandAirSea hardwire kit for GPS tracker | $24.95 | 6–24 V input | [LandAirSea](https://landairsea.com/products/landairsea-54-waterproof-hardwire-power-adapter-cable-kit-from-external-power-source) |
| IPA 9036 relay bypass switch set (diagnostic tool) | not captured | Plugs into the fuel pump relay socket. 20 A continuous / 30 A surge | [VehicleServicePros](https://vehicleservicepros.com/directory/tools/product/10668515/innovative-products-of-america-ipa-relay-bypass-switch-set-no-9036) |
| Bussmann BP/HHH-RP-WM add-a-circuit (ATM/mini) | $7.97 | Up to 10 A, 32 Vdc | [Walmart](https://www.walmart.com/ip/ATM-Add-A-Circuit/52034992) |
| Bussmann BP/HHA-RP add-a-circuit (ATC/ATO) | $9.95 | Wrong size for mini-fuse boxes | [eBay](https://www.ebay.com/p/1637668461) |
| Posi-Tap connectors | $10.95 "each" (pack size unclear) | Reviewers call them "the best non-solder connector made" | [Custom Dynamics](https://www.customdynamics.com/posi-taptm-connectors) |

**Behavior facts tied to specific ideas:**
- Backup camera manual-on: forum installers wire a switched +12 V (ignition-switched, **not** battery-constant) to the camera trigger, with a diode or relay so the manual switch doesn't also light the reverse bulbs. Another option is a 2-position switch: always-on (key on) vs reverse-only — COMMUNITY: [Tahoe/Yukon forum](https://www.tahoeyukonforum.com/threads/backup-camera-with-manual-on-switch-question.25082/), [the12volt](https://www.the12volt.com/installbay/forum_posts.asp?tid=146857).
- Amp remote turn-on: factory radios have no remote output. Use an ignition-switched fuse confirmed with a meter, or a signal-sensing amp/LOC. On constant power "your amp will never shut off" — [MTX](https://www.mtx.com/library-remote-turn-on), [Audio Intensity](https://audiointensity.com/blogs/how-to-wire/how-to-wire-an-amplifier-remote-turn-on-wire).
- Fuel-pump-relay kill switches: forum posters say they are easy to bypass. On some cars an oil-pressure switch path keeps the pump running, so the engine only cranks longer. Switching the relay *ground* may not disable the pump and can cause problems if it fails open under load — COMMUNITY: [GMT400](https://www.gmt400.com/goto/post?id=1393788), [civic-eg](https://forum.civic-eg.com/viewtopic.php?p=160325), [NSXPrime](https://www.nsxprime.com/threads/kill-switches.188105/post-2060878).
- Seat heaters: the factory heater exists only on the EX-V6 and EX-L. (2026-11-07: this car turned out to be an EX-L, per its dual-zone climate panel, so it may already have them; look for switches beside the shifter.) "Because of the sensors for the side airbag system, there is no heater in the passenger's seat-back." Ignition must be ON — VERIFIED: OM p.87. A Carbotex-type aftermarket kit guide says the seat cover and seams must stay unmodified on seats with side airbags, and elements go only in the middle of the seat — [mx5parts guide PDF](https://www.mx5parts.co.uk/instructions/si5132.pdf). The Rostra listing excludes seats whose fabric is bonded to the foam or held with metal rings/rods — [Quadratec](https://www.quadratec.com/products/14159_1020.htm).
- This car has front side airbags and side curtain airbags — VERIFIED: OM pp.9, 23. "Do not attach hard objects on or near a front door" (side airbag zone). Nothing on the front airbag covers — VERIFIED: OM p.19.
- Garage-door / HomeLink-type devices: a 2010s-Accord DriveAccord poster tapped the door-lock fuse for constant power to an auto-dim HomeLink mirror — COMMUNITY: [DriveAccord](https://www.driveaccord.net/threads/constant-power-fuse-for-dashcam-hardwiring.500210/).

### Candidate list (70 ideas)

Columns: **Cost** = sourced price where the table above has one; otherwise "UNVERIFIED est." (my estimate, to be checked). **Diff** = DIY difficulty 1–5. **Time** is my estimate (UNVERIFIED) for a first-timer with panels already learned. "ACC tap" = add-a-circuit on an ACC-switched fuse (see Q2). "Relay" = dash switch drives a relay coil, and the load gets its own fuse on a battery feed.

**Lighting**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Genuine Honda fog kit (08V31-SDA-101) | Factory-look fogs; Honda switch fills the slot | Discontinued; used/NOS only (HondaPartsNow) | 4 | 4–6 h (bumper off) | Honda harness plugs in; relay | WA: ≤2 fog lamps, 12–30 in high (RCW 46.37.180). Bulb listed as both 9005 and H11 in repo `parts.md`: confirm |
| 2 | Aftermarket OEM-style fog housings + harness | Same function, aftermarket | ~$89/side Go-Parts (dealer-fog cars only) | 4 | 4–6 h | Relay kit; ACC or parking-light trigger | Name brand only per owner rules. Fitment by OEM number |
| 3 | Cargo-area LED flood/dome (rear seat area) | Lights the cargo floor where the seats were | UNVERIFIED est. $15–40 | 2 | 1–2 h | ACC tap → switch → LED; ground to existing bolt | Must not be constant-fed (drain) |
| 4 | Trunk LED strip | Brighter trunk than the 5 W bulb (OM p.275) | UNVERIFIED est. $15–30 | 2 | 1–2 h | Trunk-light circuit + switch, or ACC tap | Constant-fed trunk light = drain risk if it stays on |
| 5 | Driver footwell LED (white) | Floor light | UNVERIFIED est. $10–25 | 1–2 | 1 h | ACC tap, or Posi-Tap to dome circuit | Keep color white/amber; avoid red visible from the front |
| 6 | Puddle / ground lights | Light ground at the door | UNVERIFIED est. $20–40 | 3 | 2 h | ACC tap; door mounting usually means drilling | Usually drill → fails the owner's rule. WAC 204-21-230 bars neon-type lighting in motion |
| 7 | Under-hood work light (LED, switched from cabin) | Night roadside repair | UNVERIFIED est. $20–40 | 3 | 1–2 h | Fused battery feed under hood; switch wire through an existing firewall grommet | A rechargeable magnetic work light does the job with zero wiring |
| 8 | Ambient interior LED (white/amber, dimmable) | Mood/visibility | UNVERIFIED est. $20–40 | 2 | 1–2 h | ACC tap | Red visible from the front is illegal (RCW 46.37.280); keep dim |
| 9 | Cargo-area reading/task light | Paperwork light for a work car | UNVERIFIED est. $15–30 | 2 | 1 h | ACC tap | — |
| 10 | Auxiliary reverse lights (rear pods) | Better backing at night | UNVERIFIED est. $30–80 | 3–4 | 2–3 h | Trigger from reverse circuit via relay (interior fuse #7 Back-Up Lights 10 A) | Mounting often drills; WA reverse-lamp rules not researched (gap) |
| 11 | Backlight for added switches tied to dash dimmer | Added switches glow with the dash at night | ~$0 extra | 2 | 0.5 h | Posi-Tap to the illumination (small light) circuit | Under-hood fuse #4 "Small Light" 15 A (OM p.268) |
| 12 | LED light bar (front) | Off-road light | $41–63 bundles (Walmart, eBay) | 3 | 2–3 h | Relay harness | **Bad fit:** WA limits aux lamps to 2 and to 16–42 in mounting. Off-road only. Hurts resale look |
| 13 | Strobe/flash "warning" lights | — | — | — | — | — | **Illegal** (RCW 46.37.280; WAC 204-21-230) |

**Power**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 14 | USB-C PD port in the blank (panel-mount) | Fast phone/laptop charging | No name-brand Honda-shaped PD insert found (gap). Blue Sea has none in the line | 2 | 1–2 h | ACC tap (#9 accessory socket or #32 ACC) | Pick a unit with a published standby current |
| 15 | Dual USB-A port | Charging | Blue Sea 1016 $25.98–29.99 (2.1 A); 1045 $45.95–74.99 (4.8 A) | 2 | 1–2 h | ACC tap | Round 1-1/8" body; needs a modified spare blank |
| 16 | Extra 12 V socket (cargo area or slot) | Cooler, inflator, tools | Blue Sea 1011 $9.95–16.99 | 2 | 1–2 h | ACC tap ≤10 A, or relay + battery feed for more | Factory sockets: 120 W / 10 A combined (OM p.103) |
| 17 | Inverter remote on/off | Turn a cargo-area inverter on from the dash | Inverter price not researched (gap) | 3–4 | 2–3 h | Inverter on its own fused battery cable through a grommet; dash switch → inverter remote port | Big inverters drain fast; use only with the engine running |
| 18 | Panel voltmeter (always-on display) | Shows battery/charging voltage | Blue Sea 1833 price gap | 2 | 1 h | **ACC tap only** | Digital meters can draw 15–30 mA key-off if constant-fed (COMMUNITY, Q4) |
| 19 | Push-to-read voltmeter (momentary button) | Reads voltage only while pressed, key off too | UNVERIFIED est. $10–25 | 2 | 1 h | Constant tap through a momentary switch | **Zero draw** when not pressed; best for drain watch |
| 20 | Bluetooth shunt battery monitor (Victron SmartShunt) | Logs current in/out; catches drain in the act | $100.30–105.55 | 3 | 1–2 h | Shunt on the battery negative, under hood; no dash wiring; slot can hold nothing or an LED | ~1 mA draw; best drain diagnostic |
| 21 | SoC monitor display in slot (Blue Sea M2) | Battery % | $294.99 | 3 | 2 h | Shunt + display | Too big and expensive for a sedan dash; reference only |
| 22 | USB + voltmeter combo insert | Charging plus voltage | Price gap | 2 | 1–2 h | ACC tap | Same draw caveat as #18 |
| 23 | Switched laptop / tool-battery charger feed | Work-car charging | Depends on charger | 2 | 1 h | ACC tap ≤10 A | — |
| 24 | Wireless charging pad power (coin pocket) | Phone charging | UNVERIFIED est. $25–50 | 2 | 1 h | ACC tap / USB | — |
| 25 | Hardwired radar detector feed | Clean install | Price gap | 2 | 1 h | ACC tap | WA legality for passenger cars not researched (gap) |

**Battery protection / drain**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 26 | **Accessory master switch** (one switch kills every added accessory) | Instant "is it my add-ons?" drain test; peace of mind | ~$8–20 (switch + relay) | 2–3 | 1–2 h | All added loads fed from one aftermarket fuse block; dash switch drives its relay coil from an ACC tap | High value while the drain is unresolved |
| 27 | Low-voltage disconnect on the accessory bus (Victron BatteryProtect 65A) | Auto-cuts add-ons before the battery can't crank | $36.55–68.20 | 3 | 1–2 h | Between battery feed and the aftermarket fuse block | 0.6–1.5 mA own draw |
| 28 | Remote battery disconnect (Blue Sea ML-RBS) | Dash button isolates the battery (parking, anti-theft) | $195.09–233.99 | 4 | 2–4 h | Under-hood on the battery cable; control wires through a grommet | Kills radio presets/ECU memory each time (owner has the radio code). Overkill unless the drain can't be found |
| 29 | Dash-cam parking-mode on/off switch | Parking mode only when wanted | Switch ~$2–10 + HK4 $17.99 | 2 | 0.5 h extra | Switch in the HK4 constant (BATT) lead from a constant tap; ACC lead from ACC tap | HK4 cutoff 11.8–12.4 V; use 12.4 V on this weak-history battery |
| 30 | "Accessory power live" indicator LED | Warns that constant-fed add-ons are on | ~$2–5 | 1 | 0.5 h | LED across the switched side of #26 | — |
| 31 | Battery-maintainer port (pigtail at grille or bumper) | Plug a charger in without opening the hood | Price gap (NOCO/Battery Tender pigtails) | 1–2 | 0.5 h | Ring terminals on battery posts, fused | Not a dash item. Pairs with the drain fix |
| 32 | Bluetooth adapter power-cycle switch | Hard reset of the 14-pin adapter (head unit detects it only at power-up, `log.md`) | ~$5 | 3 | 1 h | Only if the adapter has a separate power lead; otherwise a T-harness. Never cut the 14-pin harness | Adapter is a drain suspect; a switch also proves/disproves it (gap: adapter wiring unknown) |

**Cameras**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 33 | Backup camera manual-on | Rear view while driving (cargo blocks the mirror) | Switch + diode/relay ~$5–15 | 2–3 | 1–2 h | Ignition-switched +12 V → switch → diode → camera trigger; keep the reverse trigger on its own diode | Never battery-constant (COMMUNITY) |
| 34 | 2-position camera mode (always-on vs reverse-only) | Same, cleaner | ~$5–15 | 2–3 | 1–2 h | SPDT switch between ACC feed and reverse feed | — |
| 35 | Camera monitor power switch | Monitor off at night (glare) | ~$5 | 1–2 | 0.5–1 h | Switch in the monitor's ACC feed | Monitor adhesive fails in heat; keep it out of the passenger airbag zone (`open-issues.md` #7, OM p.19) |
| 36 | Front/curb camera on demand | Front parking view | Price gap | 3 | 2–3 h | Video selector + ACC feed; route through an existing grommet | Plate-frame front mount avoids drilling |
| 37 | Video input selector (rear/front/cargo cam) on the 4.3" monitor | One screen, multiple cams | Price gap | 3 | 1–2 h | ACC tap | — |
| 38 | Dash cam (Viofo A229 Pro) hardwired, slot holds its switch | Evidence for a work car | $289.99–359.99 + HK4 $17.99 | 2–3 | 1.5–3 h | HK4 on two fuse taps (ACC + constant) | Parking mode draws ~0.25–0.42 A (BlackVue-class, COMMUNITY): hold off until the drain is fixed |
| 39 | Dash-cam "lock event" remote button in slot | Saves a clip hands-free | Viofo Bluetooth remote price gap | 1 | 0.25 h | Battery remote, no wiring | — |
| 40 | Cargo/cabin camera (theft/load check) | See cargo from the driver seat | Price gap | 3 | 2 h | ACC tap | Privacy considerations |

**Audio**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 41 | Sub bass knob in the slot | Bass level at hand | Kicker CXARC $39.99; Rockford PEQ $49.99; PLC2 $49.99; JL RBC-1 $59.99 | 2 (if amp exists) | 1 h | Brand cable to the amp; mount the knob in a modified spare blank | Needs a matching-brand amp |
| 42 | Amp remote on/off (sub mute) | Kill the sub without touching the radio | ~$2–10 | 2 | 0.5 h | Switch in the remote lead from an ACC tap | Never constant power (MTX) |
| 43 | Bluetooth mic mounted in the blank | Better call quality, clean look | ~$0 | 1–2 | 0.5–1 h | Mic cable routed behind the panel; drill only the spare blank | Passive. Keep out of airbag zones |
| 44 | Mic mute switch | Privacy mute | ~$5 | 2 | 0.5 h | Only via an inline 3.5 mm mute adapter if the mic is plug-in; don't cut the adapter's mic lead | Gap: the adapter's mic connector type is unknown |
| 45 | 3.5 mm AUX / USB audio jack in slot | Wired audio | Price gap | 2–3 | 1 h | Depends on the 14-pin adapter having aux in | Gap |
| 46 | Powered-sub / amp fuse-block master | Shut off all audio add-ons | ~$10–20 | 2–3 | 1 h | Relay + ACC tap | Overlaps #26 |

**Security**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 47 | Hidden kill switch via relay-socket adapter | Car won't start unless the hidden switch is set | IPA 9036-style bypass is a diagnostic tool (20 A / 30 A); price gap | 3–4 | 1–2 h | Adapter plugs into the relay socket; switch wire to a hidden spot | Which relay to use on this Honda is not verified (PGM-FI main relay layout: gap). Forum: fuel-pump kills are easy to bypass. A failure strands you: it's your only car |
| 48 | Starter-signal interrupt (relay in the start circuit) | Same idea, no fuel starvation | Price gap | 4 | 2–3 h | Needs a T-harness at an ignition or starter connector; no confirmed plug-in point | Shop job if no T-harness exists |
| 49 | GPS tracker hardwired (LandAirSea kit) | Theft recovery for a work car | Kit $24.95 + tracker/subscription | 2 | 1 h | Constant tap (trackers are meant to stay on) | Tracker standby mA not found (gap); counts toward drain. A dash on/off switch defeats theft use |
| 50 | Tracker "privacy" switch | Turn tracking off | ~$5 | 1 | 0.25 h | Switch in the tracker feed | Contradicts #49's purpose |
| 51 | Alarm valet switch | Valet mode on an aftermarket alarm | Alarm price gap | 4 | 4+ h (alarm) | Alarm T-harness | No aftermarket alarm on the car: N/A unless one is added. Alarms add key-off draw |
| 52 | Hidden fuel-door/trunk-release button | — | — | — | — | — | Factory levers exist (OM p.4); low value |

**Comfort**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 53 | Driver seat heater (carbon pad, seat bottom only) | Heat | Rostra kit price gap | 4 | 3–5 h (seat out) | Relay; ACC/IG tap; ground at a seat bolt (do not touch seat-belt or SRS bolts) | **SRS risk:** driver seat has a side airbag and the SRS light is already on. Pulling the seat touches SRS connectors (OM p.33: don't tamper). Shop-level, or skip |
| 54 | Plug-in heated cushion (12 V socket) | Heat, no install | Price gap | 1 | 0 h | Existing 12 V socket (≤10 A, OM p.103) | Don't route the cord near seat-side airbag seams. Socket is ACC-switched, so no key-off drain |
| 55 | 12 V fan (dash or cargo) | Airflow (rear seat area) | Price gap | 1–2 | 0.5–1 h | ACC tap | — |
| 56 | Cooler power (cargo area) | Keep lunch/work items cold | Price gap; coolers draw several amps (gap) | 2–3 | 1–2 h | Relay + battery feed + LVD (#27) | Thermoelectric coolers left on key-off kill batteries |
| 57 | Heated jacket / blanket outlet | Personal heat | Price gap | 1–2 | 0.5 h | 12 V socket | — |

**Utility**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 58 | Dedicated tire-inflator socket (high current) | Run a full-size compressor | Socket $9.95–16.99 + relay kit | 3 | 1–2 h | Relay + fused battery feed through a grommet | Many compressors exceed the factory sockets' 10 A (OM p.103); compressor draw not sourced (gap) |
| 59 | Horn upgrade (Hella Supertone) | Louder horn | $35.99–50.00 | 3 | 1–2 h | Plug-and-play harness to the factory horn connector + relay; steering-wheel button unchanged | ~11 A pair; relay required. Factory horn fuse: under-hood #13 "Horn, Stop" 20 A (OM p.268). Horn must stay on the wheel button; no dash horn needed |
| 60 | Horn selector (factory vs Supertone) | Quiet horn in town | ~$5 | 2 | 0.5 h | Switch in the relay trigger | Low value |
| 61 | Trailer-light test switch | Check trailer lights alone | Price gap | 2 | 1 h | Needs a hitch and T-connector harness | Car has no hitch recorded → N/A for now |
| 62 | Universal garage-door remote mounted in the slot | Garage/gate opener on the dash | Price gap | 2 | 0.5–1 h | Button cell, or ACC tap via 3 V/12 V regulator | A popular blank-slot use |
| 63 | Toll pass / parking tag holder | — | ~$0 | 1 | 0.1 h | None | Passive |

**Mirror / defrost-type**
| # | Idea | What it does | Cost | Diff | Time | No-cut wiring | Flags |
|---|---|---|---|---|---|---|---|
| 64 | Heated mirror retrofit | De-ice mirrors | Price gap | 4–5 | 3–5 h | Mirror glass swap + harness | Not confirmed whether the US EX had heated mirrors (gap). The manual's rear defroster is the only defrost circuit found (under-hood #14, 40 A, OM p.268) |
| 65 | Wiper-park / windshield heat strip | De-ice | Price gap | 5 | — | Usually cuts/drills | Skip |

**Passive uses**
| # | Idea | What it does | Cost | Diff | Time | Wiring | Flags |
|---|---|---|---|---|---|---|---|
| 66 | Keep the OEM blank cover | Factory look, best for resale | $0 | 0 | 0 | None | Default choice |
| 67 | Coin holder insert | Coins/tokens | Price gap | 1 | 0.1 h | None | — |
| 68 | SD card / small-item cubby | Dash-cam cards, fuses | Price gap | 1 | 0.1 h | None | — |
| 69 | Phone-mount base in a spare blank | Mount point without touching the dash | Price gap | 1–2 | 0.5 h | None; drill only the spare blank | Keep out of airbag and visibility zones (OM p.19) |
| 70 | Spare-fuse / tap kit stash (behind the blank) | Roadside fuses | ~$5–16 (Walmart 24-pc tap kit $15.99) | 1 | 0.1 h | None | Keep the Honda fuse puller (OM p.266) |

### Inferences
- Because the blank is a separate plastic piece, cutting a **spare** blank (keeping the original) satisfies "reversible, no drilling of the car." The owner's rules forbid drilling the car, not a replacement blank. A Honda part number and price for the 03–07 blank were not found (see the sibling note `blank_insert_products.md`).
- For a work car with no rear seats, the strongest ideas are #26, #19/#20, #33/#34, #3/#9, #15/#14, #29/#38 (after the drain fix), #59 and #66. Weakest or rule-breaking: #12, #13, #6, #53, #65, #28 (cost/benefit), #50, #51, #61.

### Gaps
- No verified name-brand USB-C PD insert in Honda switch form. Blue Sea's USB products found are USB-A (1016, 1045).
- 2003–2007 Accord blank-switch dimensions and part number were not found. DriveAccord threads were paywalled (HTTP 402). The 44 × 26 mm figure is from a listing for other Hondas.
- Prices not found for: Blue Sea 1833 voltmeter, Rostra seat-heater kits, inverters, coolers, compressors, front cameras, garage remotes, GPS tracker hardware, Bouncie, NOCO/Battery Tender pigtails.
- All install times and difficulty ratings are my estimates (UNVERIFIED). Install labor is covered in `install_labor_costs.md`.

---

## Q2. Correct no-cut power on a 2005 Accord: fuse type, switched fuses, relays, grounds, firewall

### Takeaway
The owner's manual identifies **interior fuse #9 "Front Accessory Sockets" 15 A**, **#32 "ACC" 7.5 A** and **#5 "Radio" 10 A** as the accessory-related fuses. It also says the accessory sockets work in ACCESSORY (I), so #9 is the best candidate for an ACC-switched add-a-circuit (confirm with a test light). Honda's parts catalog calls the 2005 Accord's small fuses "Fuse, Mini" (98200-4xxxx). Whether the interior box takes standard mini (ATM) or low-profile mini taps is **not confirmed**: pull a fuse and look. Anything over ~5–10 A should go through a relay with its own fused battery feed. Never tap SRS, OPDS, ECU or fuel-pump fuses.

### Cited Findings
- **Fuse box locations:** interior fuse box "on the driver's lower left side"; pull the lid toward you and off its hinges. Under-hood box "near the back of the engine compartment on the driver's side" — VERIFIED: OM p.265.
- **Interior fuse box chart (all values VERIFIED: OM p.269; parentheses = not on all models):** 1 (15 A) Drive by Wire [V6]; 2 15 A Ignition Coil; 3 (10 A) Day Light [Canada]; 4 15 A LAF Heater; **5 10 A Radio**; **6 7.5 A Interior Light**; **7 10 A Back-Up Lights**; **8 20 A Door Lock**; **9 15 A Front Accessory Sockets**; 10 7.5 A IG OPDS; 11 30 A IG Wiper; 12 not used; 13 (20 A) Passenger's Power Seat Recline; 14 (20 A) Driver's Power Seat Slide; **15 (20 A) Heated Seat**; 16 (20 A) Driver's Power Seat Recline; 17 (20 A) Passenger's Power Seat Slide; 18 15 A IG ACG; 19 15 A IG Fuel Pump; 20 7.5 A IG Washer; 21 7.5 A IG Meter; **22 10 A IG SRS**; 23 7.5 A IGP (PGM-FI ECU); 24–27 20 A power windows; 28 (20 A) Moonroof; 29 not used; 30 7.5 A IG HAC; 31 not used; **32 7.5 A ACC**; 33 7.5 A HAC OP.
- **Under-hood chart (VERIFIED: OM p.268):** 4 15 A Small Light; 7 7.5 A Back Up; 13 20 A Horn, Stop; 14 40 A Rear Defroster; 15 40 A Back Up, ACC; 16 15 A Hazard; 20 (40 A) Power Seats, Seat Heaters; 22 100 A Battery; 23 50 A IG1 Main / 50 A Power Window Main.
- **Conflict:** fuse-box.info says 2005 changes fuses 1, 3, 10, 14–16, 26, 27 and leaves 13, 17, 24, 25, 33 unused — [fuse-box.info](https://fuse-box.info/honda/honda-accord-2003-2007-fuses). The 2005 owner's manual (Tier 1, higher rank) shows the table above with those slots assigned. **Use the manual and the fuse-box lid label on the car.**
- **Which fuses are switched:** "ACCESSORY (I) You can operate the audio system and the accessory power sockets in this position" — VERIFIED: OM p.78. So the socket circuit (#9) is key-switched. Towing advice says to turn off "the radio and any items plugged into the accessory power socket ... so they do not run down the battery" with the key in ACC — VERIFIED: OM p.264.
- **Socket limit:** sockets supply 12 V accessories "rated 120 watts or less (10 amps)", combined across all sockets. They will not power a cigarette lighter element — VERIFIED: OM p.103.
- **Fuse rules:** replace with the same or lower rating, never higher. "Replacing a fuse with one that has a higher rating greatly increases the chances of damaging the electrical system" — VERIFIED: OM pp.266–267.
- **Fuse type:** HondaPartsNow lists 2005 Accord fuses as "Fuse, Mini" 5/7.5/10/15/20/30 A (98200-40500 … 98200-43000), plus block/multi-block fusible links. "Low-profile" is never mentioned — [HondaPartsNow](https://www.hondapartsnow.com/oem-2005-honda-accord-fuse.html). A DriveAccord thread (model generation unclear, likely newer Accords) answers "low-profile mini fuse" — COMMUNITY: [DriveAccord](https://www.driveaccord.net/threads/dashcam-install-soon-which-of-these-fuse-taps-will-i-need.508234/). The two don't agree on the physical form, so it's unresolved for this car.
- **Add-a-circuit ratings:** Bussmann BP/HHH-RP-WM (ATM/mini) is rated up to 10 A, 32 Vdc, $7.97 — [Walmart](https://www.walmart.com/ip/ATM-Add-A-Circuit/52034992). BP/HHA is the ATC version — [eBay](https://www.ebay.com/p/1637668461).
- **Tap orientation:** posters found taps only worked one way round ("the left side is hot"). The accessory's fuse goes in the tap's outer slot and the original fuse in the slot nearest the blade — COMMUNITY: [DriveAccord](https://www.driveaccord.net/threads/hardwiring-dash-cam.556265/). A generic guide says to find the slot's input side with a voltmeter (input ≈ battery voltage, output 0 V with the fuse out), test ACC slots with the key in ACC, and test constant slots with the key removed — [Nexar](https://www.getnexar.com/blogs/blog/how-to-hardwire-dash-cam-step-by-step).
- **Constant-fuse timers:** on some cars a "constant" fuse kept a camera powered ~30 min after shutoff because it's on a delay timer — COMMUNITY: [DriveAccord](https://www.driveaccord.net/threads/dashcam-install-diy-switched-power.539137/).
- **Ground:** use a body bolt near the fuse box, metal to chassis — [Nexar](https://www.getnexar.com/blogs/blog/how-to-hardwire-dash-cam-step-by-step). Disconnect the battery negative first — [Wolfbox](https://uk.wolfbox.com/blogs/news/the-ultimate-guide-to-installing-a-hardwire-kit-for-dashcam-a-step-by-step-tutorial).
- **Firewall pass-through:** a 2004 Accord owner reports an unused firewall grommet "just above the gas pedal" with a circular knock-out mark. The same poster was unsure whether 06–07 match 03–05. Slit the rubber, lubricate, and push wire through. Avoid routing behind the fender (shorts). Grommet all metal edges — COMMUNITY: [CarAudio.com](https://www.caraudio.com/threads/help-2004-honda-accord-amp-install.566166/), [the12volt](https://www.the12volt.com/INSTALLBAY/forum_posts.asp?tid=3374).
- **Amp remote:** use an ignition-switched fuse confirmed by meter, or signal-sense. Never constant — [MTX](https://www.mtx.com/library-remote-turn-on).
- **Fog-switch wiring pattern (other Hondas):** feed the switch from a switched source, switch output → relay/fog lamp, switch ground to a dash bracket. An add-a-fuse on the fog fuse works but shares that circuit — COMMUNITY (Acura TL): [AcuraZine](https://acurazine.com/forums/3g-tl-2004-2008-93/fog-light-wiring-help-999686/?nojs=1). Honda's own fog install PDFs exist for 2008–10 Accords, not the 7th gen — [Bernardi](https://www.bernardiparts.com/Images/Install/2008_AccordSedan_Foglights(L4)_AII35357.pdf).
- **Posi-Taps:** non-cut piercing-free tap — [Custom Dynamics](https://www.customdynamics.com/posi-taptm-connectors).
- **Airbag wiring:** "Do not tamper with airbag components or wiring for any reason" — VERIFIED: OM p.33. Honda SRS harnesses and connectors are yellow; the repo log notes three yellow connectors at the SRS unit on the floor tunnel (`log.md` 2026-09-07).

### Inferences
- **Recommended taps (UNVERIFIED until tested with a test light at the box):**
  - Switched (ACC/RUN): **#9 Front Accessory Sockets (15 A)** is first choice. It has the most headroom, and OM p.78 says the sockets work in ACC. Put the add-on on the tap's 5–7.5 A slot, and keep the socket's own total in mind (10 A combined for the sockets, OM p.103). **#32 ACC (7.5 A)** is second choice for very small loads (relay coils, camera trigger, amp remote) only.
  - Constant (key-off): **#8 Door Lock (20 A)** or **#6 Interior Light (7.5 A)** are the usual candidates. The radio memory may sit on #5, since the manual's anti-theft section relates the radio fuse to code entry. Use constant taps **only** for items with a low-voltage cutoff or a momentary switch (#19, #29), and only after the drain is diagnosed.
  - **Never tap:** #22 IG SRS, #10 IG OPDS, #23 IGP ECU, #19 IG Fuel Pump, #2 Ignition Coil, #21 IG Meter, #18 IG ACG. A fault on these can disable airbags, the engine or charging.
  - Unused slots (#12, #29, #31) may have no live terminals. A tap in an empty slot will not get power.
- **"IG" prefix = ignition-switched** is Honda's naming convention. That reading is UNVERIFIED here; confirm with a test light.
- **Relay rule:** loads over ~5 A (fogs ~110 W/pair, horns ~11 A, compressors, inverters, coolers) should get a 30/40 A automotive relay. The relay load feed comes from the battery through an inline fuse within ~7 in (18 cm) of the battery (common 12 V practice, UNVERIFIED). The dash switch drives only the relay coil (~0.15 A) from an ACC tap. That keeps the 10 A tap limit irrelevant and keeps factory circuits unloaded.
- **Grounds without drilling:** use existing body-ground bolts near the kick panel/fuse box, the factory ground studs, or a seat-track bolt **that is not a seat-belt anchor or SRS ground**. Never use seat-belt anchor bolts (safety-critical, CLAUDE.md).
- Crimped nylon butt connectors, no heat (owner rule, changed 2026-11-26 from solder + heat-shrink) apply at the accessory side. Fuse taps and Posi-Taps are the no-cut interfaces at the car side.

### Gaps
- Physical fuse form (standard mini vs low-profile mini) in the 2005 interior box is unconfirmed. Pull one fuse and compare, or buy a tap kit with both.
- Which interior fuses are constant vs switched is not stated outright in the manual (only #9 is implied ACC). Needs a test-light check at each slot, or the library service manual's wiring diagrams (Chilton Library/ALLDATA via a public library).
- The location of the 7th-gen firewall grommet comes from one forum post. Confirm visually.
- Honda fuel-pump/main-relay layout for a relay-socket kill switch was not researched (library service manual).

---

## Q3. Which ideas are bad or illegal, and why

### Takeaway
In Washington: no flashing lights (except the listed signal/hazard uses), no red visible from the front, no red/blue/green emergency-type lamps, no flashing white, no neon lighting in motion, and at most two fog lamps and two auxiliary driving lamps at legal heights. Mechanically bad: anything that draws key-off without a cutoff on a car with an unresolved drain, and aftermarket seat heaters in the driver's side-airbag seat on a car whose SRS light is already on.

### Cited Findings
- **Flashing lights are prohibited** except as required in RCW 46.37.190, .200, .210, .215, .300, WSP-authorized warning lamps, and bicycle LED taillights — RCW 46.37.280(3), [WA Legislature file](https://lawfilesext.leg.wa.gov/law/RCW/RCW%20%2046%20%20TITLE/RCW%20%2046%20.%2037%20%20CHAPTER/RCW%20%2046%20.%2037%20.280.htm), [Syfert copy, current May 2026](https://syfert.com/washington/sections/46.37.280.html).
- **No lamp displaying red visible from directly in front** except as RCW 46.37.190 requires — RCW 46.37.280(2), same sources.
- **Max two each** of spot, fog, auxiliary passing and auxiliary driving lamps. Fog lamps mount 12–30 in above the road. Aux passing 24–42 in. Aux driving 16–42 in. Fog/aux use is tied to RCW 46.37.220. The section sets no colors — [RCW 46.37.180](https://app.leg.wa.gov/RCW/default.aspx?cite=46.37.180).
- **WAC 204-21-230:** a vehicle in motion may not display aftermarket neon lighting. Red, blue and green lamps are restricted to emergency, police, tow, firefighter, and maintenance vehicles. Flashing white is prohibited except on authorized vehicles. Changing/moving lighted signs are barred in motion. A vehicle parked on private property may use aftermarket lighting except as RCW 46.37.180 limits. The rule does not address interior lighting — [WAC 204-21-230](https://app.leg.wa.gov/WAC/default.aspx?cite=204-21-230).
- WSP has cited RCW 46.37 and WAC 204-21-230 against decorative car lighting (e.g., Christmas lights) — [FOX26 Medford](https://www.fox26medford.com/news/state/washington-state-patrol-issues-reminder-wrapping-your-car-in-christmas-lights-is-illegal/article_09deb60c-f9a6-5358-9bab-b4d61d3c8df2.html). A law-firm blog lists ~$124 for a lighting ticket without a statute cite (low reliability) — [West Coast Trial Lawyers](https://westcoasttriallawyers.com/8-illegal-car-mods-in-washington-state).
- **Seat heaters and airbags:** Honda left the heater out of the passenger seatback "because of the sensors for the side airbag system" — VERIFIED: OM p.87. Aftermarket guide: on side-airbag seats, the cover and seams must stay unmodified — [mx5parts](https://www.mx5parts.co.uk/instructions/si5132.pdf). Owners report heated pads tripping occupant-sensor airbag lights — COMMUNITY: [NicoClub](https://forums.nicoclub.com/after-market-passenger-seat-bottom-won-t-heat-t324444.html). Honda: "Do not remove or modify a front seat without consulting your dealer" (driver position sensor / passenger weight sensors) — VERIFIED: OM p.33. Nothing hard on or near a front door (side airbag) or on airbag covers — VERIFIED: OM p.19.
- **Key-off loads:** amps on constant power never shut off — [MTX](https://www.mtx.com/library-remote-turn-on). Backup cameras on battery-constant feeds drain the battery — COMMUNITY: [Tahoe/Yukon forum](https://www.tahoeyukonforum.com/threads/backup-camera-with-manual-on-switch-question.25082/). Factory seat heaters can weaken the battery at long idle — VERIFIED: OM p.87.
- **Kill switches:** easy to bypass, and switching the wrong side can cause failures under load — COMMUNITY (see Q1 sources).

### Inferences
- **Do not do on this car:** strobes or flashing modes on any LED (#13). Light bars on a sedan (#12). Red/blue/green exterior-visible LEDs, including footwell/ambient that shows through the windshield (#5, #8 color choice). Underglow/puddle used in motion (#6). Aftermarket heater in the driver seat (#53), because of the side airbag, the existing SRS fault, and the fact that seat removal touches SRS connectors. Fuel-pump kill switch (#47) as a casual DIY on the owner's only car (a fault strands the car; better as a shop job or skipped). Any constant-fed accessory without a cutoff until the parasitic draw test is done.
- Fog lamp color: neither RCW 46.37.180 nor WAC 204-21-230 states a fog color. Selective yellow/amber vs white legality in WA is unconfirmed (gap). Stay with white or selective-yellow DOT/SAE-marked lamps and never red/blue/green.

### Gaps
- RCW 46.37.040/.190 color text for front lamps and the legality of auxiliary reverse lamps in WA were not fetched.
- WA radar-detector legality for private cars was not researched.

---

## Q4. Battery drain: draw of add-ons, and which ideas help diagnose or protect

### Takeaway
A healthy car's key-off draw is commonly cited as ≤ ~50 mA. An always-on digital voltmeter (15–30 mA, forum figures) or a parking-mode dash cam (~250–420 mA measured) is a large share of that, or several times over it. With a 38 Ah battery and an unresolved drain, the right order is: (1) parasitic draw test, (2) a master switch and/or Bluetooth shunt monitor to see and stop add-on draw, and only then (3) any constant-fed add-ons, each behind a low-voltage cutoff.

### Cited Findings
- Normal key-off draw: "Fifty milliamps would be a safe upper limit," many cars draw less. Let the car sit 10–45 min so modules sleep before measuring — [Fluke](https://fluke.com/en-in/learn/blog/digital-multimeters/how-to-find-parasitic-battery-drain-with-a-multimeter). Some devices draw substantially for up to ~20 min after shutoff — COMMUNITY: [Corvette Club UK](https://www.corvetteclub.org.uk/goto/post?id=5496).
- Voltmeter draw: analog ~1–2 mA. Digital 15–30 mA "enough to give you problems" — COMMUNITY: [Bimmerforums](https://bimmerforums.com/forum/archive/index.php/t-2448585.html). LED displays draw more than LCD, which draws more than a needle meter — COMMUNITY: [Maxima.org](https://maxima.org/forums/nissan-maxima-research/t-71234.html).
- Dash cam parking draw ~250 mA, ~420 mA with a rear camera, little difference in parking mode — COMMUNITY: [DashCamTalk](https://dashcamtalk.com/forum/threads/how-power-magic-pro-works.35038/post-431468). The Viofo HK4 cuts off at a user-set 11.8–12.4 V — [Viofo](https://www.viofo.com/products/viofo-6m-19-68fttype-c-hk4-hardwire-kit-for-a119-mini-2-a229-duo-a229-plus-a229-pro-t130-wm1-a329).
- Victron SmartShunt ~1 mA (~0.7 Ah/month) — [Solacity](https://www.solacity.com/product/victron-smartshunt/). Victron BatteryProtect 0.6–1.5 mA — [Bimble](https://www.bimblesolar.com/BatteryProtect65A).
- GPS trackers draw "a tiny amount" (no figure) — [Logistimatics](https://logistimatics.com/blogs/guides/hardwired-gps-tracker-for-car).
- Battery rating 12 V, 38 AH/5 HR — VERIFIED: OM p.275 (via `specs.md`). Repo history: the car died ~5 min after shutoff once, and was too weak to crank after a long key-on session. 12.6 V at rest. Load and draw tests not done. Suspects: Bluetooth adapter, camera wiring (`log.md` 2026-09-08, `open-issues.md` #5).
- Factory accessory sockets are key-switched (OM p.78). Plug-in devices in them cannot drain key-off unless the key is left in ACC (OM p.264 warning).

### Inferences
- Rough math (UNVERIFIED, my arithmetic): a 25 mA meter uses ~0.6 Ah/day, about 2–4 weeks to a no-crank state on a 38 Ah battery if roughly half is usable. A 300 mA parking-mode cam uses ~7 Ah/day and could flatten it in ~2–3 days without a cutoff. A 12.4 V HK4 cutoff stops well before that.
- **Ideas that help with the drain:** #26 accessory master switch (flip it off: if the drain stops, it's an add-on). #20 SmartShunt (logs real draw over a night). #19 push-to-read voltmeter (zero draw). #27 BatteryProtect on the accessory bus. #29 parking-mode switch. #32 Bluetooth adapter power switch (tests the top suspect, only if possible without cutting). #31 maintainer port.
- **Ideas that make it worse if wired constant:** #18 always-on voltmeter, #38 parking-mode cam, #49 GPS tracker, #51 alarm, #56 cooler, #4 trunk strip on the trunk-light circuit, #35 monitor on constant power. Wire every new add-on to an ACC-switched tap until the draw test is done.
- Fuse-pull drain diagnosis uses the same interior/under-hood charts (OM pp.268–269). Measure in series at the battery negative after a 10–45 min sleep wait (Fluke), then pull fuses one at a time. Check the camera/adapter taps first.

### Gaps
- Standby draw of the installed 14-pin Bluetooth adapter (B08JQ9G2LP), the 4.3" monitor and the plate camera are not published in sources found. They must be measured.
- No manufacturer-published standby current for typical name-brand panel voltmeters or USB sockets (Blue Sea 1016/1045) was found.
- Factory key-off draw spec for the 2005 Accord is not in the owner's manual. Check the library service manual.
