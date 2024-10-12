<template>
    <div class="feature">
        <div class="icon text-center mb-1">
            <i class="fa-solid fa-graduation-cap fa-3x icon-custom"></i>
        </div>
        <h2 class="text-left font-weight-bold text-yellow">Evaluadores</h2>

        <div class="evaluation-section">
            <p class="text-left">
                <strong>Calificación Virtual</strong>
            </p>
            <div class="text-left evaluator-names">
                <span v-for="(evaluador, index) in evaluadores.virtual" :key="index">
                    {{ evaluador.nombres }} {{ evaluador.apellidos }}<br>
                </span>
            </div>
        </div>

        <div class="evaluation-section" v-if="id_etapa == '1'">
            <p class="text-center">
                <strong>Calificación Presencial</strong>
            </p>
            <div class="text-left evaluator-names">
                <span v-for="(evaluador, index) in evaluadores.presencial" :key="index">
                    {{ evaluador.nombres }} {{ evaluador.apellidos }}<br>
                </span>
            </div>
        </div>
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
        id_etapa: {
            type: String,
            required: true,
        },
    },
};
</script>

<style scoped>
.icon-custom {
    color: #ffb606;
    margin-bottom: 0.5rem; 
    display: flex; 
    justify-content: center; 
    align-items: center; 
}

.text-yellow {
    color: #ffb606;
}

h2 {
    font-size: 1.1rem; 
    margin-bottom: 3px; 
}

.evaluator-names {
    font-size: 0.8rem; 
    color: #000; 
}

.text-left {
    text-align: left;
}

p {
    margin-bottom: 0.5rem;
}
</style>



