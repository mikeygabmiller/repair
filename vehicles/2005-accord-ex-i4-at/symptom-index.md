# Symptom index: 2005 Accord EX-L 2.4 L automatic

Start here when something new happens. Each row: the **cheap-first path** (free checks →
cheap tests → shop), the car-specific records that match, and where the fix lives.

Rules that apply to every row (`CLAUDE.md`): get codes read first (many chain parts stores
read them free; the owner's MADDOX reads engine codes but **may not reach ABS/SRS**, `log.md`
2026-10-23); check recalls (`recalls.md`, VIN shows 0 open) and bulletins (`tsb-guide.md`);
inspect; test; only then buy parts. Write the **odometer** with every symptom.

Sources in the "Matches on this car" column: **OFFICIAL RECORD** for bulletins/recalls;
**COMMUNITY** for NHTSA complaint numbers (owner reports, searchable in
`complaints-all.md`). "Path" steps without a source are Claude's diagnostic order
(UNVERIFIED reasoning, standard practice).

## Lights on the dash

| Symptom | Cheap-first path | Matches on this car | Fix lives in |
|---|---|---|---|
| Check engine light, steady | 1) Gas cap if just fuelled (OM p.260). 2) Read code + **freeze frame** before clearing. 3) Look the code up in `tsb-guide.md`. 4) Fix the cause, clear, drive 3+ days | P0685 now (open issue 2); P0507 came with the car (`log.md`). Bulletins for P0139 (L4), P2646-family, P0171, P0116, P0973 | `diagnostics.md` P0685 tree; `tsb-guide.md` |
| Check engine light **flashing** | Misfire: ease off, no hard acceleration, read code today. Swap coils to see if it follows (`procedures/accord-2005-spark-plugs.md`) | Plugs new 2026-10-18 | Spark plug procedure |
| ABS light | 1) Code read with an ABS-capable tool (parts-store loaner scanners vary; ask). 2) Check fuses under-hood #17/#18 (OM p.268). 3) Look at the sensor wire and the wheel's encoder side. | **Known cause on this car: right front bearing encoder** (open issue 4). Bulletin DTC 68 = brake switch | `diagnostics.md` ABS tree |
| SRS light | Shop only. Free: call Honda with the VIN about recall history | Open issue 1; 40 NHTSA complaints mention the airbag/SRS light (search "airbag light") | Dealer / SRS shop |
| BRAKE light (parking brake off) | Check brake fluid level now (OM p.261). Low = pads worn or a leak; pedal soft = stop driving | — | `procedures/accord-2005-brake-fluid-coolant.md` |
| Charging light | Engine on, accessories off, drive to help (OM p.259). Then free charging test at a parts store | Several Honda alternator bulletins for 2004–05 (`tsb-guide.md`) | `procedures/accord-2005-battery-charging-tests.md` |
| Oil pressure light | **Stop now** (OM p.258). Check level. Low oil → add, check for leaks. Full oil and light stays → tow | — | — |
| D light blinking (automatic) | Transmission fault code stored. Read codes (P07xx). Don't keep driving hard | P0973 bulletins A05-071 (`tsb-guide.md`); complaint 11120196 (stuck in 2nd) | Shop with a Honda-capable scanner |
| Immobilizer light flashing, won't start | Wrong or damaged key (OM pp.77, 252). Try the spare key | Bulletin A02-053 | Dealer/locksmith for keys |

## Noises

| Symptom | Cheap-first path | Matches on this car | Fix lives in |
|---|---|---|---|
| Grinding/growl from a wheel that changes with speed, not steering | Jack up, spin the wheel, feel for roughness; rock at 12/6 o'clock | **Right front bearing** history (open issue 4, `issues-history.md`) | Shop (bearing press job) |
| Scraping/squeal when braking | Look at pad thickness through the wheel; minimum 0.060 in front (Chilton) | Grooved right front rotor (open issue 5) | `procedures/accord-2005-front-brakes.md` |
| Clunk over bumps | Rock each wheel; check stabilizer links (front and rear) and ball joints; check lug nuts | Right front lower ball joint new 2026-10-27; bulletin A05-021 (rear stabilizer link) | 10k inspection in `procedures/accord-2005-routine-checks.md` |
| Click when turning at full lock | Outer CV joint; look at the boots | Right axle new ~2026-10-22; left axle original | Shop or DIY axle (hard: `log.md` 2026-10-19) |
| Rattle for a second or two at **cold start** | Note when; record a video. Oil level right? | Owner reports a VTC cold-start rattle (open issue 8, UNVERIFIED as VTC) | `diagnostics.md` cold-start rattle |
| Ticking that speeds up with rpm | Oil level; listen at the valve cover; valve clearance overdue since 110k (OM p.203) | Valve clearance spec unsettled (`specs.md`) | Shop (valve adjust) |
| Squeal on start-up or with A/C/steering load | Drive belt: cracks, glazing; tensioner indicator | Belt inspect overdue | `procedures/accord-2005-drive-belt.md` |
| Whine from the steering when turning | PS fluid level, engine cold (OM p.224); Honda PSF only | A07-086 is V6 | Routine checks |
| Grinding/whining from the transmission | Fluid level and condition; don't ignore | Recall 11V395000 symptom: bearing noise + check engine light | Dealer (recall history) |
| Humming from speakers | Ground loop / install wiring | Bulletin A06-005; Eonon install (open issue 9) | `mods/plan-head-unit-2026-10.md` |

## Shakes, pulls, feel

| Symptom | Cheap-first path | Matches on this car | Fix lives in |
|---|---|---|---|
| Shake at 55–65 mph, worse on the gas | Lugs to 80 lbf·ft; balance; inner CV seated; **ATF change**; mounts | **Open issue 3**; complaints 10299703, 11076272 (light-throttle shudder, COMMUNITY) | `diagnostics.md` shake tree |
| Low-speed wheel wobble after hitting something | Rim runout, tire belt, bent tie rod/arm | **Open issue 11** (ditch) | `diagnostics.md` ditch tree |
| Pulls/drifts right | Tire pressures equal side to side; swap front tires left/right (if it follows the tire, it's the tire) | Bulletins A03-036 and A06-068 | Alignment shop with printout |
| Pedal pulsation / shake **only when braking** | Rotor runout (limit 0.004 in, Chilton) or thickness variation | Bulletin A06-087 (front brake judder) | Front brakes procedure |
| Soft or low brake pedal | Fluid level; bleed; then shop | Bulletin A07-045 | Brake fluid procedure |
| Harsh/late shifts, flare between gears, slipping | ATF level and condition; codes | 11V395000 recall; complaints 10435221, 10452237 (slipping, COMMUNITY) | ATF procedure; shop |
| Shudder on the 1–2 shift at ~2,000 rpm | ATF change first | Bulletin "1-2 upshift shudder" (10018079) | ATF procedure |
| Creeps forward fast after a cold start | Software (bulletin A06-041) | — | Dealer |
| Hard steering | PS fluid level (engine cold), belt | — | Routine checks |

## Won't start, stalls

| Symptom | Cheap-first path | Matches on this car | Fix lives in |
|---|---|---|---|
| Clicks / slow crank | Terminals tight and clean; battery test free at parts store; jump (OM p.253) | Open issue 6 (past drains); loose terminal found 2026-10-31 | `procedures/accord-2005-roadside.md`; battery tests |
| Cranks, won't start | Fuel? Immobilizer light? Fuses #19 IG Fuel Pump, #23 IGP (interior), #8 FI ECU (under-hood) | Recalls 07V097000 (fuel pump relay), 05V132000 (fuse box): not open on VIN | Roadside procedure |
| Stalls, especially with electrical load | Codes; battery/terminal check; P0685 history | Open issue 2; "stall" appears in 79 complaints (all versions) | `diagnostics.md` P0685 tree |
| Stalls/hard restart when very hot | Vapor lock bulletin A06-022 | — | Dealer |

## Electrical

| Symptom | Cheap-first path | Matches on this car | Fix lives in |
|---|---|---|---|
| Battery dead overnight | Charge, test battery; parasitic draw test | Open issue 6 | Battery/charging tests procedure |
| Lights dim with accessories | Battery terminals; charging voltage; P1298 code | Bulletin A05-034 (P1298, ELD); open issue 9 | Battery/charging tests |
| Phone/USB drops when lights switch | Split test (open issue 9) | Open issue 9 | `diagnostics.md` USB tree |
| Climate/radio panel backlights out at night | Bulbs inside the panel (COMMUNITY pattern: complaints 10241768, 10260177, 10340009) | Factory climate panel still in use | Shop or careful DIY (dash pod out: `log.md` 2026-09-07 notes) |
| Door locks act up, lock by themselves | Door lock actuator / switch | ServiceNews 10018164, 10018022; 19 complaints mention door locks | — |
| Accessory socket dead | Fuse #9 15 A (OM p.269); 120 W limit combined (OM p.103) | Bulletin A20-018 | — |
| Backup camera doesn't come on | Open issue 10 path | Open issue 10 | `diagnostics.md` camera tree |
| Window goes up then reverses, or auto-up lost | Reset after battery disconnect (`chilton-checklist.md` 51) | Bulletin A10-011 | — |

## Leaks and smells

| Symptom | Cheap-first path | Matches on this car | Fix lives in |
|---|---|---|---|
| Oil spots | Clean, cardboard under overnight, find the drip's colour and spot | Bulletin A15-020 (rear head-cover gasket); oil-leak ServiceNews | — |
| Red/brown drip, front middle | ATF (red when fresh). Check dipstick | Axle seal bulletin (10016290); right axle was swapped | ATF procedure |
| Sweet smell, green/blue drip | Coolant. Reserve level cold | Coolant overdue | Coolant procedure |
| Water on the front floor | A/C drain or cowl; bulletin "HVAC front interior water leak" | 10016310, 10015347 | — |
| Burning oil smell after driving | Oil on the exhaust: valve cover gasket (A15-020) | — | — |
| Fuel smell | Fuel lines (20k inspection). **Fuel spilled in the cabin in Oct 2026** (`log.md`) — smell from there is expected to fade | — | — |
| Rotten egg smell | Catalytic converter working hard / rich running: read codes | — | — |

## Tires and wheels

| Symptom | Cheap-first path | Matches on this car | Fix lives in |
|---|---|---|---|
| Slow leak | Soap test: tread, sidewall, bead, valve | **Left front bead leak** (open issue 11) | Tire shop |
| Uneven wear | Pressures; alignment printout | Alignment worse since the ditch | Alignment |
