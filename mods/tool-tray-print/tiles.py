"""Tile outlines for the toolbox bottom layer, and the fit-test frames.

Floor designed at 17 x 6 in (431.8 x 152.4 mm) minus 1 mm, so it drops into a box that
is "a little more than" that. Two tiles joined by dovetails. Each tile, tabs included,
is 218.4 mm long: fits the Ender 3 Pro's bed (3..228 mm in PrusaSlicer's profile) with
no skirt.

python3 tiles.py  -> fit-test-A.stl, fit-test-B.stl
"""
import numpy as np
import trimesh
from shapely.geometry import box, Polygon
from shapely import affinity
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties

FLOOR_L, FLOOR_W = 431.8 - 1.0, 152.4 - 1.0
CORNER_R = 6.0
TAB_D, TAB_NECK, TAB_HEAD = 6.0, 10.0, 15.0
TAB_Y = (-38.0, 38.0)          # tab centres across the width
JOINT_GAP = 0.25               # clearance each side in the notch
A_BODY = FLOOR_L / 2 - TAB_D / 2   # A's body; its tabs reach into B
FONT = FontProperties(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')


def rrect(x0, y0, x1, y1, r):
    return box(x0 + r, y0 + r, x1 - r, y1 - r).buffer(r, 24)


def tab(x_seam, yc, grow=0.0):
    """Dovetail pointing +x from the seam."""
    n, h, d = TAB_NECK / 2 + grow, TAB_HEAD / 2 + grow, TAB_D + grow
    return Polygon([(x_seam - 1, yc - n), (x_seam, yc - n), (x_seam + d, yc - h),
                    (x_seam + d, yc + h), (x_seam, yc + n), (x_seam - 1, yc + n)])


def outlines():
    """Floor coordinates: x along the 17 in, y across, origin at A's outer end, y centred."""
    W2 = FLOOR_W / 2
    seam = A_BODY
    full = rrect(0, -W2, FLOOR_L, W2, CORNER_R)
    a = full.intersection(box(-1, -W2 - 1, seam, W2 + 1))
    b = full.intersection(box(seam, -W2 - 1, FLOOR_L + 1, W2 + 1))
    for yc in TAB_Y:
        a = a.union(tab(seam, yc))
        b = b.difference(tab(seam, yc, JOINT_GAP))
    return a, b, seam


def text(s, size, cx, cy):
    tp = TextPath((0, 0), s, size=size, prop=FONT)
    p = Polygon()
    for ring in tp.to_polygons():
        if len(ring) >= 3:
            p = p.symmetric_difference(Polygon(ring).buffer(0))
    x0, y0, x1, y1 = p.bounds
    return affinity.translate(p, cx - (x0 + x1) / 2, cy - (y0 + y1) / 2)


def prism(poly, z0, h):
    poly = poly.buffer(0.01, join_style=2).buffer(-0.01, join_style=2)
    polys = list(poly.geoms) if hasattr(poly, 'geoms') else [poly]
    ms = []
    for p in polys:
        if p.area > 0.5:
            m = trimesh.creation.extrude_polygon(p, h)
            m.apply_translation([0, 0, z0])
            ms.append(m)
    return ms[0] if len(ms) == 1 else trimesh.boolean.union(ms, engine='manifold')


def fit_frame(outline, label, cx, band=4.0, h=1.2):
    """Outline ring + a cross brace + a raised label; tabs/notches kept solid around."""
    ring = outline.difference(outline.buffer(-band, join_style=2))
    x0, y0, x1, y1 = outline.bounds
    brace = box(x0, -band / 2, x1, band / 2).union(box(cx - band / 2, y0, cx + band / 2, y1))
    plate = ring.union(brace.intersection(outline))
    # keep material around the joint so the dovetails are tested properly
    for yc in TAB_Y:
        plate = plate.union(outline.intersection(box(x0, yc - 14, x1, yc + 14)).intersection(
            box(A_BODY - 12, -200, A_BODY + 12, 200)))
    plate = plate.union(text(label, 16, cx, 35).buffer(1.2).intersection(outline))
    m = prism(plate, 0, h)
    m = trimesh.boolean.union([m, prism(text(label, 16, cx, 35), h, 0.6)], engine='manifold')
    return m


if __name__ == '__main__':
    a, b, seam = outlines()
    A = fit_frame(a, 'A  FIT TEST', seam / 2)
    B = fit_frame(b, 'B  FIT TEST', (seam + FLOOR_L) / 2)
    A.export('fit-test-A.stl'); B.export('fit-test-B.stl')
    for n, m in (('A', A), ('B', B)):
        print(n, [round(v, 1) for v in m.extents], 'watertight', m.is_watertight)
    ta = tab(seam, TAB_Y[0]); print('tab neck/head', TAB_NECK, TAB_HEAD, 'gap', JOINT_GAP)
    print('assembled length', round(FLOOR_L, 1), 'width', round(FLOOR_W, 1))
