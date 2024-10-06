<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-graduation-cap fa-lg text-dark mb-3"></i>
        </div>
        <h2 class="text-dark text-left font-weight-bold">Evaluadores</h2>
        <p class="text-dark text-left">
            <span v-for="(evaluador, index) in evaluadores.virtual" :key="index">
                {{ evaluador.nombres }} {{ evaluador.apellidos }}  <strong>Virtual</strong><br>
            </span>
            <span v-for="(evaluador, index) in evaluadores.presencial" :key="index">
                {{ evaluador.nombres }} {{ evaluador.apellidos }}  <strong>Presencial</strong><br>
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
h2,
p {
    font-size: 0.8rem;
    margin-bottom: 4px;
}

.text-left {
    text-align: left;
}
</style>
