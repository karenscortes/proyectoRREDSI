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
        <div class="container mt-4">
            <div>
                <!-- <h3 class="text-center m-0">{{ horario.fecha }}</h3> -->
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
</template>

<script>
import { obtenerDetalleSala } from "@/services/salasDelegadoService";
export default {
    props: {
        sala: Object,
        index: Number
    },
    data() {
        return {
            timeSlots: [
                "6:00am", "6:30am", "7:00am", "7:30am", "8:00am", "8:30am", "9:00am", "9:30am",
                "10:00am", "10:30am", "11:00am", "11:30am", "12:00pm", "12:30pm", "1:00pm", "1:30pm",
                "2:00pm", "2:30pm", "3:00pm", "3:30pm", "4:00pm", "4:30pm", "5:00pm", "5:30pm", "6:00pm", "6:30pm"
            ],
            detalleSala: [],
            evaluador1: "",
            evaluador2: "",
            horario: {
                fecha: "",
                hora_inicio: "",
                hora_fin: "",
            },
            listaPresentaciones: [],
            evaluadores: [],
        }
        
    },
    methods: {
        imprimirHorario() {
            const newEvaluador1 = {
                nombreEvaluador: this.evaluador1,
                proyecto: {
                    titulo: this.proyectoSeleccionado.id_proyecto,
                    inicio: this.calcularPosicion(this.horario.hora_inicio),
                    fin: this.calcularPosicion(this.horario.hora_fin)
                }
            };

            this.evaluadores.push(newEvaluador1);

            this.proyectoSeleccionado.id_proyecto = "";
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
        async obtenerDatosSala() {
            const datosSala = await obtenerDetalleSala(this.sala.id_sala);
            this.detalleSala = datosSala.data;
            console.log(this.detalleSala)
        },
        
        obtenerHoraMinutos(duracion) {
            // Remover "PT" del inicio de la cadena
            duracion = duracion.replace('PT', '');

            // Inicializar valores de horas y minutos
            let horas = 0;
            let minutos = 0;

            // Dividir la cadena por la letra 'H' para obtener horas y el resto
            const partesHoras = duracion.split('H');

            if (partesHoras.length > 1) {
                // Si hay una parte con 'H', extraer las horas
                horas = parseInt(partesHoras[0]);
                duracion = partesHoras[1];  // El resto contiene minutos
            } else {
                // Si no hay 'H', significa que no hay horas y todo es minutos
                duracion = partesHoras[0];
            }

            // Dividir la parte restante por la letra 'M' para obtener los minutos
            if (duracion.includes('M')) {
                minutos = parseInt(duracion.split('M')[0]);
            }

            return { horas, minutos };
        }
    },
    mounted() {
        this.obtenerDatosSala()
    }
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
