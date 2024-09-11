<template>
    <!-- Header -->

    <!-- Contenido principal -->
    <div class="container pt-5">
        <div class="row mb-4 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Proyectos Asignados</h1>
                    <h2 class="text-muted">Primera Etapa</h2>
                </div>
            </div>
        </div>

        <!-- Mostrar proyectos -->
        <div class="row justify-content-center">
            <ProyectosAsignados v-for="(proyecto, index) in proyectos" :key="index" :proyecto="proyecto" />
        </div>
    </div>
    <!-- Fin contenido principal -->

    <!-- Footer -->
</template>

<script>
    import { obtenerProyectosAsignados } from '../services/evaluadorService';
    import ProyectosAsignados from '../components/Users/evaluador/ProyectosAsignados.vue';

    export default {
        components: {
            ProyectosAsignados
        },
        data() {
            return {
                proyectos: []
            };
        },
        methods: {
            async fetchProyectos() {
                try {
                    const response = await obtenerProyectosAsignados(1, 1, 10);
                    // Asegúrate de acceder correctamente a la data de la respuesta
                    this.proyectos = response.data.data; 
                    console.log(this.proyectos);
                } catch (error) {
                    console.error("Error al obtener proyectos: ", error);
                    alert("Error al obtener proyectos");
                }
            }
        },
        mounted() {
            this.fetchProyectos();
        }
    };
</script>