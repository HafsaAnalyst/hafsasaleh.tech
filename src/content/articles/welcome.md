---
title: "A model nobody deploys is a hobby"
description: "Why I care more about the gap between technically correct and actually used — and what I plan to write about here."
pubDate: 2026-08-20
tags: ["analytics", "attribution", "writing"]
draft: false
---

The most useful thing I've learned in two and a half years of analytics work has
nothing to do with modelling. It's this: the hard part is almost never the analysis.
The hard part is that four systems disagree about what a "lead" is.

At my current role I spent a long stretch building an integration layer across Meta
Ads, GoHighLevel, GA4 and Google Search Console. The statistics in it are not
sophisticated. What made it work was deciding — once, and enforcing it everywhere —
what counted as a lead, when an appointment was real, and which timestamp won when
two platforms disagreed. That's data governance, not data science, and it's the
reason the thing gets opened every morning instead of gathering dust.

## What I write about here

Three things, roughly:

**The unglamorous middle.** Everyone writes about model architectures. Almost nobody
writes about the week you spend discovering that your CRM's "created date" is the
date the record was *imported*, not the date the lead arrived — and that every
attribution number you've reported for a month is quietly wrong because of it.

**Analysis that changes a decision.** A dashboard that nobody acts on is a very
expensive screensaver. I'm interested in what makes the difference: which number goes
at the top, what the default date range is, whether it answers the question the CEO
was actually asking rather than the one they typed.

**Working notes on AI-assisted development.** A meaningful chunk of my recent
integration work was built with Claude Code. That has changed how I work, and not
always in the ways I expected. I'd like to write honestly about where it helps and
where it quietly costs you.

## Where I'm coming from

My background is statistics, not marketing. I published a multiple linear regression
study modelling PM2.5 in Islamabad before I'd ever touched an ad platform, and my
first analyst job was on a factory floor at a textile mill. That turns out to be a
useful sequence: the factory taught me that trust is earned by taking something that
takes an hour and making it take fourteen seconds, and the statistics degree stops me
from being impressed by a chart that goes up.

## Frequency

I'd rather publish something considered once a month than something thin every week.
If that suits you, the [RSS feed](/rss.xml) is the reliable way to follow along.

---

*If something here is useful, wrong, or worth arguing about, [I'd like to hear it](/contact/).*
