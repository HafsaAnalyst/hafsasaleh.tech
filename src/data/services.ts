// ---------------------------------------------------------------------------
// Services and pricing.
//
// HOW THESE PRICES WERE SET — read before changing them.
// Everything is anchored to a base rate of USD 35/hour, which sits mid-range for
// an analyst with your experience selling to US/UK/AU clients on Upwork. Each
// "from" price is roughly (realistic hours x 35), rounded to a clean number:
//
//   Dashboard setup    ~17h  ->  $600
//   Predictive model   ~21h  ->  $750
//   GoHighLevel build  ~24h  ->  $850
//   Reporting system   ~51h  -> $1,800   (a four-week build)
//   Excel template      n/a  ->    $39   (digital product, market is $29-79)
//
// They hang together because they share one rate — so if you raise the rate,
// raise them all proportionally rather than editing one in isolation.
//
// These are STARTING prices. Everything real gets quoted after a call.
// ---------------------------------------------------------------------------

export const HOURLY = 35;

export interface Service {
  id: string;
  /** Short label above the title */
  kind: string;
  title: string;
  /** The hook — one sentence, in the client's words */
  summary: string;
  /** Headline price, already formatted */
  price: string;
  /** e.g. 'one-off', 'per month' */
  priceNote: string;
  /** Optional second price line, e.g. a trial or an add-on */
  altPrice?: string;
  /** Realistic delivery window */
  turnaround: string;
  /** What the buyer actually receives */
  includes: string[];
  /** Who this is for */
  bestFor: string;
  /** Pull one to the front of the page */
  featured?: boolean;
  cta: string;
}

export const services: Service[] = [
  {
    id: 'intelligence-dashboard',
    kind: 'Flagship',
    title: 'Plug-and-Play Intelligence Dashboard',
    summary:
      'The live dashboard from my portfolio, connected to your own platforms. Ads, CRM, analytics and payments in one view — so you can finally see cost per paying client by channel, not just cost per lead.',
    price: 'Free',
    priceNote: 'first month, no card',
    altPrice: 'From $600 to connect and customise your platforms',
    turnaround: '5–10 days after access',
    includes: [
      'A full month on the working dashboard before you pay anything',
      'Your platforms connected — Meta, Google, GA4, Search Console, your CRM',
      'End-to-end funnel: impression → click → enquiry → booking → showed → paid',
      'True cost per client by channel, plus leak detection on no-shows and dead leads',
      'Metric definitions agreed once and enforced, so numbers stop disagreeing',
      'Handover session, and it stays yours',
    ],
    bestFor: 'Service businesses spending real money on marketing across more than two platforms.',
    featured: true,
    cta: 'Start the free month',
  },
  {
    id: 'reporting-template',
    kind: 'Digital product',
    title: 'Client Reporting Dashboard Template',
    summary:
      'Turn the monthly client report from a half-day rebuild into a five-minute job. Paste your numbers into one tab; a branded, client-ready dashboard updates itself.',
    price: '$39',
    priceNote: 'one-off, instant download',
    altPrice: '$180 for a branded build in your colours, set up for your channels',
    turnaround: 'Instant · 3 days for the branded build',
    includes: [
      'Three tabs: Start Here, Data, Dashboard — nothing else to learn',
      'Headline KPIs: ROAS, CPL, CAC, lead-to-customer %, conversion rate',
      'Performance-by-channel table and a monthly trend, charted automatically',
      'Client name flows into the report title for you',
      'Metric glossary written in plain English, for you and your client',
      'Excel file that works in Google Sheets · setup guide included',
      'Licence: unlimited clients, unlimited reports. One user, no resale.',
    ],
    bestFor: 'Agencies, freelancers and in-house marketers who report to clients or leadership.',
    cta: 'Get the template',
  },
  {
    id: 'predictive-model',
    kind: 'Machine learning',
    title: 'Predictive Model — Churn or Lead Scoring',
    summary:
      'A Random Forest model that ranks every client or lead by risk of lapsing, or likelihood of converting. Built honestly, audited for leakage, and delivered with the reasons behind the score.',
    price: 'From $750',
    priceNote: 'one-off',
    turnaround: '2–3 weeks',
    includes: [
      'Feature engineering from the behaviour you already collect',
      'Leakage audit — every feature checked for whether you would actually have it at scoring time',
      'Honest accuracy reported against a baseline, never a flattering number',
      'A ranked at-risk or high-intent list your team can work from Monday',
      'The drivers behind the score, so you can fix causes rather than chase symptoms',
      'Written handover: what it does, what it cannot do yet, and why',
    ],
    bestFor: 'Businesses with 12+ months of client history that repeat-buy or run a sales pipeline.',
    cta: 'Discuss a model',
  },
  {
    id: 'ghl-build',
    kind: 'CRM architecture',
    title: 'Full GoHighLevel Build',
    summary:
      'Workflows, pipelines, calendars and integrations built properly the first time — with the data governance that makes every downstream number trustworthy.',
    price: 'From $850',
    priceNote: 'one-off',
    turnaround: '2–3 weeks',
    includes: [
      'Custom field schema normalised, so a "lead" means one thing everywhere',
      'One canonical pipeline with stages that cannot be skipped',
      'Lifecycle automations: intake, routing, nurture, reminders, outcome capture',
      'Calendars wired to the right teams and locations',
      'Platform integrations so leads arrive already attributed to their source',
      'Governance rules documented, so it stays clean after I leave',
    ],
    bestFor: 'Teams on GoHighLevel whose reporting cannot be trusted because the CRM was never structured.',
    cta: 'Scope a build',
  },
  {
    id: 'automated-reporting',
    kind: 'Done-for-you system',
    title: 'Automated Reporting System',
    summary:
      'One month of work and reporting stops being someone\'s job. A self-running system that pulls, reconciles and delivers your numbers on schedule — needing only occasional attention afterwards.',
    price: 'From $1,800',
    priceNote: 'four-week build',
    altPrice: 'Optional $150/month if you would rather I keep running it',
    turnaround: '4 weeks',
    includes: [
      'Every source connected and pulled on a schedule — no more manual exports',
      'Reconciliation layer so your systems stop returning different answers',
      'Reports delivered automatically to inbox or Slack, on your cadence',
      'Reliability flags: when source data is stale or incomplete, you are told',
      'Full documentation and a walkthrough, so your team can run it',
      'Two weeks of post-launch support included',
    ],
    bestFor: 'Teams losing 5+ hours a week to manual reporting they still do not fully trust.',
    cta: 'Book a scoping call',
  },
];
