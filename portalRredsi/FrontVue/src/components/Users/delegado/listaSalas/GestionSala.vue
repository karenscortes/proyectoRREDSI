<template>
    <div>
        <div class="col-3">
            <a class="btn_regresar text-dark fw-bold d-flex align-items-center" @click="$emit('volver')">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                    fill="#00000" class="me-2">
                    <path d="m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z" />
                </svg>
                Lista de salas
            </a>
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
                <div class="container">



                    <form class="mt-4" @submit.prevent="asignarHorario">
                        <!-- Proyecto -->
                        <div class="row mb-4 justify-content-center">
                            <div class="col-12 col-md-6">
                                <label for="proyecto_codigo" class="fw-bold text-dark text-center">Proyecto:</label>
                                <select id="id_proyecto" v-model="proyectoSeleccionado"
                                    @change="seleccionarProyecto(proyectoSeleccionado.id_proyecto, proyectoSeleccionado.id_area_conocimiento, proyectoSeleccionado.id_institucion)"
                                    class="form-select text-dark" required>
                                    <option value="" disabled selected>Seleccione una opción</option>
                                    <option v-for="(proyecto, index) in listaProyectosSinAsignar" :key="index"
                                        :value="proyecto">
                                        {{ proyecto.titulo }}
                                    </option>
                                </select>
                            </div>
                        </div>
                        <!-- Ponentes -->
                        <div class="row mb-4">
                            <div class="col-md-6">
                                <label for="ponente_1" class="form-label text-black">Ponente 1:</label>
                                <input type="text" class="form-control" id="ponente_1" :value="ponente1" disabled>
                            </div>
                            <div class="col-md-6">
                                <label for="ponente_2" class="form-label text-black">Ponente 2 (Opcional):</label>
                                <input type="text" class="form-control" id="ponente_2" :value="ponente2" disabled>
                            </div>
                        </div>

                        <hr class="my-4">

                        <!-- Evaluadores -->
                        <div class="row mb-4">
                            <div class="col-md-6">
                                <label for="evaluador_1" class="fw-bold text-dark">Evaluador 1:</label>
                                <select id="id_evaluador_1" v-model="id_evaluador1" class="form-select text-dark"
                                    required>
                                    <option value="" disabled selected>Seleccione una opción</option>
                                    <option v-for="(evaluador, index) in evaluadoresFiltrados1" :key="index"
                                        :value="evaluador.id_evaluador">
                                        {{ evaluador.nombre_evaluador }} {{ evaluador.apellidos_evaluador }}
                                    </option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label for="evaluador_2" class="fw-bold text-dark">Evaluador 2:</label>
                                <select id="id_evaluador_2" v-model="id_evaluador2" class="form-select text-dark"
                                    required>
                                    <option value="" disabled selected>Seleccione una opción</option>
                                    <option v-for="(evaluador, index) in evaluadoresFiltrados2" :key="index"
                                        :value="evaluador.id_evaluador">
                                        {{ evaluador.nombre_evaluador }} {{ evaluador.apellidos_evaluador }}
                                    </option>
                                </select>
                            </div>
                        </div>

                        <hr class="my-4">

                        <div class="row mb-4">
                            <div class="col-md-4">
                                <label for="fecha" class="form-label text-black">Fecha:</label>
                                <input id="fecha" type="date" v-model="horario.fecha" class="form-control text-dark">
                            </div>
                            <div class="col-md-4">
                                <label for="horario_inicio" class="form-label text-black">Hora de Inicio:</label>
                                <input id="horario_inicio" type="time" v-model="horario.hora_inicio"
                                    class="form-control text-dark" min="06:00" max="18:30" step="1800" required>
                            </div>
                            <div class="col-md-4">
                                <label for="horario_fin" class="form-label text-black">Hora de Fin:</label>
                                <input id="horario_fin" type="time" v-model="horario.hora_fin"
                                    class="form-control text-dark" min="06:00" max="18:30" step="1800" required>
                            </div>
                        </div>

                        <!-- Submit Button -->
                        <div class="text-center">
                            <button class="btn text-dark fw-bold" type="submit" id="asignar_horario"
                                style="background-color: rgb(255, 182, 6);">
                                Asignar Horario
                            </button>
                        </div>
                    </form>
                </div>

                <div class="title-line mt-3"></div>
                <!-- Línea debajo del título -->

                <!-- Tabla Horarios agregados -->
                <ComponenteHorario ref="horario" :sala="sala" />
            </div>
        </div>

    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { obtenerPonentesProyecto, obetnerProyectosSinAsignarEtapaPresencial, obtenerPosiblesEvaluadoresEtapaPresencial, asignarEvaluadoresEtapaPresencial } from '@/services/salasDelegadoService';
import { obtenerProyectoConvocatoria } from '@/services/DelegadoService';
import ComponenteHorario from './ComponenteHorario.vue';
import { useToastUtils } from '@/utils/toast';

export default defineComponent({
    props: {
        sala: Object,
        index: Number
    },
    components: {
        ComponenteHorario
    },
    data() {
        const { showSuccessToast, showErrorToast, showWarningToast, showDefaultToast, showInfoToast } = useToastUtils();
        return {
            proyectoSeleccionado: {
                id_proyecto: "",
                titulo: "",
                id_institucion: "",
                id_area_conocimiento: ""
            },
            ponente1: "",
            ponente2: "",
            posiblesEvaluadores: [],
            id_evaluador1: "",
            id_evaluador2: "",
            horario: {
                fecha: "",
                hora_inicio: "",
                hora_fin: "",
            },
            showInfoToast,
            id_proyecto_convocatoria: "",
            evaluadores: [],
            listaProyectosSinAsignar: [],
            actualizarHorario: true,
        };
    },
    emits: ['component-selected'],
    methods: {
        selectComponent(componentName) {
            this.$emit('component-selected', componentName);
        },
        async asignarHorario() {
            try {
                if (this.horario.hora_inicio < this.horario.hora_fin) {
                    await asignarEvaluadoresEtapaPresencial(this.id_evaluador1, this.id_evaluador2, this.proyectoSeleccionado.id_proyecto, this.id_proyecto_convocatoria, this.sala.id_sala, this.horario.fecha, this.horario.hora_inicio, this.horario.hora_fin);

                    alert("La asignación del horario ha sido exitosa");
                    this.fetchProyectosSinAsignar();
                    this.limpiarFormulario();

                    // actualiza la tabla de horario 
                    this.$refs.horario.obtenerDatosSala();
                } else {
                    alert("Debes ingresar una hora de finalización mayor a la de inicio")
                }

            } catch (error) {
                alert("No se ha podido asignar el proyecto a esta sala");
            }
        },
        limpiarFormulario() {
            this.id_evaluador1 = "";
            this.id_evaluador2 = "";
            this.proyectoSeleccionado = "";
            this.id_proyecto_convocatoria = "";
            this.sala.id_sala = "";
            this.horario.fecha = "";
            this.horario.hora_inicio = "";
            this.horario.hora_fin = "";
            this.ponente1 = "";
            this.ponente2 = "";
        },
        async fetchProyectosSinAsignar() {
            try {
                const response = await obetnerProyectosSinAsignarEtapaPresencial();
                this.listaProyectosSinAsignar = response.data.proyectos;

            } catch (error) {
                this.showInfoToast("Todos los proyectos están asignados");
            }
        },
        async consultarPonentesProyecto(id_proyecto) {
            try {
                // Obtengo los ponentes del proyecto seleccionado
                const ponentes = await obtenerPonentesProyecto(id_proyecto);
                let listaPonentes = ponentes.data.ponentes;

                // Con esta condición valido cuantos ponentes tiene el proyecto y si impresión
                if (listaPonentes.length == 1) {
                    this.ponente1 = `${listaPonentes[0].nombres} ${listaPonentes[0].apellidos}`;
                    this.ponente2 = "";
                } else if (listaPonentes.length == 2) {
                    this.ponente1 = `${listaPonentes[0].nombres} ${listaPonentes[0].apellidos}`;
                    this.ponente2 = `${listaPonentes[1].nombres} ${listaPonentes[1].apellidos}`;
                }


            } catch (error) {
                this.ponente1 = "Sin ponente registrado";
                this.ponente2 = "Sin ponente registrado";
            }

        },
        async fetchPosiblesEvaluadores(p_id_area_conocimiento, p_id_institucion) {
            try {
                // Consulta los posibles evaluadores del proyecto seleccionado
                const response = await obtenerPosiblesEvaluadoresEtapaPresencial(p_id_area_conocimiento, p_id_institucion);
                this.posiblesEvaluadores = response.data.evaluadores;
                console.log(this.posiblesEvaluadores)
            } catch (error) {
                console.error(error)
            }
        },
        async seleccionarProyecto(p_id_proyecto, p_id_area_conocimiento, p_id_institucion) {
            await this.consultarPonentesProyecto(p_id_proyecto);
            await this.fetchPosiblesEvaluadores(p_id_area_conocimiento, p_id_institucion);

            const proyecto_convocatoria = await obtenerProyectoConvocatoria(p_id_proyecto);
            this.id_proyecto_convocatoria = proyecto_convocatoria.data.proyecto_convocatoria.id_proyecto_convocatoria;
        },

    },
    computed: {
        evaluadoresFiltrados1() {
            // Filtra los evaluadores para el primer select
            return this.posiblesEvaluadores.filter(evaluador => evaluador.id_evaluador !== this.id_evaluador2);
        },
        evaluadoresFiltrados2() {
            // Filtra los evaluadores para el segundo select
            return this.posiblesEvaluadores.filter(evaluador => evaluador.id_evaluador !== this.id_evaluador1);
        }
    },
    mounted() {
        this.fetchProyectosSinAsignar();
    }
});
</script>

<style scoped>
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