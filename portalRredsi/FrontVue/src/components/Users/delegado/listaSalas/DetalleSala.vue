<template>
    <div class="container mt-4">
        <!-- Botón de regresar -->
        <div class="d-flex justify-content-start mb-4">
            <a class="btn_regresar text-dark fw-bold d-flex align-items-center" @click="$emit('volver')">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                    fill="#00000">
                    <path d="m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z" />
                </svg>
                <span class="ms-2">Lista de salas</span>
            </a>
        </div>

        <!-- Información de sala y delegado -->
        <div class="text-center mb-4">
            <div class="row">
                <div class="col">
                    <h2 class="text-dark fs-3">SALA {{ sala.numero_sala }}</h2>
                </div>
                <div class="col">
                    <h2 class="text-dark fs-3">{{ sala.nombre_sala }}</h2>
                </div>
            </div>
            <div class="mt-2">
                <strong class="fs-5">Delegado: </strong>
                <span class="fs-5">{{ sala.nombres_delegado }} {{ sala.apellidos_delegado }}</span>
            </div>
        </div>
        <!-- Linea que divide el horario  -->
        <!-- <div class="title-line my-3"></div> -->
        <!-- Fecha -->
        <div class="text-center mb-4">
            <h3 class="text-muted mb-3">Sep 6 de 2024</h3>
        </div>

        <!-- Tabla de horarios -->
        <ComponenteHorario :sala="sala" />

    </div>
</template>

<script>
import ComponenteHorario from "./ComponenteHorario.vue";

export default {
    props: {
        sala: Object,
        index: Number
    },
    components:{
        ComponenteHorario
    },
    
}
</script>

<style scoped>
.btn_regresar:hover {
    cursor: pointer;
    color: #007bff;
}

.table {
    background-color: #f9f9f9;
    border: 1px solid #dee2e6;
}

.table th,
.table td {
    vertical-align: middle;
}
</style>
