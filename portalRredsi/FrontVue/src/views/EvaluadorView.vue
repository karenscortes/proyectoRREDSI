<template>
    <div>
        <!-- HEADER  -->
        <MenuPrincipal :rol="user?.id_rol" @component-selected="changeComponent"/>
        
        <main class="content mt-4">
            <ComponenteDinamicoEvaluador :currentComponent="currentComponent" />
        </main>

        <!-- FOOTER  -->
        <FooterSecundario />
    </div>
</template>

<script>
import { markRaw } from 'vue';
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import ProyectosAsignadosEvaluadorView from './ProyectosAsignadosEvaluadorView.vue';
import ComponenteDinamicoEvaluador from '../components/Users/evaluador/ComponenteDinamicoEvaluador.vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router'; 
import FooterSecundario from '../components/Footers/FooterSecundario.vue';

export default {
    components: {
        ComponenteDinamicoEvaluador, 
        MenuPrincipal: markRaw(MenuPrincipal),
        ProyectosAsignadosEvaluadorView: markRaw(ProyectosAsignadosEvaluadorView),
        FooterSecundario: markRaw(FooterSecundario),

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
    padding-top: 70px;
}

</style>
