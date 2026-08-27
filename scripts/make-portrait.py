"""
Crops the source photo into the portraits the site uses.

Run:  python scripts/make-portrait.py

The source is a casual full-scene photo. This crops in to head-and-shoulders so
the busy background (bowling pins, framed artwork, table clutter) falls outside
the frame. The right edge is held at x<575 because the framed artwork behind her
starts there and its corner reads as a second face in shot.

  public/hafsa-saleh.jpg         4:5 portrait  — About section
  public/hafsa-saleh-square.jpg  1:1           — nav avatar and anywhere circular
"""

from pathlib import Path
from PIL import Image

SRC = Path(r"C:\Users\DELL\Pictures\WhatsApp Image 2026-07-26 at 3.02.15 PM (1).jpeg")
PUBLIC = Path(__file__).resolve().parent.parent / "public"

PORTRAIT_BOX = (175, 225, 573, 723)   # 398 x 498  (~4:5)
SQUARE_BOX = (175, 232, 573, 630)     # 398 x 398  (1:1)

PORTRAIT_OUT = (800, 1000)
SQUARE_OUT = (720, 720)


def render(box, out_size, filename, quality=88):
    im = Image.open(SRC).convert("RGB").crop(box).resize(out_size, Image.LANCZOS)
    path = PUBLIC / filename
    im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"wrote {path.name}  ({path.stat().st_size // 1024} KB, {out_size[0]}x{out_size[1]})")


if not SRC.exists():
    raise SystemExit(f"Source photo not found: {SRC}")

PUBLIC.mkdir(parents=True, exist_ok=True)
render(PORTRAIT_BOX, PORTRAIT_OUT, "hafsa-saleh.jpg")
render(SQUARE_BOX, SQUARE_OUT, "hafsa-saleh-square.jpg")
