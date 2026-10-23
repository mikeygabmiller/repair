# Chilton Library pull: prompt for a browsing AI (Muse)

Paste everything between the two `---` lines into Muse. Log in to Chilton Library
through your library yourself first. Don't put your library card number in the prompt.

How the results get used (for Claude, when importing):
- A **screenshot** of the Chilton page counts as the source. Claude reads the screenshot and labels the
  value `VERIFIED: Chilton Library > <path>` (Tier 1). The value Muse typed is only a pointer to the
  screenshot. If Muse's number and the screenshot disagree, the screenshot wins.
- A value with **no screenshot** is imported as `UNVERIFIED (Chilton via Muse, <path>; no screenshot)`.
  Never import a safety-critical torque (brakes, wheels, suspension, steering, axle nut) without a screenshot.
- Specs go to `specs.md`, part numbers to `parts.md`, full procedures to `procedures/`,
  and code meanings to the matching item in `open-issues.md`. Screenshots go in `sources/chilton/`
  and are copyrighted, so they're removed before any public release (see `CLAUDE.md`).

---

You are collecting repair data from **Chilton Library** (Gale) for one car. I'm already logged in
through my public library. Your job is to find, screenshot and transcribe, **not** to fill gaps.

## The car (choose exactly this in Chilton's vehicle selector)
- 2005 Honda Accord **EX sedan**, **2.4 L 4-cylinder (K24 engine)**, **5-speed automatic**, U.S. model.
- If Chilton asks for an engine or trim, pick the 2.4 L. If a spec is listed separately for the 3.0 L V6,
  coupe or manual transmission, **record only the 2.4 L / sedan / automatic value**, and note that
  other versions exist.

## Hard rules
1. **Copy numbers exactly as printed**, with their units. Don't convert units or round. If the page shows
   both N·m and lb-ft, record both.
2. **Never use your own knowledge or any other website.** If you can't find something in Chilton, write
   `NOT FOUND` and list where you looked. A blank is useful; a guess is harmful.
3. **Screenshot every page you take a number, code meaning or part number from.** Name the files
   `A01-axle-nut-torque.png` and so on (task ID + short name). Make sure the number is readable in the
   screenshot.
4. For every item, record the **Chilton navigation path** (for example
   `Repair Manual > Drive Train > Halfshafts > Removal & Installation`) and the **page title**.
5. Record any **warning or note** on the page: "replace with a new nut", "one-time-use bolt",
   "stake the nut", "torque with the vehicle on the ground", "do not reuse".
6. If two Chilton pages give **different values** for the same thing, record both with both paths.
   Don't pick one.
7. Procedures: write the steps in short numbered lines, in your own words. Keep every number, tool
   name and warning exactly as printed. Don't paste whole pages of text.
8. Work at a normal reading pace, one page at a time. **Don't bulk-download or save whole chapters or
   PDFs.** Library licenses forbid systematic downloading. If the site shows a usage warning,
   CAPTCHA or limit message, **stop** and report how far you got.

## What to collect (in this order; finish each group before the next)

**A. Right front suspension and axle (urgent: there's a job coming up)**
- A01 Front axle (spindle) nut torque, and whether it must be a new nut or staked
- A02 Front halfshaft/CV axle removal & installation (steps, special tools, and how the inner joint
  comes out of the transmission)
- A03 Front hub/wheel bearing removal & installation: is the bearing pressed in? Steps and tools
- A04 Lower ball joint replacement: press-in or bolted? Steps, plus the ball joint castle nut torque
- A05 Every other torque you'd need in that corner: wheel lug nuts, brake caliper mounting bracket
  bolts, caliper slide/guide bolts, tie rod end nut, stabilizer (sway bar) link nuts, lower arm bolts,
  damper (strut) fork pinch bolt and through-bolt, ABS wheel speed sensor bolt, splash shield screws
- A06 Front brake rotor: minimum thickness, runout limit, thickness variation (parallelism) limit. Front
  pad minimum thickness
- A07 Front wheel alignment specs (toe, camber, caster), and whether camber is adjustable

**B. Trouble codes (meanings and the first test steps only)**
- B01 ABS code **12-1** (and **61-1**): meaning, and the first 3–5 test steps
- B02 SRS (airbag) codes **61-10, E2-11, F1-11**: meaning only. (I won't work on airbags myself; I
  just want to know what the codes mean.)
- B03 How to read and clear ABS and SRS codes on this car

**C. Fluids and capacities (2.4 L, automatic)**
- C01 ATF: type, drain-and-refill capacity, total capacity, drain plug torque, drain plug washer part
  number (if shown), and the fluid level check procedure
- C02 Engine oil: capacity with filter change, drain plug torque, viscosity
- C03 Coolant: type, capacity, and the air-bleeding procedure
- C04 Brake fluid: type, and the bleeding order (which wheel first)
- C05 Power steering fluid: type and capacity

**D. Maintenance jobs**
- D01 Valve clearance spec (intake and exhaust, cold) and adjustment procedure, plus the valve cover
  bolt torque and gasket part notes
- D02 Spark plugs: gap and torque
- D03 Drive belt: inspection limits, routing diagram, tensioner check
- D04 Throttle body cleaning, and any idle relearn procedure after cleaning or a battery disconnect
  (I've had an idle code, P0507)
- D05 Engine and transmission mount locations, inspection, and bolt torques

**E. Electrical (interior)**
- E01 Front ceiling/map light (EX): how to remove the lens or housing, and the bulb type for the two
  push-on spotlights and the middle courtesy light
- E02 Other interior bulb types: dome, door courtesy, trunk, glovebox
- E03 Wiring diagram for the interior lights / front ceiling light (screenshot the whole diagram)
- E04 Fuse box charts (under-hood and interior)
- E05 Charging system spec (normal charging voltage) and any parasitic battery drain spec or procedure

## Output format (one markdown file)

Start with a summary line: `Found: N · Not found: N · Stopped early: yes/no (why)`.

Then a table with one row per value:

| ID | Item | Value exactly as printed | Applies to (engine/body/trans) | Chilton path > page title | Warnings/notes | Screenshot file |
|---|---|---|---|---|---|---|

Then, for each procedure (A02, A03, A04, C01, C03, C04, D01, D04, E01), a section:

```
### A02 Front halfshaft removal & installation
Path: ...
Screenshots: A02-1.png, A02-2.png, ...
Special tools: ...
Steps:
1. ...
Warnings: ...
```

End with a `NOT FOUND` list showing where you looked for each item.

Attach every screenshot file with the report.

---
