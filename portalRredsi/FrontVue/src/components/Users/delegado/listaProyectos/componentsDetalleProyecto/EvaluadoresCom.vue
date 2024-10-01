<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-graduation-cap fa-lg text-dark mb-3"></i>
        </div>
        <h2 class="text-dark text-left font-weight-bold">Evaluadores</h2>
        <p class="text-dark text-left">
            <span v-for="(evaluador, index) in evaluadores" :key="index">
                {{ evaluador.nombres }} {{ evaluador.apellidos }}<br>
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
