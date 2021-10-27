export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "Tickets",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },

  watchers: {
    webpack: {
      poll: true,
    },
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    "bootstrap-vue/nuxt",
    // https://go.nuxtjs.dev/axios
    "@nuxtjs/axios",
    // https://go.nuxtjs.dev/pwa
    "@nuxtjs/pwa",
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    progress: true,
  },

  publicRuntimeConfig: {
    maintainerEmail: process.env.MAINTAINER_EMAIL,
    axios: {
      browserBaseURL: `https://${process.env.DOMAIN}/api/`,
    },
  },

  privateRuntimeConfig: {
    axios: {
      baseURL: 'http://api:8000/api/',
    },
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    meta: {
      name: 'Tickets',
      theme_color: '#FFFFFC',
    },
    manifest: {
      name: 'Tickets',
      short_name: 'Tickets',
      lang: 'en',
    },
  },


  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
};
