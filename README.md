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

- [ ] Fill in `src/site.ts` (especially GitHub + LinkedIn URLs)
- [ ] Replace the three placeholder projects with real ones
- [ ] Replace the placeholder publication in `src/data/research.ts`
- [ ] Write the About page bio and update skills/experience/education
- [ ] Add `public/hafsa-saleh-cv.pdf`
- [ ] Add `public/og.png` (1200×630) — the image shown when the site is shared on
      LinkedIn/X. Without it, shares look blank.
- [ ] Delete or rewrite `src/content/articles/welcome.md`
- [ ] Submit the sitemap to [Google Search Console](https://search.google.com/search-console)
