// ---------------------------------------------------------------------------
// Publications, papers, theses, posters, preprints.
// ---------------------------------------------------------------------------

export interface Publication {
  title: string;
  authors: string;
  venue: string;
  year: string;
  /** 2-3 sentences in plain English — most readers here are recruiters, not reviewers. */
  abstract: string;
  links?: { label: string; href: string }[];
}

export const publications: Publication[] = [
  {
    title: 'Multiple Linear Regression Model for Air Quality Prediction in Islamabad',
    // TODO: add co-authors exactly as they appear on the published paper.
    authors: 'H. Saleh',
    venue: 'Acta Geophysica (Springer)',
    year: '2025',
    abstract:
      'Models PM2.5 concentration in Islamabad as a function of sulphur dioxide, nitrogen dioxide, temperature and humidity using multiple linear regression. The validated model provides a reusable framework for ongoing air-quality monitoring and gives policymakers a quantitative basis for emissions and climate decisions in the region.',
    links: [{ label: 'Read the paper', href: 'https://rdcu.be/eF8VH' }],
  },
];
