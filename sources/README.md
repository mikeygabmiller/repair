# Sources

Reference files that Claude reads during a session. Free documents only.

Have:
- `2005-accord-owners-manual.pdf`: Honda's 2005 Accord 4dr Online Reference Owner's
  Manual, 302 pages. Printed page N = PDF page N+1. Specs are on printed pp.274–276,
  maintenance schedules on pp.199–203, oil change on pp.214–215, the Service Information
  Summary on the last page. The PDF is scanned images: read pages as images, text search
  doesn't work.
- `chilton-2026-10-23.md`: first Chilton Library pull, plus parts catalog and NHTSA
  lookups, run by Claude in Chrome (values, menu paths, which engine version each article
  covers).
- `chilton-pack-F-2026-10-27.md` and `chilton-report-A-I-2026-10-27.md`: the owner's
  Chilton research packs. Pack A–E is referred to but not uploaded yet.
- `project-history-2026-10-21.md`: the owner's history compiled from past AI chats. Trust
  it for what the owner did, never for specs or part numbers.

Free library access to Chilton (the owner's county library, via Gale):
`http://infotrac.galegroup.com/default/tel_p_obioncpl?db=CHLL`. It opened without a
password on 2026-10-23. Many articles for this car only come in V6, Hybrid or Acura TSX
versions, so always note which version a number came from.

Wanted (Tier 1, free, a phone photo each). Save as `.jpg` in `sources/photos/`:
- **Driver door-jamb sticker**: build month (decides whether recall 11V395000 covers this
  car) and tire pressures (the manual and Chilton disagree, `specs.md`).
- **Under-hood emissions label**: SULEV or not (decides spark plug gap and the -11 vs -13
  plug, `specs.md`).
- **Battery label**: group size (51R is unverified, `parts.md`).
- Any part label or stamp before the old part is thrown away.

Invoices, quotes and inspection sheets go in `receipts/`, not here.

Copyrighted manuals stay here only while the repo is private (see `CLAUDE.md`).
