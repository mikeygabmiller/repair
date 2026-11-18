# Printed tool tray: bottom layer of the toolbox

Started 2026-11-18. The owner's toolbox bottom layer gets 3D-printed inserts (PLA,
Ender 3 Pro, 220 x 220 mm bed) with a cutout shaped to each tool and a pressed-in label.
It replaces the foam "Core layer v4" plan (`mods/tool-tray-core-layer.jpg`) for this layer.
Not a repair item: no specs here, only tool sizes.

## The box (owner, 2026-11-18, not measured exactly)
Floor a little over **17 x 6 in**, a little over 6 in tall. **Nothing sits on top of this
layer**, so tools can stand up. Design to exactly 17 x 6 in (431.8 x 152.4 mm) so it fits
whatever the extra is.

## What goes in this layer (owner, 2026-11-18)
| Item | Notes |
|---|---|
| 3/8 in drive sockets 10, 11, 12, 13, 15, 17 mm | All 3/8 (owner) |
| 19 mm 1/2 in impact socket | **The lug socket** (owner). Not bought yet: leave its spot, make its cup when it arrives |
| Quinn 1/2 in digital torque adapter (58706) | |
| Hex-shank to square-drive adapter (black) | |
| Hyper Tough ratcheting wrenches (2) + 3 hex inserts | The pictured wrench is stamped 19 mm / 14 mm; the inserts drop into its ring for smaller sizes (read from the photo, set name not found online) |
| Pittsburgh 1/4 x 3/8 in dual-drive extendable ratchet (62312 / 70149) | 9-1/2 in pushed in, 13-1/2 in out (HF listing) |
| Not in this layer | 17 and 21 mm impact sockets |
More gets added later (owner): leave open space on tile 2.

## Design
- **Tiles**, because the bed is 220 mm: two tiles about 214 x 149 mm that lock together.
  Long tools (ratchet ~241 mm) run across the seam. Swap one tile later without
  reprinting the rest.
- **Sockets sit in small cups** that drop into standard holes in the tile: a new or
  changed socket is a 15-minute cup, not a new tile.
- **Cutouts traced from photos** (owner chose this over measuring, 2026-11-18), with
  about 0.5 to 1 mm room per side, plus finger scoops.
- **Labels pressed in** beside each pocket and on each cup rim; white paint marker
  rubbed in for contrast. No filament swap.

## Getting the outlines: the scan sheet
`scan-sheet.pdf` (made by `make_sheet.py`): four ArUco markers fix the angle, and a bank
card or license in the box sets the true size (ISO ID-1, 85.60 x 53.98 mm), so it works
even if the printer shrank the page. `python3 scan.py photo.jpg out` writes a flat,
true-scale image (8 px/mm) and prints the card's measured size.

Tested 2026-11-18 on synthetic tilted photos printed at 100%, 97% and 94%: a 24.00 mm
circle measured 23.88 mm, a 50 x 80 mm block 49.9 x 79.9 mm. Real photos will be worse
(lens distortion, shadows, a socket's top sitting closer to the camera): expect about
0.5 to 1 mm, which the pocket clearance covers.

### The photos (owner)
1. Print at 100% / "Actual size". Card face up in its box.
2. Indoor light or shade, **no flash** (glare on chrome), no hard sun shadows.
3. Phone straight above, about 3 ft up, zoomed about 2x so the sheet fills the screen.
   All 4 black squares in the shot.
4. Photos, tools not touching each other:
   - A: the six sockets **lying on their sides** (gives width and height), the hex
     adapter, the 3 wrench inserts
   - B: the Quinn adapter, display up
   - C: both wrenches
   - D: the ratchet pushed in, corner to corner (it may cover the card box; the scale
     from photo A is reused because it's the same printed sheet)
5. Send the **original files**. Images pasted into chat arrive shrunk to 512 x 384
   (2026-11-18), about 0.6 mm per pixel; uploading to Google Drive keeps the full size.

## Phases
| Phase | What | Status |
|---|---|---|
| 0 | Scan sheet + photos | Sheet done 2026-11-18; photos pending |
| 1 | Fit test: 2 mm outlines of both tiles in the box | |
| 2 | Tile 1: sockets (cups), 19 lug spot, Quinn, hex adapter | |
| 3 | Tile 2: wrenches, inserts, ratchet, open space | |
| 4+ | Added tools: new cups or a replacement tile | |
