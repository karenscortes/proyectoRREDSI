<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-graduation-cap fa-1.5x text-dark mb-3"></i>
        </div>
        <h2 class="text-dark text-left font-weight-bold">Evaluadores</h2>
        <p class="text-dark text-left">
            <strong>Calificación Virtual</strong><br>
            <span v-for="(evaluador, index) in evaluadores.virtual" :key="index">
                {{ evaluador.nombres }} {{ evaluador.apellidos }} <br> 
            </span>
            <strong>Calificación Presencial</strong><br>
            <span v-for="(evaluador, index) in evaluadores.presencial" :key="index">
                {{ evaluador.nombres }} {{ evaluador.apellidos }} <br>
            </span>
        </p>
    </div>
</template>

<script>
export default {
    name: 'EvaluadoresComponent',
    props: {
        evaluadores: {
            type: Array,
            required: true,
        },
    },
};
</script>

<style scoped>
h2 {
    font-size: 0.8rem;
    margin-bottom: 3px;
}

.text-left {
    text-align: left;
}
</style>
