// ---------------------------------------------------------------------------
// EDIT ME FIRST. Everything on the site reads from this one file.
// ---------------------------------------------------------------------------

export const site = {
  name: 'Hafsa Saleh',
  // Shown in the browser tab after the page title
  shortName: 'Hafsa Saleh',
  domain: 'hafsasaleh.tech',
  url: 'https://hafsasaleh.tech',

  // One line under your name on the home page
  role: 'Data Scientist & Analytics Professional',

  // 2-3 sentences. This is your positioning statement - the single most
  // important paragraph on the whole site. Say who you help and how.
  tagline:
    'I turn messy, real-world data into decisions people actually act on — building models, dashboards and analyses that move the number that matters.',

  // Used for SEO meta descriptions and social sharing previews
  description:
    'Hafsa Saleh is a data scientist working across machine learning, analytics engineering and data visualisation. Portfolio, research and writing on turning data into decisions.',

  email: 'hello@hafsasaleh.tech',

  // Set to '' to hide a link. Add your real handles here.
  socials: {
    github: 'https://github.com/YOUR-USERNAME',
    linkedin: 'https://www.linkedin.com/in/YOUR-HANDLE',
    x: '',
    kaggle: '',
    scholar: '',
  },

  // Path to your CV in /public. Drop the PDF there and it works.
  cv: '/hafsa-saleh-cv.pdf',

  location: 'Australia',
};

export const nav = [
  { href: '/', label: 'Home' },
  { href: '/about/', label: 'About' },
  { href: '/projects/', label: 'Projects' },
  { href: '/research/', label: 'Research' },
  { href: '/articles/', label: 'Articles' },
  { href: '/contact/', label: 'Contact' },
];
