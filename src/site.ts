// ---------------------------------------------------------------------------
// Central config. Everything on the site reads from this one file.
// ---------------------------------------------------------------------------

export const site = {
  name: 'Hafsa Saleh',
  shortName: 'Hafsa Saleh',
  domain: 'hafsasaleh.tech',
  url: 'https://hafsasaleh.tech',

  role: 'Marketing Intelligence Analyst',

  // Your positioning statement — the most important sentence on the site.
  tagline:
    'I build the data layer marketing teams actually run on — unifying ad platforms, CRM and analytics into one source of truth that leadership uses to decide where the money goes.',

  // Used for SEO meta descriptions and social sharing previews
  description:
    'Hafsa Saleh is a Marketing Intelligence Analyst specialising in ETL pipelines, multi-touch attribution and AI-assisted reporting systems. Portfolio, research and writing on turning marketing data into decisions.',

  // TODO: swap to hello@hafsasaleh.tech once you set up domain email (Zoho is free).
  email: 'hafsa.saleh1821@gmail.com',

  // Phone deliberately omitted — a public number on a personal site attracts spam.
  // People who need it will get it from your CV.

  // Set any of these to '' to hide the link.
  socials: {
    github: 'https://github.com/HafsaAnalyst',
    linkedin: 'https://www.linkedin.com/in/hafsa-saleh-027924216/',
    x: '',
    kaggle: '',
    scholar: '',
  },

  // Drop the PDF into /public with this exact filename.
  cv: '/hafsa-saleh-cv.pdf',

  location: 'Lahore, Pakistan',
};

export const nav = [
  { href: '/', label: 'Home' },
  { href: '/about/', label: 'About' },
  { href: '/projects/', label: 'Projects' },
  { href: '/research/', label: 'Research' },
  { href: '/articles/', label: 'Articles' },
  { href: '/contact/', label: 'Contact' },
];
