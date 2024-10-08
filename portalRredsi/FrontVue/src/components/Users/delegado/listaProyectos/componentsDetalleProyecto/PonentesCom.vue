<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-users fa-1.5x text-dark mb-3"></i>
        </div>
        <h2 class="text-dark text-left font-weight-bold">Ponentes</h2>
        <p class="text-dark text-left">
            <span v-for="(ponente, index) in ponentes" :key="index">
                {{ ponente.nombres }} {{ ponente.apellidos }}<br>
            </span>
        </p>
    </div>
</template>

<script>
export default {
    name: 'PonentesComponent',
    props: {
        ponentes: {
            type: Array,
            required: true,
        },
    },
};
</script>

<style scoped>
h2{
    font-size: 0.8rem;
    margin-bottom: 2px;
}
.text-left {
    text-align: left;
}
</style>