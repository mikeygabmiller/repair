"""Tool scan sheet: US Letter, four ArUco markers for perspective, and a box
for a bank card / license (85.60 x 53.98 mm, ISO ID-1) that sets the true
scale, so it still works if the printer shrank the page.

Run: python3 make_sheet.py -> scan-sheet.pdf
The geometry below is shared with scan.py.
"""
import cv2
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import Color
import io

MM = 72 / 25.4
PAGE_W, PAGE_H = 215.9, 279.4
M, MARGIN = 30.0, 10.0
DICT = cv2.aruco.DICT_4X4_50
# marker id -> top-left corner (mm, y down)
MARKERS = {0: (MARGIN, MARGIN), 1: (PAGE_W - MARGIN - M, MARGIN),
           2: (PAGE_W - MARGIN - M, PAGE_H - MARGIN - M), 3: (MARGIN, PAGE_H - MARGIN - M)}
CARD_W, CARD_H = 85.60, 53.98
CARD_BOX = (PAGE_W / 2 - 50, PAGE_H - MARGIN - 62, 100, 62)   # x, y, w, h (mm, y down)


def marker_corners_mm(mid):
    x, y = MARKERS[mid]
    return np.array([[x, y], [x + M, y], [x + M, y + M], [x, y + M]], np.float32)


def build(path):
    c = canvas.Canvas(path, pagesize=letter)
    d = cv2.aruco.getPredefinedDictionary(DICT)
    for mid, (x, y) in MARKERS.items():
        img = cv2.aruco.generateImageMarker(d, mid, 600)
        ok, png = cv2.imencode('.png', img)
        c.drawImage(ImageReader(io.BytesIO(png.tobytes())), x * MM, (PAGE_H - y - M) * MM, M * MM, M * MM)
    grey = Color(0.55, 0.55, 0.55)
    # title
    c.setFont('Helvetica-Bold', 13)
    c.drawCentredString(PAGE_W / 2 * MM, (PAGE_H - 20) * MM, 'TOOL SCAN SHEET')
    c.setFont('Helvetica', 8.5)
    c.drawCentredString(PAGE_W / 2 * MM, (PAGE_H - 26) * MM, 'Print at 100% / "Actual size". Keep all 4 black squares in the photo.')
    c.drawCentredString(PAGE_W / 2 * MM, (PAGE_H - 31) * MM, 'Tools anywhere in the dashed area, not touching each other.')
    # tool area
    c.setStrokeColor(grey); c.setDash(3, 3); c.setLineWidth(0.6)
    top, bottom = MARGIN + M + 4, CARD_BOX[1] - 4
    c.rect(MARGIN * MM, (PAGE_H - bottom) * MM, (PAGE_W - 2 * MARGIN) * MM, (bottom - top) * MM)
    # card box
    x, y, w, h = CARD_BOX
    c.rect(x * MM, (PAGE_H - y - h) * MM, w * MM, h * MM)
    c.setDash()
    c.setFillColor(grey); c.setFont('Helvetica', 7.5)
    c.drawCentredString((x + w / 2) * MM, (PAGE_H - y - h / 2 + 2) * MM, 'Lay a bank card or license here,')
    c.drawCentredString((x + w / 2) * MM, (PAGE_H - y - h / 2 - 2) * MM, 'face up (it sets the true size)')
    c.save()


if __name__ == '__main__':
    import os
    build(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scan-sheet.pdf'))
    print('ok')
