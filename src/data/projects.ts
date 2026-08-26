// ---------------------------------------------------------------------------
// Flagship projects. `featured: true` pulls a project onto the home page.
// ---------------------------------------------------------------------------

export interface Project {
  title: string;
  /** Where the work was done — shown as context under the title */
  org?: string;
  /** One or two sentences on what it does. Lead with the outcome, not the tooling. */
  summary: string;
  /** The result. A number beats an adjective every time. */
  outcome?: string;
  kind: 'ml' | 'dashboard' | 'analysis' | 'engineering' | 'automation';
  tags: string[];
  year: string;
  featured?: boolean;
  links?: { label: string; href: string }[];
}

export const kindLabel: Record<Project['kind'], string> = {
  ml: 'Predictive Modelling',
  dashboard: 'BI & Dashboards',
  analysis: 'Analysis',
  engineering: 'Data Engineering',
  automation: 'Automation',
};

export const projects: Project[] = [
  {
    title: 'Marketing Intelligence Platform',
    org: 'The Migration',
    summary:
      'Sole architect of a multi-touch attribution platform unifying Meta Ads, GoHighLevel, GA4 and Google Search Console through native API integration — replacing siloed marketing and CRM data with a single Streamlit-based source of truth.',
    outcome:
      '5,200+ leads, 3,300+ appointments and 395 conversions tracked against a USD 10K/month media budget. Drove cost-per-lead to USD 7.45 and cost-per-appointment to USD 11.58. Adopted by the CEO as the primary strategic decision tool.',
    kind: 'engineering',
    tags: ['Python', 'Streamlit', 'Meta Graph API', 'GHL API', 'GA4', 'GSC', 'ETL'],
    year: '2026',
    featured: true,
    // TODO: paste the public Streamlit URL here, or remove this link if it is internal-only.
    links: [{ label: 'Live dashboard', href: '#' }],
  },
  {
    title: 'Counsellor Revenue Performance Dashboard',
    org: 'The Migration',
    summary:
      'Per-agent BI dashboard surfacing individual revenue contribution, nurturing velocity and pipeline-to-close conversion rates for the counsellor team.',
    outcome:
      'Used directly by leadership to run data-driven 1-on-1 performance reviews, replacing subjective assessment with per-agent pipeline evidence.',
    kind: 'dashboard',
    tags: ['Streamlit', 'Python', 'GoHighLevel', 'Revenue Analytics'],
    year: '2026',
    featured: true,
  },
  {
    title: 'Critical Report ETL Pipeline',
    org: 'Sapphire Finishing Mills',
    summary:
      'Automated extraction, transformation and load pipeline replacing a recurring manual reporting workflow that consumed an hour of analyst time per run.',
    outcome:
      'Compressed a 1-hour analysis cycle to 14 seconds — eliminating manual transcription errors and reclaiming 4+ team hours per iteration.',
    kind: 'engineering',
    tags: ['Python', 'Pandas', 'OpenPyXL', 'ETL', 'Process Automation'],
    year: '2024',
    featured: true,
  },
  {
    title: 'Dyeing Process Predictive Automation',
    org: 'Sapphire Finishing Mills',
    summary:
      'Python-based predictive scheduling system for monthly fabric-dyeing operations — integrating multi-source datasets, mapping operation codes and forecasting job completion via Z-test modelling.',
    outcome: 'Delivered a 20% gain in operational planning efficiency.',
    kind: 'ml',
    tags: ['Python', 'Z-test', 'Forecasting', 'SAP/ERP', 'Scheduling'],
    year: '2024',
  },
  {
    title: 'AI-Assisted ClickUp Workflow Automation',
    org: 'The Migration',
    summary:
      'Programmatic synchronisation of quarterly OKRs and daily task execution in ClickUp via custom API integrations, built with Claude Code — closing the loop between analytics outputs and project delivery.',
    outcome:
      'Modernised the Agile project management framework for a 12-person marketing department.',
    kind: 'automation',
    tags: ['ClickUp API', 'Claude Code', 'Python', 'OKR Frameworks', 'Agentic AI'],
    year: '2026',
  },
];
