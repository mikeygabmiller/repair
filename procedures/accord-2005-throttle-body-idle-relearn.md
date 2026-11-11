# Throttle body cleaning and idle relearn: 2005 Accord EX-L 2.4 L

**DRAFT.** No 2.4 L Chilton article pulled yet (checklist 36–37). The idle-learn steps below
come from Chilton's **V6 manual-transmission** article (`sources/chilton-2026-10-23.md`
D04), labeled. No torque specs are given here.

Why it's on the list: the car came with **P0507 (idle higher than expected)**, which went
away; whether the throttle body was ever cleaned is unknown (`log.md` 2026-08-26). Not
urgent while idle is normal and no code is set. Idle spec for reference: **620–770 rpm (AT)**
(VERIFIED: Chilton K24A4 tune-up row, `specs.md`).

Difficulty: easy. Time: ~45 min including the relearn (estimate). Car stays drivable.

## Shop method
Ask a shop for "throttle body service and idle relearn" with a Honda-capable scanner. The
relearn needs the ECM reset, which Chilton does with Honda's HDS tool.

## DIY (in place, cold engine, key off)
1. Remove the intake tube from the throttle body (hose clamp).
2. **Electronic or cable throttle?** The interior fuse chart lists "Drive by Wire" only for
   the 6-cylinder (OM p.269), which suggests the 2.4 L has a cable throttle (UNVERIFIED
   inference). If the plate is motor-driven (no cable), **don't push the plate open by hand
   with the key on**.
3. Spray throttle body cleaner on a rag, not straight into the bore with the engine off
   (COMMUNITY: keeps cleaner off sensors and out of the intake). Wipe the bore and both
   faces of the plate, opening the plate by the throttle cam/cable.
4. Let it dry 10 min. Refit the tube.
5. **Idle learn** (Chilton **V6 M/T** article, UNVERIFIED for the 2.4 AT): all electrical
   loads off; (ECM reset with HDS, or a battery disconnect resets it, COMMUNITY); key ON (II)
   2 s; start, hold **3,000 rpm in P/N until the radiator fan comes on**; then idle **5 min**
   with the throttle closed (fan run time doesn't count). Needed after a throttle body
   cleaning or ECM reset, not after just clearing codes.

## Backyard notes (COMMUNITY)
- Don't remove the throttle body: coolant runs through it on this engine (`parts.md`
  note) and the gasket (16176-RAA-A01) is a must-replace if it comes off.
- Rough or high idle after cleaning usually means the learn didn't finish: repeat step 5.

## Still needed from Chilton (library)
2.4 L throttle body article (cable vs drive-by-wire, cleaning cautions), 2.4 L idle relearn
(checklist 36–37; Part 3 prompt doesn't include it yet: Part 2 G10 covers idle control).
