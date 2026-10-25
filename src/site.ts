// ---------------------------------------------------------------------------
// Central config. Everything on the site reads from this one file.
// ---------------------------------------------------------------------------

export const site = {
  name: 'Hafsa Saleh',
  shortName: 'Hafsa Saleh',
  domain: 'hafsasaleh.tech',
  url: 'https://hafsasaleh.tech',

  role: 'Marketing Intelligence Analyst',
  // Shown as pills in the hero — kept short so they read as capabilities,
  // not as a job title. GTM here means Google Tag Manager (measurement),
  // never go-to-market.
  positioning: ['Attribution', 'GTM & GA4 tracking', 'Dashboards', 'Predictive models'],

  // TODO: replace with your real Calendly link once the event type exists.
  booking: 'https://calendly.com/REPLACE-ME',

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
    upwork: 'https://www.upwork.com/freelancers/~01b9511023176f2c8b',
    fiverr: 'https://www.fiverr.com/s/ZoB5Ljm',
    x: '',
    kaggle: '',
    scholar: '',
  },

  location: 'Lahore, Pakistan',
};

// Primary nav is deliberately short — a buyer needs three choices and one CTA.
// The booking button lives in the header, so it is not repeated here.
export const nav = [
  { href: '/projects/', label: 'Work' },
  { href: '/services/', label: 'Services' },
  { href: '/about/', label: 'About' },
];

// Everything else is still a real page, reachable from the footer.
export const moreNav = [
  { href: '/dashboard/', label: 'Live dashboard' },
  { href: '/articles/', label: 'Articles' },
  { href: '/research/', label: 'Research' },
  { href: '/contact/', label: 'Contact' },
];
