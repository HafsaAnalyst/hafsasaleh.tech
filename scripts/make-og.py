"""
Generates public/og.png — the 1200x630 preview card shown when the site is shared
on LinkedIn, X, Slack, WhatsApp etc.

Run:  python scripts/make-og.py

Uses Windows system fonts directly rather than relying on fontconfig, so the
output is identical on every run. Re-run it after changing the name or tagline.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
OUT = Path(__file__).resolve().parent.parent / "public" / "og.png"

# Site palette (matches the case-study hero gradient)
TEAL_DARK = (18, 60, 71)
TEAL = (15, 107, 96)
MINT = (127, 227, 212)
PAPER = (251, 250, 247)
MUTED = (143, 201, 195)

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
    """Linear gradient along the diagonal, matching the CSS 135deg hero."""
    w, h = size
    base = Image.new("RGB", (w, h), c1)
    px = base.load()
    for y in range(h):
        for x in range(0, w, 4):  # step 4px, then smooth by resizing
            t = (x / w + y / h) / 2
            px[x, y] = (
                int(c1[0] + (c2[0] - c1[0]) * t),
                int(c1[1] + (c2[1] - c1[1]) * t),
                int(c1[2] + (c2[2] - c1[2]) * t),
            )
    # fill the 4px gaps
    small = base.resize((w // 4, h // 4), Image.LANCZOS)
    return small.resize((w, h), Image.LANCZOS)


img = diagonal_gradient((W, H), TEAL_DARK, TEAL)
d = ImageDraw.Draw(img, "RGBA")

# --- decorative data marks: a rising bar group, bottom right, low contrast ---
# base sits above the footer rule at y=520 so the two never intersect
bar_x, bar_base, bar_w, gap = 812, 496, 34, 14
for i, h_ in enumerate([48, 74, 96, 132, 168, 210]):
    d.rounded_rectangle(
        [bar_x + i * (bar_w + gap), bar_base - h_, bar_x + i * (bar_w + gap) + bar_w, bar_base],
        radius=6,
        fill=(255, 255, 255, 26 + i * 12),
    )

# --- accent rule ---
d.rectangle([80, 118, 80 + 68, 118 + 5], fill=MINT)

# --- eyebrow ---
d.text((80, 156), "MARKETING INTELLIGENCE ANALYST", font=font(MONO, 25), fill=MINT)

# --- name ---
d.text((80, 214), "Hafsa Saleh", font=font(SERIF_BOLD, 104), fill=PAPER)

# --- tagline, manually wrapped to control the break ---
tagline = [
    "I build the data layer marketing teams",
    "actually run on.",
]
y = 356
for line in tagline:
    d.text((80, y), line, font=font(SANS, 39), fill=(211, 236, 234))
    y += 54

# --- footer rule + domain ---
d.rectangle([80, 520, W - 80, 521], fill=(255, 255, 255, 38))
d.text((80, 548), "hafsasaleh.tech", font=font(SANS_SEMI, 32), fill=PAPER)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT}  ({OUT.stat().st_size // 1024} KB, {W}x{H})")
