// ---------------------------------------------------------------------------
// Central config. Everything on the site reads from this one file.
// ---------------------------------------------------------------------------

export const site = {
  name: 'Hafsa Saleh',
  shortName: 'Hafsa Saleh',
  domain: 'hafsasaleh.tech',
  url: 'https://hafsasaleh.tech',

  role: 'Dashboards & Reporting Automation for Recruitment Agencies',

  // Every "Book a reporting check" button points here.
  // [HAFSA TO CONFIRM: Calendly or Cal.com URL] — swap '/contact/' for the
  // booking link once the event type exists. Until then the contact page
  // carries the booking request form.
  booking: '/contact/',

  // Your positioning statement — the most important sentence on the site.
  tagline:
    'I help recruitment agency owners see which recruiters, clients and candidates turn into placements and fees, with live dashboards and automated reporting built on the data already in their ATS.',

  // Used for SEO meta descriptions and social sharing previews
  description:
    'Live dashboards and automated weekly reports for recruitment agency owners. See billings, recruiter performance and where placements leak, from your ATS data.',

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

  // International format, digits only, for wa.me links.
  whatsapp: '923044762001',

  // Linked from the About page only.
  cv: '/hafsa-saleh-cv.pdf',

  location: 'Lahore, Pakistan',
};

// The booking button lives in the header, so Contact is not repeated here.
// The site serves one niche: recruitment agency owners. Case studies are
// reachable from the proof cards, not from the nav.
export const nav = [
  { href: '/', label: 'Home' },
  { href: '/recruitment-agencies/', label: 'Recruitment Agencies' },
  { href: '/about/', label: 'About' },
];

export const moreNav = [
  { href: '/recruitment-agencies/#pricing', label: 'Packages' },
  { href: '/contact/', label: 'Contact' },
];
