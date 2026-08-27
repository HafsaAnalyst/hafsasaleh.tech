"""
Prepares the site portraits from the source photo.

Run:  python scripts/make-portrait.py

The source is a phone photo saved sideways: 1080x1920 with the subject rotated
90 degrees and no EXIF orientation tag, so nothing auto-corrects it.

  public/hafsa-saleh.jpg         the full frame, rotated upright — 1920x1080,
                                 horizontal. No crop, so it keeps every pixel of
                                 the original and stays as sharp as the source
                                 allows. The "just a Friday" sticker is still in
                                 it: removing it means either cropping to ~57%
                                 of the width (which zooms in and softens the
                                 picture) or patching over it (which leaves a
                                 visible block). Re-export the photo without the
                                 sticker and this script needs no changes.

  public/hafsa-saleh-square.jpg  1:1 crop for the nav avatar. Centred on her
                                 face, which puts the sticker outside the frame.
"""

from pathlib import Path
from PIL import Image

SRC = Path.home() / "Downloads" / "WhatsApp Image 2026-08-27 at 10.56.37 PM.jpeg"
PUBLIC = Path(__file__).resolve().parent.parent / "public"

# Square box in rotated (1920x1080) coordinates. Her face sits at x 480-950,
# y 60-560; the sticker is at x 1120-1160, so a face-centred square misses it.
SQUARE_BOX = (310, 0, 1110, 800)
SQUARE_OUT = (760, 760)


def save(im: Image.Image, filename: str, quality: int = 90) -> None:
    path = PUBLIC / filename
    im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"wrote {path.name}  ({path.stat().st_size // 1024} KB, {im.width}x{im.height})")


if not SRC.exists():
    raise SystemExit(f"Source photo not found: {SRC}")

PUBLIC.mkdir(parents=True, exist_ok=True)

im = Image.open(SRC).convert("RGB").rotate(90, expand=True)
save(im, "hafsa-saleh.jpg")
save(im.crop(SQUARE_BOX).resize(SQUARE_OUT, Image.LANCZOS), "hafsa-saleh-square.jpg")
