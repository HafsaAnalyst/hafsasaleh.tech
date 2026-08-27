"""
Prepares the site portraits. Two different source photos, because the two slots
have opposite requirements.

Run:  python scripts/make-portrait.py

  public/hafsa-saleh.jpg         4:5 portrait for the About section, from the
                                 outdoor shot. Wide framing works there — the
                                 sky and hillside give the frame depth.
                                 Source is 1200x1600, upright.
                                 Measured: cap top y~370, face x 600-740 /
                                 y 400-560, child x 130-430 / y 1140-1450.
                                 The crop stops at y=1130 so the child is out.

  public/hafsa-saleh-square.jpg  1:1 nav avatar, from the indoor shot. At 30px a
                                 wide outdoor frame renders as sky and a cap, so
                                 the avatar needs a tight, front-on face. That
                                 photo is saved sideways (1080x1920, no EXIF
                                 tag) and needs rotating 90 CCW first; the crop
                                 is centred on her face, which also leaves the
                                 "just a Friday" sticker (x 1120-1160) outside.
"""

from pathlib import Path
from PIL import Image

DOWNLOADS = Path.home() / "Downloads"
PORTRAIT_SRC = DOWNLOADS / "WhatsApp Image 2026-08-27 at 11.17.11 PM.jpeg"   # outdoor
AVATAR_SRC = DOWNLOADS / "WhatsApp Image 2026-08-27 at 10.56.37 PM.jpeg"     # indoor
PUBLIC = Path(__file__).resolve().parent.parent / "public"

PORTRAIT_BOX = (280, 250, 984, 1130)   # 704 x 880  (4:5)
PORTRAIT_OUT = (880, 1100)

AVATAR_BOX = (310, 0, 1110, 800)       # 800 x 800, in rotated coordinates
AVATAR_OUT = (700, 700)


def save(im: Image.Image, filename: str, quality: int = 90) -> None:
    path = PUBLIC / filename
    im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"wrote {path.name}  ({path.stat().st_size // 1024} KB, {im.width}x{im.height})")


for f in (PORTRAIT_SRC, AVATAR_SRC):
    if not f.exists():
        raise SystemExit(f"Source photo not found: {f}")

PUBLIC.mkdir(parents=True, exist_ok=True)

portrait = Image.open(PORTRAIT_SRC).convert("RGB")
save(portrait.crop(PORTRAIT_BOX).resize(PORTRAIT_OUT, Image.LANCZOS), "hafsa-saleh.jpg")

avatar = Image.open(AVATAR_SRC).convert("RGB").rotate(90, expand=True)
save(avatar.crop(AVATAR_BOX).resize(AVATAR_OUT, Image.LANCZOS), "hafsa-saleh-square.jpg")
