# Spark plugs: 2005 Accord EX-L 2.4 L K24A4

Done 2026-10-18 at 138,943 mi (Bosch 9614, `log.md`). Next due ~248,900 mi (110,000 mi
interval, OM p.203). This is for the next time, or for a misfire.

Sources: Chilton Spark Plugs R&I (general article, pack F04) and the K24A4 tune-up and
torque rows (report D) (`specs.md`); plug numbers OM p.275.
Difficulty: easy–moderate. Time: ~1 h (estimate). Car undrivable only during the job.
**Cold engine only** (aluminum head).

| Item | Value | Source |
|---|---|---|
| Factory plug | NGK IZFR6K-11 or DENSO SKJ20DR-M11; manual also lists -13 versions "on some models" | VERIFIED: OM p.275 |
| Gap | 0.039–0.043 in (1.0–1.1 mm) except **SULEV** 0.047–0.051 in (1.2–1.3 mm). Check, don't bend iridium plugs. Replace if over 0.051 in (non-SULEV) | VERIFIED: Chilton K24A4 tune-up row, footnote ① |
| Torque | **13 lbf·ft (18 N·m)** | VERIFIED: Chilton K24A4 torque row and the general article |
| Anti-seize | Chilton: light coat on the threads. Plug makers often say none on plated plugs. Last install was dry | Conflict shown in `specs.md`; plug maker's box is the tiebreaker |
| SULEV or not | **Unknown**: read the under-hood emissions label (`owner-checklist.md`) | — |

## Steps (Chilton F04)
1. Engine cold. Note the radio code (owner has it). Chilton says disconnect the negative
   battery cable; on this car re-tighten it properly afterwards (open issue 2).
2. Remove the engine cover (if fitted). Unplug each coil connector (press the tab), remove
   the coil bolt, pull the coil straight up. One coil per plug.
3. Spark plug socket with a rubber insert, **solid extension: no wobble/flex extension**
   (Chilton warning: side load can snap a plug). Counterclockwise out.
4. Look at the coils: cracks, oil in the boot = replace that coil, and find the oil (valve
   cover gasket: Honda bulletin A15-020 exists for a rear head-cover gasket leak on this
   model family, `tsbs.md`; not read in full).
5. Check the gap with a **wire** gauge only.
6. Thread each new plug in **by hand** (a short piece of rubber hose on the plug works as a
   handle, Chilton). Never force it: cross-threading the head is an expensive mistake.
7. Torque **13 lbf·ft**. Coils, bolts, connectors (click), cover.
8. Start: smooth idle, no check engine light.

## Backyard notes (COMMUNITY)
- Blow the plug wells out with compressed air or a straw **before** pulling the plugs. Why:
  grit in the well falls into the cylinder when the plug comes out.
- A misfire code (P0301–P0304) right after: swap that cylinder's coil with a neighbour. If
  the code moves, it's the coil; if not, the plug or injector. Free test, no parts.
  Honda bulletin A07-016 covers paired misfire codes on this model family (`tsbs.md`; the
  P0301/P0305 versions are V6).

## After
`log.md`, `maintenance.md` (already up to date for 2026-10-18).
