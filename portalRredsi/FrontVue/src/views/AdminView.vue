<template>
    <div>
        <!-- HEADER  -->
        <MenuPrincipal :rol="user?.id_rol" @component-selected="changeComponent"/>
        
        <main class="content mt-4">
            <ComponenteDinamicoAdmin :currentComponent="currentComponent" />
        </main>

        <!-- FOOTER  -->
        <FooterSecundario />
    </div>
</template>

<script>
import { markRaw } from 'vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router'; 
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import FooterSecundario from '../components/Footers/FooterSecundario.vue';
import RubricaAdminView from './RubricaAdminView.vue';
import SalasAdminView from './SalasAdminView.vue';

import MenuUsuarios from '../components/Menus/MenuUsuarios.vue';
import ComponenteDinamicoAdmin from '../components/Users/administrador/ComponenteDinamicoAdmin.vue';
import InicioAdminView from './InicioAdminView.vue';

export default {
    components: {
        ComponenteDinamicoAdmin, 
        FooterSecundario,
        MenuPrincipal: markRaw(MenuPrincipal),
        MenuUsuarios: markRaw(MenuUsuarios),
        InicioAdminView: markRaw(InicioAdminView),
        RubricaAdminView: markRaw(RubricaAdminView),
        SalasAdminView: markRaw(SalasAdminView),
    },
    data() {
        //El componente por defecto que se mostrará
        return {
            currentComponent: InicioAdminView,
        };
    },
    computed: {
        selectedMenu() {
            // Aquí defines la lógica para elegir el menú correcto según el componente actual
            if (this.currentComponent === InicioAdminView) {
                return MenuPrincipal;
            }
            return MenuUsuarios;
        }
    },
    methods: {
        changeComponent(componentName) {
            console.log(componentName)
            const componentMap = {
                RubricaAdminView: RubricaAdminView,
                SalasAdminView: SalasAdminView, 
                InicioAdmin: InicioAdminView,
            };
            this.currentComponent = componentMap[componentName] || InicioAdminView;
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
