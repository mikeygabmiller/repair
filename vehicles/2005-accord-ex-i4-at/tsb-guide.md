# Honda bulletins that matter for this car, by symptom

The raw list is `tsbs.md` (183 entries NHTSA holds for the 2005 Accord, OFFICIAL RECORD,
pulled 2026-11-10) plus Chilton's 92-title list (`sources/chilton-report-A-I-2026-10-27.md`
section I). This file keeps only the ones that can apply to a **2.4 L automatic sedan** and
says why. V6-only, hybrid-only, coupe-only, manual-transmission-only, navigation and
dealer-tool items are left out.

**What's known about each bulletin is only its title and NHTSA's one-line summary.** Honda's
actual fix (parts, steps, VIN range) is in the bulletin PDF, which nobody has read yet. Free
way to read one: nhtsa.gov → search "2005 Honda Accord" → **Manufacturer Communications** →
find the NHTSA ID → open the PDF. Or ask a Honda service advisor to print it (free to ask).
When one is read, write the fix here as `VERIFIED: bulletin <number>, p.N`.

Label for every row: **OFFICIAL RECORD** (bulletin exists, NHTSA summary) unless marked.

## Engine running, idle, check engine light

| Symptom | Honda no. | NHTSA ID | Title / NHTSA summary | Why it matters here |
|---|---|---|---|---|
| MIL with P0139 (rear O2 sensor) | A14-001 | — (Chilton list) | "MIL Comes On With DTC P0139 (L4)" | **L4-specific.** If P0139 ever shows up, this is Honda's fix to ask for |
| MIL with P2646/P2647/P2651/P2652 (rocker arm oil pressure switch, VTEC) | A13-021 / A-13-021 | 10098946, 10052884 | "The rocker arm oil pressure switch may need to be replaced" | Common K-series code; also low/dirty oil can set it. Oil change first |
| MIL with P0171 (lean) | A06-039 | — (Chilton list) | "MIL Is On With DTC P0171" | Engine split not shown: read before using |
| MIL with P0116 (coolant temp sensor) | A06-048 | 10040404 (SB-06-048) | "MIL comes on with trouble code stored. Software concern." | Software fix at a dealer |
| MIL with P0135/P0155/P0462/U0110 | A05-057 | — (Chilton list) | Title only | — |
| MIL with paired misfire P0303+P0304 and/or P0301+P0305 | A07-016 | 10021328 | Title only | P0303/P0304 pair could apply to an L4; P0305 is V6. Read before using |
| MIL from a software problem, 2005 Accord | SB-08-022 | 10040424 | "2005 Accord. The malfunction light is on with stored trouble codes due to a software problem" | Which codes: in the PDF |
| Creeps faster than expected at idle in gear after a cold start | A06-041 | 10022954, 10039537 | "Software is causing extra engine torque after a cold start" | Software update. Note the car came with P0507 (idle high) |
| Engine performance problems at high altitude/temperature | A06-022 (fuel vapor lock) / SB-06-022 | 10022953, 10039344 | "Fuel vapor lock" | Hot-weather stalling/hard restart |
| Rear cylinder head cover gasket leaks oil | A15-020 | 10108226 | "The rear cylinder head cover gasket leaks oil" | Engine family not shown in the summary: check the PDF. Oil on the back of the engine / burning smell |
| Engine oil leak at head cover, rear seal, oil pan; oil pump or spool valve | (ServiceNews 11/13/2003, 10/26/04) | 10010614, 10016778 | Dealer visit request | Oil leak guidance from early production |
| Stalls / no start after body shop repair | 0305, 1006 | 10020687, 10021129 | "Stalls with electrical load after body shop repair. DTC P1588/P1589…" | Relevant if the car was in a collision repair (unknown history) |
| Immobilizer won't start / light flashes | A02-053 and ServiceNews items | 10087261, 10016295, 10018015 | "Type 4 immobilizer… rolling code" | Only a programmed key starts it. Copies of keys: dealer or locksmith with the right tool |

## Charging, battery, electrical

| Symptom | Honda no. | NHTSA ID | Summary | Why it matters here |
|---|---|---|---|---|
| Alternator no or low output | several dealer visit requests 2004–05 | 10016355, 10014754, 10018176, 10016305, 10018089, 10014527 | "Alternator condition (no or low output)" | 2004–05 alternator complaints were common enough for Honda to collect parts. Relevant to open issue 6 (battery) |
| Alternator testing / regulator circuit | A12-002, A10-054 | 10043248 (SB-12-002) | "Service manual update: alternator and regulator circuit troubleshooting" | The fix for wrong diagnosis: ask the shop to use this procedure |
| Battery testing and replacement | A88-023 (rev. 2023) | — (Chilton list) | Title only | Honda's battery test standard |
| Headlights dim, or P1298 (ELD) | A05-034 | 10017428 | "Headlights dim or DTC P1298 is stored in the ECM/PCM" | Electrical load detector: ties into dimming with accessories (open issue 9) |
| Accessory power socket inoperative | A20-018, ServiceNews | 10018257 | "Service manual update: accessory power socket troubleshooting" | Socket on fuse #9 powers add-ons |
| Power locks lock by themselves / cycle twice | ServiceNews 06/2005, 07/2005 | 10018164, 10018022 | Title only | Known door lock actuator / switch behaviour |
| Radio volume drops after station change; no sound | 205 | 10015297, 10015298 | Dealer visit requests | Factory radio only (now replaced by the Eonon) |
| Humming or booming from speakers | A06-005 | — (Chilton list) | Title only | Could matter with the Eonon |
| Rear window regulator noise | 205, 1204, 01162005 | 10015305, 10018095, 10014760 | Title only | Rear windows grinding/clicking |
| Power window reverses / slow | A10-011 | — (Chilton list) | "Service manual update: power window goes up and reverses on its own, is slow…" | Auto-up reset after a battery disconnect (`chilton-checklist.md` 51) |

## Transmission (automatic)

| Symptom | Honda no. | NHTSA ID | Summary | Why it matters here |
|---|---|---|---|---|
| **Secondary shaft bearing / transmission damage prevention** | A11-050 (recall **11V395000**) | — | "Safety Recall: A/T software update to prevent transmission damage" | NHTSA shows no open recall on this VIN; whether it was done is in Honda's records (call 1-888-234-2138). The door-jamb build month says if it was covered (built from July 1, 2004) |
| MIL with P0973 (shift solenoid A short) | A05-071 / 705 | 10019416, 10018080 | "The MIL is on with DTC P0973" | NHTSA complaint 11120196 (2005 Accord, P0973, stuck in 2nd) matches this |
| Shift solenoid test, '03–'06 Accord L4 | ServiceNews 09/01/2005 | 10018475 | "S/M fix: shift solenoid valve test, '03-'06 Accord L4" | **L4-specific** correction to the shop manual |
| MIL with stored code from TCM software configuration | SB-06-039 | 10039466 | Title only | Software |
| 1-2 upshift shudder/judder at 2,000 rpm | 705, 08012005 | 10018079, 10018005 | "1-2 upshift shudder, judder, vibration at 2,000 rpm" | **Check against open issue 3** (shake): this is low-speed 1-2, not 60 mph |
| ATF leaks | 405 | 10016346 | "ATF leaks. Honda tech line summary" | — |
| Low-mileage A/Ts leak from axle seals | 05012005 | 10016290 | Title only | After the right axle swap, check the right seal for wetness |
| A/T in-warranty exchange program | A98-061 | — (Chilton list) | Title only | Dealer reman program; not a free fix |

## Brakes, steering, suspension, tires

| Symptom | Honda no. | NHTSA ID | Summary | Why it matters here |
|---|---|---|---|---|
| **Front brakes judder** | A06-087 | 10011766 (parts collection) | "Front brakes judder (rev. 5/11/2010)" | Shake under braking. The grooved right rotor (open issue 5) is a separate cause |
| On-car brake disc refinishing | A00-088 | — (Chilton list) | "On-car brake disc refinishing equipment and guidelines" | Honda prefers on-car lathe over swapping parts for judder |
| **Brake pedal low and soft** | A07-045 / 07045 | 10023898 | "Brake pedal is low and feels soft" | Read before a brake bleed if the pedal is soft |
| ABS/TCS DTC 68 (brake pedal switch) | ServiceNews 11/2004, 405 | 10013649, 10016352, 10014472 | "ABS/TCS DTC 68 brake switch failure… troubleshooting error" | If the ABS code changes from 12/61 to 68 |
| **Vehicle drifts to the right** | A03-036 | 10003480 | "2003–2005 Accord: vehicle drifts to the right" | After the ditch slide (open issue 11) a pull is more likely bent parts, but this is the known baseline |
| Pulls or drifts; steering wheel off-centre | A06-068 | — (Chilton list) | "Vehicle pulls or drifts, and/or steering wheel is off-center (rev. 2009)" | Honda's alignment diagnosis order. **Ask the alignment shop to follow it** |
| Rear stabilizer link broken | A05-021 / 05021 | 10017432 | "Rear stabilizer link is broken" | Clunk over bumps from the rear |
| Power steering moans when cold | A07-086 | 10024236 | Chilton marks it **V6** | Not this car (V6) |
| Tubeless tire repair | A06-082 | — (Chilton list) | Title only | Honda's plug/patch rules |
| Low fuel light at 1/4 tank | ServiceNews 11/2004, 10/2004 | 10013651, 10014475 | Title only | Known gauge behaviour |

## Body, interior, climate

| Symptom | Honda no. | NHTSA ID | Summary |
|---|---|---|---|
| Front interior water leak (HVAC) | 05162005, 02282005 | 10016310, 10015347 | "HVAC-front interior water leak" / dealer visit request |
| Poor A/C cooling during hard acceleration | ServiceNews 07/2004 | 10014017 | Title only (A/C cuts out at wide-open throttle: may be normal) |
| A/C leak detection; refrigerant and oil | A07-030, A16-064 | — | Shop references |
| Creak/click at dashboard or A-pillar; driver A-pillar noise | A04-057, A04-056, 205 | 10015306 | Title only |
| Front door noise or rattle | 1204, 11162004 | 10018096, 10014539 | Title only |
| B-pillar trim loose / noise; sash tape peeling | 1105, 805, 05162005 | 10018266, 10018265, 10016309 | Title only |
| Headliner sags at the back | A03-007 | — | Title only |
| Moonroof glass weatherstrip damaged | A05-012 | — | Title only |
| Driver's door panel lifts when closing the window | A06-043 | — | Title only |
| Door glass weatherstrip damaged by tinting | 02012005 | 10015289 | **Relevant: the owner tints his own windows** (log 2026-10-20) |
| Windshield side trim retainer loose/broken | A09-051 | — | Title only |
| Paint damage from environmental fallout | A99-062 | — | Title only |
| Center pocket lid doesn't open/close | A07-040 | — | Title only |
| Clock/sub-display wrong time | ServiceNews 11/2004 | 10013650, 10014474 | Factory display only |
| Low beam distributes light poorly | A08-010 | 10024628 | Title only; check before buying headlight upgrades |

## Airbags (SRS): for talking to the dealer only. Never DIY.

| Honda no. | NHTSA ID | Summary |
|---|---|---|
| A20-010 | 10172564 | Warranty extension: defects in the **replacement driver's** airbag inflator |
| A20-015 | 10172568, 10213538 | Warranty extension: defects in the **replacement front passenger's** airbag inflator |
| A15-040, A15-067, A19-076, A19-080, A19-030 | many | Takata inflator recalls and their consolidations |
| A16-033 | 10099382, 10099383 | Noncompliance recall: wrong passenger airbag installed at the factory, 2004–07 |
| A18-035 | — | Recall: incorrect installation of the Takata passenger inflator (= 18V268000) |
| A07-002 | — | Recall: driver's seat position sensor harness (= 07V001000) |
| A02-052 | — | Initializing the OPDS unit (passenger seat occupant sensor) |
| 1205 | 10018873 | SRS DTC 81-64 |

Ask the dealer about A02-052, A07-002 and A20-010/A20-015 when the SRS light gets diagnosed
(`open-issues.md` item 1).

## Next step for this file
Read the PDFs of the six most useful ones and write Honda's fix into this file: **A06-087**
(judder), **A03-036** and **A06-068** (pull/drift: alignment after the ditch), **A07-045**
(soft pedal), **A05-034** (dim lights / P1298), **A10-054** (charging diagnosis). All free on
nhtsa.gov (Manufacturer Communications) or on paper from a Honda service advisor.
