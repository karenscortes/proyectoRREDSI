import axios from 'axios';
import { useAuthStore } from '@/store';
import router from '@/router';
import { useSpinnerStore } from '@/store/spinner';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_API,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
});

api.interceptors.request.use(config => {
    const authStore = useAuthStore();

    const spinnerStore = useSpinnerStore(); // Obtener el store del spinner
    spinnerStore.showSpinner();

    const token = authStore.accessToken;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  }, error => {
    return Promise.reject(error);
  });


api.interceptors.response.use(response => {
  const spinnerStore = useSpinnerStore(); // Obtener el store del spinner
  spinnerStore.hideSpinner(); // Ocultar el spinner al recibir la respuesta

  return response;
}, error => {
  if (error.response && error.response.status === 401 && error.response.data.detail === 'Invalid token') {
    const spinnerStore = useSpinnerStore(); // Obtener el store del spinner
    spinnerStore.hideSpinner();

    const authStore = useAuthStore();
    authStore.logout();

    router.push('/'); 
  }
  const spinnerStore = useSpinnerStore(); // Obtener el store del spinner
  spinnerStore.hideSpinner();
  return Promise.reject(error);
});


export default api;