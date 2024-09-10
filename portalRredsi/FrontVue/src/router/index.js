import { createRouter, createWebHistory } from 'vue-router';
<<<<<<< HEAD
// import { useAuthStore } from '@/store'; 
import SuperAdminView from '../views/SuperAdminView.vue';
=======
import { useAuthStore } from '@/store'; 
import RubricaAdminView from '../views/RubricaAdminView.vue';
import InicioLogin from '../views/InicioLogin.vue';
import DelegadoView from '../views/DelegadoView.vue';
import PostulacionesEvaluadoresView from '../views/PostulacionesEvaluadoresView.vue'

import AsignarProyecto from '../components/Users/delegado/AsignarProyectos/AsignarProyectos.vue';
>>>>>>> origin

const routes = [
  
  // Ruta por defecto que apunta a LoginView
<<<<<<< HEAD
  { path: '/', name: 'SuperAdminView', component: SuperAdminView },
  // Otras rutas
=======
  { path: '/', name: 'InicioLogin', component: InicioLogin },
  
  // RUTAS EVALUADOR

  // RUTAS DELEGADO
  { path: '/asignar-proyecto', name: 'AsignarProyecto', component: AsignarProyecto },
  { path: '/principal-delegado', name: 'DelegadoView', component: DelegadoView },
  { path: '/postulaciones-evaluadores', name: 'PostulacionesEvaluadoresView', component: PostulacionesEvaluadoresView},

  // RUTAS ADMIN
  { path: '/rubrica-admin', name: 'RubricaAdminView', component: RubricaAdminView },

  // RUTAS SUPERADMIN
>>>>>>> origin

  // Redirección en caso de ruta no encontrada
  { path: '/:pathMatch(.)', redirect: '/not-found' },
];

const router = createRouter({
  history: createWebHistory(process.env.VITE_BASE_URL),
  routes,
});


// Verifica la autenticación antes de cada navegación
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore(); // Obtiene la instancia del store de autenticación

  // Si la ruta requiere autenticación y no hay token
  if (to.meta.requiresAuth && !authStore.accessToken) {
    next('/'); // Redirige al login
  } else if (to.path === '/' && authStore.accessToken) {
    next('/asignar-proyecto'); // Si está autenticado, redirige al dashboard
  } else {
    next(); // Si todo está bien, permite la navegación
  }
});


export default router;