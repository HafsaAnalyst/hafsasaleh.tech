"""
Prepares the site portraits from the source photo.

Run:  python scripts/make-portrait.py

The source is a phone photo saved sideways (1080x1920 with the subject rotated
90 degrees) and carrying a story caption. This script:
  1. rotates 90 counter-clockwise so she is upright — which also makes the frame
     horizontal, 1920x1080;
  2. crops the right-hand strip away, because the "just a Friday" caption sits at
     roughly x >= 1100 and has no place on a portfolio;
  3. writes the two crops the site actually uses.

  public/hafsa-saleh.jpg         4:3 horizontal — About section
  public/hafsa-saleh-square.jpg  1:1            — nav avatar
"""

from pathlib import Path
from PIL import Image

SRC = Path.home() / "Downloads" / "WhatsApp Image 2026-08-27 at 10.56.37 PM.jpeg"
PUBLIC = Path(__file__).resolve().parent.parent / "public"

# Boxes are in rotated (1920x1080) coordinates. Measured off the source:
#   head top  y ~ 20   (the source has almost no headroom, so both crops start
#                       at y=0 or the hijab clips)
#   face      x 480-950, y 60-560
#   caption   x 1120-1160  -> every crop stops before x=1110
# 4:3 rather than 3:2 — the source has no headroom, and the wider ratio was
# cropping into the hijab and cutting the shoulders off.
WIDE_BOX = (0, 0, 1100, 825)      # 1100 x 825  (4:3 horizontal)
SQUARE_BOX = (310, 0, 1110, 800)  # 800 x 800   (1:1, centred on her face)

# Output at native crop size — the source is already soft, so upscaling only
# amplifies the noise.
WIDE_OUT = (1100, 825)
SQUARE_OUT = (760, 760)


def render(box, out_size, filename, quality=88):
    im = Image.open(SRC).convert("RGB").rotate(90, expand=True)
    im = im.crop(box).resize(out_size, Image.LANCZOS)
    path = PUBLIC / filename
    im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"wrote {path.name}  ({path.stat().st_size // 1024} KB, {out_size[0]}x{out_size[1]})")


if not SRC.exists():
    raise SystemExit(f"Source photo not found: {SRC}")

PUBLIC.mkdir(parents=True, exist_ok=True)
render(WIDE_BOX, WIDE_OUT, "hafsa-saleh.jpg")
render(SQUARE_BOX, SQUARE_OUT, "hafsa-saleh-square.jpg")
