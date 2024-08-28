<template>
    <div class="container mt-5">
        <div class="row mb-3">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Gestión de Sala</h1>
                </div>
            </div>
        </div>
        <div class=" container mt-5">
            <div class="container">
                <!-- Proyecto -->
                <div class="row mb-4 justify-content-center">
                    <div class="col-12 col-md-6 text-center">
                        <label for="proyecto_codigo" class="fw-bold text-dark">Proyecto:</label>
                        <select class="form-select text-dark">
                            <option selected>Seleccione un opción</option>
                            <option v-for="(proyecto, index) in proyectos" :key="index"
                                :value="proyecto.codigoProyecto">
                                {{ proyecto.codigoProyecto }}</option>
                        </select>
                    </div>
                </div>
                <form class="mt-4" id="formulario">
                    <div class="row mb-3">
                        <div class="col-12 col-md-6">
                            <label for="ponente_1" class="form-label text-black">Ponente 1:</label>
                            <input type="text" class="form-control" id="ponente_1" :value="ponenteActual.ponenteUno"
                                placeholder>
                        </div>
                        <div class="col-12 col-md-6">
                            <label for="ponente_2" class="form-label text-black">Ponente 2 (Opcional):</label>
                            <input type="text" class="form-control" id="ponente_2" :value="ponenteActual.ponenteDos"
                                placeholder>
                        </div>
                    </div>
                    <div class="row mb-3">
                        <div class="col-12 col-md-6">
                            <label for="evaluador_1" class="fw-bold text-dark">Evaluador 1:</label>
                            <select class="form-select text-dark">
                                <option selected>Seleccionar evaluador</option>
                                <option v-for="(evaluador, index) in evaluadores" :key="index"
                                    :value="evaluador.nombreEvaluador"> {{ evaluador.nombreEvaluador }}
                                </option>
                            </select>
                        </div>
                        <div class="col-12 col-md-6">
                            <label for="evaluador_2" class="fw-bold text-dark">Evaluador 2:</label>
                            <select class="form-select text-dark">
                                <option selected>Seleccionar evaluador</option>
                                <option v-for="(evaluador, index) in evaluadores" :key="index"
                                    :value="evaluador.nombreEvaluador"> {{ evaluador.nombreEvaluador }}
                                </option>
                            </select>
                        </div>
                    </div>

                    <div class="row mb-3 align-items-center">
                        <div class="col-12 col-md-4">
                            <label class="form-label">Fecha:</label>
                            <input type="date" id="fecha" class="form-control text-dark">
                        </div>
                        <div class="col-12 col-md-4">
                            <label>Hora de Inicio:</label>
                            <input type="time" class="form-control text-dark" id="horario_inicio">
                        </div>
                        <div class="col-12 col-md-4">
                            <label>Hora de Fin:</label>
                            <input type="time" class="form-control text-dark" id="horario_fin">
                        </div>
                    </div>
                    <!-- Botón para agregar horario -->
                    <div class="text-center mt-4">
                        <button class="btn text-dark " type="submit" id="asignar_horario"
                            style="background:rgb(255, 182, 6);">Asignar Horario</button>
                    </div>
                </form>
                <div class="title-line mt-3"></div>
                <!-- Línea debajo del título -->
                <div class="container mt-4">
                    <ComponenteHorario :evaluadores="evaluadores" :proyecto="proyectos" :horario="horario"></ComponenteHorario>
                </div>
            </div>
        </div>



    </div>
</template>

<script>
import { reactive } from 'vue';
export default{
    data(){
        return{
            proyectos:[
                {codigoProyecto: "A001"},
                {codigoProyecto: "A002"},
                {codigoProyecto: "A003"},
            ],
            evaluadores: [
                                    { nombreEvaluador: "Este es el evaluador 1" },
                                    { nombreEvaluador: "Este es el evaluador 2" }
                                ],
            horario:{
                        fecha: "28-08-2024",
                        hora_inicio: "7:00",
                        hora_fin: "8:00"
                    }
        }
    },
    setup(){
        const ponenteActual = reactive({
            ponenteUno: "Federico García Lorca",
            ponenteDos: "Jorge Luis Borges"
        });
        return {
            ponenteActual,
            
        }
    }

    
}

</script>

<style>
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
    -webkit-transform: translateX(-50%);
    -moz-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    -o-transform: translateX(-50%);
    transform: translateX(-50%);
    width: 55px;
    height: 4px;
    content: '';
    background: #ffb606;
}

/* Estilos para el paginador */
.pagination .page-item .page-link {
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 50px;
}

.pagination .page-item .page-link:hover {
    background-color: rgb(255, 182, 6);
    color: #ffffff;
}

</style>