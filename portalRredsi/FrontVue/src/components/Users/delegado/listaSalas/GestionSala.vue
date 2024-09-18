<template>
    <div>
        <div class="row mb-3">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Sala</h1>
                    </div>
                </div>
            </div>
            <div class="row justify-content-start">
                <div class="col-4">
                    <button class="boton_gestion_sala btn btn-dark text-white" @click="selectComponent('ListaSalasDelegado')">Volver</button>
                </div>
            </div>
            <div class=" container mt-5">
                <div class="container">
                    <!-- Proyecto -->
                    <div class="row mb-4 justify-content-center">
                        <div class="col-12 col-md-6 text-center">
                            <label for="proyecto_codigo" class="fw-bold text-dark">Proyecto:</label>
                            <select id="id_proyecto" class="form-select text-dark" required>
                                <option value="Seleccionar" selected>Seleccione una opción</option>
                            </select>
                        </div>
                    </div>
                    <form class="mt-4" id="formulario">
                        <div class="row mb-3">
                            <div class="col-12 col-md-6">
                                <label for="ponente_1" class="form-label text-black">Ponente 1:</label>
                                <input type="text" class="form-control" id="ponente_1" >
                            </div>
                            <div class="col-12 col-md-6">
                                <label for="ponente_2" class="form-label text-black">Ponente 2 (Opcional):</label>
                                <input type="text" class="form-control" id="ponente_2" >
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-12 col-md-6">
                                <label for="evaluador_1" class="fw-bold text-dark">Evaluador 1:</label>
                                <select id="id_evaluador_1" class="form-select text-dark" required>
                                    <option value="Seleccionar" selected>Seleccione una opción</option>
                                </select>
                            </div>
                            <div class="col-12 col-md-6">
                                <label for="evaluador_2" class="fw-bold text-dark">Evaluador 2:</label>
                                <select id="id_evaluador_2" class="form-select text-dark" required>
                                    <option value="Seleccionar" selected>Seleccione una opción</option>
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
                        <!-- Encabezado con fecha y botones -->
                        <div class="">
                            <h3 class="text-center m-0">Sep 6 de 2024</h3>
                        </div>
                        <table class="table table-hover border table-responsive">
                            <thead>
                                <tr id="headerRow">
                                    <th class="text-center">Evaluadores</th>
                                    <th class="text-center time-slot" data-time="6am">6:00am</th>
                                    <th class="text-center time-slot" data-time="6am">6:30am</th>
                                    <th class="text-center time-slot" data-time="7am">7:00am</th>
                                    <th class="text-center time-slot" data-time="7am">7:30am</th>
                                    <th class="text-center time-slot" data-time="8am">8:00am</th>
                                    <th class="text-center time-slot" data-time="8am">8:30am</th>
                                    <th class="text-center time-slot" data-time="9am">9:00am</th>
                                    <th class="text-center time-slot" data-time="9am">9:30am</th>
                                    <th class="text-center time-slot" data-time="10am">10:00am</th>
                                    <th class="text-center time-slot" data-time="10am">10:30am</th>
                                    <th class="text-center time-slot" data-time="11am">11:00am</th>
                                    <th class="text-center time-slot" data-time="11am">11:30am</th>
                                    <th class="text-center time-slot" data-time="12pm">12:00pm</th>
                                    <th class="text-center time-slot" data-time="12pm">12:30pm</th>
                                    <th class="text-center time-slot" data-time="1pm">1:00pm</th>
                                    <th class="text-center time-slot" data-time="1pm">1:30pm</th>
                                    <th class="text-center time-slot" data-time="2pm">2:00pm</th>
                                    <th class="text-center time-slot" data-time="2pm">2:30pm</th>
                                    <th class="text-center time-slot" data-time="3pm">3:00pm</th>
                                    <th class="text-center time-slot" data-time="3pm">3:30pm</th>
                                    <th class="text-center time-slot" data-time="4pm">4:00pm</th>
                                    <th class="text-center time-slot" data-time="4pm">4:30pm</th>
                                    <th class="text-center time-slot" data-time="5pm">5:00pm</th>
                                    <th class="text-center time-slot" data-time="5pm">5:30pm</th>
                                    <th class="text-center time-slot" data-time="6pm">6:00pm</th>
                                    <th class="text-center time-slot" data-time="6pm">6:30pm</th>
                                </tr>
                            </thead>
                            <tbody id="scheduleBody">

                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

    </div>
</template>

<script>
import { defineComponent } from 'vue';
export default defineComponent({
    props: {
        sala: Object,
        index: Number
    },
    emits: ['component-selected'],
    methods: {
            selectComponent(componentName) {
                this.$emit('component-selected', componentName);
            }
        }
});
</script>