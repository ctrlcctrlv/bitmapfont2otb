# `bitmapfont2otb`

This font converts a bitmap font in BDF, PCF, or SFD format, into an OTB (OpenType Bitmap) font.

New versions of HarfBuzz no longer support BDF, so this is necessary. However, existing scripts either only create outlines with squares, or only create bitmaps. This script does both: it creates fallback glyphs made of square outlines, but _also_ adds a bitmap strike to the font.

## Requirements

* FontForge
* [`bdflib`](https://pypi.org/project/bdflib/)
