<template>
    <div>
        <!-- HEADER  -->
        <MenuPrincipal :rol="user?.id_rol"/>
        <h4>{{ user?.nombres }} {{ user?.apellidos }}</h4>
        
        <main class="content mt-4">
            <ComponenteDinamicoEvaluador :currentComponent="currentComponent" />
        </main>

        <footer class="bg-dark mt-5 text-white text-center py-3">
            <h2>ESTE ES EL FOOTER</h2>
        </footer>
    </div>
</template>

<script>
import { markRaw } from 'vue';
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import ProyectosAsignadosEvaluadorView from './ProyectosAsignadosEvaluadorView.vue';

import ComponenteDinamicoEvaluador from '../components/Users/evaluador/ComponenteDinamicoEvaluador.vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router'; 

export default {
    components: {
        ComponenteDinamicoEvaluador, 
        MenuPrincipal: markRaw(MenuPrincipal),
        ProyectosAsignadosEvaluadorView: markRaw(ProyectosAsignadosEvaluadorView)

    },
    data() {
        return {
            currentComponent: ProyectosAsignadosEvaluadorView
        };
    },
    methods: {
        changeComponent(componentName) {
            const componentMap = {
                ProyectosAsignadosEvaluadorView: ProyectosAsignadosEvaluadorView,
            };
            this.currentComponent = componentMap[componentName] || ProyectosAsignadosEvaluadorView;
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

<style scoped>

.content {
    padding-top: 20px;
}

</style>
