// ---------------------------------------------------------------------------
// Publications, papers, theses, posters, preprints.
// Replace the placeholder with your real paper.
// ---------------------------------------------------------------------------

export interface Publication {
  title: string;
  /** e.g. "H. Saleh, A. Other" — put yourself in the list exactly as published */
  authors: string;
  /** Journal, conference, or "Preprint" / "Undergraduate thesis" */
  venue: string;
  year: string;
  /** 2-3 sentences in plain English. Assume the reader is a hiring manager, not a reviewer. */
  abstract: string;
  links?: { label: string; href: string }[];
}

export const publications: Publication[] = [
  {
    title: 'Your Research Paper Title Goes Here',
    authors: 'H. Saleh, Co-Author Name',
    venue: 'Journal or Conference Name',
    year: '2025',
    abstract:
      'Two or three sentences describing what question you asked, what method you used, and what you found. Write it for a smart non-specialist — most people who read this page will be recruiters or collaborators, not reviewers in your subfield.',
    links: [
      { label: 'PDF', href: '/papers/your-paper.pdf' },
      { label: 'DOI', href: '#' },
      { label: 'Code', href: 'https://github.com/YOUR-USERNAME/paper-code' },
    ],
  },
];
