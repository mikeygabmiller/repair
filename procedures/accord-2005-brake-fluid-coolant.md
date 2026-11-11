# Brake fluid exchange and coolant change: 2005 Accord EX-L 2.4 L AT

Both are overdue (no record, `maintenance.md`). **Recommended: have a shop do both**
(`plans/2026-11-catch-up-maintenance.md`): a brake bleed done wrong leaves air in the brakes,
and coolant needs the air bled out and the old coolant disposed of. This file is so you can
**order the job correctly, check the shop's work, or do it yourself if you choose**.

Sources: OM pp.203, 217–218, 223, 257, 274; Chilton bleed order (report B, `specs.md`);
Chilton coolant bleed summary is from the **V6** article (`sources/chilton-2026-10-23.md`
C03), labeled below.

---

## Part 1. Brake fluid (every 3 years regardless of miles, OM p.203)

| Item | Value | Source |
|---|---|---|
| Fluid | **Honda Heavy Duty Brake Fluid DOT 3**; DOT 3 or DOT 4 from a sealed container only as a temporary replacement; **never DOT 5** | VERIFIED: OM p.223 |
| Bleed order | **Front left → front right → rear right → rear left** | Chilton "Accord and Prelude shown" figure (report B, G16): generic figure, `specs.md` |
| ABS unit | No scan-tool bleed unless the ABS modulator was opened | Chilton report (`chilton-checklist.md` 22) |
| Bleeder screw torque | **Not found.** Snug only; don't use a number from memory | — |
| How much fluid | Not found (`chilton-checklist.md` 23). Buy 2 × 12 oz bottles (COMMUNITY, typical for a car this size) | — |

**What to ask the shop for:** "Brake fluid exchange with Honda Heavy Duty DOT 3, bled at all
four wheels until clean fluid comes out, and a full brake inspection. Please tell me the
front pad thickness and rotor thickness, and whether the rear brakes are disc or drum."
Time at a shop: ~1 h. **Undrivable only while it's there.**

### DIY two-person method (if you choose it)
Tools: 8 mm or 10 mm wrench for the bleeders (size **not confirmed**: check before buying),
clear hose that fits the bleeder snugly, bottle, helper, jack + **stands**, turkey baster.
Time ~1.5 h first time (estimate). The car is undrivable until done.

1. Key off. Baster out most of the old fluid from the reservoir (gray cap, OM p.210);
   refill with fresh fluid to MAX. **Never let the reservoir run low during the job**
   (Chilton): air in the ABS unit is a shop job.
2. Start at **front left**: hose on the bleeder into the bottle with fluid covering the hose
   end. Helper presses the pedal slowly and holds; you open the bleeder 1/4 turn, close
   it; helper releases. Repeat until the fluid in the hose is clean and bubble-free
   (Chilton: at least 4–5 times per wheel). Top up the reservoir every few strokes.
3. Front right, rear right, rear left (Chilton order).
4. Reservoir to MAX. Pedal must be firm and high **before the car moves**. Low or soft
   pedal = don't drive it; tow it to a shop.
5. Clean spilled fluid off paint right away with water (brake fluid strips paint:
   COMMUNITY, well known).

**Backyard tool (COMMUNITY):** a one-person check-valve bleeder bottle (~$10–20) or a
hand vacuum pump (often free as a parts-store loaner). Why it works: the check valve or
vacuum stops air being sucked back in at the bleeder when the pedal comes up, so one person
can do it. Still check pedal feel before driving.

Honda bulletin **A07-045 "Brake Pedal Is Low and Feels Soft"** exists for this model
(`tsbs.md`, Chilton list): not read in full. If the pedal is soft after a correct bleed, ask
the shop about it.

---

## Part 2. Coolant (120,000 mi or 10 yr, then every 60,000 mi or 5 yr; OM p.203)

| Item | Value | Source |
|---|---|---|
| Coolant | **Honda All Season Antifreeze/Coolant Type 2**, premixed 50/50. Never straight antifreeze, never plain water (except to get home). No additives or rust inhibitors | VERIFIED: OM pp.217–218 |
| Change amount (automatic) | **1.32 US gal (5.0 L)** incl. reserve tank | VERIFIED: OM p.274; Chilton 5.3 qt agrees |
| Total | 1.88 US gal (7.1 L) | VERIFIED: OM p.274 |
| Honda part (premixed) | OL999-9001 (Chilton **V6** article): confirm at the counter | `parts.md` |
| Radiator cap pressure, thermostat temperature | **Not found** (`chilton-checklist.md` 40) | — |

**Before paying anyone:** look at the reserve tank cold (level, colour). Honda Type 2 is
blue (COMMUNITY: well known; the bottle shows it). Rusty brown, oily, or crusty = do it soon
and ask the shop to pressure-test for leaks. Clean blue at the right level = it can wait a
month or two.

**What to ask the shop for:** "Drain and refill with Honda Type 2 premixed coolant, air bled
out, no flush chemicals." Time ~1 h; undrivable while there.

### DIY outline (steps from Chilton's **V6** article, C03: UNVERIFIED for the 2.4 L)
Engine **cold** (OM p.217 warning). Heater set to max hot. Drain at the radiator drain plug
into a pan; refill the radiator to the base of the filler neck and the reserve tank to MAX;
run with the cap off/loose until the fan cycles at least twice, topping up as bubbles come
out; cap on, reserve to MAX; check for leaks; recheck the level cold next morning. Old
coolant is toxic and sweet-tasting to animals: sealed jug to a parts store or recycler.

**Backyard tool (COMMUNITY):** a spill-free funnel kit (~$20–35, or a parts-store loaner)
that clamps to the radiator neck. Why it works: the funnel sits higher than the engine, so
trapped air rises out through it instead of staying in the head and causing a false
overheat.

---

## After either job
`log.md` with the **odometer**, product and amount; update the row in `maintenance.md`
(brake fluid next due in 3 years; coolant 60,000 mi or 5 yr).

## What I couldn't verify
- Bleeder wrench size and bleeder torque: Chilton (library) or look at the bleeder.
- Brake flush fluid amount: Chilton checklist 23.
- 2.4 L coolant drain/bleed steps, radiator cap pressure, thermostat temperature: Chilton
  2006–07 Accord 2.4 L "Coolant Replacement" (library).
- Whether the rear brakes are disc or drum on this EX: look through the rear wheel (free).
