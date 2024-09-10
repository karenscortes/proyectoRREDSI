<template>
    <div>
        <!-- HEADER  -->
        <MenuPrincipal :rol="'Delegado'"/>
        
        <main class="content mt-4">
            <ComponenteDinamicoDelegado :currentComponent="currentComponent" />
        </main>

        <footer class="text-white text-center py-3">
            <h2>ESTE ES EL FOOTER</h2>
        </footer>
    </div>
</template>

<script>
import { markRaw } from 'vue';
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import AsignarProyectos from '../components/Users/delegado/AsignarProyectos/AsignarProyectos.vue';

import ComponenteDinamicoDelegado from '../components/Users/delegado/ComponenteDinamicoDelegado.vue';

export default {
    components: {
        ComponenteDinamicoDelegado, // Registra el componente dinámico
        MenuPrincipal: markRaw(MenuPrincipal),
        AsignarProyectos: markRaw(AsignarProyectos)

    },
    data() {
        return {
            // Define el componente que se mostrará inicialmente
            currentComponent: AsignarProyectos
        };
    },
    methods: {
        changeComponent(componentName) {
            // Mapea nombres a componentes
            const componentMap = {
                AsignarProyectos: AsignarProyectos,
                MenuPrincipal: MenuPrincipal, // Añade el componente ListUsers al mapeo de nombres a componentes
                // Añadir aquí más componentes al mapear nombres a componentes, como:
                // otros componentes
            };
            // Cambia el componente actual
            this.currentComponent = componentMap[componentName] || AsignarProyectos;
        }
    }
};
</script>

<style scoped>

.content {
    padding-top: 20px;
}

</style>
