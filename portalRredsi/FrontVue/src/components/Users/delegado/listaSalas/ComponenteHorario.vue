<template>
    <div>
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
                    <tr class="fila_tabla" v-for="(detalle, index) in detalleSala" :key="index">
                        <td class="nombre_evaluador">{{ detalle.nombre_evaluador }}</td>
                        <td class="align-middle" v-for="(slot, i) in 24" :key="i"
                            :style="getStyle(i, detalle.hora_inicio, detalle.hora_fin)">
                            <span
                                v-if="isProjectTime(i, detalle.hora_inicio, detalle.hora_fin) && i === getMiddleSlot(detalle.hora_inicio, detalle.hora_fin)">
                                <a class="text-dark fw-semibold text-center" type="button" data-bs-toggle="modal"
                                    data-bs-target="#detalle_proyecto"
                                    @click="proyectoSeleccionado(detalle.id_proyecto)">Ver Detalle</a>
                            </span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <!-- Modal con detalles del proyecto  -->
        <div class="modal fade" id="detalle_proyecto" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content bg-light shadow-sm border border-dark border-5 rounded-5 text-dark">
                    <div class="modal-header text-center">
                        <h3 class="modal-title w-100 fs-4 text-dark" id="modalLabel">{{ detalle_proyecto.titulo }}</h3>
                        <button type="button" class="btn-close mr-1 mt-1" data-bs-dismiss="modal" aria-label="Close"
                            @click="limpiarModalDetalleProyecto"></button>
                    </div>
                    <div class="modal-body text-center mt-3">
                        <div class="row align-items-center text-center">
                            <div class="col-md-6">
                                <h4 class="fs-5 text-dark">Ponentes</h4>
                                <p class="fs-6 text-muted mb-0">Pendiente...</p>
                            </div>
                            <div class="col-md-6 border-start">
                                <h4 class="fs-5 text-dark">Evaluadores</h4>
                                <p class="fs-6 text-muted mb-0">Pendiente...</p>
                            </div>
                        </div>

                        <!-- Línea de separación superior para la siguiente fila -->
                        <hr class="border-dark my-4">

                        <div class="row align-items-center text-center">
                            <div class="col-md-6">
                                <h4 class="fs-5 text-dark">Horarios</h4>
                                <p class="fs-6 text-muted mb-0">Pendiente...</p>

                            </div>
                            <div class="col-md-6 border-start">
                                <h4 class="fs-5 text-dark">URL Propuesta Escrita</h4>
                                <p class="fs-6">
                                    <a :href="detalle_proyecto.url_propuesta_escrita" target="_blank"
                                        class="text-primary">Ver Propuesta</a>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>





        <!-- alerta  -->
        <FlashMessage v-if="isOpen" @close="closeModal" :titulo="titulo_alerta" :mensaje="mensaje_alerta"
            :tipo="tipo_alerta" />
    </div>
</template>

<script>
import { obtenerDetalleSala, obtenerDatosProyecto } from "@/services/salasDelegadoService";
import FlashMessage from "../../../FlashMessage.vue";

export default {
    props: {
        sala: Object,
    },
    data() {
        return {
            timeSlots: [
                "6:00am", "6:30am", "7:00am", "7:30am", "8:00am", "8:30am", "9:00am", "9:30am",
                "10:00am", "10:30am", "11:00am", "11:30am", "12:00pm", "12:30pm", "1:00pm", "1:30pm",
                "2:00pm", "2:30pm", "3:00pm", "3:30pm", "4:00pm", "4:30pm", "5:00pm", "5:30pm", "6:00pm", "6:30pm"
            ],
            detalleSala: [],
            evaluadores: [],
            titulo_alerta: "",
            mensaje_alerta: "",
            tipo_alerta: "",
            isOpen: false,
            detalle_proyecto: {}
        }

    },
    components: {
        FlashMessage
    },
    methods: {
        calcularPosicion(hora) {
            let [horas, minutos] = hora.split(":").map(Number);
            let posicion = (horas - 6) * 2;
            if (minutos >= 30) {
                posicion += 1;
            }
            return posicion;
        },
        getMiddleSlot(horaInicio, horaFin) {
            return Math.floor((horaInicio + horaFin) / 2);
        },
        isProjectTime(i, inicio, fin) {
            return i >= inicio && i <= fin;
        },
        getStyle(i, inicio, fin) {
            if (this.isProjectTime(i, inicio, fin)) {
                return {
                    backgroundColor: 'rgb(255, 182, 6)',
                    textAlign: 'center',
                    color: 'black',
                };
            }
            return {};
        },
        async obtenerDatosSala() {
            try {
                const datosSala = await obtenerDetalleSala(this.sala.id_sala);
                this.detalleSala = datosSala.data.detalle_sala;

                // Convierte las horas a minutos en cada fila de la tabla
                for (let i = 0; i < this.detalleSala.length; i++) {
                    // castea el formato a horas y minutos validos 
                    this.detalleSala[i].hora_inicio = this.obtenerHoraMinutos(this.detalleSala[i].hora_inicio);
                    this.detalleSala[i].hora_fin = this.obtenerHoraMinutos(this.detalleSala[i].hora_fin);

                    // obtiene la posicion en la tabla para que se pueda imprimir
                    this.detalleSala[i].hora_inicio = this.calcularPosicion(this.detalleSala[i].hora_inicio);
                    this.detalleSala[i].hora_fin = this.calcularPosicion(this.detalleSala[i].hora_fin);
                }
            } catch (error) {
                this.titulo_alerta = "Sala sin detalle";
                this.mensaje_alerta = "Aún no se han asignado proyectos a esta sala";
                this.tipo_alerta = 1;
                this.openModal();
            }
        },

        obtenerHoraMinutos(duracion) {
            // Remover "PT" del inicio de la cadena
            duracion = duracion.replace('PT', '');

            let horas = 0;
            let minutos = '00';

            const partesHoras = duracion.split('H');

            if (partesHoras.length > 1) {
                // Si hay una parte con 'H', extraer las horas
                horas = parseInt(partesHoras[0]);
                duracion = partesHoras[1];  // El resto contiene minutos
            } else {
                duracion = partesHoras[0];
            }

            // Dividir la parte restante por la letra 'M' para obtener los minutos
            if (duracion.includes('M')) {
                minutos = parseInt(duracion.split('M')[0]);
            }

            return horas + ":" + minutos
        },
        //Metodos para abrir y cerrar el Modal Informativo
        openModal() {
            this.isOpen = true;
        },
        closeModal() {
            this.isOpen = false;
        },
        async obtenerDetalleProyecto(p_id_proyecto) {
            try {
                const response = await obtenerDatosProyecto(p_id_proyecto);
                this.detalle_proyecto = response.data;
            } catch (error) {
                alert("error")
            }
        },
        proyectoSeleccionado(p_id_proyecto) {
            this.obtenerDetalleProyecto(p_id_proyecto);
        },
        limpiarModalDetalleProyecto() {
            this.detalle_proyecto = "";
        }
    },
    mounted() {
        this.obtenerDatosSala();
    }
}
</script>

<style scoped>
.nombre_evaluador {
    font-weight: bold !important;
    font-size: 15px !important;
}

.btn-close {
    width: 8px;
    height: 8px;
}
</style>