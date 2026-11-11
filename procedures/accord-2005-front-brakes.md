# Front brake pads and rotors: 2005 Accord EX-L 2.4 L

Sources: Chilton Brakes > Front Disc Brakes > Pads / Rotor R&I (pack F03; front figure
captioned V6, text not engine-specific); Chilton Brake Specifications table, 2005 Accord row
(report B), and the 2026-10-23 pull (`specs.md`); lug torque OM p.250.
Difficulty: moderate. Time: ~1.5–2 h for both front corners, first time (estimate).
**Undrivable** from the first caliper bolt until the pedal is firm again: **start in the
morning on a day off, parts in hand**.

**Safety-critical job.** Pads and rotors: OEM or name-brand only (Akebono, Bosch, Wagner,
Raybestos, Centric, Brembo, Honda; one-line reason: friction quality and fit are the
brakes). Every torque below must come from the table: if a value says TENTATIVE, look at the
Chilton table once more before using it (that's an owner library job: `owner-checklist.md`).

## Specs (from `specs.md`)

| Item | Value | Status |
|---|---|---|
| Caliper **bracket** bolts | **80 lbf·ft** | VERIFIED: Chilton Brake Specifications, 2005 Accord row |
| Caliper **mounting/slide (flange)** bolts | 26 lbf·ft (4-cyl) | **TENTATIVE**: footnote reading unclear in one pull, read as "4 cyl." in the other. **Confirm before use** |
| Pad minimum lining | 0.060 in | VERIFIED: Chilton |
| Rotor runout limit | 0.004 in | VERIFIED: Chilton |
| Rotor minimum thickness | 0.830 in for non-V6 | **TENTATIVE** (footnote). The number cast/stamped on the rotor itself wins |
| Rotor retaining screws | torque not found (Hybrid figure 7.2 lbf·ft, not this car) | Snug; they only hold the rotor while the wheel is off |
| Lug nuts | **80 lbf·ft (108 N·m)** crisscross | VERIFIED: OM p.250 |
| Pad shim grease | Honda M-77 assembly paste (part shown as "o8798-9010", probably 08798-9010) on the pad side of the shims and the backs of the pads; wipe excess | VERIFIED: Chilton F03; part number to confirm at a Honda counter |
| Stuck rotor | Two **8 × 1.25 mm** bolts in the rotor's threaded holes, two turns at a time | VERIFIED: Chilton F03 |
| Fluid | Honda DOT 3 (OM p.223) | VERIFIED |

## Parts (to confirm by VIN, `parts.md`)
- Front rotor: Honda **45251-TA0-A02 or 45251-TA5-A00** (the catalog lists both for a
  4-door EX KA 5AT; the VIN decides).
- Pads: Honda front pad set number **not yet looked up**. Name-brand pads: look up by the
  Honda number at the parts counter.

## Steps (Chilton F03)
1. Siphon about half the fluid out of the reservoir (pushing the pistons back raises the
   level).
2. Loosen lugs, raise, **jack stands**, wheel off.
3. **Pads only:** remove the brake hose bracket bolt and the lower caliper flange bolt,
   pivot the caliper up, remove pads, shims, pad retainers. Check the caliper pins slide
   freely (clean and re-grease if sticky). Fit new retainers if supplied, M-77 on shims
   and pad backs, new pads, lower the caliper (push the piston back with a C-clamp and the
   old pad if needed), flange bolt to the table value.
4. **Rotor too:** remove both caliper bolts, hang the caliper on wire (**never by the
   hose**), remove the bracket bolts and bracket, remove the rotor screws, pull the rotor
   (stuck: the 8 × 1.25 mm bolt trick). Clean the hub face of rust (a flat face prevents
   runout). New rotor, screws, bracket at **80 lbf·ft** (Chilton), pads, caliper.
5. Other side the same. Lug nuts **80 lbf·ft** crisscross.
6. **Pump the pedal until it's firm before the car moves** (Chilton warning). Top the
   reservoir to MAX.
7. Bed the pads: several moderate stops from ~35 mph, no full stop with the pedal held hard
   while hot (COMMUNITY; follow the pad maker's instructions on the box if given).

## Backyard method (COMMUNITY)
- Measure rotors with a $20 micrometer or a parts-store loaner, not a tape: a few
  thousandths decide reuse vs replace.
- Brake parts cleaner + wire brush on the hub face and the bracket's pad slots. Why: rust
  on the hub tilts the rotor (runout → judder, the symptom of bulletin A06-087); rust in
  the slots makes pads stick and wear unevenly.
- Free loaner: brake caliper piston tool and torque wrench at chain parts stores.

## Gotchas
- **Right front on this car:** the rotor was cut by a loose bearing (open issue 5) and the
  bearing still has to be replaced (open issue 4). If the bearing job is happening, the
  shop has the rotor off anyway: buy the rotors for that visit.
- After the job, the ABS light won't change: that fault is the bearing encoder (issue 4).
- Brake dust: damp wipe, no compressed air (Chilton warning).

## After
`log.md` (date, **odometer**, brands, part numbers, rotor thickness measured);
`maintenance.md` brakes row.

## What I couldn't verify
- Slide/flange bolt torque and rotor minimum for the 4-cyl: Chilton Brake Specifications
  table, one careful screenshot (library).
- Honda front pad number: Honda counter with the VIN.
- Rear brakes disc or drum: look through the rear wheel.
