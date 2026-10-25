"""
Prepares the service screenshots for the public site.

Run:  python scripts/make-work-shots.py

WHY THIS SCRIPT EXISTS
The raw captures are of a live production GoHighLevel account, GA4 property and
GTM container belonging to Hafsa's employer. Several of them contain, in plain
text: the full names of real visa applicants, their appointment times, the
employer's pipeline values and revenue, the GTM container ID and the Google Ads
conversion ID — plus a red "your payment method is missing" billing banner.

None of that belongs on a public marketing page. So every capture is processed
here before it reaches public/: the billing banner is cropped away, and each
region holding a person's name, a client value or an account identifier is
blurred past legibility. Structure, layout and volume all survive, which is what
actually demonstrates the work.

Boxes are (left, top, right, bottom) in the SOURCE image's own pixels.
"""

from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "work-src"
OUT = ROOT / "public" / "work"

# crop_top   : pixels shaved off the top (the billing banner)
# blur       : regions blurred past legibility
# max_width  : downscale target for the web
JOBS = {
    # ---- Streamlit dashboard: Hafsa's own demo app, already public ----
    "ss01-dashboard-executive": dict(crop_top=0, blur=[], max_width=1600),
    "ss02-dashboard-counsellors": dict(crop_top=0, blur=[], max_width=1600),
    "ss03-dashboard-forecast": dict(crop_top=0, blur=[], max_width=1600),

    # ---- Excel template: sample data only, nothing to redact ----
    "ss04-template-dashboard": dict(crop_top=0, blur=[], max_width=1200),
    "ss05-template-data": dict(crop_top=0, blur=[], max_width=1400),

    # ---- GA4: hide the property/account name ----
    "ss06-ga4-debugview": dict(
        crop_top=0,
        blur=[(125, 0, 315, 38)],          # account + property name
        max_width=1600,
    ),

    # ---- GTM: hide the domain, container ID and Ads conversion ID ----
    "ss07-gtm-tags": dict(
        crop_top=0,
        blur=[
            (238, 0, 420, 26),        # "All accounts > <employer> GTM"
            (172, 36, 352, 82),       # container title (the domain)
            (1398, 94, 1522, 132),    # GTM-XXXXXXX
            (278, 684, 486, 716),     # "Google Tag - AW-XXXXXXXXXX"
        ],
        max_width=1600,
    ),

    # ---- GHL pipeline: real applicant names on every card ----
    "ss08-ghl-pipeline": dict(
        crop_top=58,                  # billing banner
        blur=[
            (14, 56, 196, 106),       # sidebar account name + location
            (196, 298, 1902, 324),    # per-stage opportunity values (A$...)
            (196, 328, 1902, 830),    # the cards — every applicant name lives here
        ],
        max_width=1600,
    ),

    # ---- GHL calendar: real appointment titles and staff calendar names ----
    "ss09-ghl-calendar": dict(
        crop_top=72,
        blur=[
            (14, 58, 196, 112),       # sidebar account name
            (448, 336, 842, 772),     # appointment blocks (applicant names)
            (1622, 536, 1913, 706),   # "Calendars" filter list (staff names)
        ],
        max_width=1600,
    ),

    # ---- GHL marketing/integrations: hide the account name ----
    "ss10-ghl-integrations": dict(
        crop_top=58,
        blur=[(14, 56, 198, 108)],
        max_width=1600,
    ),

    # ---- GHL attribution: employer revenue figures ----
    "ss11-ghl-dashboard": dict(
        crop_top=0,
        blur=[
            (952, 258, 1072, 296),    # "Total revenue A$..."
            (1452, 258, 1580, 296),   # "Won revenue A$..."
            (100, 424, 172, 620),     # funnel stage values (A$...)
        ],
        max_width=1600,
    ),
}


def process(name: str, cfg: dict) -> None:
    src = SRC / f"{name}.png"
    if not src.exists():
        raise SystemExit(f"missing source: {src}")

    im = Image.open(src).convert("RGB")

    if cfg["crop_top"]:
        im = im.crop((0, cfg["crop_top"], im.width, im.height))

    for box in cfg["blur"]:
        l, t, r, b = box
        t = max(0, t - cfg["crop_top"])
        b = max(0, b - cfg["crop_top"])
        l, r = max(0, l), min(im.width, r)
        b = min(im.height, b)
        if r <= l or b <= t:
            continue
        region = im.crop((l, t, r, b))
        # Tuned to defeat 12-16px UI text without dissolving the layout.
        # A radius proportional to the region turns big areas into white mush.
        radius = max(6, min(16, min(region.width, region.height) // 6))
        im.paste(region.filter(ImageFilter.GaussianBlur(radius)), (l, t))

    if im.width > cfg["max_width"]:
        h = round(im.height * cfg["max_width"] / im.width)
        im = im.resize((cfg["max_width"], h), Image.LANCZOS)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.jpg"
    im.save(path, "JPEG", quality=82, optimize=True, progressive=True)
    marks = f"{len(cfg['blur'])} blurred" if cfg["blur"] else "no redaction needed"
    print(f"  {path.name:34} {im.width}x{im.height}  {path.stat().st_size // 1024:>4} KB  ({marks})")


if __name__ == "__main__":
    for name, cfg in JOBS.items():
        process(name, cfg)
    print(f"\nwrote {len(JOBS)} images to {OUT}")
