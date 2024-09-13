<template>
    <div>
        <!-- HEADER  -->
        <!-- <MenuPrincipal :rol="user?.id_rol" @component-selected="changeComponent"/> -->
        <component :is="selectedMenu" :rol="user?.id_rol" @component-selected="changeComponent"/>


        <!-- BODY  -->
        <main class="content mt-4">
            <ComponenteDinamicoDelegado :currentComponent="currentComponent" />
        </main>

        <!-- FOOTER -->
        <FooterSecundario />
    </div>
</template>

<script>
import { markRaw } from 'vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router'; 
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import FooterSecundario from '../components/Footers/FooterSecundario.vue';
import AsignarProyectos from '../components/Users/delegado/AsignarProyectos/AsignarProyectos.vue';
import AsistenciaEvento from '../components/Users/delegado/asistencia/AsistenciaEvento.vue';
import PostulacionesEvaluadores from '../components/Users/delegado/postulaciones/PostulacionesEvaluadores.vue';
import ListaEvaluadores from '../components/Users/delegado/listaEvaluadores/ListaEvaluadores.vue';

import ComponenteDinamicoDelegado from '../components/Users/delegado/ComponenteDinamicoDelegado.vue';
import MenuUsuarios from '../components/Menus/MenuUsuarios.vue';

export default {
    components: {
        ComponenteDinamicoDelegado, 
        FooterSecundario,
        MenuPrincipal: markRaw(MenuPrincipal),
        MenuUsuarios: markRaw(MenuUsuarios),
        AsignarProyectos: markRaw(AsignarProyectos),
        PostulacionesEvaluadores: markRaw(PostulacionesEvaluadores),
        AsistenciaEvento: markRaw(AsistenciaEvento),
        ListaEvaluadores: markRaw(ListaEvaluadores)

    },
    data() {
        return {
            currentComponent: AsignarProyectos
        };
    },
    computed: {
        selectedMenu() {
            // Aquí defines la lógica para elegir el menú correcto según el componente actual
            if (this.currentComponent === ListaEvaluadores) {
                return MenuPrincipal;
            }
            return MenuUsuarios;
        }
    },
    methods: {
        changeComponent(componentName) {
            const componentMap = {
                AsignarProyectos: AsignarProyectos,
                PostulacionesEvaluadores: PostulacionesEvaluadores,
                AsistenciaEvento: AsistenciaEvento,
                ListaEvaluadores: ListaEvaluadores
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
    },
};
</script>

<style scoped>

.content {
    padding-top: 20px;
}

</style>
