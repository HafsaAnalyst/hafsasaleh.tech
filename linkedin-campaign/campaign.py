"""
20-post LinkedIn campaign selling the Marketing Intelligence Dashboard.

This file is the single source of truth: it holds the copy AND the image specs,
and `build.py` renders both `posts.md` and `images/01..20.png` from it.

Narrative arc, 4 posts per phase:
  1-4   EDUCATE  — teach the gap. No pitch at all.
  5-8   TAILOR   — same gap, in their industry's own words.
  9-12  FOMO     — the people who closed it are already ahead of you.
  13-16 DOLLARS  — what the gap costs, in money, with the arithmetic shown.
  17-20 CLOSE    — what closing it looks like, why trust it, and the ask.

Nothing sells before post 13. That is deliberate: on LinkedIn the audience you
convert in week 4 is the one you taught in week 1.

IMPORTANT — the numbers:
  * Figures attributed to Hafsa's own work are real (68%→82% show rate, 77% vs
    62% model accuracy, 90% vs 26% conversion by channel, $7.45 CPL).
  * Every worked example in the DOLLARS phase is labelled as an illustration and
    uses round, obviously-hypothetical inputs. Never present those as a client
    result — the credibility of the real numbers depends on it.
"""

SITE = "hafsasaleh.tech"

POSTS = [
    # ---------------------------------------------------------------- EDUCATE
    dict(
        n=1, phase="EDUCATE", theme="The gap between the click and the cash",
        hook="Your ad platform knows exactly who clicked.\nIt has no idea who paid you.",
        body="""That gap is where most marketing budgets quietly die.

Here's what each of your tools actually knows:

→ Meta and Google know who clicked.
→ Your website knows who visited.
→ Your CRM knows who enquired.
→ Your calendar knows who showed up.
→ Your bank knows who paid.

Five systems. Five fragments. Not one of them can follow a single person from "saw your ad" all the way to "became a client."

So what gets measured instead? Whatever is easy. Clicks. Impressions. Cost per lead.

But a click doesn't sit in your chair. A lead that never books is worth exactly nothing. And when you optimise for the cheap thing, you get more of the cheap thing.

The businesses that grow profitably aren't spending more than you. They've just connected the click to the cash — so they can see which marketing actually produces revenue, and which only produces activity.""",
        cta="Which of your tools is holding the piece you're missing?",
        tags="#MarketingAnalytics #Attribution #DataDriven #SmallBusinessGrowth",
        img=dict(kind="versus", kicker="THE ATTRIBUTION GAP",
                 left=("KNOWS", "who clicked"), right=("DOESN'T KNOW", "who paid"),
                 foot="Your ad platform"),
    ),
    dict(
        n=2, phase="EDUCATE", theme="Cost per lead is a trap",
        hook="The cheapest leads you buy\nare often the most expensive clients you never get.",
        body="""Cost per lead is the most quoted number in service marketing. It's also the most misleading.

Two channels. Same month.

Channel A: $12 per lead. Looks brilliant.
Channel B: $48 per lead. Looks wasteful.

Then you follow them past the form fill.

Channel A's leads book 8% of the time and half of those don't show.
Channel B's leads book 40% of the time and nearly all show up.

Suddenly Channel A costs you far more per actual paying client than Channel B ever did.

You just spent three months scaling the wrong one — because the only number you could see stopped at the lead.

The number that should run your marketing isn't cost per lead.

It's cost per *client*, by channel.

Almost nobody measures it. Everybody who does spends differently within a month.""",
        cta="Do you know what a paying client costs you, by channel?",
        tags="#CostPerLead #MarketingROI #PaidMedia #Analytics",
        img=dict(kind="versus", kicker="THE SAME MONTH, TWO CHANNELS",
                 left=("$12", "per lead"), right=("$48", "per lead"),
                 foot="One of these is cheaper. The other is profitable."),
    ),
    dict(
        n=3, phase="EDUCATE", theme="Five tools, five answers",
        hook="Ask five of your systems how many leads you got last month.\nYou'll get five different answers.",
        body="""And that's why your Monday meeting is an argument instead of a decision.

It isn't that your tools are broken. It's that each one counts something slightly different.

Your ad platform counts form submissions.
Your website counts sessions.
Your CRM counts contacts — including duplicates and the ones your team typed in manually.
Your calendar counts bookings.
Your payment system counts humans who actually paid you.

All five are "right." None of them agree.

So you sit in a room with five tabs open, and instead of deciding where next month's budget goes, you spend an hour deciding whose number to believe.

Then you decide nothing, and the budget stays exactly where it was — not because it's working, but because nobody could prove it wasn't.

Data paralysis: data-rich, decision-poor.

The fix isn't a sixth dashboard. It's one reconciled number everybody in the room already agreed to trust before the meeting started.""",
        cta="How many tabs are open in your Monday meeting?",
        tags="#DataGovernance #SingleSourceOfTruth #BusinessIntelligence #Reporting",
        img=dict(kind="list", kicker="\"HOW MANY LEADS LAST MONTH?\"",
                 rows=[("Ad platform", "587"), ("Website", "1,204"),
                       ("CRM", "412"), ("Calendar", "208"), ("Payments", "61")],
                 foot="All five are right. None of them agree."),
    ),
    dict(
        n=4, phase="EDUCATE", theme="Churn is invisible",
        hook="Nobody cancels.\nThey just stop coming back.",
        body="""That's what makes client churn so expensive — and so easy to miss.

There's no cancellation email. No angry review. No moment where someone tells you they've gone.

Visits just get further apart. A rebooking gets missed. Spend tapers. And then one day you notice a name you haven't seen in eight months, and it's far too late to do anything about it.

Meanwhile you're spending to acquire a replacement for someone you already had.

Two numbers worth sitting with:

→ It costs roughly 5–7× more to win a new client than to keep an existing one.
→ A repeat client spends more, books more often, and refers more people.

Yet almost every marketing budget I see is ~95% acquisition and ~5% retention.

Here's the part most owners don't realise: the signal is already in your data. How recently someone visited. How often. How much they spend. Whether they've engaged lately.

Those patterns predict who's about to drift — usually weeks before they do.

You're not missing the data. You're just not reading it yet.""",
        cta="When did you last look at who *hasn't* been back?",
        tags="#ClientRetention #ChurnPrediction #CustomerLifetimeValue #DataScience",
        img=dict(kind="statement", kicker="THE QUIET LEAK",
                 lines=["Nobody cancels.", "They just stop", "coming back."],
                 foot="And by the time you notice, it's too late to act."),
    ),

    # ----------------------------------------------------------------- TAILOR
    dict(
        n=5, phase="TAILOR", theme="Law firms",
        hook="For law firms: which of your marketing brings signed cases —\nand which brings free consultations that never sign?",
        body="""Most firms genuinely cannot answer this. Not because they're careless, but because the answer lives in two systems that never speak.

Your ad platform knows the enquiry came from a campaign.
Your practice management system knows the matter was signed.
Nothing connects the two.

So the firm optimises toward "enquiries," and enquiries are exactly what it gets — including a great many people who wanted forty free minutes and were never going to retain anyone.

What changes when you connect them:

→ You see cost per *signed matter* by channel, not cost per enquiry.
→ You find out which campaigns bring the case types you actually want.
→ You stop paying for the ones that fill your calendar and empty your afternoon.

One firm's cheapest enquiry source can be its worst source of signed work. Until the click is joined to the matter, you're funding it blind.

Your intake team already knows which enquiries waste their time. Your marketing budget doesn't — yet.""",
        cta="Lawyers: do you know your cost per *signed* matter by channel?",
        tags="#LegalMarketing #LawFirmGrowth #LegalTech #Attribution",
        img=dict(kind="versus", kicker="FOR LAW FIRMS",
                 left=("ENQUIRIES", "what you measure"),
                 right=("SIGNED CASES", "what pays you"),
                 foot="These two rarely come from the same channel."),
    ),
    dict(
        n=6, phase="TAILOR", theme="Medspas and aesthetic clinics",
        hook="For medspas: a price-shopper and a $6,000 package client\ncost you exactly the same to acquire.",
        body="""The difference is which channel sent them — and almost nobody is measuring that.

Aesthetics marketing has a particular trap. The offers that generate the most enquiries are the discount ones. Cheap leads, high volume, front desk delighted.

Then you look at what those enquiries actually became: consultations that didn't convert, single treatments that never rebooked, and a lot of people asking whether you'll price-match.

Meanwhile a quieter channel brought fewer enquiries — and most of them booked a package and came back.

Connect your ads to your booking system and your payments, and three things surface immediately:

→ Cost per *booked, high-value treatment* by channel
→ Which sources produce rebookers rather than one-timers
→ Which of your offers is quietly training the algorithm to find you price-shoppers

Volume is not the goal. A full calendar of low-value, non-returning clients is a very expensive way to look busy.""",
        cta="Medspa owners: which channel brings your *rebookers*?",
        tags="#MedspaMarketing #AestheticsBusiness #ClinicGrowth #MarketingAnalytics",
        img=dict(kind="versus", kicker="FOR MEDSPAS & CLINICS",
                 left=("PRICE", "shopper"), right=("$6,000", "package client"),
                 foot="Same acquisition cost. Very different channel."),
    ),
    dict(
        n=7, phase="TAILOR", theme="Dental and medical practices",
        hook="For dental and medical practices:\nthe patient overdue for a recall is worth more than your next new patient.",
        body="""And they're dramatically cheaper to bring back.

Most practices run their marketing almost entirely on new patient acquisition. New ads, new offers, new names through the door.

Meanwhile the recall list quietly grows — patients who were due six months ago, then nine, then a year. No one flagged them. No one called. They didn't leave; they drifted.

Every one of those is revenue you already paid to acquire, walking out a door you can't see.

What connecting your systems shows you:

→ Which patients are statistically most likely to lapse next — before they do
→ What a new patient truly costs by channel, once no-shows are counted
→ Where the recall process is leaking, and roughly what that leak is worth

There's a second problem hiding here too. Practices routinely have a no-show rate they can't measure, because appointment outcomes aren't reliably recorded. You can't fix a number you can't see.

Fix the measurement first. The rest follows.""",
        cta="Practice owners: what's your real no-show rate — and can you prove it?",
        tags="#DentalMarketing #MedicalPractice #PatientRetention #HealthcareAnalytics",
        img=dict(kind="stat", kicker="FOR DENTAL & MEDICAL PRACTICES",
                 value="5–7×", label="more expensive to win a new patient\nthan to bring back an existing one",
                 foot="Most budgets are ~95% acquisition."),
    ),
    dict(
        n=8, phase="TAILOR", theme="Real estate teams",
        hook="For real estate teams: you know your listings inside out.\nDo you know your cost per closed transaction, by channel?",
        body="""Real estate has one of the longest gaps between the click and the commission — which is exactly why attribution breaks.

Someone sees a portal listing in March, downloads a guide in April, books an appraisal in June, lists in August and settles in October.

By the time the money arrives, nobody remembers where the lead came from. The CRM has them tagged "website." The ad account claims the conversion. Your agent swears it was a referral.

So the budget goes wherever it went last year.

Joining ad spend to the actual transaction gives you:

→ Cost per *appraisal booked*, and cost per *listing won*, by source
→ Which portals and campaigns produce vendors versus tyre-kickers
→ Which agents convert appraisals best, with evidence rather than impressions

Long sales cycles don't make attribution impossible. They make it more valuable — because with a cycle that long, spending twelve months on the wrong channel is a genuinely expensive mistake.""",
        cta="Agents: can you trace last month's commission back to a campaign?",
        tags="#RealEstateMarketing #PropTech #LeadGeneration #Attribution",
        img=dict(kind="statement", kicker="FOR REAL ESTATE TEAMS",
                 lines=["Click in March.", "Commission in October.", "Nobody remembers why."],
                 foot="Long cycles don't break attribution. They make it worth more."),
    ),

    # ------------------------------------------------------------------- FOMO
    dict(
        n=9, phase="FOMO", theme="Your competitor already knows",
        hook="Somewhere in your market, a competitor already knows\nexactly what a paying client costs them.",
        body="""They're not smarter than you. Most of the time they're not spending more, either.

They just stopped guessing.

They know their cost per booked client by channel. They know which campaign brings work that closes and which brings people who were never going to buy. They know their no-show rate to the decimal, and what it costs them every week.

So when they sit down to allocate next month's budget, it takes ten minutes. Move money here. Cut it there. Done.

You're in the same meeting spreading budget across channels on gut feel, because nobody can prove which one is working.

Over one month, that difference is invisible.

Over a year, it's the whole game. Every dollar they spend is sharper than every dollar you spend — compounding, month after month, while you're still arguing about whose lead number is correct.

The gap between you and them isn't budget.

It's visibility. And it widens every month it stays open.""",
        cta="How long has your budget been sitting where it is out of habit?",
        tags="#CompetitiveAdvantage #MarketingStrategy #DataDriven #GrowthMarketing",
        img=dict(kind="statement", kicker="THE REAL GAP",
                 lines=["It isn't your budget.", "It's your visibility.", "And it widens monthly."],
                 foot=""),
    ),
    dict(
        n=10, phase="FOMO", theme="The algorithm is learning for them",
        hook="Your competitor's ad account is getting smarter every week.\nYours is learning the wrong lesson.",
        body="""This is the part almost nobody thinks about, and it's the most damaging.

Meta and Google optimise toward whatever outcome you feed back to them. If the only signal they ever receive is "someone filled in a form," they get extremely good at finding people who fill in forms and never buy.

The platform isn't failing. It's succeeding at the wrong objective — the one you gave it.

Now picture the competitor who feeds real conversions back: not form fills, but clients who actually paid. Their algorithm starts hunting for people who look like paying clients.

Same platform. Same budget. Completely different instruction.

Every week that runs, their targeting sharpens and yours stays where it is. Six months later they're paying less for better clients, and it looks like magic.

It isn't magic. They just told the machine what "good" means.

You can too — but only once your offline outcomes are connected back to the ad account.""",
        cta="What outcome is your ad account currently optimising toward?",
        tags="#PaidAds #MetaAds #ConversionTracking #PerformanceMarketing",
        img=dict(kind="versus", kicker="WHAT YOU FEED THE ALGORITHM",
                 left=("FORM FILLS", "you get more forms"),
                 right=("PAID CLIENTS", "you get more clients"),
                 foot="Same platform. Same budget. Different instruction."),
    ),
    dict(
        n=11, phase="FOMO", theme="Retention compounds",
        hook="You can out-spend a competitor on ads and still lose —\nif they keep their clients and you don't.",
        body="""Acquisition is linear. Retention compounds. That asymmetry decides who wins a market over five years.

Run it forward.

Two practices. Same market, same ad budget, same number of new clients each month.

One loses 30% of its client base a year and doesn't notice, because nobody's counting. The other spots at-risk clients before they drift and wins a good share of them back.

Year one, they look identical.

Year three, one has a large, loyal base that books repeatedly and refers people — and its acquisition costs have *fallen*, because it needs fewer new clients to grow. The other is running faster every year just to stand still, refilling a bucket with a hole in it.

The second business isn't better at marketing. It's better at noticing.

Retention is the growth nobody sees — right up until it's the reason someone else is winning.""",
        cta="Do you know your annual client retention rate? Actual number.",
        tags="#Retention #CustomerLoyalty #CompoundGrowth #BusinessStrategy",
        img=dict(kind="statement", kicker="THE ASYMMETRY",
                 lines=["Acquisition is linear.", "Retention compounds."],
                 foot="Over five years, that decides the market."),
    ),
    dict(
        n=12, phase="FOMO", theme="Decision speed is the moat",
        hook="In a competitive market, the business that decides fastest usually wins.\nNot the one with the most reports.",
        body="""Speed of decision is an underrated moat, and it's downstream of exactly one thing: whether you trust your numbers.

When a question comes up — should we move budget off this channel? — there are two kinds of business.

The first opens five dashboards, finds three different answers, debates for an hour, and defers the decision to next month's meeting.

The second looks at one reconciled number and decides before lunch.

Both businesses have the same data available. Only one can act on it.

And this compounds in the ugliest way: every week you don't move budget off a losing channel, you keep paying for it. Indecision has a price, it just never appears on an invoice.

The competitor who decided in ten minutes has already redeployed that money and started learning from the result.

You're still deciding whose number to believe.""",
        cta="How long does a budget decision take in your business, honestly?",
        tags="#DecisionMaking #BusinessIntelligence #Leadership #DataStrategy",
        img=dict(kind="versus", kicker="SAME QUESTION, TWO BUSINESSES",
                 left=("1 HOUR", "arguing"), right=("10 MIN", "deciding"),
                 foot="Both had the same data available."),
    ),

    # ---------------------------------------------------------------- DOLLARS
    dict(
        n=13, phase="DOLLARS", theme="What no-shows cost",
        hook="A booking that doesn't show is wasted twice.\nHere's the arithmetic most practices never run.",
        body="""You pay once to win the lead. You pay again with the empty slot your team held open.

Worked example — round numbers, illustrative:

→ 200 consultations booked per month
→ 68% show rate → 64 no-shows
→ 30% of attended consultations convert
→ Average client value $1,500

Those 64 no-shows would have produced roughly 19 clients.
At $1,500 each, that's about **$28,800 of revenue every month** — sitting in bookings you already paid to create.

Now lift the show rate to 82%.

You recover roughly 28 of those appointments a month. About 8 additional clients. Roughly **$12,600 a month**, from the same leads, the same bookings, and zero extra ad spend.

That 68% → 82% isn't hypothetical, by the way. It's a real result — from fixing outcome tracking first so the number could be trusted, then closing the drop-off it exposed.

The leads were never the problem. The leak was.""",
        cta="What's your show rate — and what would 14 points be worth?",
        tags="#RevenueLeakage #NoShows #OperationalEfficiency #MarketingROI",
        img=dict(kind="money", kicker="ILLUSTRATIVE — 200 BOOKINGS/MONTH",
                 value="$12,600", label="recovered per month",
                 foot="Same leads. Same spend. 68% → 82% show rate."),
    ),
    dict(
        n=14, phase="DOLLARS", theme="What the wrong channel costs",
        hook="Scaling your cheapest channel can be the most expensive decision you make all year.",
        body="""Here's the maths that changes budget meetings.

Worked example — illustrative, round numbers:

**Channel A** — $10,000/month
$20 per lead → 500 leads
6% become clients → 30 clients
**Cost per client: $333**

**Channel B** — $10,000/month
$80 per lead → 125 leads
32% become clients → 40 clients
**Cost per client: $250**

Channel A produces four times the leads. Channel B produces more actual clients, for less money each.

If you're judging on cost per lead, you scale A. You'd be wrong by about $83 per client — and every dollar you move into A makes it worse.

Shift that $10,000 from A to B and you gain roughly 10 more clients a month for identical spend.

In my own work, this pattern was stark: referral leads converted at 90%, paid social at 26%. A 3.5× difference in quality that cost-per-lead hides completely.

The cheapest lead and the most profitable client almost never come from the same place.""",
        cta="If you had to name your worst channel right now — could you prove it?",
        tags="#BudgetAllocation #MarketingROI #PaidMedia #Attribution",
        img=dict(kind="versus", kicker="ILLUSTRATIVE — $10,000 EACH",
                 left=("$333", "per client · Channel A"),
                 right=("$250", "per client · Channel B"),
                 foot="Channel A had 4× the leads. And cost more per client."),
    ),
    dict(
        n=15, phase="DOLLARS", theme="What churn costs",
        hook="Losing 5% of your clients a year sounds survivable.\nRun it for three years.",
        body="""Churn is the slowest, quietest, most expensive thing in a service business — because it never shows up as a line item.

Worked example — illustrative:

→ 500 active clients
→ Average annual value $1,200
→ Annual churn 20% → 100 clients lost per year
→ **$120,000 of recurring revenue, gone**

Now the replacement cost. If a new client costs $300 to acquire, replacing those 100 costs **$30,000** — just to stand still.

So a 20% churn rate costs you $150,000 a year in lost revenue and replacement spend combined.

Cut churn from 20% to 14% — entirely achievable when you can see who's drifting before they go — and you keep 30 more clients. That's **$36,000 in retained revenue plus $9,000 in acquisition you didn't have to spend.**

$45,000 a year. No new leads. No bigger budget. Just noticing earlier.

The clients are already yours. You're simply not being told when they're about to stop being yours.""",
        cta="What's your annual churn rate? Most owners guess low.",
        tags="#ChurnRate #CustomerRetention #RecurringRevenue #PredictiveAnalytics",
        img=dict(kind="money", kicker="ILLUSTRATIVE — 500 CLIENTS",
                 value="$150,000", label="annual cost of 20% churn",
                 foot="Lost revenue + replacing what you already had."),
    ),
    dict(
        n=16, phase="DOLLARS", theme="What manual reporting costs",
        hook="Six hours a week pulling numbers into a spreadsheet —\nand you still don't trust the result.",
        body="""The hidden cost of disconnected data isn't only bad decisions. It's the hours spent producing the numbers you then don't believe.

Worked example — illustrative:

→ 6 hours/week compiling reports across tools
→ 52 weeks → 312 hours/year
→ At $40/hour loaded cost → **$12,480 a year**

That's a part-time salary spent on copy-paste.

But the direct cost is the smaller half. The real damage:

→ The report is always days old, so decisions lag reality
→ Manual transcription introduces errors nobody catches
→ Because it's laborious, it gets done less often than it should
→ And because it's error-prone, nobody fully trusts it anyway

You're paying $12,000 a year for a number you hedge on in the meeting.

I once compressed a recurring one-hour reporting job to 14 seconds. The time saved mattered. What mattered more: it started being right every time, so people actually acted on it.

Automation isn't about saving hours. It's about the report being trustworthy enough to use.""",
        cta="How many hours a week does your team spend building reports?",
        tags="#Automation #ETL #Productivity #DataEngineering",
        img=dict(kind="money", kicker="ILLUSTRATIVE — 6 HRS/WEEK",
                 value="$12,480", label="a year, spent on copy-paste",
                 foot="For a number you still hedge on in the meeting."),
    ),

    # ------------------------------------------------------------------ CLOSE
    dict(
        n=17, phase="CLOSE", theme="What closing the gap looks like",
        hook="You don't need another dashboard.\nYou need one number you'd stake a decision on.",
        body="""For four weeks I've been describing the same gap from different angles: the click that never connects to the cash.

Here's what closing it actually looks like.

One connected view across your ad platforms, website analytics, CRM, booking system and payments. Not five tools. One.

**The full journey, end to end** — impression → click → enquiry → booking → showed up → paid, with a conversion rate at every stage, so you can see precisely where people fall out.

**True cost per client, by channel** — not per click, not per lead. What it costs to win someone who actually pays.

**Leak detection** — no-shows, un-followed-up enquiries and wasted spend, surfaced automatically instead of discovered in hindsight.

**Flagged when a number can't be trusted** — if source data is stale or incomplete, you're told, rather than handed a confident figure that's quietly wrong.

**A "so what," not just a "what"** — what changed, and what to do about it.

The meeting stops being about the data and starts being about the business.""",
        cta="See it running: " + SITE + "/dashboard",
        tags="#MarketingIntelligence #Dashboard #BusinessIntelligence #DataDriven",
        img=dict(kind="list", kicker="ONE VIEW, FIVE SYSTEMS",
                 rows=[("Ad platforms", "→"), ("Website analytics", "→"),
                       ("CRM", "→"), ("Booking system", "→"), ("Payments", "one number")],
                 foot=SITE + "/dashboard"),
    ),
    dict(
        n=18, phase="CLOSE", theme="Why trust this one",
        hook="My prediction model once scored 100%.\nI deleted the data that made it perfect.",
        body="""If you're going to let a number drive your budget, you should know the standard behind it.

I built a model to predict which leads would convert. It scored 100% accuracy.

That's not a triumph. It's a symptom. A perfect score almost always means the model has been handed information it wouldn't actually have at the moment of prediction — it's reading the answer off the back of the page.

I audited every feature, found the ones that only get populated *after* a lead converts, and removed them.

The honest model scores 77%, against a 62% baseline. A real, defensible 15-point lift — and one I'd argue for in any room.

I could have shipped the 100%. It would have looked extraordinary in a slide deck for exactly as long as it took someone to rely on it.

Same instinct on a different project: a flattering 86% headline that turned out to be unknowable — the true figure sat somewhere between 56% and 91% because the source data was never completed. I flagged it rather than let a false number reach leadership and poison every report downstream.

A number that's impressive is worthless. A number that's true is something you can spend against.""",
        cta="Would you rather have the impressive number or the true one?",
        tags="#DataIntegrity #MachineLearning #DataScience #Trust",
        img=dict(kind="versus", kicker="THE MODEL I REFUSED TO SHIP",
                 left=("100%", "leaking"), right=("77%", "honest"),
                 foot="Baseline was 62%. Only one of these is real."),
    ),
    dict(
        n=19, phase="CLOSE", theme="Proof",
        hook="68% → 82% show rate.\nSame leads. Same bookings. Zero extra ad spend.",
        body="""Everything I've written this month comes from doing this work. Here's the clearest example.

**The problem.** Nearly a third of booked consultations never happened. Worse — outcomes weren't being recorded consistently, so nobody could even see the true number, let alone why people dropped off.

**What I did.** Fixed the measurement first. Every consultation outcome recorded, so show rate became trustworthy. Only then did I analyse where the drop happened — by channel, and by the gap between booking and appointment.

That pointed at three targeted fixes: automated reminders, an explicit confirmation step, and same-day follow-up on the bookings the data flagged as most likely to slip.

**The result.** Show rate went from 68% to 82%. Roughly one in five no-shows recovered. More consultations attended every week, from the same bookings, with no additional media budget.

That's the leverage of analytics. I didn't spend another rupee on leads. I made the leak visible, then closed it.

Note the order, because it's the part people skip: **make it measurable, then move it.** You cannot fix a number you cannot see.""",
        cta="Full breakdown with the numbers: " + SITE + "/projects",
        tags="#CaseStudy #MarketingAnalytics #RevenueGrowth #Results",
        img=dict(kind="versus", kicker="REAL RESULT", left=("68%", "showed up"),
                 right=("82%", "showed up"),
                 foot="Same leads. Same spend. +14 points."),
    ),
    dict(
        n=20, phase="CLOSE", theme="The ask",
        hook="You don't need more leads.\nYou need to know which of the ones you already pay for turn into money.",
        body="""Four weeks ago I started writing about one gap: your ad platform knows who clicked, and nothing in your business connects that to who paid.

We've covered what it costs — no-shows, the wrong channel scaled, churn you can't see, hours lost to spreadsheets you don't trust. Depending on your size, that's tens of thousands of dollars a year, every year, quietly.

And it's all recoverable without spending a cent more on marketing. The clients are already in your funnel. You just can't see which ones, or where they're falling out.

So here's the offer.

**A free walkthrough.** I'll look at your actual setup — what you're running, what's connected, what isn't — and show you where your specific gap is. You'll leave knowing your biggest leak whether or not you work with me.

If it's useful, we talk about connecting it properly. If not, you've still got the map.

Best fit: law firms, medspas, clinics, dental and medical practices, and real estate teams spending real money on marketing.

Message me, or start here → """ + SITE,
        cta="Book a walkthrough: " + SITE + "/contact",
        tags="#MarketingIntelligence #Consulting #DataDriven #BookACall",
        img=dict(kind="statement", kicker="THE ASK",
                 lines=["You don't need", "more leads."],
                 foot="Free walkthrough → " + SITE + "/contact"),
    ),
]

PHASE_NOTES = {
    "EDUCATE": "Posts 1–4 · Teach the gap. No pitch, no link to the product. "
               "You are buying permission to sell later.",
    "TAILOR":  "Posts 5–8 · The same gap in each industry's own language. "
               "Tag or target the relevant audience on each one.",
    "FOMO":    "Posts 9–12 · Someone in their market already closed this gap. "
               "Urgency by comparison, never by fake deadline.",
    "DOLLARS": "Posts 13–16 · Put a number on the loss and show the arithmetic. "
               "Every example is labelled illustrative — keep it that way.",
    "CLOSE":   "Posts 17–20 · What closing it looks like, why trust it, "
               "proof, and the ask. Only now does the link appear.",
}
