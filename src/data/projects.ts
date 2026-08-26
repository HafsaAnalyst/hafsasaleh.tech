// ---------------------------------------------------------------------------
// Your portfolio. Replace these three placeholders with your real work.
// Add as many as you like — the grid handles any number.
//
// `kind` controls the little label on the card: 'ml' | 'dashboard' | 'analysis' | 'engineering'
// `featured: true` pulls a project onto the home page (keep it to 3).
// ---------------------------------------------------------------------------

export interface Project {
  title: string;
  /** One sentence on what it does. Lead with the outcome, not the tooling. */
  summary: string;
  /** The result. A number beats an adjective every time. */
  outcome?: string;
  kind: 'ml' | 'dashboard' | 'analysis' | 'engineering';
  tags: string[];
  year: string;
  featured?: boolean;
  links?: { label: string; href: string }[];
}

export const kindLabel: Record<Project['kind'], string> = {
  ml: 'Machine Learning',
  dashboard: 'Dashboard',
  analysis: 'Analysis',
  engineering: 'Data Engineering',
};

export const projects: Project[] = [
  {
    title: 'Customer Churn Prediction Model',
    summary:
      'Gradient-boosted classifier that flags at-risk subscription customers 30 days before they lapse, with SHAP explanations so the retention team knows why.',
    outcome: 'Recall of 0.81 on held-out data; surfaced 3 churn drivers the business had not tracked.',
    kind: 'ml',
    tags: ['Python', 'scikit-learn', 'XGBoost', 'SHAP'],
    year: '2025',
    featured: true,
    links: [
      { label: 'GitHub repo', href: 'https://github.com/YOUR-USERNAME/churn-model' },
      { label: 'Write-up', href: '/articles/' },
    ],
  },
  {
    title: 'Sales Performance Dashboard',
    summary:
      'End-to-end Power BI dashboard over a modelled star schema, replacing a weekly manual spreadsheet process for a 40-person sales org.',
    outcome: 'Cut reporting turnaround from 2 days to near real-time.',
    kind: 'dashboard',
    tags: ['Power BI', 'DAX', 'SQL', 'Data modelling'],
    year: '2025',
    featured: true,
    links: [{ label: 'Live dashboard', href: '#' }],
  },
  {
    title: 'Exploratory Analysis of Urban Mobility Data',
    summary:
      'Geospatial analysis of two years of public transit records to identify underserved corridors and peak-load bottlenecks.',
    outcome: 'Identified 6 corridors where demand outstripped scheduled capacity.',
    kind: 'analysis',
    tags: ['pandas', 'GeoPandas', 'Plotly', 'Jupyter'],
    year: '2024',
    featured: true,
    links: [{ label: 'Notebook', href: 'https://github.com/YOUR-USERNAME/urban-mobility' }],
  },
];
