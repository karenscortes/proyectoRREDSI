import { createRouter, createWebHistory } from 'vue-router';
// import { useAuthStore } from '@/store'; 
import AsistenciaEvento from '../components/Users/delegado/asistencia/AsistenciaEvento.vue';

const routes = [
  // Ruta por defecto que apunta a LoginView
  { path: '/', name: 'AsistenciaEvento', component: AsistenciaEvento },
  // Otras rutas

  // Redirección en caso de ruta no encontrada
  { path: '/:pathMatch(.)', redirect: '/not-found' },
];

const router = createRouter({
  history: createWebHistory(process.env.VITE_BASE_URL),
  routes,
});


// Verifica la autenticación antes de cada navegación
// router.beforeEach((to, from, next) => {
//   const authStore = useAuthStore(); // Obtiene la instancia del store de autenticación

  // Si la ruta requiere autenticación y no hay token
  // if (to.meta.requiresAuth && !authStore.accessToken) {
  //   next('/'); // Redirige al login
  // } else if (to.path === '/' && authStore.accessToken) {
  //   next('/dashboard'); // Si está autenticado, redirige al dashboard
//   // } else {
//     next(); // Si todo está bien, permite la navegación
//   }
// });


export default router;