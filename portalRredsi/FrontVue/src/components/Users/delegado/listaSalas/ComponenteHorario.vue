<template>
    <div>
        <!-- Tabla de horarios -->
        <div class="container">
            <div>
                <h3 class="text-center m-0 mb-2">{{ sala.fechasEvento.fecha_inicio }}</h3>
            </div>
            <table class="table table-hover border table-responsive">
                <thead>
                    <tr>
                        <!-- <th class="text-center">Evaluadores</th> -->
                        <th v-for="time in timeSlots" :key="time" class="text-center time-slot">{{ time }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="fila_tabla" v-for="(detalle, index) in detalleSala" :key="index">
                        <td class="align-middle" v-for="(slot, i) in 24" :key="i"
                            :style="getStyle(i, detalle.hora_inicio, detalle.hora_fin)">
                            <div v-if="i === getMiddleSlot(detalle.hora_inicio, detalle.hora_fin) && isProjectTime(i, detalle.hora_inicio, detalle.hora_fin)"
                                class="d-flex justify-content-center align-items-center h-100" style="height: 100%;">
                                <a class="text-dark fw-semibold" type="button" @click="proyectoSeleccionado(detalle)">{{
                                    editarHorario ? 'Editar' : 'Ver Detalle' }}</a>
                            </div>
                        </td>
                    </tr>



                </tbody>
            </table>
        </div>
        <!-- Modal para editar un horario  -->
        <div class="modal fade" id="actualizarHorarioModal" tabindex="-1" aria-labelledby="actualizarHorarioLabel"
            aria-hidden="true">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title fs-3" id="actualizarHorarioLabel">Actualización de Horario</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
                            @click="cerrarModalActualizar"></button>
                    </div>
                    <div class="modal-body">
                        <form class="mt-4" @submit.prevent="actualizarHorario">
                            <div class="row mb-4 justify-content-center">
                                <div class="col-12 text-center mb-1">
                                    <label for="proyecto_codigo" class="fw-bold text-dark">Proyecto:</label>
                                </div>
                                <div class="col-12 col-md-8 text-center">
                                    <span class="text-dark">{{ detalle_proyecto.titulo }}</span>
                                </div>
                            </div>


                            <hr class="my-4">

                            <div class="row mb-4">
                                <div class="col-md-6">
                                    <label for="evaluador_1" class="fw-bold text-dark">Evaluador 1:</label>
                                    nombre del evaluador 1
                                </div>
                                <div class="col-md-6">
                                    <label for="evaluador_2" class="fw-bold text-dark">Evaluador 2:</label>
                                    nombre del evaluador 2
                                </div>
                            </div>

                            <hr class="my-4">

                            <div class="row mb-4">
                                <div class="col-md-4">
                                    <label for="fecha" class="form-label text-black">Fecha:</label>
                                    <input id="fecha" type="date" v-model="detalles_editables_horario.fecha"
                                        class="form-control text-dark" :min="sala.fechasEvento.fecha_inicio"
                                        :max="sala.fechasEvento.fecha_fin">
                                </div>
                                <div class="col-md-4">
                                    <label for="horario_inicio" class="form-label text-black">Hora de Inicio:</label>
                                    <input id="horario_inicio" v-model="detalles_editables_horario.hora_inicio"
                                        type="time" class="form-control text-dark" min="06:00" max="18:30" step="1800"
                                        required>
                                </div>
                                <div class="col-md-4">
                                    <label for="horario_fin" class="form-label text-black">Hora de Fin:</label>
                                    <input id="horario_fin" type="time" v-model="detalles_editables_horario.hora_fin"
                                        class="form-control text-dark" min="06:00" max="18:30" step="1800" required>
                                </div>
                            </div>

                            <div class="text-center">
                                <button class="btn text-dark fw-bold" type="submit" id="asignar_horario"
                                    style="background-color: rgb(255, 182, 6);">
                                    Actualizar Horario
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal con detalles del proyecto  -->
        <div class="modal fade" id="detalle_proyecto" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content bg-light shadow-sm border border-dark border-5 rounded-5 text-dark">
                    <div class="modal-header">
                        <h3 class="modal-title w-100 fs-5 text-dark text-wrap text-center" id="modalLabel">
                            {{ detalle_proyecto.titulo }}
                        </h3>
                        <button type="button" class="btn-close me-1 mt-1" data-bs-dismiss="modal" aria-label="Close"
                            @click="limpiarModalDetalleProyecto"></button>
                    </div>

                    <div class="modal-body text-center mt-3">
                        <div class="row align-items-start text-center">
                            <div class="col-md-6">
                                <h4 class="fs-6 text-dark mb-3">Ponentes</h4>
                                <div v-if="ponentes.length === 0" class="fs-7 text-muted">No se registraron ponentes
                                </div>
                                <div v-else>
                                    <div class="ponente-item mb-2" v-for="(ponente, index) in ponentes" :key="index">
                                        <span class="fs-6 text-dark">{{ ponente.nombres }} {{ ponente.apellidos
                                            }}</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6 border-start">
                                <h4 class="fs-6 text-dark mb-3">Evaluadores</h4>
                                <div v-if="evaluadoresProyectoSeleccionado.length === 0" class="fs-7 text-muted">No se
                                    registraron evaluadores</div>
                                <div v-else>
                                    <div class="evaluador-item mb-2"
                                        v-for="(evaluador, index) in evaluadoresProyectoSeleccionado" :key="index">
                                        <span class="fs-6 text-dark">{{ evaluador.nombres }} {{ evaluador.apellidos
                                            }}</span>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <!-- Línea de separación superior para la siguiente fila -->
                        <hr class="border-dark my-4">

                        <div class="row align-items-center text-center">
                            <div class="col-md-6">
                                <h4 class="fs-6 text-dark">Horarios</h4>
                                <p class="fs-6 text-muted mb-0">{{ horariosProyectoSeleccionado.hora_inicio }} - {{
                                    horariosProyectoSeleccionado.hora_fin }}</p>

                            </div>
                            <div class="col-md-6 border-start">
                                <h4 class="fs-6 text-dark">URL Propuesta Escrita</h4>
                                <p class="fs-6">
                                    <a :href="detalle_proyecto.url_propuesta_escrita" target="_blank"
                                        class="text-primary">Ver Propuesta</a>
                                </p>
                            </div>
                        </div>
                        <!-- Línea de separación superior para la siguiente fila -->
                        <hr class="border-dark my-4">

                        <div class="row justify-content-center align-items-center text-center">
                            <div class="col-md-6">
                                <h4 class="fs-5 text-dark">URL de presentación</h4>
                                <p class="fs-6">
                                    <a v-if="existe_presentacion" :href="url_presentacion" target="_blank"
                                        class="text-primary">
                                        <span>Ver
                                            presentación</span>
                                    </a>
                                    <span v-else class="text-dark">No hay presentación</span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { obtenerDetalleSala, obtenerDatosProyecto, obtenerPonentesProyecto, actualizarHorarioAsignado } from "@/services/salasDelegadoService";
import { obtenerEvaluadoresProyecto, obtenerUrlPresentacionProyecto } from "@/services/delegadoService";
import { useToastUtils } from '@/utils/toast';

export default {
    props: {
        sala: Object,
        editarHorario: Boolean || false,
    },
    setup() {
        const { showSuccessToast, showErrorToast, showInfoToast, showWarningToast } = useToastUtils();
        return {
            showInfoToast,
            showErrorToast,
            showSuccessToast,
            showWarningToast
        }
    },
    data() {
        return {
            timeSlots: [
                "6:00am", "6:30am", "7:00am", "7:30am", "8:00am", "8:30am", "9:00am", "9:30am",
                "10:00am", "10:30am", "11:00am", "11:30am", "12:00pm", "12:30pm", "1:00pm", "1:30pm",
                "2:00pm", "2:30pm", "3:00pm", "3:30pm", "4:00pm", "4:30pm", "5:00pm", "5:30pm", "6:00pm", "6:30pm"
            ],
            detalleSala: [],
            copiaDetalleSala: [],
            evaluadores: [],
            ponentes: [],
            url_presentacion: "",
            existe_presentacion: false,
            horariosProyectoSeleccionado: {
                hora_inicio: "",
                hora_fin: ""
            },
            evaluadoresProyectoSeleccionado: [],
            detalle_proyecto: {},
            detalles_editables_horario: {}
        }

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

                // Filtra los proyectos que ya están en la sala para que no salgan duplicados
                this.detalleSala = this.detalleSala.filter((item, index, self) => {
                    // Usamos 'findIndex' para ver si el mismo 'id_sala' y 'id_proyecto_convocatoria' ya apareció antes
                    return self.findIndex(
                        elem => elem.id_sala === item.id_sala && elem.id_proyecto_convocatoria === item.id_proyecto_convocatoria
                    ) === index;
                });

                this.copiaDetalleSala = JSON.parse(JSON.stringify(this.detalleSala));

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
                this.showInfoToast("Aún no se han asignado proyectos a esta sala");
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
            if (horas < 10) {
                horas = `0${horas}`;
            }
            return horas + ":" + minutos
        },
        async obtenerDetalleProyecto(p_id_proyecto) {
            try {
                const response = await obtenerDatosProyecto(p_id_proyecto);
                this.detalle_proyecto = response.data;
            } catch (error) {
                alert("error")
            }
        },
        async proyectoSeleccionado(p_detalle_sala) {

            if (this.editarHorario) {
                $("#actualizarHorarioModal").modal('show');
                // Se busca en la copia del detalle de sala el id del proyecto para traer los datos editables 
                this.detalles_editables_horario = this.copiaDetalleSala.find(detalle => detalle.id_proyecto === p_detalle_sala.id_proyecto);
                this.detalles_editables_horario.hora_inicio = this.obtenerHoraMinutos(this.detalles_editables_horario.hora_inicio);
                this.detalles_editables_horario.hora_fin = this.obtenerHoraMinutos(this.detalles_editables_horario.hora_fin);
                this.detalles_editables_horario.id_proyecto_convocatoria = p_detalle_sala.id_proyecto_convocatoria;
                this.detalles_editables_horario.id_sala = p_detalle_sala.id_sala;
                ;

                this.detalle_proyecto = "";
                this.obtenerDetalleProyecto(p_detalle_sala.id_proyecto);
                console.log(p_detalle_sala)

            } else {
                $("#detalle_proyecto").modal('show');

                // Inicializar variables antes de la carga de datos
                this.ponentes = "";
                this.evaluadoresProyectoSeleccionado = "";
                this.horariosProyectoSeleccionado.hora_inicio = "";
                this.horariosProyectoSeleccionado.hora_fin = "";

                // Obtener el horario asignado al proyecto sin necesidad de hacer una consulta extra
                const horarioProyectoEspecifico = this.buscarProyectoPorId(p_detalle_sala.id_proyecto);
                if (horarioProyectoEspecifico) {
                    this.horariosProyectoSeleccionado.hora_inicio = this.formatearHora(this.obtenerHoraMinutos(horarioProyectoEspecifico.hora_inicio));
                    this.horariosProyectoSeleccionado.hora_fin = this.formatearHora(this.obtenerHoraMinutos(horarioProyectoEspecifico.hora_fin));
                }
                this.obtenerDetalleProyecto(p_detalle_sala.id_proyecto);

                // Ejecutar todas las consultas en paralelo y manejar los resultados de manera independiente
                const [responseEvaluadores, responsePonentes, responseUrlPresentacion] = await Promise.allSettled([
                    obtenerEvaluadoresProyecto(p_detalle_sala.id_proyecto),
                    obtenerPonentesProyecto(p_detalle_sala.id_proyecto),
                    obtenerUrlPresentacionProyecto(p_detalle_sala.id_proyecto)
                ]);

                // Evaluadores
                if (responseEvaluadores.status === "fulfilled") {
                    this.evaluadoresProyectoSeleccionado = responseEvaluadores.value;
                } else {
                    console.error("Error al obtener evaluadores:", responseEvaluadores.reason);
                }

                // Ponentes
                if (responsePonentes.status === "fulfilled") {
                    this.ponentes = responsePonentes.value.data.ponentes;
                } else {
                    console.error("Error al obtener ponentes:", responsePonentes.reason);
                }

                // URL de presentación
                if (responseUrlPresentacion.status === "fulfilled") {
                    this.url_presentacion = responseUrlPresentacion.value.data;
                    this.existe_presentacion = true;
                } else {
                    this.existe_presentacion = false;
                    console.error("Error al obtener URL de presentación:", responseUrlPresentacion.reason);
                }
            }
        },
        async actualizarHorario() {
            try {
                if (this.detalles_editables_horario.hora_inicio < this.detalles_editables_horario.hora_fin) {
                    if ( this.detalles_editables_horario.hora_inicio == this.detalles_editables_horario.hora_fin ) {
                        this.showInfoToast("Ya hay un proyecto asignado a esta hora o estas ingresando la misma hora en los dos campos, intenta con otro horario");
                    } else {
                        await actualizarHorarioAsignado(
                            this.detalles_editables_horario.id_sala,
                            this.detalles_editables_horario.id_proyecto_convocatoria,
                            this.detalles_editables_horario.fecha,
                            this.detalles_editables_horario.hora_inicio,
                            this.detalles_editables_horario.hora_fin
                        );

                        // ALERTA Y RECARGA DE COMPONENTES DE LA VISTA 
                        this.showSuccessToast("Horario actualizado con exito");
                        this.obtenerDatosSala();
                        $("#actualizarHorarioModal").modal('hide');
                    }
                } else {
                    this.showWarningToast("Debes ingresar una hora de finalización mayor a la de inicio")
                }


            } catch (error) {
                console.log(error);
                this.showErrorToast("No se pudo actualizar el horario");
            }
        }
        ,
        cerrarModalActualizar() {
            this.obtenerDatosSala();

        },
        limpiarModalDetalleProyecto() {
            this.detalle_proyecto = "";
        },
        buscarProyectoPorId(p_id_proyecto) {
            // Busca el primer detalle que coincida con el id_proyecto
            const detalleEncontrado = this.copiaDetalleSala.find(detalle => detalle.id_proyecto == p_id_proyecto);

            // Si lo encuentra, lo retorna; de lo contrario, maneja un resultado no encontrado
            if (detalleEncontrado) {
                return detalleEncontrado;
            } else {
                console.warn('No se encontró el proyecto con el id:', p_id_proyecto);
                return null; // O maneja como prefieras
            }
        },
        formatearHora(hora) {
            // Verifica si la hora está en formato HH:mm
            const [h, m] = hora.split(':');
            let horas = parseInt(h, 10);
            const minutos = m;

            // Determina si es AM o PM
            const modifier = horas < 12 ? 'AM' : 'PM';

            // Convierte las horas a formato 12
            if (horas === 0) {
                horas = 12; // 00:xx a 12:xx AM
            } else if (horas > 12) {
                horas -= 12; // 13:xx a 1:xx PM
            }

            return `${horas}:${minutos} ${modifier}`;
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