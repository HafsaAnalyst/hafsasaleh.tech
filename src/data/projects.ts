// ---------------------------------------------------------------------------
// Project catalog. `href` points at the full case study where one exists.
// `featured: true` pulls a project onto the home page.
// ---------------------------------------------------------------------------

export interface Project {
  title: string;
  org?: string;
  /** One or two sentences. Lead with the outcome, not the tooling. */
  summary: string;
  /** The result. A number beats an adjective every time. */
  outcome?: string;
  kind: 'ml' | 'dashboard' | 'analysis' | 'engineering' | 'automation';
  tags: string[];
  year: string;
  featured?: boolean;
  /** Generated cover art variant, drawn by ProjectCover.astro */
  cover?:
    | 'integration'
    | 'liftbars'
    | 'model'
    | 'pipeline'
    | 'dashboard'
    | 'etl'
    | 'forecast'
    | 'cycle';
  /** Internal case study page */
  href?: string;
  links?: { label: string; href: string }[];
}

export const kindLabel: Record<Project['kind'], string> = {
  ml: 'Predictive Modelling',
  dashboard: 'BI & Dashboards',
  analysis: 'Analysis',
  engineering: 'Data Engineering',
  automation: 'CRM & Automation',
};

export const projects: Project[] = [
  {
    title: 'Marketing Intelligence Platform',
    cover: 'integration',
    org: 'The Migration',
    summary:
      'Sole architect of a multi-touch attribution platform unifying six systems — Meta Ads, GoHighLevel, GA4, Google Search Console, Stripe and Google Sheets — through native API integration. A Streamlit application that replaced siloed marketing, payment and CRM data with one source of truth.',
    outcome:
      '5,200+ leads and a USD 10K/month media budget tracked end to end. CPL USD 7.45, cost-per-appointment USD 11.58. Adopted by the CEO as the primary strategic decision tool.',
    kind: 'engineering',
    tags: ['Python', 'Streamlit', 'Meta Graph API', 'GHL API', 'GA4', 'Stripe API', 'Google Sheets API', 'Prophet', 'ETL'],
    year: '2026',
    featured: true,
    href: '/projects/marketing-intelligence-platform/',
    links: [
      {
        label: 'Live dashboard',
        href: '/dashboard/',
      },
    ],
  },
  {
    title: 'The Half That Never Showed Up',
    cover: 'liftbars',
    org: 'The Migration',
    summary:
      'Nearly a third of booked consultations never happened — and outcome data was too unreliable to see it. I fixed the measurement first, then found the leak and closed it.',
    outcome:
      'Show rate climbed from 68% to 82% — roughly one in five no-shows recovered, from the same bookings and zero extra ad spend.',
    kind: 'analysis',
    tags: ['Funnel Analytics', 'Data Governance', 'GoHighLevel', 'Attribution'],
    year: '2026',
    featured: true,
    href: '/projects/show-rate-recovery/',
  },
  {
    title: 'The Most Valuable Thing Was What I Threw Away',
    cover: 'model',
    org: 'The Migration',
    summary:
      'A lead conversion model that scored a suspicious 100%. I audited it, found the leakage, deleted the data that made it perfect, and rebuilt it honestly.',
    outcome:
      '77% accuracy against a 62% baseline. Top-scoring 20% of leads converted at 84%; referral converted at 90% versus 26% for paid social.',
    kind: 'ml',
    tags: ['Python', 'scikit-learn', 'Feature Leakage', 'Lead Scoring', 'Model Validation'],
    year: '2026',
    featured: true,
    href: '/projects/lead-conversion-model/',
  },
  {
    title: 'GoHighLevel CRM Architecture',
    cover: 'pipeline',
    org: 'The Migration',
    summary:
      'Full CRM build-out — workflows, automations, pipelines, calendars and platform integrations — with data governance protocols that made GoHighLevel the enterprise single source of truth.',
    outcome:
      'Every lead lifecycle stage captured consistently, which is what made attribution and show-rate measurement possible in the first place.',
    kind: 'automation',
    tags: ['GoHighLevel', 'Workflow Automation', 'Pipelines', 'SSOT Design', 'Data Governance'],
    year: '2026',
    href: '/projects/ghl-crm-architecture/',
  },
  {
    title: 'Counsellor Revenue Performance Dashboard',
    cover: 'dashboard',
    org: 'The Migration',
    summary:
      'Per-agent BI dashboard surfacing individual revenue contribution, nurturing velocity and pipeline-to-close conversion rates for the counsellor team.',
    outcome:
      'Used by leadership to run data-driven 1-on-1 performance reviews, replacing subjective assessment with per-agent pipeline evidence.',
    kind: 'dashboard',
    tags: ['Streamlit', 'Python', 'GoHighLevel', 'Revenue Analytics'],
    year: '2026',
  },
  {
    title: 'Critical Report ETL Pipeline',
    cover: 'etl',
    org: 'Sapphire Finishing Mills',
    summary:
      'Automated extraction, transformation and load pipeline replacing a recurring manual reporting workflow that consumed an hour of analyst time per run.',
    outcome:
      'Compressed a 1-hour analysis cycle to 14 seconds — eliminating transcription errors and reclaiming 4+ team hours per iteration.',
    kind: 'engineering',
    tags: ['Python', 'Pandas', 'OpenPyXL', 'ETL', 'Process Automation'],
    year: '2024',
  },
  {
    title: 'Fabric Dispatch On-Time Predictor',
    cover: 'riskbands',
    org: 'Sapphire Finishing Mills',
    summary:
      "Z-test model that reads a fabric's reprocess history to predict how long it will take to reach dispatch. It returns a day range rather than a false-precision single date, and scores every order against its due date as a probability of packing on time — surfaced as a colour-coded metric across the floor.",
    outcome:
      'Production leadership could see at a glance which orders were on track, at risk, or certain to miss — turning scheduling from reactive firefighting into planning. Delivered a 20% gain in operational planning efficiency.',
    kind: 'ml',
    tags: ['Python', 'Z-test', 'Hypothesis Testing', 'Forecasting', 'SAP/ERP', 'Production Planning'],
    year: '2024',
  },
  {
    title: 'Sales Call Conversion Scoring',
    cover: 'waveform',
    org: 'The Migration',
    summary:
      'Machine learning model over historical client call audio from the CRM, predicting which clients are most likely to convert. It rates each conversation and surfaces the patterns that separate a call that closes from one that does not.',
    outcome:
      'Turns a subjective "how did that call go?" into a rated, comparable signal — feeding both lead prioritisation and specific coaching points for the sales team.',
    kind: 'ml',
    tags: ['Python', 'Speech-to-Text', 'NLP', 'Conversation Analytics', 'Lead Scoring', 'GoHighLevel'],
    year: '2026',
  },
  {
    title: 'AI-Assisted ClickUp Workflow Automation',
    cover: 'cycle',
    org: 'The Migration',
    summary:
      'Programmatic synchronisation of quarterly OKRs and daily task execution in ClickUp via custom API integrations, built with Claude Code — closing the loop between analytics outputs and project delivery.',
    outcome: 'Modernised the Agile framework for a 12-person marketing department.',
    kind: 'automation',
    tags: ['ClickUp API', 'Claude Code', 'Python', 'OKR Frameworks', 'Agentic AI'],
    year: '2026',
  },
];
