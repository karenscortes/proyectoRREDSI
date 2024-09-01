<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-person-booth fa-lg text-dark mb-3"></i>
        </div>
        <h3 class="text-dark text-left">Evento</h3>
        <p class="text-dark text-left">
            Horario: {{ horario }}<br>
            Sala: {{ sala }}
        </p>
    </div>
</template>

<script>
export default {
    name: 'EventoComponent',
    props: {
        horario: {
            type: String,
            required: true,
        },
        sala: {
            type: String,
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