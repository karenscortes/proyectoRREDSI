<template>
    <div>
        <!-- HEADER  -->
        <MenuPrincipal :rol="'Delegado'"/>
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
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import AsignarProyectos from '../components/Users/delegado/AsignarProyectos/AsignarProyectos.vue';

import ComponenteDinamicoDelegado from '../components/Users/delegado/ComponenteDinamicoDelegado.vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router'; 

export default {
    components: {
        ComponenteDinamicoDelegado, 
        MenuPrincipal: markRaw(MenuPrincipal),
        AsignarProyectos: markRaw(AsignarProyectos)

    },
    data() {
        return {
            currentComponent: AsignarProyectos
        };
    },
    methods: {
        changeComponent(componentName) {
            const componentMap = {
                AsignarProyectos: AsignarProyectos,
                MenuPrincipal: MenuPrincipal, 
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
