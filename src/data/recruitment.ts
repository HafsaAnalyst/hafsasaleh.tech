// ---------------------------------------------------------------------------
// Recruitment-agency offer. Home and /recruitment-agencies/ both read from here,
// so the FAQ, packages and proof never drift apart between the two pages.
//
// HONESTY RULES — read before editing.
// - There are no recruitment-agency clients yet. No testimonials, logos, client
//   counts or recruitment results anywhere in this file.
// - Every recruitment dashboard or screenshot is labelled "Sample data".
// - The proof figures are real, but come from other pipelines (migration
//   consultancy, manufacturing). Say so wherever they appear.
// - ATS tools are named only as data sources, never as partners or integrations.
// ---------------------------------------------------------------------------

/** Marks anything Hafsa still has to supply. Visible on purpose, so it cannot ship unnoticed. */
export const TBC = '[HAFSA TO CONFIRM]';

// [HAFSA TO CONFIRM demo URL] — set to the recruitment demo once it is live.
// While null, every "sample dashboard" link falls back to the on-page placeholder.
export const DEMO_URL: string | null = null;
export const demoHref = DEMO_URL ?? '/recruitment-agencies/#demo';

export const problems: { thumb: 'sheet' | 'bars' | 'funnel'; t: string; d: string }[] = [
  { thumb: 'sheet', t: 'Monday reports built by hand', d: 'Hours of exports, and nobody fully trusts the result.' },
  { thumb: 'bars', t: "Recruiter performance you can't see", d: 'Billings, activity and pipeline live in different places.' },
  { thumb: 'funnel', t: 'Placements leaking from the pipeline', d: "You don't know if candidates drop at CV sent, interview or offer." },
];

export const builds: { thumb: 'dashboard' | 'report' | 'alert'; t: string; d: string }[] = [
  {
    thumb: 'dashboard',
    t: 'Owner dashboard',
    d: 'Billings, placements, recruiter performance and pipeline conversion (CV sent → interview → offer → placement) in one live view.',
  },
  {
    thumb: 'report',
    t: 'Automated weekly report',
    d: 'Delivered by email or Slack/Teams every Monday morning. No manual exports, no rebuilding numbers in Excel.',
  },
  {
    thumb: 'alert',
    t: 'Pipeline and follow-up automation',
    d: 'Follow-up reminders, "client gone quiet" alerts, timesheet chasers for contract desks, and database clean-up.',
  },
];

export const metrics = [
  { m: 'Billings per recruiter / desk', w: 'Who is profitable' },
  { m: 'CV sent → interview → offer → placement', w: 'Where placements leak' },
  { m: 'Fill rate and time to fill', w: 'Are you winning the jobs you take on' },
  { m: 'Offer acceptance and fall-offs', w: 'Money lost at the last step' },
  { m: 'Revenue by client', w: 'Which clients are worth the effort' },
  { m: 'Contract margin (contract desks)', w: 'Which contractors and clients earn most' },
];

export const steps = [
  { n: 1, t: 'Reporting check', d: '20-minute call on how you report today.' },
  { n: 2, t: 'Data audit', d: "What's in your ATS and spreadsheets, and what can be trusted." },
  { n: 3, t: 'Build', d: 'Dashboard and automations, set up in your own accounts.' },
  { n: 4, t: 'Validate', d: 'Numbers checked against what you already know.' },
  { n: 5, t: 'Hand over', d: 'Weekly report running, plus a short walkthrough for your team.' },
];

// Real, measured results — from a migration consultancy and a manufacturer,
// not from recruitment. The `from` line says so on the card.
export const proof = [
  {
    big: '68% → 82%',
    label: 'Appointment show rate, after fixing how it was measured',
    from: 'Migration consultancy pipeline',
    href: '/projects/show-rate-recovery/',
  },
  {
    big: '1 hr → 14 s',
    label: 'A recurring report, once it was automated',
    from: 'Manufacturing operations reporting',
    href: '/about/',
  },
  {
    big: '77% vs 62%',
    label: 'Lead conversion model accuracy against the baseline',
    from: 'Migration consultancy pipeline',
    href: '/projects/lead-conversion-model/',
  },
];

export const whyMe = [
  { t: 'A statistician first', d: 'BSc Statistics. I check whether a number can be trusted before anyone acts on it.' },
  { t: 'Long people-pipelines', d: 'At an Australian migration consultancy I track people from first enquiry to final outcome: the same shape as CV sent to placement.' },
  { t: 'Counts, not CVs', d: 'I work inside your own accounts with stages, dates and fee values. Candidate documents stay where they are.' },
  { t: 'Builds quickly', d: 'Python, SQL and AI-assisted development, so a working dashboard arrives in days rather than months.' },
];

export const faq = [
  {
    q: 'Do you need access to candidate CVs?',
    a: 'No. Counts, stages, dates and fee values are enough.',
  },
  {
    q: 'Which ATS do you work with?',
    a: 'Any that can export to CSV or has an API. That covers data from tools like JobAdder, Bullhorn, Vincere, Recruit CRM and Loxo, via exports or API.',
  },
  {
    q: 'Where does the dashboard live?',
    a: 'A private link, or inside tools you already use.',
  },
  {
    q: 'What time zones do you cover?',
    a: 'I\'m based in Lahore (UTC+5), which overlaps with the UK afternoon and the Australian morning. US calls are in the evening, by arrangement.',
  },
  {
    q: 'What does it cost?',
    a: 'Fixed packages, priced up front, starting with a free reporting check.',
    href: '/recruitment-agencies/#pricing',
  },
];

export const packages = [
  {
    t: 'Free reporting check',
    price: 'Free',
    note: '20 minutes, no obligation',
    d: 'A short call on how you report today. You leave knowing where your numbers are weakest, whether or not we work together.',
  },
  {
    t: 'Starter dashboard',
    price: TBC,
    note: 'one-off',
    d: 'One live owner dashboard built from your ATS export: billings, placements, recruiter performance and pipeline conversion.',
  },
  {
    t: 'Dashboard + automated weekly report',
    price: TBC,
    note: 'one-off',
    d: 'The owner dashboard, plus a report that lands in your inbox or Slack/Teams every Monday without anyone exporting anything.',
    featured: true,
  },
  {
    t: 'Monthly care',
    price: TBC,
    note: 'per month',
    d: 'Updates, fixes and a monthly insights note on what changed in your numbers and what it means.',
  },
];

export const privacy = [
  { t: 'Works in your accounts', d: 'Everything is built inside tools you own. Nothing is copied to a system of mine.' },
  { t: 'Counts, not CVs', d: 'Stages, dates and fee values only. Candidate documents and personal details are not needed.' },
  { t: 'NDA on request', d: 'Happy to sign yours before you share anything.' },
  { t: 'Data stays in your tools', d: 'When the work ends, the dashboard and the data stay with you.' },
];
