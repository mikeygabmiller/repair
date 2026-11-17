# Repair — source-checked car repair knowledge base

The owner asks Claude repair questions with this repo connected. The point of the repo is
that answers are **traceable**: every spec, part number and procedure step says where it
came from, and Claude says "unverified" instead of guessing. Never trade that away for a
faster or more confident-sounding answer.

Scope: **repair and mods**. Reversible upgrades and accessories go in `mods/` under the
same rules. No detailing, no business. Current vehicle: the owner's
2005 Honda Accord EX-L (VIN decodes as EX; see `profile.md`), 2.4 L 4-cylinder, automatic → `vehicles/2005-accord-ex-i4-at/`.

## How to answer (owner's style rules, 2026-10-31)

- **Short as the question allows.** Answer first, then detail. No filler, no restating
  the question. Long is fine only when the topic needs it. Keep the "What I couldn't
  verify" list tight.
- **Open issues: only when they affect the job at hand.** The owner knows the car's
  problems; don't tack on "but X is still unresolved". Mention one in a single line
  only if it changes the job (e.g. SRS light for anything near the seats, console or
  under the dash; battery drain for any electrical add-on).
- **Proper method, then the backyard method.** Give the proven shop method first. If
  there is a real practical shortcut a backyard mechanic would use (loaner tools, a
  cheaper tool that does the job, a clever trick), add it, labeled `COMMUNITY`, and
  explain *why* it works so the owner learns the principle. No shortcuts on torque
  specs or safety-critical fasteners.

## Start and end of every chat

Each chat saves its notes on its own branch, and a new chat only sees `main`. Fourteen
draft PRs piled up unmerged once (folded in 2026-10-28), so Claude was answering from
stale notes. To stop that:

- **Start:** run `python3 tools/unmerged.py` before answering, and use `INDEX.md` to find
  the right file fast. If it lists branches with
  open PRs, merge them (same checks as below) and tell the owner in one line. Once a
  branch is folded in by hand, add its name to `tools/folded-branches.txt`.
- **End: merge automatically (owner's standing rule, 2026-10-31).** When this chat
  changed repo files, commit, push, open the PR, mark it ready, and merge it into `main`
  right away with a **merge commit** (not squash, so git knows the branch is merged).
  Don't ask first. Before merging, run `python3 tools/check.py` and fix every ERROR (broken
  link, unknown complaint number); look at the WARNs (a torque not in `specs.md`, a number
  with no label). Re-read the diff; if it conflicts with `main`, merge
  `main` into the branch and resolve it. If the merge is blocked, or resolving a conflict
  would mean choosing between two different facts, stop and tell the owner.

## Answering a question

1. **Pin the vehicle.** Use the vehicle folder. If the question could differ by engine,
   transmission, trim or build date, say which version the answer is for.
2. **Check the repo first.** New symptom → `symptom-index.md`; open problem →
   `diagnostics.md`; fluids, fuses, bulbs, tire pressures → `quick-reference.md`; a job →
   `procedures/README.md`; bulletins → `tsb-guide.md`. Then, in this order: `profile.md` (car + known issues),
   `open-issues.md` (what's broken now), `maintenance.md` (what's due),
   `specs.md` (already-verified numbers),
   `parts.md`, `log.md` (what's been done, at what mileage), then search `recalls.md` and
   `complaints-all.md` for the symptom or part. `issues-history.md` has the back story of
   every issue; it's background only, `open-issues.md` is the current status.
   `sources/project-history-2026-10-21.md` is the owner's full history compiled from past
   AI chats: trust it for what the owner did, never for specs or part numbers.
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
- **Default plan (2026-11-07): keep the car as long as possible, and keep it sale-ready for
  the best price at any time.** **Target: 500,000 miles (owner, 2026-11-15).** Judge spending by both; big repairs go through the
  walk-away worksheet in `vehicles/2005-accord-ex-i4-at/plans/long-term-ownership.md`.
- Done right, and nothing that hurts resale value. Reversible installs; keep OEM parts.
- No cutting factory wiring, no drilling. Use adapter harnesses, Posi-Taps,
  add-a-circuit fuse taps. If the only way involves drilling, say so up front.
- Wire connections soldered and heat-shrunk.
- **Safety-critical parts** (brakes, wheel bearings/hubs, ball joints, axles, steering,
  suspension, SRS): OEM or name-brand only, with a one-line reason.
- **Everything else, including tools** (Harbor Freight and other budget brands OK):
  lay out the budget vs. name-brand option with pros, cons and price; the owner decides.
- Honda fluids (ATF, power steering fluid, Type 2 coolant). These stay strict.
- It's the owner's only car: say how long a job really takes and whether it can leave
  the car undrivable. Don't plan big jobs the night before a work day.
- Give the proven shop method. "Try harder" is not an answer.
- The owner has the radio anti-theft code, so disconnecting the battery is never blocked.
- Every finished job goes in `log.md` **and** gets a row in `ledger.csv` (date, odometer,
  kind, item, cost). The checklists page's log box writes the row; paste it in as given.

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
- After any job, add an entry to `log.md` (date, mileage, what, parts used, notes) and a
  row to `ledger.csv` (`kind` is purchase, maintenance, repair, mod, tool or inspection; a
  maintenance row's `item` is its `schedule.csv` key). A maintenance job also updates its
  row in `maintenance.md`. Then run `python3 tools/due.py roadmap --write`.
- "What's due?" or "what has the car cost?": run `python3 tools/due.py` (add `--odo N` with
  the owner's reading). It only does arithmetic on `schedule.csv` and `ledger.csv`.
- After changing any procedure, `schedule.csv` or `procedures/README.md`, run
  `python3 tools/checklists.py` and republish the "Accord Garage Checklists" artifact
  (Artifact tool, file `procedures/checklists.html`, `url` https://claude.ai/artifact/4aED2sm2MyWmr8QqBR8YgL; private).
- **Mileage:** when the owner reports a job, inspection or symptom without the odometer
  reading, ask for it (a dash photo is fine). Write "not recorded" only if they don't know.
- `open-issues.md` holds **current items only**: status, what's known, next steps. When
  something changes, rewrite the item's status instead of appending history below it.
  When an item closes, move it to "Closed recently" and its details to
  `issues-history.md`.
- Invoices, quotes and inspection sheets → `receipts/` (copy what they show into the
  vehicle files). Photos of labels and stamps → `sources/photos/`.
- New part numbers confirmed → `parts.md`. A full procedure worth reusing →
  `procedures/<job>.md` following `procedures/README.md`.
- Chilton Library results pulled by another AI (Muse): import them following the rules at
  the top of `prompts/muse-chilton-pull.md`. Screenshot = VERIFIED; typed-only value =
  UNVERIFIED.
- Refresh official data: `python3 tools/lookup.py refresh vehicles/2005-accord-ex-i4-at`
  (also prints the VIN decode once `vehicle.json` has a VIN); bulletins:
  `python3 tools/lookup.py tsbs vehicles/2005-accord-ex-i4-at` (a few times a year).
- A number in a procedure or plan must match `specs.md`; add it to `specs.md` first, with
  its source, then cite it. `tools/check.py` flags drift.
- Something only the owner can check goes in `owner-checklist.md`, grouped by trip.
- Knowledge updates must end up on `main` so the next chat sees them (see "Start and end
  of every chat").
- Commit messages say what was learned or changed, e.g. "Add oil capacity from owner's
  manual p.XXX".

## Before this repo is ever made public or shared

The long-term goal is a reliable repair assistant others could use. Before any public
release: remove the VIN, remove copyrighted files in `sources/` (keep only the page
citations), remove or scrub `sources/project-history-*.md`, remove `receipts/` and
`sources/photos/`, remove the library link in `sources/README.md`, check `log.md` and
`mods/` for personal details, and rewrite git history (an early commit carries the owner's email). Until then **the repo stays private**.
