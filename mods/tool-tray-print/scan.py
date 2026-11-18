"""Turn a phone photo of the scan sheet into a flat, true-scale image.

python3 scan.py photo.jpg out_prefix
  -> out_prefix-flat.png   sheet seen straight down, PX_PER_MM px per mm, scale corrected by the card
  -> prints the card's measured size and the scale correction
"""
import sys
import cv2
import numpy as np
from make_sheet import (DICT, MARKERS, marker_corners_mm, PAGE_W, PAGE_H,
                        CARD_W, CARD_H, CARD_BOX)

PX_PER_MM = 8


def detect(img):
    det = cv2.aruco.ArucoDetector(cv2.aruco.getPredefinedDictionary(DICT),
                                  cv2.aruco.DetectorParameters())
    corners, ids, _ = det.detectMarkers(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    if ids is None:
        raise SystemExit('no markers found')
    found = {int(i): c.reshape(4, 2) for i, c in zip(ids.ravel(), corners) if int(i) in MARKERS}
    if len(found) < 4:
        raise SystemExit(f'only found markers {sorted(found)}; all 4 must be in the photo')
    for c in found.values():
        cv2.cornerSubPix(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), c, (5, 5), (-1, -1),
                         (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.01))
    src = np.vstack([found[i] for i in sorted(found)])
    dst = np.vstack([marker_corners_mm(i) for i in sorted(found)]) * PX_PER_MM
    H, _ = cv2.findHomography(src, dst, 0)
    reproj = cv2.perspectiveTransform(src.reshape(-1, 1, 2), H).reshape(-1, 2)
    return H, float(np.abs(reproj - dst).max() / PX_PER_MM)


def card_size(flat):
    """Find the card inside the card box; return its (long, short) side in sheet-mm."""
    x, y, w, h = CARD_BOX
    pad = 3
    roi = flat[int((y - pad) * PX_PER_MM):int((y + h + pad) * PX_PER_MM),
               int((x - pad) * PX_PER_MM):int((x + w + pad) * PX_PER_MM)]
    g = cv2.GaussianBlur(cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY), (5, 5), 0)
    edges = cv2.Canny(g, 30, 90)
    edges = cv2.dilate(edges, np.ones((3, 3), np.uint8))
    cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    best = None
    for c in cnts:
        (cx, cy), (a, b), ang = cv2.minAreaRect(c)
        L, S = max(a, b) / PX_PER_MM, min(a, b) / PX_PER_MM
        if 60 < L < 110 and 35 < S < 70 and abs(L / S - CARD_W / CARD_H) < 0.25:
            if best is None or L * S > best[0] * best[1]:
                best = (L, S)
    return best


def main(photo, prefix):
    img = cv2.imread(photo)
    if img is None:
        raise SystemExit('cannot read ' + photo)
    H, err = detect(img)
    flat = cv2.warpPerspective(img, H, (int(PAGE_W * PX_PER_MM), int(PAGE_H * PX_PER_MM)),
                               flags=cv2.INTER_CUBIC)
    card = card_size(flat)
    if card:
        L, S = card
        # dilating the edge map grows the outline ~1 px each side
        L -= 2 / PX_PER_MM; S -= 2 / PX_PER_MM
        scale = ((CARD_W / L) + (CARD_H / S)) / 2
        aspect_err = abs((CARD_W / L) - (CARD_H / S)) / scale
        print(f'card measured {L:.2f} x {S:.2f} sheet-mm -> scale x{scale:.4f} (aspect mismatch {aspect_err*100:.2f}%)')
    else:
        scale = 1.0
        print('CARD NOT FOUND: assuming the sheet printed at exactly 100%')
    if abs(scale - 1) > 1e-4:
        flat = cv2.resize(flat, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(prefix + '-flat.png', flat)
    print(f'marker fit error {err:.2f} mm; flat image {flat.shape[1]}x{flat.shape[0]} at {PX_PER_MM} px/mm')
    return scale


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
