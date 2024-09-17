<template>
    <!-- Contenido principal -->
    <div class="container">
        <div class="row mb-5 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Calificar Proyecto</h1>
                    <h2 class="text-muted">Primera Etapa</h2>
                </div>
            </div>
        </div>

        <!-- Pasar el proyecto seleccionado al componente CalificarProyecto -->
        <CalificarProyecto :proyecto="proyectoSeleccionado"/>
        <div class="text-center mb-3">
            <button @click="$emit('volver')" class="btn btn-warning font-weight-bold text-dark">Volver a Proyectos Asignados</button>
        </div>
    </div>
    <!-- Fin contenido principal -->
</template>

<script>
    import CalificarProyecto from '../components/Users/evaluador/CalificarProyecto.vue';
    export default {
        components: {
            CalificarProyecto
        },
        props: {
            proyectoSeleccionado: {
                type: Object,
                required: true
            }
        }
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