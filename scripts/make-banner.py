"""
Generates public/linkedin-banner.png — 1584x396, LinkedIn's cover photo size.

Run:  python scripts/make-banner.py

Design: a mesh gradient — several soft, heavily blurred colour blobs over a deep
navy base. Reads far richer than a two-stop linear wash, which went muddy.

Layout constraints:
  * LinkedIn drops the circular profile photo over the LEFT of the banner, and it
    reaches further right and higher than the docs imply — measured against a real
    profile it covers roughly the left third and the lower half. So the left third
    is left EMPTY and the text block is CENTRED, which also survives LinkedIn
    cropping the sides on narrow viewports.
  * Vertical crop on mobile means everything stays inside y 90-360.
  * The name is already printed under the banner by LinkedIn, so the banner leads
    with the positioning statement instead of repeating it.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1584, 396
OUT = Path(__file__).resolve().parent.parent / "public" / "linkedin-banner.png"

BASE = (11, 18, 48)           # deep navy ground

# (centre_x, centre_y, radius_x, radius_y, colour, strength)
BLOBS = [
    (1230,  70, 560, 430, (16, 185, 165), 215),   # teal, upper right
    (1480, 330, 380, 300, (45, 212, 191), 150),   # brighter cyan, far right
    ( 380, 340, 620, 400, ( 79,  70, 215), 175),  # indigo, lower left
    ( 830, -70, 520, 300, (150,  52, 140), 105),  # plum, top centre — depth only
]

MINT = (150, 240, 226)
GOLD = (250, 204, 112)
PAPER = (255, 255, 255)
SUB = (205, 226, 233)
INK = (9, 26, 46)

FONT_DIR = Path("C:/Windows/Fonts")
SERIF_BOLD = FONT_DIR / "georgiab.ttf"
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
        mask = Image.new("L", size, 0)
        ImageDraw.Draw(mask).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=strength)
        mask = mask.filter(ImageFilter.GaussianBlur(170))
        img.paste(Image.new("RGB", size, colour), (0, 0), mask)
    return img


img = mesh((W, H), BASE, BLOBS)

# Scrim behind the headline so white type stays crisp over the brighter blobs
scrim = Image.new("L", (W, H), 0)
ImageDraw.Draw(scrim).ellipse([420, 40, 1400, 380], fill=64)
scrim = scrim.filter(ImageFilter.GaussianBlur(120))
img.paste(Image.new("RGB", (W, H), (7, 14, 36)), (0, 0), scrim)

# ---- faint data grid, right side — texture, not decoration ----
grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grid)
for i in range(9):
    x = 1090 + i * 60
    gd.line([(x, 56), (x, 344)], fill=(255, 255, 255, 16), width=1)
for i in range(6):
    y = 56 + i * 58
    gd.line([(1090, y), (1570, y)], fill=(255, 255, 255, 16), width=1)
img = Image.alpha_composite(img.convert("RGBA"), grid).convert("RGB")

d = ImageDraw.Draw(img, "RGBA")

# ---- rising bars, far right, clear of the centred text ----
bar_base, bw, gap = 318, 26, 14
for i, h_ in enumerate([30, 48, 70, 96, 126]):
    x = 1336 + i * (bw + gap)
    fill = GOLD + (225,) if i == 4 else MINT + (70 + i * 30,)
    d.rounded_rectangle([x, bar_base - h_, x + bw, bar_base], radius=5, fill=fill)

# ---- centred text block ----
CX = 910


def centred(text, f, y, fill):
    w = d.textlength(text, font=f)
    d.text((CX - w / 2, y), text, font=f, fill=fill)


d.rectangle([CX - 30, 96, CX + 30, 100], fill=GOLD)
centred("MARKETING INTELLIGENCE ANALYST", font(MONO, 21), 120, MINT)

y = 160
for line in ["I build the data layer", "marketing teams actually run on."]:
    centred(line, font(SERIF_BOLD, 44), y, PAPER)
    y += 55

centred("ETL pipelines  \u00b7  Multi-touch attribution  \u00b7  Dashboards leadership decides from",
        font(SANS, 19), 278, SUB)

# ---- the destination, as a button-like pill so it reads as "go here" ----
url = "hafsasaleh.tech"
f_url = font(SANS_SEMI, 25)
pad_x, pad_y = 28, 13
tw = d.textlength(url, font=f_url)
pw = tw + pad_x * 2
px0, py0 = CX - pw / 2, 316
px1, py1 = px0 + pw, py0 + 25 + pad_y * 2
d.rounded_rectangle([px0, py0, px1, py1], radius=(py1 - py0) / 2, fill=MINT)
d.text((px0 + pad_x, py0 + pad_y - 2), url, font=f_url, fill=INK)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT.name}  ({OUT.stat().st_size // 1024} KB, {W}x{H})")
