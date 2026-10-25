"""
Generates public/work/ss12-model-scoring.jpg — a sample output screen for the
predictive-model service.

Run:  python scripts/make-model-shot.py

There is no client-facing screenshot for this service, so this is drawn rather
than captured. It is labelled "Sample output" on the image itself and again in
the caption on the page, because a mocked interface must never be mistaken for
a real client's account.

The model metrics shown ARE real and measured — 77% accuracy against a 62%
baseline, top-decile conversion of 89%, top-20% at 84%. Only the client rows
and the at-risk counts are invented, and they use obviously placeholder IDs.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 1000
OUT = Path(__file__).resolve().parent.parent / "public" / "work" / "ss12-model-scoring.jpg"

BG = (247, 248, 250)
CARD = (255, 255, 255)
LINE = (223, 227, 234)
INK = (17, 20, 26)
MUT = (108, 116, 130)
ACC = (11, 110, 130)
GOOD = (16, 150, 105)
WARN = (214, 154, 20)
CRIT = (200, 62, 62)

FD = Path("C:/Windows/Fonts")
BOLD = FD / "seguisb.ttf"
BLACK = FD / "seguibl.ttf"
REG = FD / "segoeui.ttf"


def f(p, s):
    return ImageFont.truetype(str(p), s)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def card(x, y, w, h, r=12):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=CARD, outline=LINE, width=1)


# ---------- header ----------
d.rectangle([0, 0, W, 74], fill=CARD)
d.line([(0, 74), (W, 74)], fill=LINE)
d.text((40, 22), "Lead Conversion Model", font=f(BLACK, 25), fill=INK)
d.text((352, 30), "Scored 2,480 open leads  ·  refreshed nightly", font=f(REG, 16), fill=MUT)
d.rounded_rectangle([W - 210, 22, W - 40, 54], radius=16, fill=(238, 244, 246), outline=LINE)
d.text((W - 194, 30), "Sample output", font=f(BOLD, 15), fill=ACC)

# ---------- KPI row ----------
kpis = [
    ("MODEL ACCURACY", "77%", "vs 62% baseline", GOOD),
    ("TOP DECILE CONVERTS", "89%", "highest-scoring 10%", GOOD),
    ("TOP 20% CONVERTS", "84%", "2.2x the average", GOOD),
    ("LEADS FLAGGED HIGH", "312", "of 2,480 scored", ACC),
    ("LEAKING FEATURES", "0", "audited and removed", ACC),
]
x, y, cw, gap = 40, 106, 292, 12
for label, val, sub, col in kpis:
    card(x, y, cw, 108)
    d.text((x + 18, y + 16), label, font=f(BOLD, 12), fill=MUT)
    d.text((x + 18, y + 36), val, font=f(BLACK, 34), fill=col)
    d.text((x + 18, y + 80), sub, font=f(REG, 14), fill=MUT)
    x += cw + gap

# ---------- decile lift chart ----------
card(40, 240, 900, 340)
d.text((66, 264), "Conversion rate by model score decile", font=f(BOLD, 18), fill=INK)
d.text((66, 292), "Leads ranked by score, split into ten equal groups", font=f(REG, 14), fill=MUT)

deciles = [89, 79, 61, 52, 44, 33, 25, 17, 10, 6]
bx, by, bw, bh, bgap = 78, 546, 74, 190, 12
for i, v in enumerate(deciles):
    hgt = int(bh * v / 100)
    xx = bx + i * (bw + bgap)
    colr = ACC if i < 2 else (176, 190, 205)
    d.rounded_rectangle([xx, by - hgt, xx + bw, by], radius=5, fill=colr)
    d.text((xx + bw // 2 - 14, by - hgt - 22), f"{v}%", font=f(BOLD, 14), fill=INK if i < 2 else MUT)
    d.text((xx + bw // 2 - 8, by + 8), f"D{i + 1}", font=f(REG, 12), fill=MUT)
d.line([(70, by), (924, by)], fill=LINE)

# ---------- risk bands ----------
card(956, 240, 604, 340)
d.text((982, 264), "Where the risk sits", font=f(BOLD, 18), fill=INK)
bands = [
    ("High intent — work first", 312, GOOD, 100),
    ("Worth nurturing", 604, WARN, 62),
    ("Low probability", 1564, CRIT, 34),
]
yy = 316
for name, n, col, pct in bands:
    d.text((982, yy), name, font=f(REG, 15), fill=INK)
    d.text((1470, yy), f"{n:,}", font=f(BOLD, 15), fill=INK)
    d.rounded_rectangle([982, yy + 26, 982 + int(4.9 * pct), yy + 38], radius=6, fill=col)
    d.rounded_rectangle([982 + int(4.9 * pct), yy + 26, 1472, yy + 38], radius=6, fill=(236, 239, 243))
    yy += 74
d.text((982, yy + 6), "Bands are set by score threshold, not by fixed quota,", font=f(REG, 13), fill=MUT)
d.text((982, yy + 26), "so they move with the quality of the intake.", font=f(REG, 13), fill=MUT)

# ---------- scored table ----------
card(40, 604, 1520, 356)
d.text((66, 628), "Highest-scoring open leads", font=f(BOLD, 18), fill=INK)
d.text((66, 656), "What the sales team opens on Monday morning", font=f(REG, 14), fill=MUT)

cols = [(70, "LEAD"), (330, "SOURCE"), (620, "FIRST RESPONSE"), (900, "TOUCHPOINTS"), (1130, "SCORE"), (1330, "BAND")]
d.line([(66, 700), (1534, 700)], fill=LINE)
for cx, label in cols:
    d.text((cx, 710), label, font=f(BOLD, 12), fill=MUT)
d.line([(66, 736), (1534, 736)], fill=LINE)

rows = [
    ("Lead #4821", "Referral", "8 min", "11", "0.94", "High", GOOD),
    ("Lead #4776", "Referral", "14 min", "9", "0.91", "High", GOOD),
    ("Lead #4903", "Organic search", "22 min", "8", "0.88", "High", GOOD),
    ("Lead #4694", "Organic search", "1 hr 05", "7", "0.81", "High", GOOD),
    ("Lead #4855", "Paid social", "36 min", "6", "0.62", "Nurture", WARN),
    ("Lead #4712", "Paid social", "3 hr 40", "4", "0.48", "Nurture", WARN),
]
ry = 752
for lead, src, resp, tp, score, band, col in rows:
    d.text((70, ry), lead, font=f(BOLD, 15), fill=INK)
    d.text((330, ry), src, font=f(REG, 15), fill=MUT)
    d.text((620, ry), resp, font=f(REG, 15), fill=MUT)
    d.text((900, ry), tp, font=f(REG, 15), fill=MUT)
    d.text((1130, ry), score, font=f(BOLD, 15), fill=ACC)
    d.rounded_rectangle([1330, ry - 3, 1330 + (58 if band == "High" else 82), ry + 23], radius=11, fill=col + ())
    d.text((1340, ry + 1), band, font=f(BOLD, 13), fill=(255, 255, 255))
    d.line([(66, ry + 32), (1534, ry + 32)], fill=(240, 242, 246))
    ry += 34

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, "JPEG", quality=88, optimize=True, progressive=True)
print(f"wrote {OUT.name}  ({OUT.stat().st_size // 1024} KB, {W}x{H})")
