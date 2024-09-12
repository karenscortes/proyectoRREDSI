<template>
    <div>
        <!-- HEADER  -->
        <MenuPrincipal :rol="user?.id_rol" @component-selected="changeComponent"/>
        <h4>{{ user?.nombres }} {{ user?.apellidos }}</h4>
        
        <main class="content mt-4">
            <ComponenteDinamicoDelegado :currentComponent="currentComponent" />
        </main>

        <footer class="bg-dark mt-5 text-white text-center py-3">
            <h2>ESTE ES EL FOOTER</h2>
        </footer>
    </div>
</template>

<script>
import { markRaw } from 'vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router'; 
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import AsignarProyectos from '../components/Users/delegado/AsignarProyectos/AsignarProyectos.vue';
import AsistenciaEvento from '../components/Users/delegado/asistencia/AsistenciaEvento.vue';
import PostulacionesEvaluadores from '../components/Users/delegado/postulaciones/PostulacionesEvaluadores.vue';


import ComponenteDinamicoDelegado from '../components/Users/delegado/ComponenteDinamicoDelegado.vue';

export default {
    components: {
        ComponenteDinamicoDelegado, 
        MenuPrincipal: markRaw(MenuPrincipal),
        AsignarProyectos: markRaw(AsignarProyectos),
        PostulacionesEvaluadores: markRaw(PostulacionesEvaluadores),
        AsistenciaEvento: markRaw(AsistenciaEvento)

    },
    data() {
        return {
            currentComponent: AsistenciaEvento

        };
    },
    methods: {
        changeComponent(componentName) {
            const componentMap = {
                AsignarProyectos: AsignarProyectos,
                PostulacionesEvaluadores: PostulacionesEvaluadores,
                AsistenciaEvento: AsistenciaEvento
            };
            this.currentComponent = componentMap[componentName] || AsignarProyectos;
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
