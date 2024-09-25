<template>
    <!-- Contenido principal -->
    <div class="container">
        <div class="row mb-5 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Calificar Proyecto</h1>
                    <h2 class="text-muted">{{ tituloEtapa }}</h2>
                </div>
            </div>
        </div>
    </div>
    <!-- Pasar el proyecto seleccionado al componente CalificarProyecto -->
    <CalificarProyecto :proyecto="proyectoSeleccionado"/>
    <div class="text-center mb-3">
        <button @click="$emit('volver')" class="btn btn-warning font-weight-bold text-dark">Volver a Proyectos Asignados</button>
    </div>
    <!-- Fin contenido principal -->
</template>

<script>
    import CalificarProyecto from '../components/Users/evaluador/CalificarProyecto.vue';
    import obtenerEtapaActual from '../services/evaluadorService';
    
    export default {
        components: {
            CalificarProyecto
        },
        data() {
            return {
                currentEtapa: '' 
            };
        },
        props: {
            proyectoSeleccionado: {
                type: Object,
                required: true
            }
        },
        computed: {
            tituloEtapa() {
                return this.currentEtapa === 'Virtual' ? 'Primera Etapa' : 'Segunda Etapa';
            }
        },
        methods: {
            async obtenerEtapa() {
                try {
                    const response = await obtenerEtapaActual();
                    this.currentEtapa = response.nombre_etapa;
                } catch (error) {
                    console.error("Error al obtener la etapa actual: ", error);
                    alert("Error al obtener la etapa actual");
                }
            },
        },
        mounted() {
            this.obtenerEtapa();
        },
        emits: ['volver'], 
    };
</script>

<style scoped>
    .text-muted {
        font-size: 1.2rem;
        color: #999;
    }

    .btn-warning {
        width: 300px;
    }
</style>