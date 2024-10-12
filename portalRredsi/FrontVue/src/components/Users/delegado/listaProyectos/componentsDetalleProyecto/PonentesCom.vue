<template>
    <div class="feature">
        <div class="icon-custom text-center">
            <i class="fa-solid fa-users fa-3x"></i>
        </div>
        <h2 class="text-left font-weight-bold text-yellow mb-3">Ponentes</h2>
        <div class="text-left ponente-names ">
            <span v-for="(ponente, index) in ponentes" :key="index">
                {{ ponente.nombres }} {{ ponente.apellidos }}<br>
            </span>
        </div>
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
.ponente-names {
    font-size: 0.8rem; 
    color: #000; 
    line-height: 1.6;
}
.text-left {
    text-align: left;
}
</style>
