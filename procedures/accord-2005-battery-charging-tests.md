# Battery, charging and parasitic draw tests: 2005 Accord EX-L 2.4 L

For open issues 2 (P0685), 6 (past drains) and 9 (USB drops). Cheap-first: the parts-store
tests are free; the draw test needs only a multimeter (owner bought one, 2026-11-05).

Sources: battery rating OM p.275; battery care OM pp.242–243; jump OM pp.253–255; charging
fault limits are from Chilton's **Acura TSX** article (same K24 family, **not confirmed for
this car**, `specs.md`). Steps without a source: standard practice, labeled.
Car stays drivable throughout.

## 1. Free tests at a chain parts store (~15 min)
Ask for a **battery load/conductance test and a charging system test**. Bring the car with
the engine cold-ish so they can test cranking. Write the printout numbers into `log.md`.
Battery: EverStart Maxx, made May 2025, rated 12 V 38 AH/5 HR minimum (OM p.275), under
warranty (owner).

## 2. Quick voltage checks with the multimeter (~10 min)
| Condition | Reading | What it means | Source |
|---|---|---|---|
| Engine off, sat 2+ h | ~12.6 V full; ~12.2 V about half; under 12.0 V discharged | Battery state | COMMUNITY (general lead-acid table) |
| Engine running, 2,000 rpm, lights off | Fault if over **15.1 V** or under **13.5 V** | Charging | Chilton **TSX** article (UNVERIFIED for this car) |
| Engine running, flick high beams / rear defrost | Should stay in range; a big drop = weak alternator or bad connection | Load | COMMUNITY |
| Voltage drop: meter from battery − post to engine block while cranking | Over ~0.3 V = bad ground (COMMUNITY rule of thumb) | Ground path | COMMUNITY |
| Same, battery + post to alternator output stud, engine running with loads on | Over ~0.3 V = bad positive cable/connection | Feed path | COMMUNITY |

Measure **on the posts**, then **on the clamps**: a difference between the two = the clamp
contact is bad (the loose terminal found 2026-10-31).

## 3. Parasitic draw test (~1 h, mostly waiting)
Needs the meter's **10 A** jack. The car must be "asleep".
1. Everything off, key out, doors closed (trunk/door latches pressed shut with a screwdriver
   so the courtesy lights are off, or the hood switch if fitted). Hood open.
2. Meter on the 10 A DC range, leads in the 10 A and COM jacks.
3. Loosen the **negative** clamp. Clip one meter lead to the post and the other to the
   clamp, **then** lift the clamp off the post, so the circuit never opens (opening it
   wakes the modules and resets the radio).
4. Wait **30–45 min** for modules to sleep (COMMUNITY; Honda's own sleep time is not in the
   repo). Don't open a door: it wakes everything.
5. Read the current. Normal maximum for this car: **not found** (Chilton checklist 46).
   COMMUNITY rule of thumb for older cars: under ~50 mA is normal. Several hundred mA = a
   real drain.
6. High: pull fuses one at a time (interior and under-hood; charts in `quick-reference.md`),
   watching the meter. The fuse whose removal drops the current is the circuit. Put each
   fuse back in its own slot.
7. Prime suspects on this car: the Eonon (radio fuse #5 / ACC #32 depending on how it was
   wired), the aux-light relay harness (fused separately at the battery, `log.md`
   2026-10-29), anything spliced for the camera.
8. Clamp back on, tighten until it **can't be turned by hand**.

Safety: don't crank the engine or switch on headlights with the meter in series: it will
blow the meter's fuse. Battery gas is explosive: no sparks near it (OM p.243).

## 4. If the battery tests bad
Warranty swap at the store. Before installing the new one: clean both clamps (baking soda
and water, OM p.242), check the group size label (51R is **unverified**, `parts.md`).
Disconnect **negative first, reconnect it last** (OM p.242). Radio code: owner has it.
After a disconnect the readiness monitors take 3+ days to reset (OM p.260); the power window
auto function may need a reset (Chilton checklist 51).

## What I couldn't verify
- Honda's charging voltage spec and max parasitic draw for the 2005 2.4 L: Chilton
  (library) checklist 46–47; bulletin A10-054 also covers charging diagnosis.
- Battery group size: label on the battery.
