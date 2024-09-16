<template>
    <!-- Contenido principal -->
    <div class="container pt-5">
        <div class="row mb-5 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Calificar Proyecto</h1>
                    <h2 class="text-muted">Primera Etapa</h2>
                </div>
            </div>
        </div>

        <CalificarProyecto/> <!-- Botón de volver -->
        <div class="text-center mb-3 ">
            <button @click="$emit('volver')" class="btn btn-warning  font-weight-bold text-dark">Volver a Proyectos Asignados</button>
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