# NotebookLM research: prompts for Google NotebookLM

Written 2026-11-07. Reusable: rerun Q1–Q3 whenever new sources go in the notebook.

## What NotebookLM is (and isn't) for this repo

- It answers **only from the sources loaded into the notebook**, with a citation to the
  passage. It is not a source itself. Its value = the documents behind it.
- Good at: reading long PDFs (owner's manual, bulletins, Chilton screenshots) fast,
  cross-checking them against the repo's notes, and finding what's missing.
- Bad at: anything not in its sources. If it answers without a citation, treat it as a
  guess.

## Sources to load (all free)

1. `sources/2005-accord-owners-manual.pdf` from this repo.
2. **Honda bulletins:** nhtsa.gov → Recalls → search 2005 Honda Accord → "Manufacturer
   Communications" → download the PDFs (start with any that mention the engine, automatic
   transmission, ABS, SRS, electrical, steering/suspension).
3. **Recall notices** for the campaigns in `recalls.md` (same NHTSA page, PDFs).
4. Chilton Library screenshots, if saved (private notebook only: copyrighted).
5. **Repo notes as context**, renamed so the title starts with `REPO NOTES -`:
   `profile.md`, `open-issues.md`, `specs.md`, `maintenance.md`, `parts.md`,
   `plans/long-term-ownership.md`. (Rename because NotebookLM uses the file name as the
   source title; the setup prompt tells it never to cite these as proof.)
6. Community (labeled COMMUNITY when imported): `complaints-all.md`, threads from
   driveaccord.net (7th-gen Accord forum), YouTube how-to videos (paste the link).

**Privacy:** the repo notes contain the VIN. Keep the notebook private; don't share it.

## How results get imported (for Claude)

- NotebookLM's text is only a pointer. The label comes from the **underlying source**,
  checked at the cited page: owner's manual / Chilton screenshot → `VERIFIED`; Honda
  bulletin or NHTSA recall/complaint data → `OFFICIAL RECORD`; forum, video, complaint
  text → `COMMUNITY`.
- NotebookLM has labeled a torque-spec website as "Service manual" (2026-11-07). Check
  the source title yourself: a website is COMMUNITY no matter what NotebookLM calls it.
- Claude re-reads the cited page itself when it can (the owner's manual is in the repo).
  If it can't, the value goes in as `UNVERIFIED (NotebookLM citing <source, page>)` until
  the owner sends a screenshot of that page.
- **Never import a number whose only citation is a `REPO NOTES` file** (circular).
- **No safety-critical torque** (brakes, wheels, suspension, steering, axle nut) goes in
  from NotebookLM without a screenshot of the source page.
- Paste NotebookLM's answers into a chat with Claude, or save them as
  `sources/notebooklm-<date>.md`, and say which question they answer.

---

## Step 1. Setup prompt (paste once as the first message, or into "Configure chat")

```
You are helping me maintain a private, source-checked repair notebook for ONE car:
2005 Honda Accord EX-L sedan, 2.4 L 4-cylinder (K24A4), 5-speed automatic, U.S. model,
about 139,000 miles. I plan to keep it as long as possible and keep it ready to sell for
the best price at any time. I do my own work in a driveway with hand tools.

Rules for every answer:
1. Use ONLY the sources in this notebook. Never fill gaps from general knowledge. If the
   sources don't say, write "NOT IN SOURCES".
2. Every fact needs a citation and an EXACT short quote. Numbers (torque, capacity,
   clearance, part number, interval) must be copied exactly as printed, with units. Don't
   convert or round.
3. Say which version a fact is for. Many sources cover the V6, the Hybrid, the coupe, a
   manual transmission or other years. If a fact is not stated for the 2.4 L 4-cylinder
   automatic sedan, say so ("V6 only", "not stated", "2006-07").
4. Sources whose title starts with "REPO NOTES" are my own notes. Use them only to know
   what I already have and what I'm missing. NEVER cite them as proof of a fact.
5. Label each source type: Owner's manual / Service manual (Chilton) / Honda bulletin /
   NHTSA recall / NHTSA complaint / Website / Forum / Video. "Service manual" means
   Chilton, ALLDATA or Honda's own manual ONLY. A torque-spec or "database" website is
   "Website", even if it copies service manual numbers.
6. When two sources disagree, show both with citations. Don't pick one.
7. Answer in a table where possible:
   | Finding | Exact quote | Source title | Page or timestamp | Source type | Applies to 2.4 L AT sedan? |
   Then a short list: "NOT IN SOURCES" for everything I asked that you couldn't find.
```

## Step 2. Questions (send one per message; better answers than all at once)

**Q1. Gap audit (the most useful one; rerun after adding sources)**
```
Compare the REPO NOTES sources against every other source. List: (a) anything the repo
notes mark UNVERIFIED, unknown, "not recorded" or "need the service manual" that another
source actually answers; (b) any value in the repo notes that another source contradicts;
(c) any value in the repo notes that's for the wrong version (V6, Hybrid, coupe, manual).
Use the table format.
```

**Q2. Honda bulletins and recalls that apply**
```
List every Honda service bulletin and recall in the sources that could apply to a 2005
Accord 2.4 L automatic sedan. For each: number, title, symptom it fixes, VIN/build-date
range if given, and the fix. Then flag any that match these current problems from my
notes: check engine code P0685, shake at about 60 mph that gets worse on the gas, ABS
light, SRS codes 61-10 / E2-11 / F1-11, the phone's USB link dropping when lights switch.
```

**Q3. What fails on this car from 140,000 miles on**
```
From all sources, list the parts and systems that commonly fail on 2003-2007 Accords with
the 2.4 L and automatic transmission between 140,000 and 250,000 miles. For each: the
symptom, the mileage people report, the cheapest early check I can do myself, and whether
it's a DIY job or a shop job. Keep owner's manual / bulletin facts separate from forum and
video reports.
```

**Q4. Diagnosing the open problems**
```
For each open problem in the REPO NOTES "open-issues" source, list what the OTHER sources
say about its causes and the test order, cheapest test first. Quote any test values
(voltages, resistance, play limits) exactly. Mark anything the sources don't cover as
NOT IN SOURCES.
```

**Q5. Long-term ownership and resale**
```
From the sources: which maintenance items, if skipped, cause expensive damage on this
engine and transmission? What do buyers and pre-purchase inspections of a 2003-2007 Accord
check first? Which records or fixes most affect resale price? Cite each point.
```

**Q6. What should I add to this notebook next?**
```
Based on the gaps you found in Q1-Q5, list the specific documents, bulletin numbers,
service manual sections or labels on the car (door jamb, under-hood emissions label) I
should add as sources next, most useful first, and what each would answer.
```

**Q7 (optional). Reversible mods**
```
From the sources, list reversible upgrades owners make on 2003-2007 Accords that need no
cutting of factory wiring and no drilling (plug-in harnesses, OEM parts from higher trims).
For each: OEM part number if a source gives one, and the source.
```
