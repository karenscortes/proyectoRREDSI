import axios from 'axios';
import { useAuthStore } from '@/store';
import router from '@/router';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_API,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
});

api.interceptors.request.use(config => {
    const authStore = useAuthStore();
    const token = authStore.accessToken;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  }, error => {
    return Promise.reject(error);
  });


api.interceptors.response.use(response => {
  return response;
}, error => {
  if (error.response && error.response.status === 401 && error.response.data.detail === 'Invalid token') {

    const authStore = useAuthStore();
    authStore.logout();

    router.push('/'); 
  }
  return Promise.reject(error);
});


export default api;