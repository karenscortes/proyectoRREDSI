<template>
  <div>
    <!-- HEADER -->
    <MenuPrincipal :rol="user?.id_rol" @component-selected="changeComponent" />
    
    <main class="content mt-5">
      <!-- Componente dinámico -->
      <DynamicComponentSuperAdmin :currentComponent="currentComponent" />
    </main>
    
    <!-- FOOTER -->
    <FooterSecundario />
  </div>
</template>

<script>
import { markRaw } from 'vue';
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import DynamicComponentSuperAdmin from '../components/Users/superadmin/DynamicComponentSuperAdmin.vue';
import FooterSecundario from '../components/Footers/FooterSecundario.vue';
import InicioSuperAdminView from './InicioSuperAdminView.vue';
import ListaAdministradores from '../components/Users/superadmin/ListaAdministradores.vue';
import { updateUserProfile } from '../services/superadminService';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router';

export default {
  components: {
    DynamicComponentSuperAdmin,
    MenuPrincipal: markRaw(MenuPrincipal),
    FooterSecundario: markRaw(FooterSecundario),
    InicioSuperAdminView: markRaw(InicioSuperAdminView),
    ListaAdministradores: markRaw(ListaAdministradores),
    updateUserProfile: markRaw(updateUserProfile), // Registramos el nuevo componente
  },
  data() {
    return {
      currentComponent: InicioSuperAdminView, // Componente inicial
    };
  },
  methods: {
    changeComponent(componentName) {
      const componentMap = {
        InicioSuperAdminView: InicioSuperAdminView,
        ListaAdministradores: ListaAdministradores,
        updateUserProfile: updateUserProfile, // Añadimos el nuevo componente al mapeo
      };
      
      this.currentComponent = componentMap[componentName] || InicioSuperAdminView;
    },
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
      logout,
    };
  },
};
</script>

<style scoped>
.content {
  padding-top: 100px;
}
</style>
