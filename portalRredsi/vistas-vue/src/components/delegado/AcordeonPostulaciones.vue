<template>
    <!-- Acordeón para cada evaluador -->
    <div class="accordion-item">
        <h2 class="accordion-header row align-items-center">
            <div class="col-9 col-sm-11">
                <button class="accordion-button collapsed row align-items-center" type="button"
                    data-bs-toggle="collapse" :data-bs-target="`#flush-collapse${index}`" aria-expanded="false"
                    :aria-controls="`flush-collapse${index}`">
                    <div class="col-8">
                        <h4 class="h5 m-0">{{ evaluador.nombreEvaluador }}</h4>
                    </div>
                </button>
            </div>
            <div class="col-3 col-sm-1 d-flex justify-content-end">
                <div class="mx-3">
                    <a href="#">
                        <svg v-if="evaluador.estado == 'Rechazado'" xmlns="http://www.w3.org/2000/svg" height="24px"
                            viewBox="0 -960 960 960" width="24px" fill="#FF0000">
                            <path
                                d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z" />
                        </svg>
                        <svg v-else xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960"
                            width="24px" fill="#00000">
                            <path
                                d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z" />
                        </svg>
                    </a>
                </div>
                <div class="mx-3">
                    <a href="#">
                        <svg v-if="evaluador.estado == 'Aceptado'" xmlns="http://www.w3.org/2000/svg" height="24px"
                            viewBox="0 -960 960 960" width="24px" fill="#12d336">
                            <path
                                d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                        </svg>
                        <svg v-else xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960"
                            width="24px" fill="#00000">
                            <path
                                d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                        </svg>
                    </a>
                </div>
            </div>
        </h2>
        <div :id="`flush-collapse${index}`" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
            <div class="accordion-body col-10 pl-0 text-dark text-start">
                <div class="row">
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Institución:</strong></p>
                        <p class="text-dark">{{ evaluador.institucion }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Área de conocimiento:</strong></p>
                        <p class="text-dark">{{ evaluador.areaConocimiento }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Área de conocimiento secundaria:</strong></p>
                        <p class="text-dark">{{ evaluador.areaConocimientoSecundaria }}</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Teléfono:</strong></p>
                        <p class="text-dark">{{ evaluador.telefono }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Correo electrónico:</strong></p>
                        <p class="text-dark">{{ evaluador.correo }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Estado:</strong></p>
                        <p class="text-dark">{{ evaluador.estado }}</p>
                    </div>
                </div>

                <div class="row mt-4 justify-content-start">
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Etapa:</strong></p>
                        <p v-if="evaluador.etapa_virtual && evaluador.etapa_presencial" class="text-dark"> Virtual y
                            presencial</p>
                        <p v-else>{{ evaluador.etapa_virtual ? "Virtual" : "Presencial" }}</p>

                    </div>
                    <div v-if="evaluador.etapa_virtual && evaluador.etapa_presencial || evaluador.etapa_presencial"
                        class="col-md-4 col-12">
                        <p class="text-dark"><strong>Jornada:</strong></p>
                        <p v-if="evaluador.jornada_manana && evaluador.jornada_tarde" class="text-dark"> Mañana y tarde
                        </p>
                        <p v-else>{{ evaluador.jornada_manana ? "Mañana" : "Tarde" }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <a data-bs-toggle="modal" data-bs-target="#modal_titulos"
                            class="btn btn-outline-primary w-100 mb-3">Visualizar
                            Títulos</a>
                    </div>
                </div>
            </div>
        </div>


        <!-- Modal -->
        <div class="modal fade" id="modal_titulos" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="row text-center justify-content-end mt-2">
                        <div class="col-2">
                            <button type="button" class="btn-close justify-contet-end" data-bs-dismiss="modal"
                                aria-label="Close"></button>
                        </div>
                        <div class="col-12">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Programas Académicos <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00000"><path d="M480-120 200-272v-240L40-600l440-240 440 240v320h-80v-276l-80 44v240L480-120Zm0-332 274-148-274-148-274 148 274 148Zm0 241 200-108v-151L480-360 280-470v151l200 108Zm0-241Zm0 90Zm0 0Z"/></svg></h1>
                        </div>
                    </div>
                    <div class="modal-body">
                        <div class="list-group">
                            <a href="#pregrado" class="list-group-item list-group-item-action">Pregrado</a>
                            <a href="#maestria" class="list-group-item list-group-item-action">Maestría</a>
                            <a href="#especializacion"
                                class="list-group-item list-group-item-action">Especialización</a>
                            <a href="#doctorado" class="list-group-item list-group-item-action">Doctorado</a>
                        </div>
                    </div>
                    <div class="row justify-content-center mb-2">
                        <button type="button" class="btn btn-dark fw-bold col-4 text-center" data-bs-dismiss="modal">Cerrar</button>
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
        evaluador: Object,
        index: Number
    }
};
</script>


<style>
.accordion-button:not(.collapsed) {
    background-color: rgb(255, 182, 6);
    color: #000;
}

.accordion-button {
    color: #000;
}

.accordion-button::after {
    filter: invert(0);
}
</style>