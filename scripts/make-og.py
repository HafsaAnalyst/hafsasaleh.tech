"""
Generates public/og.png — the 1200x630 preview card shown when the site is shared
on LinkedIn, X, Slack, WhatsApp etc.

Run:  python scripts/make-og.py

Uses Windows system fonts directly rather than relying on fontconfig, so the
output is identical on every run. Re-run it after changing the name or tagline.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
OUT = Path(__file__).resolve().parent.parent / "public" / "og.png"

# Site palette (matches the case-study hero gradient)
BASE = (8, 8, 8)
BLOBS = [
    (860,  40, 480, 340, (0, 176, 214), 205),
    (1150, 250, 300, 230, (0, 225, 255), 150),
    (230,  280, 500, 320, (112,  62, 178), 190),
    (620,  -70, 420, 230, (150,  62, 190),  95),
]
CYAN = (120, 238, 255)
GOLD = (243, 153, 18)
PAPER = (255, 255, 255)
MUTED = (198, 216, 228)

FONT_DIR = Path("C:/Windows/Fonts")
DISPLAY = FONT_DIR / "seguibl.ttf"
SANS = FONT_DIR / "segoeui.ttf"
SANS_SEMI = FONT_DIR / "seguisb.ttf"
MONO = FONT_DIR / "consola.ttf"


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    if not path.exists():
        raise SystemExit(f"Missing font: {path}")
    return ImageFont.truetype(str(path), size)


def mesh(size, base, blobs):
    img = Image.new("RGB", size, base)
    for cx, cy, rx, ry, colour, strength in blobs:
        m = Image.new("L", size, 0)
        ImageDraw.Draw(m).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=strength)
        m = m.filter(ImageFilter.GaussianBlur(150))
        img.paste(Image.new("RGB", size, colour), (0, 0), m)
    return img


img = mesh((W, H), BASE, BLOBS)
d = ImageDraw.Draw(img, "RGBA")

# --- decorative data marks: a rising bar group, bottom right, low contrast ---
# base sits above the footer rule at y=520 so the two never intersect
bar_x, bar_base, bar_w, gap = 812, 496, 34, 14
for i, h_ in enumerate([48, 74, 96, 132, 168, 210]):
    d.rounded_rectangle(
        [bar_x + i * (bar_w + gap), bar_base - h_, bar_x + i * (bar_w + gap) + bar_w, bar_base],
        radius=6,
        fill=CYAN + (40 + i * 26,),
    )

# --- accent rule ---
d.rectangle([80, 118, 80 + 68, 118 + 5], fill=GOLD)

# --- eyebrow ---
d.text((80, 156), "MARKETING INTELLIGENCE ANALYST", font=font(MONO, 25), fill=CYAN)

# --- name ---
d.text((80, 210), "Hafsa Saleh", font=font(DISPLAY, 96), fill=PAPER)

# --- tagline, manually wrapped to control the break ---
tagline = [
    "I build the data layer marketing teams",
    "actually run on.",
]
y = 356
for line in tagline:
    d.text((80, y), line, font=font(SANS, 39), fill=MUTED)
    y += 54

# --- footer rule + domain ---
d.rectangle([80, 520, W - 80, 521], fill=(255, 255, 255, 34))
d.text((80, 548), "hafsasaleh.tech", font=font(SANS_SEMI, 32), fill=PAPER)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT}  ({OUT.stat().st_size // 1024} KB, {W}x{H})")
