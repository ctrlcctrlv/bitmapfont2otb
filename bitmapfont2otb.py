#!/usr/bin/env python3
import fontforge
import glob
import os
import sys
from bdflib import reader as bdfreader

assert len(sys.argv) == 3, "Must provide a filename: PCF, BDF, or SFD containing a bitmap font, and an output OTB filename"
(_, infile, outfile) = sys.argv

cm = fontforge.open(infile)
out_bdf = outfile.replace(".otb", ".bdf")
cm.generate(out_bdf)
bdff = glob.glob(out_bdf.split(".")[0]+"*-*.bdf")
os.rename(bdff[0], out_bdf)
f = fontforge.font()
f.ascent = cm.ascent
f.descent = cm.descent
f.importBitmaps(out_bdf, True)
with open(out_bdf, "rb") as bdff:
    bdf = bdfreader.read_bdf(bdff)

block_size = f.em / bdf[b"POINT_SIZE"]

def pos_to_contour(x, y):
    pos_x, pos_y = x*block_size, y*block_size
    c = fontforge.contour()
    c.moveTo(pos_x, pos_y)
    c.lineTo(pos_x+block_size, pos_y)
    c.lineTo(pos_x+block_size, pos_y+block_size)
    c.lineTo(pos_x, pos_y+block_size)
    c.closed = True
    return c

for i, g in enumerate(bdf.glyphs):
    gn = g.name.decode("utf-8")
    x, y, w, h = g.get_bounding_box()
    orig_x = x
    l = fontforge.layer()
    pixels = list()
    for row in g.iter_pixels():
        pixels.append([p for p in row])
    for row in reversed(pixels):
        for p in row:
            if p:
                c = pos_to_contour(x, y)
                l += c
            x += 1
        x = orig_x
        y += 1
    ffg = f.createChar(-1,gn)
    ffg.foreground = l
    ffg.width = int(block_size*(g.advance))

f.removeOverlap()
f.encoding = "UnicodeFull"
f.encoding = "compacted"
f.simplify()
f.importBitmaps(out_bdf)
f.save("output.sfd")
out_otf = out_bdf.replace(".bdf", ".otf")
f.generate(out_otf, flags=("opentype",), bitmap_type="otf")
os.rename(out_otf, outfile)
