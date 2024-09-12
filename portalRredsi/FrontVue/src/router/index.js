import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/store'; 
import RubricaAdminView from '../views/RubricaAdminView.vue';
import InicioLogin from '../views/InicioLogin.vue';
import DelegadoView from '../views/DelegadoView.vue';
import EvaluadorView from '../views/EvaluadorView.vue';
import PostulacionesEvaluadores from '../components/Users/delegado/postulaciones/PostulacionesEvaluadores.vue'
import SuperAdminView from '../views/SuperAdminView.vue';
import ProyectosAsignadosEvaluadorView from '../views/ProyectosAsignadosEvaluadorView.vue';

import AsignarProyecto from '../components/Users/delegado/AsignarProyectos/AsignarProyectos.vue';

const routes = [
  
  // Ruta por defecto que apunta a LoginView
  { path: '/', name: 'InicioLogin', component: InicioLogin },
  
  // RUTAS EVALUADOR
  { path: '/principal-evaluador', name: 'EvaluadorView', component: EvaluadorView },
  { path: '/proyectos-asignados', name: 'ProyectosAsignadosEvaluadorView', component: ProyectosAsignadosEvaluadorView },


  // RUTAS DELEGADO
  { path: '/asignar-proyecto', name: 'AsignarProyecto', component: AsignarProyecto },
  { path: '/principal-delegado', name: 'DelegadoView', component: DelegadoView },
  { path: '/postulaciones-evaluadores', name: 'PostulacionesEvaluadores', component: PostulacionesEvaluadores},

  // RUTAS ADMIN
  { path: '/rubrica-admin', name: 'RubricaAdminView', component: RubricaAdminView },

  // RUTAS SUPERADMIN
  { path: '/super-admin', name: 'SuperAdminView', component: SuperAdminView},

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