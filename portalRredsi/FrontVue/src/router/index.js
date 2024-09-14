import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/store'; 
import RubricaAdminView from '../views/RubricaAdminView.vue';
import InicioLogin from '../views/InicioLogin.vue';
import DelegadoView from '../views/DelegadoView.vue';
import EvaluadorView from '../views/EvaluadorView.vue';
import PostulacionesEvaluadores from '../components/Users/delegado/postulaciones/PostulacionesEvaluadores.vue'
import SuperAdminView from '../views/SuperAdminView.vue';
import ListaDelegados from '../components/Users/superadmin/ListaDelegados.vue'
import ProyectosAsignadosEvaluadorView from '../views/ProyectosAsignadosEvaluadorView.vue';
import AsignarProyecto from '../components/Users/delegado/AsignarProyectos/AsignarProyectos.vue';
import PaginaInicioEvaluadorView from '../views/PaginaInicioEvaluadorView.vue';

const routes = [
  
  // Ruta por defecto que apunta a LoginView
  { path: '/', name: 'InicioLogin', component: InicioLogin },
  
  // RUTAS EVALUADOR
  { path: '/principal-evaluador', name: 'EvaluadorView', component: EvaluadorView, meta: { requiresAuth: true, allowedRoles: [1] }   },
  { path: '/proyectos-asignados', name: 'ProyectosAsignadosEvaluadorView', component: ProyectosAsignadosEvaluadorView, meta: { requiresAuth: true, allowedRoles: [1] }  },
  { path: '/pagina-inicio', name: 'PaginaInicioEvaluadorView', component: PaginaInicioEvaluadorView, meta: { requiresAuth: true, allowedRoles: [1] } },


  // RUTAS DELEGADO
  { path: '/asignar-proyecto', name: 'AsignarProyecto', component: AsignarProyecto, meta: { requiresAuth: true, allowedRoles: [2] } },
  { path: '/principal-delegado', name: 'DelegadoView', component: DelegadoView, meta: { requiresAuth: true, allowedRoles: [2] } },
  { path: '/postulaciones-evaluadores', name: 'PostulacionesEvaluadores', component: PostulacionesEvaluadores, meta: { requiresAuth: true, allowedRoles: [2] }},
  

  // RUTAS ADMIN
  { path: '/rubrica-admin', name: 'RubricaAdminView', component: RubricaAdminView },

  // RUTAS SUPERADMIN
  { path: '/super-admin', name: 'SuperAdminView', component: SuperAdminView},
  { path: '/lista-delegados-superadmin', name: 'ListaDelegados', component: ListaDelegados},

  // Redirección en caso de ruta no encontrada
  { path: '/:pathMatch(.)', redirect: '/not-found' },
];

const router = createRouter({
  history: createWebHistory(process.env.VITE_BASE_URL),
  routes,
});


router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const userRole = authStore.user?.id_rol;

  // Verifica si la ruta requiere autenticación
  if (to.meta.requiresAuth) {
    if (!authStore.accessToken) {
      // Redirige al login si no está autenticado
      next('/');
    } else if (to.meta.allowedRoles && !to.meta.allowedRoles.includes(userRole)) {
      // Redirige a la ruta correcta según el rol
      if (userRole === 1) {
        next('/principal-evaluador');
      } else if (userRole === 2) {
        next('/principal-delegado');
      } else {
        next('/');
      }
    } else {
      // Permite la navegación si el usuario tiene el rol adecuado
      next();
    }
  } else {
    // Permite la navegación si la ruta no requiere autenticación
    next();
  }
});


export default router;