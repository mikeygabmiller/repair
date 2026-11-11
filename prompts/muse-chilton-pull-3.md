# Chilton Library pull, Part 3: close the open UNVERIFIED items (prompt for Muse)

Written 2026-11-10. **Run this before Part 2** (`prompts/muse-chilton-maintenance.md`): every
item here is something a procedure or open issue in the repo is waiting on right now. One
session, ~25 items. Import rules are at the top of `prompts/muse-chilton-pull.md`:
screenshot = VERIFIED; a typed value with no screenshot = UNVERIFIED; **no safety-critical
torque is imported without a screenshot**.

Paste the **Shared rules** block from `prompts/muse-chilton-maintenance.md` first (the whole
block between "## Shared rules" and the "---" after "Output"), then everything between the
two lines below. Rule 10 of the shared block (skip Part 1 items) does **not** apply here:
these are Part 1 items that came back unclear.

---

**One extra rule for this session:** many Chilton articles for the 2005 Accord list only the
Hybrid, V6 or Acura TSX. When that happens, **switch the vehicle to 2006 Honda Accord, then
2007, 2.4 L 4-cylinder, automatic** and look again. Label every value with the **model year
and engine of the article it came from**. Never present a Hybrid, V6 or TSX value as 2.4 L.

## Q. Brakes (the right front job is waiting on these)
- Q01 **Brake Specifications table, 2005 Accord**: one screenshot of the whole table **with
  its footnotes readable**. I need the row(s) for the **4-cylinder sedan**: front rotor
  original and minimum thickness, thickness variation, runout, caliper **bracket** bolt
  torque, caliper **mounting/slide/flange** bolt torque, rear disc vs drum values. Copy the
  footnote text word for word.
- Q02 Front brake bleeder screw: wrench size and torque. Rear too.
- Q03 Brake fluid amount for a full flush (if printed).
- Q04 Rotor retaining screw torque for the 2.4 L (only a Hybrid value is known: 9.8 N·m).

## R. Front suspension torques for the 2.4 L (try 2006–07 if 2005 shows only Hybrid)
- R01 Lower ball joint castle nut torque and cotter pin rule.
- R02 Front stabilizer (sway bar) link nuts: torque, and whether they're self-locking/new.
- R03 Front lower arm bolts (front and rear bushing bolts): torque, and whether they're
  tightened with the car at ride height/on the ground.
- R04 Front damper (strut) pinch bolt torque (the through-bolt is known: 47 lbf·ft).
- R05 Knuckle-to-upper-arm ball joint nut torque.
- R07 How to confirm the CV axle's inner joint clip is locked into the transmission.

## S. Engine items blocking procedures
- S01 **Valve clearance, 2.4 L, cold**: intake and exhaust, from a 2005, 2006 or 2007
  Accord 2.4 L article (the 2005 tune-up table says exhaust 0.011–0.013 in with no "cold"
  label; a TSX article says 0.25–0.29 mm). Screenshot both if they still disagree.
- S02 Engine air filter replacement, 2.4 L (any 2003–07 Accord 2.4 L article): how the
  airbox cover is fastened.
- S03 Cabin (dust and pollen) filter replacement for a non-hybrid 2003–07 Accord.
- S04 Coolant drain and refill + air bleeding for the 2.4 L (2006–07 article OK); radiator
  cap pressure; thermostat opening temperature.
- S05 Drive belt routing diagram for the 2.4 L and the auto-tensioner indicator range
  (2006–07 article OK).
- S06 Oil change steps for the 2.4 L if any article exists; oil drain bolt **socket size**
  if printed anywhere.

## T. Electrical (open issues 2, 6, 9, 10)
- T01 **DTC P0685** troubleshooting for the 2005 Accord 2.4 L: what it means, the test
  steps, and the **PGM-FI main relay 1** location, pin numbers and test.
- T02 Parasitic draw: procedure and **maximum allowed draw** (any 2003–07 Accord).
- T03 Charging system: regulated voltage spec and alternator output test for the 2.4 L.
- T04 Back-up light circuit: which **under-dash fuse number** feeds the back-up lights on
  the 2005 Accord 2.4 L **automatic**. The owner's manual chart says interior fuse **No. 7,
  "Back-Up Lights", 10 A**; an earlier Chilton read said **No. 21 (7.5 A)**. Screenshot the
  schematic's fuse label.
- T05 Interior Lights schematic: trunk light fuse, whether the trunk latch switch is on
  the ground side or the +12 V side, and whether the MICU controls the lamp.
- T06 Power window auto-up/down reset after a battery disconnect.

## U. Wheels and tires
- U01 Wheel lug nut **size** (socket size) and thread, if printed.
- U02 Jacking points and jack-stand points with the diagram (if Part 2 F01 wasn't run).

---

## After the pull (for Claude, when importing)
Each value goes to `specs.md` (with path, model year/engine of the article, date), then:
Q → `procedures/accord-2005-front-brakes.md` (remove TENTATIVE where the screenshot settles
it); R → `chilton-checklist.md` items 10, 12–15 and `plan-right-front-2026-10.md`;
S → filters, coolant, belt, oil procedures (remove DRAFT labels); T01 →
`diagnostics.md` item 2 step E; T04 → `quick-reference.md` fuse note; tick
`owner-checklist.md`.
