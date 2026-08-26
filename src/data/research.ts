// ---------------------------------------------------------------------------
// Publications, papers, theses, posters, preprints.
// ---------------------------------------------------------------------------

export interface Publication {
  title: string;
  authors: string;
  /** Journal, conference, or "Preprint" / "Undergraduate thesis" */
  venue: string;
  year: string;
  /** 2-3 sentences in plain English — most readers here are recruiters, not reviewers. */
  abstract: string;
  links?: { label: string; href: string }[];
}

export const publications: Publication[] = [
  {
    title: 'Multiple Linear Regression Model for Air Quality Prediction in Islamabad',
    // TODO: list co-authors exactly as published, if any.
    authors: 'H. Saleh',
    // TODO: replace with the actual journal name and volume.
    venue: 'Peer-reviewed journal',
    // TODO: confirm the publication year.
    year: '2023',
    abstract:
      'Models PM2.5 concentration in Islamabad as a function of sulphur dioxide, nitrogen dioxide, temperature and humidity using multiple linear regression. The validated model provides a reusable framework for ongoing air-quality monitoring and gives policymakers a quantitative basis for climate and emissions decisions in the region.',
    links: [
      // TODO: add the PDF to /public/papers/ and the real DOI, then uncomment.
      // { label: 'PDF', href: '/papers/air-quality-regression.pdf' },
      // { label: 'DOI', href: 'https://doi.org/...' },
    ],
  },
];
