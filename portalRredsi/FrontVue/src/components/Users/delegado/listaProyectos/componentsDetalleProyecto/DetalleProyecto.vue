<template>
    <div class="container pt-5">
        <div class="row mb-4 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Detalle del Proyecto</h1>
                </div>
            </div>
        </div>
        <div class="why-choose-section ">
            <div class="container">
                <div class="row justify-content-between">
                    <div class="col-lg-6 order-2 order-lg-1">
                        <div class="section-title mt-4 text-left">
                            <h4>Información del proyecto</h4>
                        </div>
                        <div class="row my-5 gy-4">
                            <!-- Ponentes -->
                            <div class="col-6 col-md-6">
                                <PonentesCom :ponentes="ponentes" />
                            </div>
                            <!-- Evaluadores -->
                            <div class="col-6 col-md-6">
                                <EvaluadoresCom :evaluadores="evaluadores" />
                            </div>
                            <!-- Evento -->
                            <div class="col-6 col-md-6 mt-3">
                                <EventoCom :horario="horario" :sala="sala" />
                            </div>
                            <!-- Suplentes -->
                            <div class="col-6 col-md-6 mt-3">
                                <SuplentesCom :tipo="tipo" :suplente="suplente" />
                            </div>
                        </div>
                        <!-- Botones -->
                        <div class="col-10 d-flex justify-content-between">
                            <button type="button" class="btn btn-sm btn-warning font-weight-bold" style="width: 36%;"
                                @click="openModal">
                                Añadir presentación
                            </button>
                            <ModalAgregarLink :isVisible="showModal" @close="closeModal" />

                            <form action="../../../assets/img/constancia_NotasAprendiz.pdf"
                                style="width: 31%;" target="_blank">
                                <button type="submit" class="btn btn-sm btn-warning font-weight-bold"
                                    style="width: 100%;">
                                    Ver presentación
                                </button>
                            </form>
                            <form action="../../../assets/img/constancia_NotasAprendiz.pdf"
                                style="width: 31%;" target="_blank">
                                <button type="submit" class="btn btn-sm btn-warning font-weight-bold"
                                    style="width: 100%;">
                                    Ver proyecto
                                </button>
                            </form>
                        </div>
                    </div>

                    <!-- Imagen del proyecto -->
                    <div class="col-lg-6 order-1 order-lg-2">
                        <div class="img-wrap mt-4">
                            <img src="../../../assets/img/course_5.jpg" style="border-radius: 25px;" alt="Image"
                                class="img-fluid shadow-lg" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Accordion -->
        <div class="accordion pt-5 mt-3" id="accordionExample">
            <div class="card p-2">
                <div id="headingOne">
                    <button class="btn btn-block toggle-button collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
                        <i style="margin-right: 10px;" class="fa-solid fa-check fa-lg"></i>
                        Respuesta rúbrica 1
                    </button>
                </div>
                <div id="collapseOne" class="collapse mt-5" aria-labelledby="headingOne"
                    data-bs-parent="#accordionExample">
                    <!-- Componente RubricaCom -->
                    <RubricaCom :tituloProyecto="tituloProyecto" :ponentesProyecto="ponentesProyecto"
                        :universidadProyecto="universidadProyecto" :puntajeTotal="puntajeTotal"
                        :nombreEvaluador="nombreEvaluador" :cedulaEvaluador="cedulaEvaluador"
                        :universidadEvaluador="universidadEvaluador" :emailEvaluador="emailEvaluador"
                        :celularEvaluador="celularEvaluador" />
                </div>
            </div>
            <div class="card p-2">
                <div id="headingTwo">
                    <button class="btn btn-block toggle-button collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                        <i style="margin-right: 10px;" class="fa-solid fa-check fa-lg"></i>
                        Respuesta rúbrica 2
                    </button>
                </div>
                <div id="collapseTwo" class="collapse mt-5" aria-labelledby="headingTwo"
                    data-bs-parent="#accordionExample">
                    <RubricaCom :tituloProyecto="tituloProyecto" :ponentesProyecto="ponentesProyecto"
                        :universidadProyecto="universidadProyecto" :puntajeTotal="puntajeTotal"
                        :nombreEvaluador="nombreEvaluador" :cedulaEvaluador="cedulaEvaluador"
                        :universidadEvaluador="universidadEvaluador" :emailEvaluador="emailEvaluador"
                        :celularEvaluador="celularEvaluador" />
                </div>
            </div>
            <div class="card p-2">
                <div id="headingThree">
                    <button class="btn btn-block toggle-button collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                        <i style="margin-right: 10px;" class="fa-solid fa-x fa-lg"></i>
                        Respuesta rúbrica 3
                    </button>
                </div>
                <div id="collapseThree" class="collapse mt-5" aria-labelledby="headingThree"
                    data-bs-parent="#accordionExample">
                    <RubricaCom :tituloProyecto="tituloProyecto" :ponentesProyecto="ponentesProyecto"
                        :universidadProyecto="universidadProyecto" :puntajeTotal="puntajeTotal"
                        :nombreEvaluador="nombreEvaluador" :cedulaEvaluador="cedulaEvaluador"
                        :universidadEvaluador="universidadEvaluador" :emailEvaluador="emailEvaluador"
                        :celularEvaluador="celularEvaluador" />
                    <!--Respaldo-->
                    <h4 class="text-center text-dark mt-4 mb-4">Respaldo</h4>
                    <div class="custom-file-upload mx-auto">
                        <input type="file" id="comprobante_pago" name="comprobante_pago" />
                        <label for="comprobante_pago" class="upload-label">
                            <i class="fas fa-cloud-upload-alt"></i>
                            Selecciona un archivo
                        </label>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import EvaluadoresCom from './EvaluadoresCom.vue';
import EventoCom from './EventoCom.vue';
import PonentesCom from './PonentesCom.vue';
import SuplentesCom from './SuplentesCom.vue';
import RubricaCom from './RubricaCom.vue';

import { ref } from 'vue';

export default {
    components: {
        EvaluadoresCom,
        EventoCom,
        PonentesCom,
        SuplentesCom,
        RubricaCom,
    },
    setup() {
        //Datos evaluadores, ponentes, horario
        const ponentes = ['Diego Fernando Legarda', 'Felipe Londoño'];
        const evaluadores = ['Sebastian Usma', 'Miguel Alzate'];
        const horario = '10:30 - 11:00 A.M.';
        const sala = '123ASV';
        const tipo = 'Evaluador';
        const suplente = 'Juana de Arco';

        // Datos para RubricaCom
        const tituloProyecto = ref('BigData');
        const ponentesProyecto = ref('Diego Legarda, Felipe Londoño');
        const universidadProyecto = ref('UTP');
        const puntajeTotal = ref('50');
        const nombreEvaluador = ref('Miguel Alzate');
        const cedulaEvaluador = ref(123456789);
        const universidadEvaluador = ref('Catolica');
        const emailEvaluador = ref('cruelo@mail.com');
        const celularEvaluador = ref(987654321);

        // Modal Agregar Presentación
        const showModal = ref(false);
        const openModal = () => {
            showModal.value = true;
        };
        const closeModal = () => {
            showModal.value = false;
        };

        return {
            ponentes,
            evaluadores,
            horario,
            sala,
            tipo,
            suplente,
            tituloProyecto,
            ponentesProyecto,
            universidadProyecto,
            puntajeTotal,
            nombreEvaluador,
            cedulaEvaluador,
            universidadEvaluador,
            emailEvaluador,
            celularEvaluador,
            showModal,
            openModal,
            closeModal,
        };
    },
};
</script>

<style scoped>
.section_title h1 {
    display: block;
    color: #1a1a1a;
    font-weight: 500;
    padding-top: 24px;
}

.section_title h1::before {
    display: block;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 55px;
    height: 4px;
    content: '';
    background: #ffb606;
}

.feature {
    display: flex;
    flex-direction: column;
    align-items: start;
    margin-bottom: 15px;
}

.icon {
    margin-bottom: 10px;
}

.toggle-button {
    text-align: center;
    padding: 5px 20px;
    width: 100%;
}

.card {
    margin-bottom: 10px;
}

.accordion {
    display: block;
}

.title-line {
    border-top: 2px solid rgb(255, 182, 6);
    margin-top: -10px;
}

.form-section {
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    padding: 20px;
    border-radius: 5px;
    max-width: 800px;
    margin: auto;
}

.form-section h2 {
    color: rgb(255, 182, 6);
    text-align: center;
}

.form-section .title-icon {
    color: rgb(255, 182, 6);
    margin-right: 10px;
    font-size: 1.5rem;
    margin-bottom: 10px;
}



@media only screen and (max-width:767px) {

    .accordion {
        display: none;
    }

    .card {
        width: 100%;
        text-align: left;
        text-decoration: none;
        background-color: #f7f7f7;
        border: 1px solid black;
        margin-bottom: 2rem;
    }

    .card button {
        font-weight: 700;
        text-align: center;
    }

    .toggle-button:not(.collapsed) {
        color: rgb(255, 182, 6);
    }

}

@media only screen and (max-width: 767px) {
    .accordion {
        display: block;
    }
}
</style>