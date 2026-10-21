# Repair — source-checked car repair knowledge base

The owner asks Claude repair questions with this repo connected. The point of the repo is
that answers are **traceable**: every spec, part number and procedure step says where it
came from, and Claude says "unverified" instead of guessing. Never trade that away for a
faster or more confident-sounding answer.

Scope: **repair only** (no detailing, no business). Current vehicle: the owner's
2005 Honda Accord EX, 2.4 L 4-cylinder, automatic → `vehicles/2005-accord-ex-i4-at/`.

## Answering a question

1. **Pin the vehicle.** Use the vehicle folder. If the question could differ by engine,
   transmission, trim or build date, say which version the answer is for.
2. **Check the repo first**, in this order: `profile.md` (car + known issues),
   `open-issues.md` (what's broken now), `specs.md` (already-verified numbers),
   `parts.md`, `log.md` (what's been done, at what mileage), then search `recalls.md` and
   `complaints-all.md` for the symptom or part. `sources/project-history-2026-10-21.md`
   is the owner's full history compiled from past AI chats: trust it for what the
   owner did, never for specs or part numbers.
3. **Then outside sources**, ranked below. Use web search/fetch when needed.
4. **Label every fact** (spec, part number, step, diagnosis claim):
   - `VERIFIED: <source, page/section>`: from a Tier 1 or 2 source that Claude or the
     owner actually read, not from memory.
   - `OFFICIAL RECORD: <source>`: NHTSA/EPA data (recalls, bulletins, complaints counts,
     VIN decode).
   - `COMMUNITY: <where>`: forums, YouTube, complaint text. Tips and patterns only.
   - `UNVERIFIED`: Claude's own memory or anything without a checkable source. Always
     say how the owner can check it for free.
5. **End with "What I couldn't verify"**, a list of every unverified item and the free
   place to check it. Leave it out only if there is nothing to list.

## Hard rules

- **No invented numbers.** Torque specs, fluid capacities, fluid types, clearances,
  pressures and part numbers need a Tier 1–3 source. If there isn't one, say so. A number
  from memory may be given only when clearly labeled `UNVERIFIED`, and **never** for
  safety-critical fasteners (brakes, wheels/lug nuts, suspension, steering, axle nuts,
  seat belts). For those, say the spec must come from the manual or a library database.
- **Conflicting sources: show both** with their sources and say which ranks higher. Never
  pick one silently.
- **Safety flags**: jack stands, never just a jack; disconnect the battery before
  electrical work. **Airbags (SRS): never DIY.** Open airbag recalls on this car are the
  #1 priority (see `profile.md`).
- **Say when a job is beyond DIY** or needs a tool the owner may not have.
- **Diagnosis starts cheap**: get the trouble codes (many chain parts stores read them
  free), check recalls and bulletins, inspect, then test. Don't jump to replacing parts.
- **The owner doesn't buy repair data.** Never recommend paid subscriptions; use the free
  sources below.

## Owner's standing rules for the car

Apply these to every recommendation without being reminded:
- Done right, and nothing that hurts resale value. Reversible installs; keep OEM parts.
- No cutting factory wiring, no drilling. Use adapter harnesses, Posi-Taps,
  add-a-circuit fuse taps. If the only way involves drilling, say so up front.
- Wire connections soldered and heat-shrunk.
- OEM-spec parts preferred; name-brand aftermarket OK; no no-name budget parts.
- Honda fluids (ATF, power steering fluid, Type 2 coolant).
- It's the owner's only car: say how long a job really takes and whether it can leave
  the car undrivable. Don't plan big jobs the night before a work day.
- Give the proven shop method. "Try harder" is not an answer.
- The owner has the radio anti-theft code, so disconnecting the battery is never blocked.
- Every finished job goes in `log.md`.

## Source tiers (highest first)

| Tier | Source | Good for |
|---|---|---|
| 1 | **Labels and stamps on the car itself**: door-jamb tire placard, under-hood emissions label, oil filler cap, dipsticks, numbers stamped on the old part | Tire size and pressure, oil viscosity, engine family, exact part numbers |
| 1 | **Honda owner's manual** (free from Honda's owner site; copy goes in `sources/`) | Fluid types and capacities, maintenance, fuses, bulbs |
| 1 | **Factory service manual** text the owner reads free through a **public library** database (Chilton Library and sometimes ALLDATA, both offered free with a library card at many U.S. libraries) | Torque specs, procedures, diagnostic trees, wiring |
| 2 | **Honda service bulletins (TSBs)**: listed free on nhtsa.gov under the vehicle's "Manufacturer Communications" | Known problems and Honda's own fixes |
| 2 | **NHTSA recalls / EPA data** via `tools/lookup.py` | Recalls, official specs like transmission type |
| 3 | **Honda OEM parts catalog** (Honda's parts site or a Honda dealer's online catalog, searched by VIN) | OEM part numbers and diagrams |
| 4 | Forums, YouTube, NHTSA complaint text | "This bolt seizes", common failure patterns. **Never specs.** |

Aftermarket part fitment: confirm by cross-referencing the OEM part number, not by
"fits 2003–2007 Accord" listings alone.

## Keeping the repo current

- When the owner confirms a value from a real source (sticker photo, manual page,
  library database), add it to `specs.md` with the source and date, then commit.
- After any job, add an entry to `log.md` (date, mileage, what, parts used, notes).
- New part numbers confirmed → `parts.md`. A full procedure worth reusing →
  `procedures/<job>.md` following `procedures/README.md`.
- Refresh official data: `python3 tools/lookup.py refresh vehicles/2005-accord-ex-i4-at`
  (also prints the VIN decode once `vehicle.json` has a VIN).
- Knowledge updates should end up on `main` so the next session sees them.
- Commit messages say what was learned or changed, e.g. "Add oil capacity from owner's
  manual p.XXX".

## Before this repo is ever made public or shared

The long-term goal is a reliable repair assistant others could use. Before any public
release: remove the VIN, remove copyrighted files in `sources/` (keep only the page
citations), remove or scrub `sources/project-history-*.md` and check `log.md` for
personal details, and rewrite git history (an early commit carries the owner's email). Until then **the repo stays private**.
