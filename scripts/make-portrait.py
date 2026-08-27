"""
Prepares the site portraits from the source photo.

Run:  python scripts/make-portrait.py

Source is 1200x1600, upright, no EXIF rotation needed. Measured off the frame:
    cap top      y ~ 370
    face         x 600-740, y 400-560
    raised hand  x 480-620, y 380-500
    child        x 130-430, y 1140-1450   <- cropped out entirely

Both crops stop above y=1130, so nobody else appears in either image.

  public/hafsa-saleh.jpg         4:5 portrait — About section, in the gradient frame
  public/hafsa-saleh-square.jpg  1:1          — nav avatar, centred on her face
"""

from pathlib import Path
from PIL import Image

SRC = Path.home() / "Downloads" / "WhatsApp Image 2026-08-27 at 11.17.11 PM.jpeg"
PUBLIC = Path(__file__).resolve().parent.parent / "public"

PORTRAIT_BOX = (280, 250, 984, 1130)   # 704 x 880  (4:5)
SQUARE_BOX = (500, 305, 850, 655)      # 350 x 350  (1:1, tight for a 30px avatar)

PORTRAIT_OUT = (880, 1100)
SQUARE_OUT = (700, 700)


def render(box, out_size, filename, quality=90):
    im = Image.open(SRC).convert("RGB").crop(box).resize(out_size, Image.LANCZOS)
    path = PUBLIC / filename
    im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"wrote {path.name}  ({path.stat().st_size // 1024} KB, {out_size[0]}x{out_size[1]})")


if not SRC.exists():
    raise SystemExit(f"Source photo not found: {SRC}")

PUBLIC.mkdir(parents=True, exist_ok=True)
render(PORTRAIT_BOX, PORTRAIT_OUT, "hafsa-saleh.jpg")
render(SQUARE_BOX, SQUARE_OUT, "hafsa-saleh-square.jpg")
