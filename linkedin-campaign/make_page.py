"""
Builds campaign-playbook.html — a browsable version of the campaign with the
image previews embedded, so the whole thing is one shareable file.

Run:  python linkedin-campaign/make_page.py
"""

import base64
import html
import io
import sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from campaign import POSTS, PHASE_NOTES, SITE  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "campaign-playbook.html"
PREVIEW = 460

PHASE_ORDER = ["EDUCATE", "TAILOR", "FOMO", "DOLLARS", "CLOSE"]
PHASE_BLURB = {
    "EDUCATE": "Teach the gap",
    "TAILOR": "Name their industry",
    "FOMO": "Someone already closed it",
    "DOLLARS": "Put a number on it",
    "CLOSE": "Show the fix, make the ask",
}


def preview_uri(n: int) -> str:
    src = HERE / "images" / f"{n:02d}.png"
    im = Image.open(src).convert("RGB").resize((PREVIEW, PREVIEW), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def post_text(p) -> str:
    return f"{p['hook']}\n\n{p['body']}\n\n{p['cta']}\n\n{p['tags']}"


def build() -> str:
    e = html.escape
    parts = [HEAD]

    # ---- nav ----
    nav = "".join(
        f'<a href="#{ph.lower()}" class="chip p{i+1}">'
        f'<span class="chip-n">{i*4+1}–{i*4+4}</span>{ph.title()}</a>'
        for i, ph in enumerate(PHASE_ORDER)
    )
    parts.append(f"""
<header class="masthead">
  <div class="wrap">
    <p class="eyebrow">LinkedIn campaign &middot; {e(SITE)}</p>
    <h1>Click to Cash</h1>
    <p class="deck">Twenty posts that sell the Marketing Intelligence Dashboard by
      teaching one idea first: your ad platform knows who clicked, and nothing in
      your business connects that to who paid.</p>
    <div class="rail">
      <div><b>20</b><span>posts</span></div>
      <div><b>5</b><span>phases</span></div>
      <div><b>4</b><span>weeks at 5&times;/wk</span></div>
      <div><b>13</b><span>first post that sells</span></div>
    </div>
    <nav class="chips">{nav}</nav>
  </div>
</header>

<section class="wrap howto">
  <h2 class="rule">How to run it</h2>
  <div class="cards">
    <div class="card"><h3>Keep the order</h3><p>The arc is the product. Posts&nbsp;1&ndash;12
      never pitch &mdash; they buy the permission that makes posts&nbsp;13&ndash;20 land.
      Shuffling them turns a campaign back into twenty ads.</p></div>
    <div class="card"><h3>Link in the first comment</h3><p>LinkedIn suppresses reach on
      posts containing outbound links. Post the text and image, then drop the URL
      in your own first comment.</p></div>
    <div class="card"><h3>Answer every reply</h3><p>Each post ends on a question on
      purpose. Replies inside the first hour decide how far the post travels &mdash;
      and the replies are where the enquiries actually start.</p></div>
    <div class="card"><h3>Guard the real numbers</h3><p>68&nbsp;&rarr;&nbsp;82%, 77% vs 62%,
      90% vs 26% are yours and true. Every worked example is labelled
      <i>illustrative</i>. Keep that line visible &mdash; it is what makes the real
      figures believable.</p></div>
  </div>
</section>
""")

    # ---- phases ----
    for i, ph in enumerate(PHASE_ORDER):
        cls = f"p{i+1}"
        parts.append(f"""
<section class="phase" id="{ph.lower()}">
  <div class="wrap">
    <div class="phase-head {cls}">
      <span class="phase-num">Phase {i+1}</span>
      <h2>{ph.title()} <span class="phase-sub">&mdash; {e(PHASE_BLURB[ph])}</span></h2>
      <p class="phase-note">{e(PHASE_NOTES[ph])}</p>
    </div>
""")
        for p in (q for q in POSTS if q["phase"] == ph):
            body = e(post_text(p))
            parts.append(f"""
    <article class="post {cls}">
      <figure class="shot">
        <img src="{preview_uri(p['n'])}" alt="Post {p['n']} image: {e(p['theme'])}"
             width="{PREVIEW}" height="{PREVIEW}" loading="lazy" />
        <figcaption>images/{p['n']:02d}.png &middot; 1200&times;1200</figcaption>
      </figure>
      <div class="body">
        <p class="post-n"><span>{p['n']:02d}</span>{e(p['theme'])}</p>
        <pre class="copy" id="c{p['n']}">{body}</pre>
        <button class="btn" data-target="c{p['n']}">Copy post text</button>
      </div>
    </article>
""")
        parts.append("  </div>\n</section>\n")

    parts.append(f"""
<footer class="foot">
  <div class="wrap">
    <p>Source of truth: <code>linkedin-campaign/campaign.py</code>. Edit the copy
      there and re-run <code>build.py</code> to regenerate every image and
      <code>posts.md</code> together.</p>
    <p class="sig">{e(SITE)}</p>
  </div>
</footer>
{SCRIPT}
""")
    return "".join(parts)


HEAD = """<title>Click to Cash</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
<style>
:root{
  --ground:#F6F6FA; --surface:#FFFFFF; --surface-2:#EEEEF6;
  --ink:#14162B; --ink-2:#3B4060; --muted:#6C7194;
  --line:#E2E2EE; --line-2:#D3D3E2;
  --teal:#0C7F72; --gold:#8F6410;
  --p1:#5348CE; --p2:#3F63C9; --p3:#2C7FB4; --p4:#158F87; --p5:#0C7F72;
  --shadow:0 1px 2px rgba(20,22,43,.04), 0 12px 32px -18px rgba(20,22,43,.22);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0C0F1E; --surface:#151930; --surface-2:#1D2238;
    --ink:#ECEEF8; --ink-2:#C2C7DF; --muted:#8C93B5;
    --line:#242942; --line-2:#333A58;
    --teal:#4FD1C0; --gold:#F0C069;
    --p1:#8C84F0; --p2:#6E9AE8; --p3:#4FB6DC; --p4:#3FCBBB; --p5:#4FD1C0;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 12px 32px -18px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  --ground:#0C0F1E; --surface:#151930; --surface-2:#1D2238;
  --ink:#ECEEF8; --ink-2:#C2C7DF; --muted:#8C93B5;
  --line:#242942; --line-2:#333A58;
  --teal:#4FD1C0; --gold:#F0C069;
  --p1:#8C84F0; --p2:#6E9AE8; --p3:#4FB6DC; --p4:#3FCBBB; --p5:#4FD1C0;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 12px 32px -18px rgba(0,0,0,.7);
}

*,*::before,*::after{box-sizing:border-box}
*{margin:0}
body{
  background:var(--ground); color:var(--ink);
  font-family:'Archivo',system-ui,-apple-system,'Segoe UI',sans-serif;
  line-height:1.6; -webkit-font-smoothing:antialiased;
}
img{display:block;max-width:100%;height:auto}
.wrap{width:100%;max-width:70rem;margin-inline:auto;padding-inline:1.5rem}

h1,h2,h3{line-height:1.15;letter-spacing:-.02em;text-wrap:balance;font-weight:600}
h1{font-size:clamp(2.4rem,6vw,3.9rem);letter-spacing:-.035em}
h2{font-size:clamp(1.4rem,3vw,1.85rem)}
h3{font-size:1rem;letter-spacing:-.005em}
.eyebrow{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:.72rem;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}

/* ---------- masthead ---------- */
.masthead{padding-block:clamp(3rem,7vw,4.6rem) 2.4rem;border-bottom:1px solid var(--line);
  background:linear-gradient(180deg,var(--surface-2),var(--ground))}
.masthead h1{margin-top:.9rem}
.deck{font-family:'Newsreader',ui-serif,Georgia,serif;font-size:clamp(1.05rem,2vw,1.28rem);
  color:var(--ink-2);max-width:46ch;margin-top:1.1rem;line-height:1.5}
.rail{display:flex;flex-wrap:wrap;gap:2.4rem;margin-top:2.2rem}
.rail div{display:flex;flex-direction:column}
.rail b{font-size:1.9rem;font-weight:600;letter-spacing:-.03em;color:var(--teal);
  font-variant-numeric:tabular-nums;line-height:1}
.rail span{font-size:.78rem;color:var(--muted);margin-top:.3rem}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:2.2rem}
.chip{display:inline-flex;align-items:center;gap:.5rem;text-decoration:none;
  font-size:.86rem;color:var(--ink-2);background:var(--surface);
  border:1px solid var(--line);border-radius:999px;padding:.4rem .95rem .4rem .5rem;
  transition:border-color .15s,color .15s}
.chip:hover{border-color:currentColor}
.chip-n{font-family:'JetBrains Mono',monospace;font-size:.68rem;
  background:var(--surface-2);border-radius:999px;padding:.16rem .5rem;color:var(--muted)}
.chip.p1{color:var(--p1)} .chip.p2{color:var(--p2)} .chip.p3{color:var(--p3)}
.chip.p4{color:var(--p4)} .chip.p5{color:var(--p5)}

/* ---------- how to ---------- */
.howto{padding-block:3rem 1rem}
.rule{padding-bottom:.7rem;border-bottom:1px solid var(--line)}
.cards{display:grid;gap:1rem;margin-top:1.5rem;
  grid-template-columns:repeat(auto-fit,minmax(min(100%,15rem),1fr))}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:1.2rem}
.card p{font-size:.9rem;color:var(--ink-2);margin-top:.45rem}

/* ---------- phases ---------- */
.phase{padding-block:2.6rem}
.phase-head{padding-left:1.1rem;border-left:3px solid;margin-bottom:2rem}
.phase-head.p1{border-color:var(--p1)} .phase-head.p2{border-color:var(--p2)}
.phase-head.p3{border-color:var(--p3)} .phase-head.p4{border-color:var(--p4)}
.phase-head.p5{border-color:var(--p5)}
.phase-num{font-family:'JetBrains Mono',monospace;font-size:.7rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted)}
.phase-head h2{margin-top:.3rem}
.phase-sub{font-family:'Newsreader',ui-serif,Georgia,serif;font-style:italic;
  font-weight:400;color:var(--muted);letter-spacing:0}
.phase-note{font-family:'Newsreader',ui-serif,Georgia,serif;font-size:1.02rem;
  color:var(--ink-2);margin-top:.6rem;max-width:60ch}

/* ---------- post ---------- */
.post{display:grid;grid-template-columns:15rem 1fr;gap:1.6rem;align-items:start;
  background:var(--surface);border:1px solid var(--line);border-radius:14px;
  padding:1.4rem;margin-bottom:1.1rem;box-shadow:var(--shadow)}
.shot img{border-radius:9px;border:1px solid var(--line-2)}
.shot figcaption{font-family:'JetBrains Mono',monospace;font-size:.68rem;
  color:var(--muted);margin-top:.5rem;text-align:center}
.post-n{display:flex;align-items:baseline;gap:.7rem;font-weight:600;font-size:1.06rem;
  letter-spacing:-.01em;margin-bottom:.85rem}
.post-n span{font-family:'JetBrains Mono',monospace;font-size:.8rem;font-weight:500;
  color:var(--surface);border-radius:6px;padding:.16rem .45rem;flex:none}
.post.p1 .post-n span{background:var(--p1)} .post.p2 .post-n span{background:var(--p2)}
.post.p3 .post-n span{background:var(--p3)} .post.p4 .post-n span{background:var(--p4)}
.post.p5 .post-n span{background:var(--p5)}
.copy{background:var(--surface-2);border:1px solid var(--line);border-radius:10px;
  padding:1rem 1.1rem;font-family:'Archivo',system-ui,sans-serif;font-size:.88rem;
  line-height:1.62;color:var(--ink-2);white-space:pre-wrap;overflow-wrap:anywhere;
  max-height:19rem;overflow-y:auto}
.btn{margin-top:.8rem;font:inherit;font-size:.82rem;font-weight:500;cursor:pointer;
  background:var(--surface);color:var(--ink);border:1px solid var(--line-2);
  border-radius:8px;padding:.45rem 1rem;transition:border-color .15s,color .15s}
.btn:hover{border-color:var(--teal);color:var(--teal)}
.btn[data-done="1"]{border-color:var(--teal);color:var(--teal)}
:focus-visible{outline:2px solid var(--teal);outline-offset:3px;border-radius:4px}

/* ---------- foot ---------- */
.foot{border-top:1px solid var(--line);padding-block:2.4rem;margin-top:2rem;
  font-size:.88rem;color:var(--muted)}
.foot code{font-family:'JetBrains Mono',monospace;font-size:.82em;
  background:var(--surface-2);padding:.1em .4em;border-radius:4px}
.sig{margin-top:.8rem;color:var(--teal);font-weight:600}

@media (max-width:46rem){
  .post{grid-template-columns:1fr}
  .shot{max-width:17rem;margin-inline:auto}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
html{scroll-behavior:smooth}
</style>
"""

SCRIPT = """
<script>
document.querySelectorAll('.btn').forEach(function (b) {
  b.addEventListener('click', function () {
    var el = document.getElementById(b.dataset.target);
    if (!el) return;
    var done = function () {
      b.textContent = 'Copied';
      b.dataset.done = '1';
      setTimeout(function () { b.textContent = 'Copy post text'; b.dataset.done = ''; }, 1800);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(el.textContent).then(done, fallback);
    } else { fallback(); }
    function fallback() {
      var r = document.createRange(); r.selectNodeContents(el);
      var s = getSelection(); s.removeAllRanges(); s.addRange(r);
      try { document.execCommand('copy'); done(); }
      catch (e) { b.textContent = 'Select and copy manually'; }
    }
  });
});
</script>
"""

if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT.name}  ({OUT.stat().st_size // 1024} KB)")
