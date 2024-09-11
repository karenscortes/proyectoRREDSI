<template>
    <div>
          <!-- HEADER  -->
          <MenuPrincipal :rol="user?.id_rol"/>

          
    </div>
  </template>
  
  <script>
  import { markRaw } from 'vue';
  import { useAuthStore } from '@/store';
  import { useRouter } from 'vue-router'; 
  import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';

  export default {
      components: {
          MenuPrincipal: markRaw(MenuPrincipal),
  
      },
      data() {
          return {
          };
      },
      methods: {
          changeComponent(componentName) {
              const componentMap = {
                  
              };
          }
      },setup() {
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
  