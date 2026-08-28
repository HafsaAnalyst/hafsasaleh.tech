"""
Prepares the nav avatar.

Run:  python scripts/make-portrait.py

The site uses one photo: a small round avatar in the header. At 30px it needs a
tight, front-on face, so it comes from the indoor close-up rather than a wider
outdoor shot.

That photo is saved sideways (1080x1920, no EXIF orientation tag) and needs
rotating 90 CCW first. The crop is centred on her face, which also leaves the
"just a Friday" sticker (x 1120-1160 in rotated coordinates) outside the frame.
"""

from pathlib import Path
from PIL import Image

SRC = Path.home() / "Downloads" / "WhatsApp Image 2026-08-27 at 10.56.37 PM.jpeg"
PUBLIC = Path(__file__).resolve().parent.parent / "public"

AVATAR_BOX = (310, 0, 1110, 800)   # 800 x 800, in rotated coordinates
AVATAR_OUT = (700, 700)

if not SRC.exists():
    raise SystemExit(f"Source photo not found: {SRC}")

PUBLIC.mkdir(parents=True, exist_ok=True)

im = Image.open(SRC).convert("RGB").rotate(90, expand=True)
im = im.crop(AVATAR_BOX).resize(AVATAR_OUT, Image.LANCZOS)
out = PUBLIC / "hafsa-saleh-square.jpg"
im.save(out, "JPEG", quality=90, optimize=True, progressive=True)
print(f"wrote {out.name}  ({out.stat().st_size // 1024} KB, {im.width}x{im.height})")
