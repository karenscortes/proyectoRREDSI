<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-graduation-cap fa-lg text-dark mb-3"></i>
        </div>
        <h3 class="text-dark text-left">Evaluadores</h3>
        <p class="text-dark text-left">
            <span v-for="(evaluador, index) in evaluadores" :key="index">
                {{ evaluador }}<br>
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
/* Reduce el tamaño del texto */
h3,
p {
    font-size: 0.9rem;
    /* Ajusta este valor según el tamaño deseado */
    margin-bottom: 5px;
    /* Opcional: agrega margen inferior para más separación */
}

/* Asegura que el texto no esté centrado */
.text-left {
    text-align: left;
}
</style>
