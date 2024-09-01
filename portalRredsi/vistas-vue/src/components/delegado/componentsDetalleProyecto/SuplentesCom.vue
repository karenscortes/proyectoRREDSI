<template>
    <div class="feature">
        <div class="icon">
            <!-- Cambia el tamaño del icono a `fa-lg` -->
            <i class="fa-solid fa-user-group fa-lg text-dark mb-3"></i>
        </div>
        <!-- Asegura que el texto está alineado a la izquierda -->
        <h3 class="text-dark text-left">Suplentes</h3>
        <p class="text-dark text-left">
            Tipo: {{ tipo }} - {{ nombre }}
        </p>
    </div>
</template>

<script>
export default {
    name: 'SuplentesCom',
    props: {
        tipo: {
            type: String,
            required: true,
        },
        nombre: {
            type: String,
            required: true,
        },
    },
};
</script>

<style scoped>


/* Reduce el tamaño del texto */
h3, p {
    font-size: 0.9rem; /* Ajusta este valor según el tamaño deseado */
    margin-bottom: 5px; /* Opcional: agrega margen inferior para más separación */
}

/* Asegura que el texto no esté centrado */
.text-left {
    text-align: left;
}
</style>
