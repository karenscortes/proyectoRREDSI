<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-users fa-lg text-dark mb-3"></i>
        </div>
        <h3 class="text-dark text-left">Ponentes</h3>
        <p class="text-dark text-left">
            <span v-for="(ponente, index) in ponentes" :key="index">
                {{ ponente }}<br>
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
h3,
p {
    font-size: 0.9rem;
    margin-bottom: 5px;
}
.text-left {
    text-align: left;
}
</style>