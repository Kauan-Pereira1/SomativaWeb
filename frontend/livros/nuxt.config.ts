// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue',
    '@sidebase/nuxt-auth',
    '@pinia/nuxt'
  ],
  primevue: {
    components: {
      include: ['Button', 'Avatar', 'InputText', 'FloatLabel', 'Menubar', 'DataTable', 'Checkbox', 'Toast', 'ProgressSpinner', 'Message', 'OverlayPanel']
    }
  },
  css: [
    'primeicons/primeicons.css',
    'primevue/resources/themes/aura-light-green/theme.css',
    'primeflex/primeflex.css',
    '~/assets/global.scss',
  ],
  auth: {
    baseURL: 'https://somativaweb-production-ea9f.up.railway.app',
    provider: {
      type: 'local',
      endpoints: {
        signIn: { path: '/token/login', method: 'post' },
        signOut: { path: '/token/logout', method: 'post' },
        getSession: { path: '/categoria-livros', method: 'get' },
      },
      token: { signInResponseTokenPointer: '/auth_token', type: 'Token' },
      pages: { login: '/' }
    }
  }
})