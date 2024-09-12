<template>
    <div>
      <!-- HEADER -->
      <MenuPrincipal :rol="user?.id_rol" @changeComponent="updateCurrentComponent" />
    
      <main class="content mt-5">
        <!-- Componente dinámico -->
        <DynamicComponentSuperAdmin :currentComponent="currentComponent" />
      </main>
    
      <FooterSecundario/>
    </div>
  </template>
  
  <script>
  import { markRaw } from 'vue';
  import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
  import InicioSuperAdminView from './InicioSuperAdminView.vue';
  
  
  import DynamicComponentSuperAdmin from '../components/Users/superadmin/DynamicComponentSuperAdmin.vue';
  import { useAuthStore } from '@/store';
  import { useRouter } from 'vue-router';
  import FooterSecundario from '../components/Footers/FooterSecundario.vue';
  import ListaDelegados from '../components/Users/superadmin/ListaDelegados.vue';
  
  export default {
    components: {
      DynamicComponentSuperAdmin,
      MenuPrincipal: markRaw(MenuPrincipal),
      InicioSuperAdminView: markRaw(InicioSuperAdminView),
      FooterSecundario,
      ListaDelegados: markRaw(ListaDelegados)
    },
    data() {
      return {
          currentComponent: InicioSuperAdminView
      };
    },
    methods: {
      updateCurrentComponent(componentName) {
        console.log('updateCurrentComponent llamada con parámetro:', componentName);
        this.changeComponent(componentName);
      }
    },
    setup() {
      const authStore = useAuthStore();
      const router = useRouter();
  
      const user = authStore.user;
      const permissions = authStore.permissions;
  
      const logout = () => {
        authStore.logout();
        router.push('/');
      };
  
      return {
        user,
        permissions,
        logout
      };
    }
  };
  </script>
  
  <style scoped>
  .content {
    padding-top: 100px;
  }
  </style>