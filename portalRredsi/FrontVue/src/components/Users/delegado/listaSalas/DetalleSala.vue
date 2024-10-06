<template>
    <div class="mt-4">
        <!-- Botón de regresar -->
        <div class="col-5 col-sm-3">
            <a class="btn_regresar text-dark fw-bold d-flex align-items-center" @click="$emit('volver')">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                    fill="#00000" class="me-2">
                    <path d="m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z" />
                </svg>
                Lista de salas
            </a>
        </div>

        <!-- Sala Information Section -->
        <div class="p-4 bg-light rounded shadow-sm">
            <div class="row align-items-center text-center">
                <!-- Sala Number -->
                <div class="col-md-4">
                    <h2 class="text-dark fs-4">Sala</h2>
                    <p class="fs-5 mb-0">{{ sala.numero_sala }}</p>
                </div>
                <!-- Sala Name -->
                <div class="col-md-4 border-start border-end">
                    <h2 class="text-dark fs-4">Nombre de la sala</h2>
                    <p class="fs-5 mb-0">{{ sala.nombre_sala }}</p>
                </div>
                <!-- Delegado Information -->
                <div class="col-md-4">
                    <h2 class="text-dark fs-4">Delegado</h2>
                    <p class="fs-5 mb-0">{{ sala.nombres_delegado }} {{ sala.apellidos_delegado }}</p>
                </div>
            </div>
        </div>
        <!-- Línea divisoria para separar la información de la sala del horario -->
        <hr class="my-4">

        <!-- Tabla de horarios asignados -->
        <div class="table-responsive">
            <ComponenteHorario :sala="sala" />
        </div>

    </div>
</template>

<script>
import ComponenteHorario from "./ComponenteHorario.vue";

export default {
    props: {
        sala: Object,
        index: Number
    },
    components: {
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


.btn_regresar {
    padding: 8px 16px;
    border: 2px solid transparent;
    transition: background-color 0.3s ease, border-color 0.3s ease;
    display: inline-flex;
    align-items: center;
}

.btn_regresar:hover {
    background-color: rgba(0, 0, 0, 0.05);
    /* Efecto de hover sutil */
    border-color: #000;
    /* Añadir un borde visible al pasar el mouse */
    cursor: pointer;
}

.btn_regresar svg {
    transition: transform 0.3s ease;
}

.btn_regresar:hover svg {
    transform: translateX(-4px);
    /* Pequeño desplazamiento del ícono al hover */
}

@media (max-width: 768px) {
    .btn_regresar {
        padding: 6px 12px;
        font-size: 14px;
    }

    .btn_regresar svg {
        width: 20px;
        height: 20px;
    }
}
</style>
