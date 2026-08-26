"""
Generates public/linkedin-banner.png — 1584x396, LinkedIn's cover photo size.

Run:  python scripts/make-banner.py

Layout constraints this design works around:
  * On desktop LinkedIn drops the circular profile photo over the BOTTOM-LEFT
    corner (roughly x < 260, y > 240), so nothing important goes there.
  * On mobile LinkedIn crops the top and bottom, so all text stays vertically
    centred, well inside y 90-300.
  * The name is already printed under the banner by LinkedIn, so the banner
    leads with the positioning statement instead of repeating it.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1584, 396
OUT = Path(__file__).resolve().parent.parent / "public" / "linkedin-banner.png"

TEAL_DARK = (18, 60, 71)
TEAL = (15, 107, 96)
MINT = (127, 227, 212)
PAPER = (251, 250, 247)
SUB = (198, 232, 228)

FONT_DIR = Path("C:/Windows/Fonts")
SERIF_BOLD = FONT_DIR / "georgiab.ttf"
SANS = FONT_DIR / "segoeui.ttf"
SANS_SEMI = FONT_DIR / "seguisb.ttf"
MONO = FONT_DIR / "consola.ttf"


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    if not path.exists():
        raise SystemExit(f"Missing font: {path}")
    return ImageFont.truetype(str(path), size)


def diagonal_gradient(size, c1, c2):
    w, h = size
    base = Image.new("RGB", (w, h), c1)
    px = base.load()
    for y in range(h):
        for x in range(0, w, 4):
            t = (x / w + y / h) / 2
            px[x, y] = (
                int(c1[0] + (c2[0] - c1[0]) * t),
                int(c1[1] + (c2[1] - c1[1]) * t),
                int(c1[2] + (c2[2] - c1[2]) * t),
            )
    small = base.resize((w // 4, h // 4), Image.LANCZOS)
    return small.resize((w, h), Image.LANCZOS)


img = diagonal_gradient((W, H), TEAL_DARK, TEAL)
d = ImageDraw.Draw(img, "RGBA")

# ---- right-hand data motif: a funnel narrowing into a rising bar group ----
fx = 1180
for i, w_ in enumerate([272, 222, 174, 120]):
    y = 78 + i * 28
    d.rounded_rectangle([fx, y, fx + w_, y + 17], radius=5, fill=(255, 255, 255, 30 + i * 16))

bar_base, bw, gap = 322, 28, 12
for i, h_ in enumerate([32, 50, 70, 94, 122]):
    x = fx + i * (bw + gap)
    d.rounded_rectangle([x, bar_base - h_, x + bw, bar_base], radius=5, fill=(127, 227, 212, 70 + i * 34))

# ---- text block ----
# X starts at 300: LinkedIn's circular profile photo covers roughly x<260, y>240
# on desktop, so the whole block clears it.
X = 300

d.rectangle([X, 92, X + 58, 96], fill=MINT)
d.text((X, 116), "MARKETING INTELLIGENCE ANALYST", font=font(MONO, 21), fill=MINT)

headline = ["I build the data layer", "marketing teams actually run on."]
y = 156
for line in headline:
    d.text((X, y), line, font=font(SERIF_BOLD, 44), fill=PAPER)
    y += 55

d.text((X, 274), "ETL pipelines  ·  Multi-touch attribution  ·  Dashboards leadership decides from",
       font=font(SANS, 19), fill=SUB)

# ---- the destination, as a button-like pill so it reads as "go here" ----
url = "hafsasaleh.tech"
f_url = font(SANS_SEMI, 25)
pad_x, pad_y = 26, 13
tw = d.textlength(url, font=f_url)
px0, py0 = X, 314
px1, py1 = X + tw + pad_x * 2, py0 + 25 + pad_y * 2
d.rounded_rectangle([px0, py0, px1, py1], radius=(py1 - py0) // 2, fill=MINT)
d.text((px0 + pad_x, py0 + pad_y - 2), url, font=f_url, fill=TEAL_DARK)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT.name}  ({OUT.stat().st_size // 1024} KB, {W}x{H})")
