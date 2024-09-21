<template>
    <div>
        <div class="col-4">
            <a class="btn_regresar text-dark fw-bold" @click="$emit('volver')"><svg xmlns="http://www.w3.org/2000/svg"
                    height="24px" viewBox="0 -960 960 960" width="24px" fill="#00000">
                    <path d="m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z" />
                </svg> Lista de salas</a>
        </div>
        <div class="row mb-3">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Sala {{ sala.numero_sala }}</h1>
                </div>
            </div>
        </div>
        <div class=" container mt-5">
            <div class="container">
                <!-- Proyecto -->
                <div class="row mb-4 justify-content-center">
                    <div class="col-12 col-md-6 text-center">
                        <label for="proyecto_codigo" class="fw-bold text-dark">Proyecto:</label>
                        <select id="id_proyecto" v-model="proyectoSeleccionado.codigo" @change="consultarPonentesProyecto(proyectoSeleccionado.codigo)" class="form-select text-dark"
                            required>
                            <option value="" disabled selected>Seleccione una opción</option>
                            <option v-for="(proyecto,index) in listaProyectosSinAsignar" :key="index" :value="proyecto.id_proyecto">{{ proyecto.titulo}}</option>
                        </select>
                    </div>
                </div>
                <!-- Ponentes -->
                <form class="mt-4" @submit.prevent="asignarHorario">
                    <div class="row mb-3">
                        <div class="col-12 col-md-6">
                            <label for="ponente_1" class="form-label text-black">Ponente 1:</label>
                            <input type="text" class="form-control" id="ponente_1" :value="ponente1" disabled>
                        </div>
                        <div class="col-12 col-md-6">
                            <label for="ponente_2" class="form-label text-black">Ponente 2 (Opcional):</label>
                            <input type="text" class="form-control" id="ponente_2" :value="ponente2" disabled>
                        </div>
                    </div>
                    <!-- Evaluadores -->
                    <div class="row mb-3 ">
                        <div class="col-12 col-md-6">
                            <label for="evaluador_1" class="fw-bold text-dark">Evaluador 1:</label>
                            <select id="id_evaluador_1" v-model="evaluador1" class="form-select text-dark" required>
                                <option value="" disabled selected>Seleccione una opción</option>
                                <option value="Christian Arce">Christian Arce</option>
                                <option value="Maribel Obando">Maribel Obando</option>
                                <option value="Diego Legarda">Diego Legarda</option>
                            </select>
                        </div>
                        <div class="col-12 col-md-6">
                            <label for="evaluador_2" class="fw-bold text-dark">Evaluador 2:</label>
                            <select id="id_evaluador_2" v-model="evaluador2" class="form-select text-dark" required>
                                <option value="" disabled selected>Seleccione una opción</option>
                                <option value="Christian Arce">Christian Arce</option>
                                <option value="Maribel Obando">Maribel Obando</option>
                                <option value="Diego Legarda">Diego Legarda</option>
                            </select>
                        </div>
                    </div>
                    <!-- Fecha, hora inicio y hora fin -->
                    <div class="row mb-3 align-items-center">
                        <div class="col-12 col-md-4">
                            <label class="form-label">Fecha:</label>
                            <input id="fecha" type="date" v-model="horario.fecha" class="form-control text-dark">
                        </div>
                        <div class="col-12 col-md-4">
                            <label>Hora de Inicio:</label>
                            <input id="horario_inicio" type="time" v-model="horario.hora_inicio"
                                class="form-control text-dark" min="06:00" max="18:30" step="1800">
                        </div>
                        <div class="col-12 col-md-4">
                            <label>Hora de Fin:</label>
                            <input id="horario_fin" type="time" v-model="horario.hora_fin"
                                class="form-control text-dark" min="06:00" max="18:30" step="1800">
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
                <!-- Tabla de horarios -->
                <div class="container mt-4">
                    <div>
                        <h3 class="text-center m-0">{{ horario.fecha }}</h3>
                    </div>
                    <table class="table table-hover border table-responsive">
                        <thead>
                            <tr>
                                <th class="text-center">Evaluadores</th>
                                <th v-for="time in timeSlots" :key="time" class="text-center time-slot">{{ time }}</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(evaluador, index) in evaluadores" :key="index">
                                <td class="text-center">{{ evaluador.nombreEvaluador }}</td>
                                <td v-for="(slot, i) in 24" :key="i"
                                    :style="getStyle(i, evaluador.proyecto.inicio, evaluador.proyecto.fin)">
                                    <span v-if="isProjectTime(i, evaluador.proyecto.inicio, evaluador.proyecto.fin)">
                                        {{ evaluador.proyecto.titulo }}
                                    </span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { obtenerPonentesProyecto } from '@/services/salasDelegadoService';
import { proyectosSinAsignar } from '@/services/delegadoService'

export default defineComponent({
    props: {
        sala: Object,
        index: Number
    },
    data() {
        return {
            proyectoSeleccionado: {
                codigo: "",
                titulo: "",
            },
            ponente1: "",
            ponente2: "",
            evaluador1: "",
            evaluador2: "",
            horario: {
                fecha: "",
                hora_inicio: "",
                hora_fin: "",
            },
            evaluadores: [],
            listaProyectosSinAsignar: [],
            timeSlots: [
                "6:00am", "6:30am", "7:00am", "7:30am", "8:00am", "8:30am",
                "9:00am", "9:30am", "10:00am", "10:30am", "11:00am", "11:30am",
                "12:00pm", "12:30pm", "1:00pm", "1:30pm", "2:00pm", "2:30pm",
                "3:00pm", "3:30pm", "4:00pm", "4:30pm", "5:00pm", "5:30pm", "6:00pm", "6:30pm"
            ],
        };
    },
    emits: ['component-selected'],
    methods: {
        selectComponent(componentName) {
            this.$emit('component-selected', componentName);
        },
        asignarHorario() {
            const newEvaluador1 = {
                nombreEvaluador: this.evaluador1,
                proyecto: {
                    titulo: this.proyectoSeleccionado.codigo,
                    inicio: this.calcularPosicion(this.horario.hora_inicio),
                    fin: this.calcularPosicion(this.horario.hora_fin)
                }
            };

            const newEvaluador2 = {
                nombreEvaluador: this.evaluador2,
                proyecto: {
                    titulo: this.proyectoSeleccionado.codigo,
                    inicio: this.calcularPosicion(this.horario.hora_inicio),
                    fin: this.calcularPosicion(this.horario.hora_fin)
                }
            };

            this.evaluadores.push(newEvaluador1, newEvaluador2);

            this.proyectoSeleccionado.codigo = "";
            this.ponente1 = "";
            this.ponente2 = "";
            this.evaluador1 = "";
            this.evaluador2 = "";
            this.horario.fecha = "";
            this.horario.hora_inicio = "";
            this.horario.hora_fin = "";
        },
        calcularPosicion(hora) {
            let [horas, minutos] = hora.split(":").map(Number);
            let posicion = (horas - 6) * 2;
            if (minutos >= 30) {
                posicion += 1;
            }
            return posicion;
        },
        isProjectTime(i, inicio, fin) {
            return i >= inicio && i <= fin;
        },
        getStyle(i, inicio, fin) {
            if (this.isProjectTime(i, inicio, fin)) {
                return {
                    backgroundColor: 'rgb(255, 182, 6)',
                    textAlign: 'center',
                    color: 'black'
                };
            }
            return {};
        },
        async fetchProyectosSinAsignar() {
            try {
                const response = await proyectosSinAsignar();
                this.listaProyectosSinAsignar = response.data.projects;

            } catch (error) {
                alert("Error al obtener proyectos: ", error);
            }
        },
        async consultarPonentesProyecto(id_proyecto) {
            try {
                const ponentes = await obtenerPonentesProyecto(id_proyecto);
                let listaPonentes = ponentes.data.ponentes;

                // Con esta condición valido cuantos ponentes tiene el proyecto y si impresión
                if(listaPonentes.length == 1) {
                    this.ponente1 = `${listaPonentes[0].nombres} ${listaPonentes[0].apellidos}`;
                    this.ponente2 = "";
                }else if(listaPonentes.length == 2){
                    this.ponente1 = `${listaPonentes[0].nombres} ${listaPonentes[0].apellidos}`;
                    this.ponente2 = `${listaPonentes[1].nombres} ${listaPonentes[1].apellidos}`;
                }
            } catch (error) {
                this.ponente1 = "Sin ponente registrado";
                this.ponente2 = "Sin ponente registrado";
            }
            
        },
    },
    mounted(){
        this.fetchProyectosSinAsignar();
    }
});
</script>

<style scoped>
.btn_regresar:hover {
    cursor: pointer;
}
</style>