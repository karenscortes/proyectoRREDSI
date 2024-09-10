import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router';

import { createPinia } from 'pinia';

const app = createApp(App);

// Crear la instancia de Pinia
const pinia = createPinia();

// Usar Pinia en la aplicación
app.use(pinia);
app.use(router); // Asegúrate de que esté registrado con la aplicación
app.mount('#app');
