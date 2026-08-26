"""
Renders the campaign: 20 square post images + a copy-paste-ready posts.md.

Run:  python linkedin-campaign/build.py

Images are 1200x1200 (LinkedIn's best-performing feed ratio — a square eats more
vertical space in the scroll than 1.91:1). Same mesh-gradient brand as the site
and the LinkedIn banner, so the campaign, the profile and the website all read as
one identity.

Five card types give the grid visual variety without breaking the system:
  stat      one big figure
  versus    two figures either side of an arrow
  statement a short serif declaration
  list      a small table of rows
  money     a dollar figure, with the warm accent
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from campaign import POSTS, PHASE_NOTES, SITE  # noqa: E402

HERE = Path(__file__).resolve().parent
IMG_DIR = HERE / "images"
S = 1200

BASE = (11, 18, 48)
BLOBS = [
    (940,  120, 520, 430, (16, 185, 165), 210),
    (1140, 980, 420, 360, (45, 212, 191), 140),
    (200,  980, 560, 420, (79, 70, 215), 180),
    (560, -120, 480, 300, (150, 52, 140), 100),
]

MINT = (150, 240, 226)
GOLD = (250, 204, 112)
PAPER = (255, 255, 255)
SUB = (200, 222, 232)
DIM = (150, 175, 195)
INK = (9, 26, 46)

FD = Path("C:/Windows/Fonts")
SERIF = FD / "georgiab.ttf"
SANS = FD / "segoeui.ttf"
SEMI = FD / "seguisb.ttf"
MONO = FD / "consola.ttf"


def f(path, size):
    return ImageFont.truetype(str(path), size)


def background():
    img = Image.new("RGB", (S, S), BASE)
    for cx, cy, rx, ry, colour, strength in BLOBS:
        m = Image.new("L", (S, S), 0)
        ImageDraw.Draw(m).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=strength)
        m = m.filter(ImageFilter.GaussianBlur(150))
        img.paste(Image.new("RGB", (S, S), colour), (0, 0), m)

    scrim = Image.new("L", (S, S), 0)
    ImageDraw.Draw(scrim).ellipse([60, 200, 1140, 1000], fill=70)
    scrim = scrim.filter(ImageFilter.GaussianBlur(130))
    img.paste(Image.new("RGB", (S, S), (7, 14, 36)), (0, 0), scrim)
    return img


def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = f"{cur} {w}".strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(d, texts, path, start, max_w, floor=34):
    """Largest size at or below `start` where every text fits inside max_w."""
    size = start
    while size > floor and max(d.textlength(t, font=f(path, size)) for t in texts) > max_w:
        size -= 2
    return f(path, size)


def centre(d, text, font, y, fill):
    d.text(((S - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def card(spec, n):
    img = background()
    d = ImageDraw.Draw(img, "RGBA")
    kind = spec["kind"]

    # ---- kicker, top ----
    d.rectangle([S // 2 - 34, 132, S // 2 + 34, 137], fill=GOLD)
    for i, line in enumerate(wrap(d, spec.get("kicker", ""), f(MONO, 24), 940)):
        centre(d, line, f(MONO, 24), 166 + i * 32, MINT)

    if kind == "stat":
        centre(d, spec["value"], f(SERIF, 200), 420, PAPER)
        y = 700
        for line in spec["label"].split("\n"):
            centre(d, line, f(SANS, 38), y, SUB)
            y += 52

    elif kind == "money":
        centre(d, spec["value"], f(SERIF, 150), 450, GOLD)
        y = 660
        for line in wrap(d, spec["label"], f(SANS, 42), 960):
            centre(d, line, f(SANS, 42), y, SUB)
            y += 56

    elif kind == "versus":
        lv, ll = spec["left"]
        rv, rl = spec["right"]
        lx, rx = 330, 870
        # each value is centred at x=330 / x=870; cap the width so it never
        # reaches the arrow sitting at x=600
        fv = fit(d, [lv, rv], SERIF, 92, 400)
        for x, v, l, col in ((lx, lv, ll, DIM), (rx, rv, rl, MINT)):
            w = d.textlength(v, font=fv)
            d.text((x - w / 2, 470), v, font=fv, fill=col)
            for i, line in enumerate(wrap(d, l, f(SANS, 30), 420)):
                lw = d.textlength(line, font=f(SANS, 30))
                d.text((x - lw / 2, 600 + i * 40), line, font=f(SANS, 30), fill=SUB)
        centre(d, "\u2192", f(SANS, 76), 480, GOLD)

    elif kind == "statement":
        fs = fit(d, spec["lines"], SERIF, 84, 1040)
        step = int(fs.size * 1.29)
        y = 600 - (len(spec["lines"]) * step) // 2
        for line in spec["lines"]:
            centre(d, line, fs, y, PAPER)
            y += step

    elif kind == "list":
        y = 400
        for label, value in spec["rows"]:
            d.text((250, y), label, font=f(SANS, 40), fill=SUB)
            vw = d.textlength(value, font=f(SEMI, 40))
            d.text((950 - vw, y), value, font=f(SEMI, 40), fill=MINT)
            d.line([(250, y + 62), (950, y + 62)], fill=(255, 255, 255, 34), width=1)
            y += 92

    # ---- foot ----
    if spec.get("foot"):
        for i, line in enumerate(wrap(d, spec["foot"], f(SANS, 30), 900)):
            centre(d, line, f(SANS, 30), 940 + i * 42, DIM)

    # ---- signature ----
    d.line([(250, 1090), (950, 1090)], fill=(255, 255, 255, 40), width=1)
    centre(d, SITE, f(SEMI, 32), 1112, MINT)

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    out = IMG_DIR / f"{n:02d}.png"
    img.save(out, "PNG", optimize=True)
    return out


def posts_md():
    lines = [
        "# LinkedIn campaign — 20 posts",
        "",
        f"Selling the Marketing Intelligence Dashboard. Images in `images/`, "
        f"copy below. Site: {SITE}",
        "",
        "**Suggested cadence:** one post every weekday for four weeks, or "
        "3×/week over seven weeks. Keep the phase order — it is the whole point.",
        "",
        "**Before you post:** LinkedIn strips formatting, so the copy below is "
        "already plain text. Paste it as-is, attach the matching image, and put "
        "any link in the FIRST COMMENT rather than the post body — LinkedIn "
        "suppresses reach on posts with outbound links.",
        "",
        "---",
        "",
    ]
    phase = None
    for p in POSTS:
        if p["phase"] != phase:
            phase = p["phase"]
            lines += [f"## {phase}", "", f"*{PHASE_NOTES[phase]}*", "", "---", ""]
        lines += [
            f"### {p['n']:02d}. {p['theme']}",
            "",
            f"**Image:** `images/{p['n']:02d}.png`",
            "",
            "```text",
            p["hook"],
            "",
            p["body"],
            "",
            p["cta"],
            "",
            p["tags"],
            "```",
            "",
            "---",
            "",
        ]
    (HERE / "posts.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    for p in POSTS:
        out = card(p["img"], p["n"])
        print(f"  {p['n']:02d} {p['phase']:<8} {p['img']['kind']:<9} "
              f"{out.stat().st_size // 1024:>4} KB  {p['theme']}")
    posts_md()
    print(f"\n{len(POSTS)} images -> {IMG_DIR}")
    print(f"copy -> {HERE / 'posts.md'}")
