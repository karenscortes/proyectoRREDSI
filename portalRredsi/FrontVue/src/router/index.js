import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/store'; 

import MainLayout from '../views/MainLayout.vue';
import UsersLayout from '../views/UsersLayout.vue';
import NotAvailable from '../views/NotAvailable.vue';
import NotFound from '../views/NotFound.vue';


const routes = [
  
  //RUTA A LOGINVIEW
  { path: '/', name: 'mainLayout', component: MainLayout },

  //RUTA A USERSLAYOUT
  { path: '/pagina-usuario', name: 'UsersLayout', component: UsersLayout },
  
  // RUTA A NOTFOUND
  { path: '/not-found', name: 'NotFound', component: NotFound },

  //RUTA A NOTAVAILABLE
  { path: '/seccionNoDisponible', name: 'NotAvailable', component: NotAvailable },

  // REDIRECCIONA SI UNA RUTA NO ES ENCONTRADA
  { path: '/:pathMatch(.*)*', redirect: '/not-found' },
];

const router = createRouter({
  history: createWebHistory(process.env.VITE_BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  // Si quiere entrar al UsersLayout y no hay token
  if (to.meta.requiresAuth && !authStore.accessToken) {
    next('/'); // Redirige al MainLayout
  } else if (to.path === '/' && authStore.accessToken) {// Si está autenticado e intenta devolverse al MainLayout
    next('/pagina-usuario'); //redirige al UsersLayout
  } else {
    next(); // Si todo está bien, permite la navegación
  }
});


export default router;