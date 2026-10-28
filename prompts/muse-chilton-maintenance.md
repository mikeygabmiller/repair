# Chilton Library pull, Part 2: future maintenance (prompt for Muse)

Run **Part 1 first** (`prompts/muse-chilton-pull.md`, the urgent right-front job). This prompt
covers the work a 2005 Accord at ~139k miles will need sooner or later. Part 1's import rules apply
(see the top of that file): a screenshot = VERIFIED, a typed value with no screenshot = UNVERIFIED.

**Run it in sessions, not all at once.** Each session below is one Muse run, on a different day if
possible. A long single run makes more mistakes and looks like the systematic downloading library
licenses forbid. For each session, paste the **Shared rules** block plus that session's block.

---

## Shared rules (paste this every session)

You are collecting repair data from **Chilton Library** (Gale) for one car. I'm already logged in
through my public library. Your job is to find, screenshot and transcribe, **not** to fill gaps.

**The car (choose exactly this in Chilton's vehicle selector):** 2005 Honda Accord **EX sedan**,
**2.4 L 4-cylinder (K24 engine)**, **5-speed automatic**, U.S. model. If a value differs by engine,
body or transmission, record only the 2.4 L / sedan / automatic value, and note that other versions
exist. If you can't tell which version a value is for, record all of them and flag it.

**Rules**
1. **Copy numbers exactly as printed**, with their units. Don't convert units or round. If both N·m
   and lb-ft are shown, record both.
2. **Never use your own knowledge or another website.** If it isn't in Chilton, write `NOT FOUND`
   and where you looked.
3. **Screenshot every page you take a number, code meaning, diagram or part number from.** Name the
   files with the item ID, e.g. `G03-1-water-pump.png`. Make sure the numbers are readable.
   **Always screenshot** tightening-sequence diagrams, belt routing, wiring diagrams and component
   location pictures.
4. For each item, record the **Chilton navigation path** and the **page title**.
5. For every procedure, also record:
   - **Special tools** (with any tool numbers printed)
   - **Parts that must be replaced, not reused** (gaskets, O-rings, crush washers, one-time-use
     bolts, self-locking nuts)
   - **Sealant or thread locker** named, and where it goes
   - **Every torque**, in the order it's used, including multi-step torques ("X, then Y degrees")
   - **Tightening sequences** (screenshot)
   - **Warnings and cautions**, word for word if they're short
   - **Anything that must be done afterwards**: relearn, bleed, refill, alignment, code clearing
6. Write procedure steps as short numbered lines, in your own words, keeping every number, tool and
   warning exact. Don't paste whole pages.
7. If two Chilton pages disagree, record both with both paths. Don't pick one.
8. Record a **part number only if Chilton prints it**. Don't look part numbers up anywhere else.
9. Work at a normal reading pace, one page at a time. **Don't bulk-download or save whole chapters or
   PDFs.** If the site shows a usage warning, CAPTCHA or limit, **stop** and report how far you got.
10. Skip anything you already collected in Part 1 (axle, hub bearing, lower ball joint, front brake
    limits, front alignment, ABS/SRS codes, fluid types/capacities, valve clearance, spark plugs,
    drive belt inspection, throttle body, mounts, interior bulbs, fuse charts, charging voltage).

**Output (one markdown file per session).**
Start with: `Session N · Found: N · Not found: N · Stopped early: yes/no (why)`.

Spec table, one row per value:

| ID | Item | Value exactly as printed | Applies to | Chilton path > page title | Warnings/notes | Screenshot |
|---|---|---|---|---|---|---|

Then one section per procedure:

```
### G03 Water pump replacement
Path: ...
Screenshots: G03-1.png, G03-2.png
Special tools: ...
Replace, don't reuse: ...
Sealant: ...
Steps:
1. ...
Torques (in order): ...
Afterwards: ...
Warnings: ...
```

End with a `NOT FOUND` list (with where you looked). Attach every screenshot.

---

## Session 1: General reference, engine, cooling

**F. General reference (do first)**
- F01 Jacking points and jack-stand (lift) points, front and rear, with the diagram
- F02 Any master **torque specification tables** for the car (engine, chassis, brakes, suspension):
  screenshot each table page
- F03 Master **fluid and lubricant capacity table**, including anything not covered in Part 1
  (A/C refrigerant and oil, windshield washer, differential if listed separately)
- F04 General fastener rules for this car: which bolts and nuts are one-time-use

**G. Engine maintenance and common repairs**
- G01 Valve cover gasket and spark plug tube seals: replacement, sealant spots, valve cover bolt
  torque and tightening sequence
- G02 Engine compression test: procedure, minimum pressure, maximum difference between cylinders
- G03 Engine oil pressure spec (at idle and at a given rpm) and how to test it
- G04 Timing chain: inspection (how to check chain stretch or tensioner extension, and the limit),
  replacement procedure, chain tensioner, crankshaft pulley bolt torque and the tool to hold the pulley
- G05 VTC actuator (cam sprocket): replacement procedure, bolt torque, any known-issue note
- G06 Crankshaft front seal and camshaft seals (if any): replacement
- G07 Oil pan: removal, sealant, bolt torque and sequence. Oil drain plug torque if not in Part 1
- G08 PCV valve: location, test, replacement
- G09 Ignition coils: removal, bolt torque, how to test one
- G10 Idle speed spec, and how idle is controlled on this engine
- G11 Drive belt **replacement** and **auto-tensioner** replacement: belt routing diagram, tensioner bolt
  torques, idler pulley bolt torque
- G12 Rear main seal: is it a transmission-out job? Procedure outline only

**H. Cooling system**
- H01 Thermostat: location, replacement, opening temperature, housing bolt torque, gasket/O-ring
- H02 Water pump: replacement procedure, bolt torque, gasket/O-ring
- H03 Radiator: removal, mounting torques, drain plug location
- H04 Radiator and heater hoses: list and routing
- H05 Radiator cap pressure rating, and cooling system pressure test spec
- H06 Cooling fans: how to test the fan motors, fan relay, and fan switch or sensor
- H07 Engine coolant temperature sensor: location, resistance or test values

## Session 2: Fuel, emissions, starting and charging, transmission

**I. Fuel, ignition and emissions**
- I01 Air/fuel ratio sensor (front) and secondary O2 sensor (rear): locations, torques, wrench or socket
  notes, test values
- I02 Fuel filter: location and service interval (is it in-tank / lifetime?)
- I03 Fuel pump: access (under the rear seat?), replacement, fuel pressure spec, how to relieve fuel
  pressure safely
- I04 Fuel injectors: test (resistance) and replacement, O-ring notes
- I05 EVAP system: purge valve and vent valve locations and tests, gas cap check
- I06 EGR (if this engine has one): location, test, cleaning
- I07 Exhaust: front pipe/flex pipe and catalytic converter flange torques, gasket types, hanger notes
- I08 Knock sensor, crankshaft position sensor, camshaft position sensor: locations, torques

**M. Starting and charging**
- M01 Battery removal/installation: hold-down and terminal torques, and **everything that must be
  reset or relearned after the battery is disconnected** (idle, radio, clock, power windows, etc.)
- M02 Alternator: removal and installation, bolt torques, output test specs (voltage and amperage)
- M03 Starter: removal and installation, bolt torques, current draw spec
- M04 Parasitic draw test procedure and the maximum allowed draw (skip if found in Part 1 E05)

**J. Automatic transmission (beyond the fluid change in Part 1)**
- J01 ATF level check: hot or cold, dipstick marks, and the check procedure
- J02 Transmission filter or strainer: does this transmission have an external filter? Location,
  replacement interval, procedure
- J03 Shift solenoids, transmission range switch, and line pressure test: locations and tests
- J04 Transmission trouble codes list (screenshot the table)
- J05 Transmission cooler lines: fittings and any cooler flushing procedure
- J06 Shift cable adjustment

## Session 3: Brakes, suspension, steering

**K. Brakes (full procedures; limits for the front are in Part 1)**
- K01 Front pads and rotors: full replacement procedure, caliper piston retraction, lubrication points
- K02 **Rear brakes**: disc or drum on this EX? Pad/shoe minimum thickness, rotor/drum limits, caliper
  bracket and caliper bolt torques, and whether the rear piston **screws in** (needs a tool) or
  pushes in
- K03 Parking brake: adjustment procedure and spec (number of clicks)
- K04 Brake fluid flush (full replacement), master cylinder bleeding, brake hose banjo bolt torque
  and washers
- K05 Brake pedal height and free play specs
- K06 ABS modulator and wheel speed sensor tests (resistance or air gap), rear sensors too

**L. Suspension and steering**
- L01 Front upper control arm and upper ball joint: replacement, torques
- L02 Front lower arm bushings (compliance bushings): replacement, torques, ride-height note
  ("tighten with the vehicle loaded / at ride height" warnings matter)
- L03 Front and rear shock absorbers/struts and springs: replacement, spring compressor notes, torques
- L04 Front and rear sway bar links and bushings: replacement, torques
- L05 Inner and outer tie rod ends: replacement, torques, toe adjustment and jam nut torque, rack boot
  clamp notes
- L06 Rear wheel hub/bearing: replacement, hub nut or bolt torque, ABS sensor notes
- L07 Rear suspension arms and trailing arm bushings: replacement, torques
- L08 **Rear** wheel alignment specs (toe, camber), and what's adjustable
- L09 Power steering: fluid flush/bleed procedure, pump replacement and torques, hose fittings, steering
  rack inspection

## Session 4: Lights, A/C and heat, body electrical, resets

**N. Exterior lighting**
- N01 Headlight bulb replacement procedure, and headlight aiming spec and procedure
- N02 Headlight assembly removal (bumper off or not?), mounting torques
- N03 Exterior bulb types: front turn/parking, side markers, rear turn, stop/tail, back-up, license
  plate, high-mount brake light, fog lights (if any). Note socket type (wedge, bayonet)
- N04 Taillight assembly removal

**O. Heating and A/C**
- O01 A/C refrigerant type and charge amount, compressor oil type and amount
- O02 A/C compressor clutch: **air gap spec and adjustment** (shims), clutch relay location and test,
  thermal protector
- O03 A/C system pressure (performance) test specs
- O04 Blower motor and blower resistor/power transistor: location, test, replacement
- O05 Heater control valve / blend door and mode door actuators: location, test
- O06 Cabin air filter replacement procedure (location and orientation)
- O07 Thermostat-related "no heat" diagnosis if Chilton has a chart

**P. Body and body electrical**
- P01 Front and rear door panel removal (clips, hidden screws), and the vapor barrier
- P02 Power window motor and regulator: replacement, bolt torques, and the window **auto up/down reset**
  procedure
- P03 Power door lock actuator: replacement procedure
- P04 Door hinges and latches: lubrication points; door striker adjustment and torque
- P05 Wiper motor and linkage, wiper arm nut torque, washer pump and reservoir
- P06 Horn: location and test
- P07 Relay locations and the relay chart (screenshot)
- P08 Wiring diagrams to screenshot: **power door locks**, **power windows**, **radio/audio**,
  **exterior lights**, **A/C compressor clutch circuit**
- P09 Hood latch and release cable, trunk latch and release cable

**Q. Relearn, reset and diagnostic procedures**
- Q01 Every **relearn or reset** procedure listed for this car: idle relearn, crankshaft position
  (CKP) pattern learn, throttle relearn, power window reset, TPMS (if equipped), maintenance
  reminder (if equipped), immobilizer key notes
- Q02 How to read and clear engine trouble codes, and Honda-specific data/self-test notes
- Q03 Readiness monitors / drive cycle procedure (for emissions testing after a battery disconnect or
  repair)
- Q04 If Chilton lists **Technical Service Bulletins** for this car, list the bulletin numbers and
  titles for the systems above (no screenshots needed for this list)
