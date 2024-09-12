<template>
  <div>
    <!-- HEADER -->
    <MenuPrincipal :rol="user?.id_rol" />

    <main class="content mt-5">
      <!-- Componente dinámico -->
      <DynamicComponentSuperAdmin :currentComponent="currentComponent" />
    </main>

    <footer class="bg-dark mt-5 text-white text-center py-3">
      <h2>ESTE ES EL FOOTER</h2>
    </footer>
  </div>
</template>

<script>
import { markRaw } from 'vue';
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import InicioSuperAdminView from './InicioSuperAdminView.vue';


import DynamicComponentSuperAdmin from '../components/Users/superadmin/DynamicComponentSuperAdmin.vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router';

export default {
  components: {
    DynamicComponentSuperAdmin,
    MenuPrincipal: markRaw(MenuPrincipal),
    InicioSuperAdminView: markRaw(InicioSuperAdminView)

  },
  data() {
    return {
        currentComponent: InicioSuperAdminView
    };
  },
  methods: {
    changeComponent(componentName) {
      const componentMap = {
        
      };
      
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
