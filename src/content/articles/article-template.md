---
title: "Article template — copy this file to start a new post"
description: "A one-sentence summary. This shows on the articles list and in Google results, so make it specific and under ~155 characters."
pubDate: 2026-01-01
tags: ["python", "machine-learning"]
draft: true
---

<!--
HOW TO WRITE A NEW ARTICLE
1. Copy this file, rename it. The filename becomes the URL:
   my-post.md  ->  hafsasaleh.tech/articles/my-post/
   Use lowercase-hyphenated names. Never rename after publishing (it breaks links).
2. Fill in the frontmatter above.
3. Set draft: false when you're ready to publish.
4. Write below. Everything below the frontmatter is normal Markdown.
-->

Open with the point, not a warm-up. Readers decide in one sentence whether to stay,
and "In today's fast-paced world of data..." loses all of them.

## Headings use two hashes

Regular paragraphs need no markup. **Bold** for emphasis, *italic* sparingly,
and [links look like this](https://example.com).

### Sub-points use three

- Bullet lists work as expected
- Keep items parallel in structure
- Three to five is usually the right number

1. Numbered lists for sequences
2. Where the order genuinely matters

## Code blocks

Fenced blocks get syntax highlighting automatically — just name the language:

```python
import pandas as pd

df = pd.read_csv("data.csv", parse_dates=["timestamp"])
daily = df.set_index("timestamp").resample("D").agg({"revenue": "sum"})
print(daily.head())
```

Inline code like `pd.merge()` uses single backticks.

## Tables

| Model | Precision | Recall | Notes |
|---|---|---|---|
| Logistic regression | 0.71 | 0.64 | Baseline |
| Random forest | 0.79 | 0.72 | Overfits without depth limit |
| XGBoost | 0.83 | 0.81 | Chosen |

## Images

Put image files in `public/images/` and reference them:

```markdown
![Description of the chart for screen readers](/images/my-chart.png)
```

Always write real alt text — it helps accessibility and SEO both.

## Quotes

> Use blockquotes for actual quotations, not for emphasis.

---

## Closing

End with the takeaway, or a question, or what you'd do next. Don't end with
"Thanks for reading!" and nothing else.
