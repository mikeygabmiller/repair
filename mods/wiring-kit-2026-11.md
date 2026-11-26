# Wiring kit: crimp, no heat (2026-11-26)

**Rule (owner, 2026-11-26, standing; also in `CLAUDE.md`):** crimped nylon-insulated
connectors in a ratcheting crimper for insulated terminals, no heat. No solder, no
heat-shrink connectors, no solder-seal sleeves, no Wago lever nuts, no bare/non-insulated
or open-barrel/Dupont terminals. Vinyl only if no nylon option exists (say so). Engine bay
and under the car: self-fusing silicone tape over the crimp. Replaces the old
"soldered and heat-shrunk" rule, and twist-and-tape. Don't suggest solder again.

Nothing below is owned yet (`tools-owned.md`: no crimper or stripper on any receipt).
Nothing bought as of 2026-11-26.

## Why crimp, why insulated (for future answers)
- Factory harnesses are crimped. Solder wicks up the strands and leaves a stiff point that
  can crack under vibration (UNVERIFIED from memory; check NASA-STD-8739.4 / IPC-WHMA-A-620
  summaries, or cut open a factory splice).
- Tape alone is not a connection: twisted strands under tape loosen and corrode. Tape (any
  kind) only covers a crimp.
- Bare joints can touch body metal (ground) and short, or leak to ground and drain the
  battery. Insulated connectors carry their own insulation, so it's one step.
- The crimp makes the connection; heat only seals. Unheated heat-shrink connectors work
  but their loose tubing needs tape everywhere: slower, so not used.
- Non-insulated connectors need a different (non-insulated) crimper die and added
  insulation on every joint: slower, not used.

## Per-joint method
Strip 1/4 in (self-adjusting stripper) → wire fully into the connector to the center stop
→ crimp in the **matching color die** until the ratchet releases → hard tug test (redo if
it moves) → other side. Engine bay: stretch silicone tape over it, half-overlap.
Two different wire sizes: use the connector for the thicker one; fold the thin wire's
stripped end back to double it.

## Sizes for current jobs
- Back-up light / camera trigger: 18 AWG → red. Back-up bulbs 21 W each (VERIFIED: OM
  p.275, `specs.md`), so two bulbs ≈ 3.5 A (math). The back-up fuse number is unsettled
  (No. 7 10 A vs No. 21 7.5 A, `specs.md`): meter it before tapping.
- Speakers: 18 AWG (head unit power) → red; 16 AWG with the amp → blue.
- Yellow (12–10) not needed for these jobs; power runs for amps use their own kits.

## Verified listings (Muse search, 2026-11-26; "live" = price seen live that day)

| # | Item | Pick | Price | Link / note |
|---|---|---|---|---|
| 1 | Ratcheting crimper, insulated | **Klein 3005CR** (Home Depot; also Zoro) | $34.97 live | [Home Depot](https://www.homedepot.com/p/Klein-Tools-Ratcheting-Crimper-10-22-AWG-Insulated-Terminals-3005CR/306884697). Only listing that says "full-cycle" ratchet. Red 22–16, blue 16–14, yellow 12–10 |
| 1b | Budget crimper + 285 connectors | IWISS IWS-03C-KIT (iwiss.com direct) | $15.99 live | [IWISS](https://www.iwiss.com/products/iws-03c-kit-ratchet-wire-crimper-for-awg20-10-insulated-terminal-with-285pcs-insulated-butt-spades-rings-connectors-kit?variant=42882015035505). Doubts: "High Precision Ratchet" only, full-cycle not promised; included connectors' material not stated (likely vinyl, UNVERIFIED). Not found on Amazon |
| 2 | Nylon butt, red 22–18 | Ancor 210100, 25-pk, Zoro (min 2) | $14.30 live | [Zoro](https://WWW.ZORO.COM/ancor-22-18-awg-nylon-single-crimp-butt-connector-25-pack-210100/i/G402942455/). "Insulation Material, Nylon" |
| 2 | Nylon butt, blue 16–14 | Ancor 210110, 25-pk, Zoro (min 2) | $15.78 live | [Zoro](https://www.zoro.com/ancor-16-14-awg-nylon-single-crimp-butt-connector-25-pack-210110/i/G802942451/) |
| 2 | Nylon butt, yellow 12–10 | Ancor 210120, 25-pk, BOE Marine | $9.79 live | [BOE Marine](https://www.boemarine.com/shop/anc-210120-ancor-12-10-awg-nylon-single-crimp-butt-connector-25-pack-593). Skip for now (no 12–10 wire in current jobs) |
| 3 | Nylon fully insulated spades | **Hold** | — | Buy after the speakers are picked: check the speaker tabs and the harness ends first. 0.250 in: AIRIC 100 pc ([Amazon B08MQ27JV8](https://www.amazon.com/dp/B08MQ27JV8), ~$8.83 secondary, not live). 0.187 in nylon fully insulated exists only as loose parts (McMaster 7243K128/131 red, 7243K129/132 blue, [McMaster](https://mcmaster.com/products/electrical-quick-connects), price not read). Feggizuli/Twidec kits fail (bare + PVC sleeve) |
| 4 | Self-adjusting stripper | Klein 11061 (Home Depot) | $22.96 live | [Home Depot](https://www.homedepot.com/p/Klein-Tools-8-1-4-in-Self-Adjusting-Wire-Stripper-and-Cutter-for-10-20-AWG-12-22-AWG-12-2-and-14-2-Romex-Wire-11061/206318106). Budget: Amazon Basics B07TS6KCXD ~$8.39 (secondary, not live) |
| 5 | 3M Super 33+ tape | Lowe's single roll 6132-DL-2W | $7.28 live | [Lowe's](https://www.lowes.com/pd/Scotch-Super-33-0-75-in-x-66-ft-Vinyl-Electrical-Tape-Black/1000506929). Home Depot 3-pack $18.88 ($6.29/roll) |
| 6 | Self-fusing silicone tape | Rescue Tape 1 in × 12 ft RT12012BBL (Ace) | $11.99 live | [Ace](https://www.acehardware.com/departments/plumbing/solvents-and-cements/plumbers-putty-and-sealers/4387437) |
| 7 | Tesa 51608 fleece harness tape | DigiKey 51608-19-15(1) | $15.63 live | [DigiKey](https://www.digikey.com/en/products/detail/tapecase/51608-19-15-1/26417203). Optional (looks only). Amazon 5-roll B00XPBB6L8 $16.05 is a stale third-party listing |
| 8 | Speaker harness (pair) | Metra 72-7800 (Crutchfield) | $9.99/pair live | [Crutchfield](https://www.crutchfield.com/I-rFBFcVA2/p_120727800/Metra-72-7800-Speaker-Wiring-Harness.html). Owners report it fits the **rear deck**; front-door fit not confirmed (`plan-front-speakers-2026-11.md`). Run Crutchfield's vehicle selector for a 2005 Accord. One pair = 2 speakers. Alt: Scosche SHHA02B (Best Buy, no price shown). **Not** Metra 70-1721 / Scosche HA08B (radio harnesses). No tweeter harness for this car: tweeters use Posi-Products |

Amazon: almost every Amazon page was a stale crawl or "No featured offers" on 2026-11-26;
re-check any Amazon price live before buying.

## Recommended buy (Claude review of Muse's list, 2026-11-26)
Muse's totals add up ($142.69 / $151.52 / $117.97). Trimmed to what the current jobs need
(no yellow, no spades yet, two harness pairs for four speakers):

| Route | Items | Total (before tax and shipping) |
|---|---|---|
| **Name-brand crimper** | Klein 3005CR 34.97 + Ancor red 14.30 + blue 15.78 + Klein 11061 22.96 + Super 33+ 7.28 + Rescue Tape 11.99 + Tesa 15.63 + Metra 72-7800 ×2 19.98 | **$142.89** |
| Budget crimper | Same, IWISS IWS-03C-KIT 15.99 instead of Klein | **$123.91** |

Pick: Klein. The crimper is the one tool that decides whether every joint holds, and it's
the only listing that states a full-cycle ratchet. Shipping from Zoro and DigiKey is not
included. Drop Tesa (-$15.63) if looks don't matter; drop one harness pair if only the
rear deck is being done.

## Still open
- Speaker terminal tab sizes (Kenwood KFC-1666S and any new speakers): measure or read the
  spec sheet before buying spades.
- Metra 72-7800 front-door fit: Crutchfield/Metra vehicle lookup.
- What ends the 72-7800 leads have (spades or bare wire): read the Crutchfield page photos.
