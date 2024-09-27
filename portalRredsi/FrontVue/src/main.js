import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';
import router from './router';
import { createPinia } from 'pinia';

const app = createApp(App);

// Configurar Toast
app.use(Toast, {
  transition: "Vue-Toastification__bounce",
  maxToasts: 1,  // Solo permitimos una alerta a la vez
  newestOnTop: true,  // Las nuevas alertas se colocan encima
  filterBeforeCreate: (toast, toasts) => {
    // Comprobar si ya hay una alerta de sesión expirada
    const sessionExpiredToast = toasts.some(t => t.content.includes('Su sesíon ha expirado...'));

    // Si ya hay una alerta de sesión expirada y la nueva no es de ese tipo, descartar la nueva
    if (sessionExpiredToast) {
      if (!toast.content.includes('Su sesíon ha expirado...')) {
        return false; // Descartar la alerta nueva
      }
    } else {
      // Si no hay alerta de sesión expirada, descartar duplicados de otro tipo
      if (toasts.filter(t => t.type === toast.type).length !== 0) {
        return false; // Descartar duplicados
      }
    }

    // Si la nueva alerta es de expiración de sesión, eliminar las demás
    if (toast.content.includes('Su sesíon ha expirado...')) {
      toasts.splice(0, toasts.length); // Limpiar la cola de toasts
    }

    return toast; // Permitir la creación de la nueva alerta
  }
});

app.use(createPinia());
app.use(router);

app.mount('#app');
