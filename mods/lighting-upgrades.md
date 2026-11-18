# Lighting upgrades: what's worth it on this car (researched 2026-11-10)

Reversible, plug-in only, OEM bulbs kept for resale (standing rules). Bulb types:
headlight high **HB3/9005 60 W**, low **HB4/9006 51 W** (VERIFIED: OM p.275). How to change
them: `procedures/accord-2005-bulbs.md`.

## The rule that decides most of it: LED bulbs in halogen headlights
NHTSA's interpretation letters say LED light sources are **not permitted in replaceable-bulb
headlamps** (LEDs are allowed only in headlamps designed and certified as integral LED
units), and that enforcement of installing them is left to state law (OFFICIAL RECORD:
NHTSA interpretation letters, e.g. <https://www.nhtsa.gov/interpretations/ledlamp1> and
<https://www.nhtsa.gov/interpretations/571108-ncc-230201-001-led-headlights-m-baker>;
**quoted from search results: the pages returned 403 to this session, so the exact wording
has not been read here**. Open either link to confirm).

What that means for this car: a "9006 LED" plug-in bulb is not a legal replacement under
federal rules, may fail an inspection, can glare oncoming drivers, and is a mark against the
car at sale. Honda bulletin **A08-010 "Low beam headlight distributes light poorly"** also
exists for this model (`tsb-guide.md`): read it before spending money.

## Option A (legal, cheapest, reversible): high-performance halogen
**Already done on the low beams (2026-10-27):** SilverStar Ultra 9006 installed; the owner
noticed little difference (`log.md`). **Owner's call (2026-11-13): skip lens restore and aim
talk; go straight to new housings** (see "Housing picks" below).

| Bulb | Price seen | Notes |
|---|---|---|
| Sylvania SilverStar **Ultra** 9006 (2-pack) | $48.75 (Walmart listing), $53.99 (Land M Supply); a past Amazon deal at $27 ([Walmart](https://www.walmart.com/ip/21950007), [Slickdeals](https://slickdeals.net/f/18461914-sylvania-9006-silverstar-ultra-high-performance-halogen-headlight-bulb-27)) | Listings call it a 55 W halogen (the OM rates the stock low beam 51 W, p.275); brighter/whiter. DOT compliance for the Ultra: check the package (not confirmed from a primary page) |
| Philips CrystalVision / X-tremeVision 9006 | not priced | Same idea |
| Standard Sylvania/Philips 9006/9005 | ~$15–25 pair | Longest life |

COMMUNITY: performance halogens trade **life** for brightness (often well under the standard
bulb's life). Why: a hotter, thinner filament makes more, whiter light and burns out sooner.
Keep a spare pair in the trunk.

**Before any bulb upgrade, the free fixes:** aim (OM p.226: dealer or qualified shop) and
lens clarity. Cloudy lenses cut light more than any bulb adds; restoring them is a cosmetic
job outside this repo's scope, but replacement housings (DOT, by part number) are a repair
option if the lenses are cracked.

## Replacing the headlight housings (researched 2026-11-12)
Only worth it if a lens is cracked, leaking (water inside), has burnt/peeling reflectors, or
still looks hazy after a restore. Plain surface haze is a sanding/clear-coat job, not a part.

| Choice | Price seen | For | Against |
|---|---|---|---|
| **Honda OEM** 33151-SDA-A01 (driver) / 33101-SDA-A01 (passenger) | $269.45 each, MSRP $390.50 ([HondaPartsNow](https://www.hondapartsnow.com/oem-2005-honda-accord-headlight.html), 2026-11-12) | Exact fit, correct beam, "OEM" at sale | ~$540 a pair |
| **Used OEM** from a salvage yard (search car-part.com free by part number) | not priced | OEM optics cheap | 20-year-old lenses may be just as hazy: inspect for cracks, broken mounting tabs, burnt reflectors |
| **CAPA-certified** aftermarket (Depo or TYC; Honda partslink HO2502120 driver / HO2503120 passenger) | ~$77–141 per side seen (GO-Parts, CarLights360 listings, 2026-11-12) | Cheap, CAPA means a third party checked fit and DOT photometrics | Lens coating tends to yellow sooner than OEM (COMMUNITY); check the CAPA label is real |
| Projector / halo / "LED strip" / black-housing styles (Spec-D, Anzo, etc.) | — | Looks | **Not recommended:** resale, glare, and a history of FMVSS 108 noncompliance recalls on aftermarket lamps for this car (`profile.md`) |

OFFICIAL RECORD (`recalls.md`): **07E004000** recalled TYC 20-6361-00 / 20-6362-00 headlamps
sold for 2003–2006 Accords (misaligned photometrics), and **07E031000** recalled some Depo
317-1131 series lamps (turn signal intensity). Both were 2007 production runs; it shows why
"DOT" printed on a cheap lamp isn't enough. CAPA is the extra check.

After any housing swap: have the aim set (OM p.226). The swap itself is front-bumper-off on
most 2003–07 Accords (UNVERIFIED: get the procedure from Chilton before starting).

## "Way more light than stock" on a budget (asked 2026-11-12)
No affordable bolt-in housing for this car is both legal and much brighter than a **good**
stock headlight. What's on the market:
- Styled plug-in projector housings (Spec-D, PRO Design, CG, Anzo): ~$80–370 a pair in
  listings (SEMotors, Vivid Racing, ProCivic, 2026-11-12). "DOT" on these is the seller's
  claim. Cheap projectors often give a blotchy beam and a poor cutoff (COMMUNITY), and Anzo
  lamps for this car were recalled (06E023000). Not recommended.
- Morimoto XB-style DOT LED assemblies: none found for the 2003–07 Accord (search 2026-11-12).

Ranked path instead:
1. **Bring stock back to new.** New housings (above) or restored lenses, fresh good
   halogens (Option A), then aim. A 20-year-old hazy lens and dulled reflector lose a lot of
   light, so this is the biggest gain per dollar.
2. **Check voltage at the bulb.** Back-probe the low-beam connector, engine running, lights
   on, and compare with battery voltage. COMMUNITY (Daniel Stern's halogen notes): halogen
   output rises steeply with voltage, so a 1 V drop costs a noticeable amount of light. A
   drop over ~0.5 V means a relay harness (ground and feed straight from the battery) is
   worth it; a small drop means skip it. The under-hood box already has separate L/R
   hi/low fuses (`quick-reference.md`), so the factory feed may already be relayed:
   measure before buying.
3. **The real step up: a projector retrofit in a second set of housings.** Buy spare
   housings (used OEM or CAPA), bake them open, fit quality bi-LED or bi-xenon projectors,
   and keep the originals on a shelf to swap back before sale. Gives a sharp cutoff and far
   more usable light, but **it is not a federally compliant headlamp** (same NHTSA problem
   as retrofit bulbs), takes a full weekend, and can fail an inspection. Prices not pinned
   down here.
4. Read bulletin **A08-010** first (free from a Honda dealer service desk; NHTSA has only
   the title). It may cover a low-beam fix on these housings.

## Housing picks for more light + style (owner asked 2026-11-13)
Ranked by real light gained:
1. **Projector retrofit in a spare pair of housings** (the only route that gives a lot
   more usable light). Base: CAPA Depo/TYC pair (prices above) or used OEM. Inside:
   name-brand bi-LED or bi-xenon projectors, shrouds, blacked-out inner bezel for the
   style. OEM pair goes on a shelf for resale. Two ways: send housings to a retrofit shop,
   or DIY over a weekend (bake open, mount, reseal with butyl). Not a federally compliant
   headlamp (see the NHTSA section). Which projector fits the 7th-gen bowl with no cutting:
   not confirmed here (6thgenaccord.com threads say the Morimoto Mini H1 is the easy one on
   the *previous* generation; COMMUNITY). Shop and kit prices not pinned down.
2. **Oracle pre-assembled halo headlights**: OEM-style housing with Oracle halo rings,
   $601.99 white, $700–859 ColorSHIFT, built to order 6–8 weeks, no cancel; page claims
   "FMVSS 108 and SAE Compliant"; lists 2003–07 EX sedan
   ([Oracle](https://oraclelightswholesale.com/products/2003-2007-honda-accord-coupe-sedan-pre-assembled-headlights),
   2026-11-13). Style upgrade only: low-beam source not stated, bulbs not included, so
   expect stock-level light.
3. **Budget styled projectors** (Spec-D 2LHP-ACD03JM-RS ~$205 with H1 low-beam bulbs,
   sold out at SEMotors; Spec-D/Spyder halo units ~$124–212; Pro Design/CG ~$200–370;
   listings 2026-11-13). Look only: thin reviews, beam quality unknown, Anzo units for this
   car were recalled (06E023000).
4. **DT Moto black "LED DRL tube" pair** (eBay seller DT_MOTOSPORT, $138.99, $125.09 with
   coupon, 2 ratings; owner screenshot 2026-11-18, owner planning to buy). Photos show
   reflector bowls for the stock 9005/9006 bulbs, so light ≈ a fresh stock lens, not more.
   Listing says "Fit 03-07 Accord All Model" and "Plug & Play": coupe lamps differ from the
   sedan, so confirm the fitment chart says **4-door sedan**, and find out what powers the
   DRL tube (an extra wire to splice = check it can go on a Posi-Tap / add-a-circuit).
   DOT/SAE marking on the lens not confirmed. Keep the OEM housings for resale.

**Budget cap $259 (owner, 2026-11-13).** A name-brand projector retrofit doesn't fit:
Morimoto M-LED 2.0 bi-LED projectors alone list at ~$370–485 a pair (The Retrofit Source,
Morimoto HID, Vehicle Accessory Pros listings, 2026-11-13; Summit's $193.60 is per
projector). Inside $259 the pick is a **new CAPA-certified Depo/TYC pair** (fresh
reflectors and lenses, factory beam, legal) plus the voltage-drop test (item 2 above),
with a relay harness only if the drop is over ~0.5 V. Real projector light needs about
$450–600 (housings + name-brand projectors; estimate, not quoted).

Don't: used JDM Inspire/Saber HID headlights (eBay listing exists). Fit to US wiring not
confirmed, and Japan drives on the left, so the beam cutoff steps up on the wrong side
(UNVERIFIED principle: check the lens/projector for an LHT marking).

## Option B: interior LEDs (fine, legal, reversible)
Name-brand only (Sylvania ZEVO, Philips Ultinon), size read off the old bulb (`parts.md`).
Dome bulb is a **31 mm festoon, 8 W** (owner, 2026-10-26). The middle courtesy light dims
with the dash brightness knob (OM p.101), so an LED there may flicker: try one first.

## Option C: the aux driving lights already installed
Status, wiring and the problems they've caused are in `log.md` (2026-10-29, 10-31) and open
issues 2 and 9. WA limits for auxiliary driving lamps are noted in `log.md` (RCW
46.37.180(4), 42 in. max mounting height). Keep the harness fused, relay diode-suppressed,
and on the high-beam trigger.

## Not recommended
- HID kits in halogen housings: same federal problem as LED retrofits.
- Tinted/"blue" bulbs: less usable light.
