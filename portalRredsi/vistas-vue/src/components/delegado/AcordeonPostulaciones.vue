<template>
    <!-- Acordeón para cada evaluador -->
    <div class="accordion-item">
        <h2 class="accordion-header row align-items-center">
            <div class="col-9 col-sm-11">
                <button class="accordion-button collapsed row align-items-center" type="button"
                    data-bs-toggle="collapse" :data-bs-target="`#flush-collapse${index}`" aria-expanded="false"
                    :aria-controls="`flush-collapse${index}`">
                    <div class="col-8">
                        <h4 class="h5 m-0">{{ nombreEvaluador }}</h4>
                    </div>
                </button>
            </div>
            <div class="col-3 col-sm-1 d-flex justify-content-end">
                <div class="mx-3">
                    <a href="#">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                            fill="#00000">
                            <path
                                d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z" />
                        </svg>
                    </a>
                </div>
                <div class="mx-3">
                    <a href="#">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                            fill="#12d336">
                            <path
                                d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                        </svg>
                    </a>
                </div>
            </div>
        </h2>
        <div :id="`flush-collapse${index}`" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
            <div class="accordion-body text-dark">
                <div class="row">
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Institución:</strong></p>
                        <p class="text-dark">{{ institucion }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Área de conocimiento:</strong></p>
                        <p class="text-dark">{{ areaConocimiento }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Área de conocimiento secundaria:</strong></p>
                        <p class="text-dark">{{ areaConocimientoSecundaria }}</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Teléfono:</strong></p>
                        <p class="text-dark">{{ telefono }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Correo electrónico:</strong></p>
                        <p class="text-dark">{{ correo }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Estado:</strong></p>
                        <p class="text-dark">{{ estado }}</p>
                    </div>
                </div>
                <div class="row mt-4 justify-content-center">
                    <div class="col-md-4 col-12">
                        <a :href="urlArchivo" target="_blank" class="btn btn-outline-primary w-100 mb-3">Visualizar
                            Títulos</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "AcordeonPostulaciones",
    props: {
        nombreEvaluador: String,
        institucion: String,
        areaConocimiento: String,
        areaConocimientoSecundaria: String,
        telefono: String,
        correo: String,
        estado: String,
        urlArchivo: String,
        index: Number // Nueva prop para el índice del acordeón
    }
};
</script>


<style>
.accordion-button:not(.collapsed) {
	background-color: rgb(255, 182, 6); /* Color amarillo */
	color: #000; /* Color del texto en la cabecera expandida */
}

.accordion-button {
	color: #000; /* Color del texto en la cabecera no expandida */
}

.accordion-button::after {
	filter: invert(0); /* Mantiene el color del icono de colapso en negro */
}

</style>