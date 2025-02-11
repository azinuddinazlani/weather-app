import { createApp } from 'vue';
import App from './App.vue';
import { createVuetify } from 'vuetify';
import 'vuetify/styles'; // Import Vuetify styles
import { aliases, mdi } from 'vuetify/iconsets/mdi'; // Material Design Icons

const vuetify = createVuetify({
  theme: {
    defaultTheme: 'light', // Set default theme
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
});

const app = createApp(App);

app.use(vuetify);
app.mount('#app');