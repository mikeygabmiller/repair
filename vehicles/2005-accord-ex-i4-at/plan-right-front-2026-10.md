# Plan: the right front job (Oct–Nov 2026)

Written 2026-10-25 from `open-issues.md` items 0–3, the Les Schwab paperwork and Honda's
online parts catalog. This is a **decision and shopping sheet**, not a procedure: the
steps and torque specs still have to come from the factory service manual (Chilton
Library, free with a library card). Once the job is done, the real procedure goes in
`procedures/` and the job goes in `log.md`.

**The car stays parked until this is done.** Loose bearing, a stripped and possibly
cross-threaded axle nut, and a caliper already grooving the rotor (`open-issues.md` item 0).
Tow it to whoever does the work.

## 1. What the job actually is

Everything wrong on the right front, in one place, so nothing gets done twice:

| # | Part | Why | Where the evidence is |
|---|---|---|---|
| 1 | Front hub bearing | Play; caliper rubbing the rotor | Les Schwab written notes, 2026-10-21 |
| 2 | Front hub | Usually replaced with the bearing because pressing the hub out of the bearing often damages one or both (UNVERIFIED: shop practice, ask the shop) | Les Schwab quote lists it |
| 3 | Right CV axle | Shake under hard acceleration; axle threads "look cross threaded" | Les Schwab notes; `open-issues.md` item 2 |
| 4 | Axle (spindle) nut | Stripped. Always new anyway | Les Schwab notes |
| 5 | Lower ball joint | Boot torn by the pickle fork, Oct 19 | `log.md` 2026-10-19 |
| 6 | ABS wheel speed sensor | ABS light, code 12-1 since Oct 20 | `open-issues.md` item 3 |
| 7 | Right front rotor | "Deep grooves" from the caliper rubbing | Owner, 2026-10-21 |
| 8 | Front pads | Same rubbing. Pads are replaced as an axle set (both sides) | Owner, 2026-10-21 |
| 9 | Alignment | Knuckle work moves it | Les Schwab quote lists it |

Items 5–8 are **not** on the Les Schwab quote. That matters for the comparison below.

## 2. The three ways to get it done

Prices are what's written down; anything not written down is marked.

### A. Les Schwab, as quoted: **$982.75**, quote valid to 2026-11-20

Covers items 1, 2, 3, labor and alignment. Does **not** cover the ball joint, ABS sensor,
rotor or pads, so the real number is $982.75 plus those parts and their labor. Bearing and
hub brands are not shown on the quote: ask. Upside: one shop, their warranty, no parts
running. Downside: the most money, and the new axle you already paid for ($83.74) goes
unused unless they'll install it.

### B. Ben's Auto Care, your parts: **$275 labor** (owner, 2026-10-22)

You supply everything. Ask before booking (write the answers in `open-issues.md`):

1. Does $275 cover **all** of items 1–8: axle, pressing the bearing and hub, pressing the
   ball joint, ABS sensor, rotor and pads? Or only some?
2. Alignment: do they do it, and what does it cost? If not, where do they send you?
3. Warranty on labor when the customer brings the parts? (Many shops give none on parts
   they didn't sell; past-chat note, `sources/project-history-2026-10-21.md` section A.)
4. Will they look at the axle threads on the hub side and the transmission side? A
   cross-threaded nut can damage the axle's own threads, which is one more reason the
   new axle goes in.
5. Can they take the car the day it's towed in, and how long do they keep it?

Parts you'd still buy are in section 3. Rough total: $275 + parts + alignment. With OEM
bearing, hub, ABS sensor, nut and rotor from the catalog prices below, the Honda parts
alone come to about $398 before pads, shipping and tax, against the $83.74 axle and the
Moog ball joint you already own. Name-brand aftermarket (NSK, Timken, SKF, Denso, Moog)
is usually cheaper than Honda; get the real prices, don't plan on a guess.

### C. DIY

Only with **all** of these: the factory torque specs in hand (section 4), the O'Reilly
loaner press kits (bearing kit 67213 and ball joint set 67045 + Honda adapter 67049,
`open-issues.md` item 2), a way to break a seized taper that isn't a pickle fork
(`log.md` 2026-10-19 lessons), and **two days off in a row** with a ride available,
because a stuck bearing or hub can leave the car on stands overnight.

Honest read: the hub bearing on this car is a press job (UNVERIFIED that it's press-in:
`open-issues.md` item 0 says Chilton should confirm). Pressing a bearing on the car with a
loaner kit is doable but it's the step most likely to go wrong (a cocked bearing is ruined
on the way in), and the Oct 19 attempt already showed the ball joint taper fights back.
With a stripped axle nut on top, **B is the better call** unless Ben's scope answer is
"no". A middle road: pull the knuckle yourself and have a shop press the bearing, hub and
ball joint on the bench (forum reports ~$25–75, COMMUNITY: past chats, project history
section A). That still needs the torque specs and still leaves the alignment.

## 3. Parts list

Numbers below are from Honda's dealer catalog at HondaPartsNow (Tier 3, looked up
2026-10-25 by model, **not** by VIN). The catalog uses transmission codes: this car is a
4-door EX, 4-cylinder, 5-speed automatic, which is **KA 5AT** (KA = U.S. model;
UNVERIFIED reading of the code). Before ordering, put the VIN
(1HGCM56895A072328, `profile.md`) into a Honda dealer's online catalog or read it to a
Honda parts counter. Free.

| Part | Honda number | Catalog note | Price seen | Already have? |
|---|---|---|---|---|
| Front hub bearing | **44300-TR4-A51** (replaces 44300-SDA-A52 and -A51, the NSK part) | Front, fits 4-door EX, KA 5AT. Same number both sides | $119.63 | No |
| Front hub | **44600-SDA-A00** | Listed only for 4-cylinder trims with KA/KL 5AT (no V6, no manual). The other hub, 44600-SDA-A10, is the V6/manual one | $101.06 | No |
| Axle (spindle) nut | **90305-692-010**, "Nut, Spindle (22MM)" | Listed only for 4-cylinder trims, KA/KL 5AT. The 24 mm nut (90305-SD4-003) is listed for V6 and others. See the note below | $4.38 | No. **New one every time** |
| Lower ball joint | **51220-SDA-A02**, now **51220-SDA-305** "Joint, Front Ball" | Front, all 2005 Accords | $168.32 | Yes: Moog K80228 |
| Right front ABS sensor | **57450-SDA-A11** "Right Front Sensor Assembly" (replaces -A02, -A01) | All 2003–07 Accords incl. 2005 4-door EX KA 5AT | $81.77 | No |
| Front rotor | **45251-TA0-A02**, or **45251-TA5-A00** | The catalog lists both for a 4-door EX KA 5AT (TA0-A00 and -A01 are now TA0-A02; TA5-A00 replaces S87-A00). Two numbers for one car means the VIN decides | $91.05 | No |
| Front pads | not looked up | Buy as a front axle set; name brand only | — | No |
| Right CV axle | catalog not checked | See the note below | — | Yes: Parts Geek, $83.74 |

**Notes on the table**

- **The ball joint number in `parts.md` was wrong.** It said Moog K80228 "interchanges
  with Honda 51210-SDA-A02". 51210-SDA-A02 is the **right front knuckle**
  (HondaPartsNow, "Knuckle", replaces -A00/-A01), not the ball joint. The ball joint is
  51220-SDA-A02, now 51220-SDA-305. Fixed in `parts.md` the same day. Moog K80228's
  cross-reference to 51220-SDA-A02 still needs checking on Moog's own catalog.
- **The 22 mm nut and your 32 mm socket agree.** The "22MM" in the nut's name is its
  thread size, not the socket. You test-fit the old nut: 32 mm fit, 36 mm was too big
  (`parts.md`). A 22 mm thread taking a 32 mm socket, and a 24 mm thread taking 36 mm, is
  the usual Honda pairing (COMMUNITY, not checked against a Honda document). Either way,
  it's one more sign this car has the 4-cylinder nut, and **a torque spec found for a V6
  Accord is for a different, bigger nut**. Don't use one.
- **Les Schwab's numbers are their own.** PRB510073 is probably a "510073" pattern
  bearing: sellers list 510073 for 2003–07 Accords with ABS (Detroit Axle, ALLCOMBO,
  COMMUNITY: seller listings; Timken's own catalog wasn't found listing it). HO8176
  matches a SurTrack **HO-8176** axle that Parts Geek sells on eBay as "front right, 2003–07
  Accord 2.4L" (COMMUNITY: seller listing). **Your Parts Geek axle may well be that same
  part.** Read the box label before the job; if it says HO-8176, it's the axle Les Schwab
  would have put in.
- **Owner's rule check:** OEM or name brand only. The bearing and hub are worth buying
  Honda or NSK/Timken: a no-name bearing is the classic "loose again in a year" part.

## 4. Specs to pull from Chilton before anyone torques anything

None of these are verified. Every one is a **safety-critical fastener**, so no number goes
in this repo from memory. Get them in one library session (Chilton Library → 2005 Honda
Accord 2.4L → Suspension / Brakes / Drivetrain), add each to `specs.md` with the page, and
bring the list to the shop if B (a good shop has them; asking costs nothing).

| Spec | Note |
|---|---|
| **Axle (spindle) nut torque, 4-cylinder** | The open question since Oct 19: 181 vs 134 lb-ft in past chats (`open-issues.md` item 1). Also whether it's torqued with the wheel on the ground, and how it's staked |
| Lower ball joint castle nut torque | And the cotter pin / clip |
| Ball joint snap ring | Which way it goes, and whether a new one is required |
| Hub bearing snap ring | Same |
| Caliper bracket bolts | |
| Caliper slide pin bolts | |
| Rotor retaining screws | Two small screws hold the rotor to the hub on many Hondas: check |
| ABS sensor bolt | Small; easy to strip in an aluminium or iron knuckle |
| Tie rod end nut | If the knuckle comes off |
| Lower arm / damper fork bolts | If disturbed |
| Sway bar link nuts | Was touched in October (`log.md`) |
| Knuckle-to-strut / upper arm nut | If the knuckle comes off |
| Lug nuts | **Already verified: 80 lbf·ft, crisscross** (`specs.md`, OM p.250) |

## 5. After the job

- Alignment. Specs are in `specs.md` (OM p.275).
- Clear the ABS code and drive: does the light stay off? If 12-1 comes back with a new
  sensor, the tone ring on the new axle or the sensor's wiring is next.
- Re-check the axle nut torque after the first drive if the manual says to.
- Is the hard-acceleration shake gone? If not, the mounts are next (`open-issues.md` item 2).
- Log it: date, mileage, every part number actually installed (read off the boxes), who
  did it, cost.

## What I couldn't verify

- That HondaPartsNow's listings match this exact car: they're by model, not VIN. Check
  free with the VIN at a Honda dealer's online catalog or parts counter.
- Which of the two rotor numbers fits: same check.
- That "KA" means the U.S. model in Honda's codes: same check (the counter will just
  tell you the part).
- That the hub bearing is press-in: Chilton, free with a library card.
- Every torque spec in section 4: Chilton.
- That Moog K80228 crosses to 51220-SDA-A02: Moog's free online catalog.
- That the Parts Geek axle is a SurTrack HO-8176: read the box.
- Shop practice on replacing the hub with the bearing: ask Ben's and Les Schwab.
