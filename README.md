# hafsasaleh.tech

Personal site: portfolio, research and articles. Built with [Astro](https://astro.build).

---

## Running it locally

```bash
npm run dev      # http://localhost:4321 — live-reloads as you edit
npm run build    # production build into dist/
npm run preview  # preview the production build
```

---

## The five files you'll actually edit

| What you want to change | File |
|---|---|
| Your name, tagline, email, social links, CV path | `src/site.ts` |
| Portfolio projects | `src/data/projects.ts` |
| Papers and publications | `src/data/research.ts` |
| About page — bio, skills, experience, education | `src/pages/about.astro` |
| Articles | `src/content/articles/*.md` |

Start with `src/site.ts`. Everything else reads from it.

---

## Adding an article

1. Copy `src/content/articles/article-template.md`
2. Rename it — **the filename becomes the URL**:
   `feature-engineering.md` → `hafsasaleh.tech/articles/feature-engineering/`
   Use `lowercase-with-hyphens`. Don't rename after publishing — it breaks links.
3. Fill in the frontmatter (`title`, `description`, `pubDate`, `tags`)
4. Set `draft: false`
5. Write in Markdown

It appears on the articles page, the home page and the RSS feed automatically.
Drafts (`draft: true`) are excluded from the build entirely.

**Images:** put them in `public/images/` and reference as `/images/name.png`.

---

## Adding a project

Open `src/data/projects.ts` and add an object to the array:

```ts
{
  title: 'Project Name',
  summary: 'One sentence. Lead with the outcome, not the tooling.',
  outcome: 'The result. A number beats an adjective.',
  kind: 'ml',              // 'ml' | 'dashboard' | 'analysis' | 'engineering'
  tags: ['Python', 'PyTorch'],
  year: '2026',
  featured: true,          // shows on the home page — keep to 3
  links: [{ label: 'GitHub', href: 'https://github.com/...' }],
}
```

---

## Your CV

Drop the PDF into `public/` as `hafsa-saleh-cv.pdf`. The download buttons already
point at it. To use a different filename, update `cv` in `src/site.ts`.

---

## Deploying

Pushing to `main` on GitHub auto-deploys via Vercel. That's the whole workflow:

```bash
git add -A
git commit -m "Add article on feature engineering"
git push
```

Live in about 40 seconds.

---

## Before you go live — checklist

Content is filled in from the CV. These are the gaps only you can close —
search the codebase for `TODO:` to find them all.

- [ ] **GitHub + LinkedIn URLs** in `src/site.ts` (currently placeholders)
- [ ] **Streamlit dashboard URL** in `src/data/projects.ts` — or delete that link if
      the dashboard is internal-only
- [ ] **Journal name, year and DOI** for the air-quality paper in `src/data/research.ts`,
      and drop the PDF into `public/papers/`
- [ ] **`public/hafsa-saleh-cv.pdf`** — the download buttons already point here
- [ ] **`public/og.png`** (1200×630) — the preview image when the site is shared on
      LinkedIn. Without it, shares render blank.
- [ ] Optional: set up `hello@hafsasaleh.tech` (Zoho Mail, free) and swap the email
      in `src/site.ts`
- [ ] Submit the sitemap to [Google Search Console](https://search.google.com/search-console)
