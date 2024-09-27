import { createApp } from 'vue';
import './style.css'
import App from './App.vue';
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';
import router from './router';
import { createPinia } from 'pinia';

const app = createApp(App);

// Configurar Toast
app.use(Toast, {
  transition: "Vue-Toastification__bounce",
  maxToasts: 20,
  newestOnTop: true,
});

app.use(createPinia());
app.use(router);

app.mount('#app');






