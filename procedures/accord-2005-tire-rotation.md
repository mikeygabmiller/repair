# Tire rotation: 2005 Accord EX-L sedan

Sources: OM p.239 (rotation pattern and interval), p.250 (lug torque, crisscross), p.238
(balance, wheel weights), p.248 (jack points). Read 2026-11-10.
Difficulty: easy with two jack stands. Time: ~45 min DIY (estimate); free or cheap at a tire
shop, often bundled with a balance. Car is undrivable only while it's up.

**On this car right now:** wait. Don't rotate until open issue 11 (ditch damage, bead leak)
and open issue 3 (60 mph shake) are checked, and **chalk each tire's old position** first
(LF, RF, LR, RR) so a wobble that moves with a wheel shows which one it is
(`maintenance.md`).

## Pattern (VERIFIED: OM p.239)
- Non-directional tires: **fronts go straight back** (same side); **rears cross to the
  front** (left rear → right front, right rear → left front).
- Directional tires (arrow on the sidewall): front-to-back only, same side.
- Every **10,000 mi** (4-cylinder).

## Steps
1. Level ground, P, parking brake, chock. Loosen all lugs 1/2 turn on the ground.
2. Raise one side at a time at the jacking points (OM p.248 picture); **jack stands** under
   solid points before any wheel comes off. Never under the car on the jack.
3. Swap per the pattern. Wipe the hub faces clean (OM p.249).
4. Lugs finger-tight crisscross, snug crisscross, lower, then **80 lbf·ft (108 N·m)
   crisscross** with a torque wrench (OM p.250). **No impact gun to final torque.**
5. Set pressures: **32 front / 30 rear** cold (OM p.237). Front and rear differ, so after
   moving tires every pressure changes.
6. Re-check lug torque after ~50 miles (COMMUNITY, common shop practice; not in the OM).

## Backyard notes (COMMUNITY)
- **Spare as the placeholder (one jack, one stand, one corner up at a time).** Why it works:
  a rotation is a loop of four moves, and a loop needs one empty "slot" to start. The spare
  is that slot, like a temp variable in a swap. Each step: jack the corner, stand under it,
  swap, snug the nuts crisscross, lower.
  1. LR off → spare on LR. (LR tire is now loose.)
  2. RF off → old LR on RF. (RF loose.)
  3. RR off → old RF on RR. (RR loose.)
  4. LF off → old RR on LF. (LF loose.)
  5. Spare off LR → old LF on LR. Spare back in the trunk.
  Result matches the OM p.239 pattern (fronts straight back, rears cross forward). Torque
  all four to 80 lbf·ft crisscross at the end, on the ground. The car never moves on the
  spare, so its 50 mph limit (OM p.246) doesn't come into it. 5 lifts instead of 2, so
  ~1 h (estimate).
- With two stands and no spare trick: one side at a time does only front ↔ rear; the cross
  needs the spare trick above or a shop.
- Torque wrench: parts-store loaner is fine (deposit refunded).

## After
`log.md` (date, odometer, old → new positions, tread depth if measured);
`maintenance.md` tire rotation row. A vibration that's new after rotating = balance, or the
wheel that moved (OM p.238: "have the tires rebalanced"; aluminum wheels take **genuine
Honda wheel weights**).
