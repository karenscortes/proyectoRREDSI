<template>
    <div class="container mt-5">
        <div class="row mb-2 mt-2">
            <div class="col text-center">
                <div class="section_title">
                    <h1>Detalle del Proyecto</h1>
                </div>
            </div>
        </div>
        <div class="col-5 col-sm-3 my-3">
            <a class="btn_regresar text-dark fw-bold d-flex align-items-center" @click="$emit('volver')">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                    fill="#000000" class="me-2">
                    <path d="m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z" />
                </svg>
                Lista de proyectos
            </a>
        </div>
        <div class="why-choose-section">
            <div class="row justify-content-center">
                <div class="section-title mt-4 text-center">
                    <h2>Información del proyecto</h2>
                </div>
                <div class="col-lg-12 mt-4 p-3 bg-light rounded shadow-lg custom-shadow">
                    <div class="row text-center justify-content-center">
                        <template v-if="!isLoading">
                            <div class="col-md-3 d-flex flex-column align-items-center">
                                <EvaluadoresCom :evaluadores="evaluadores" :id_etapa="proyecto.id_etapa" />
                            </div>
                            <div class="col-md-3 d-flex flex-column align-items-center">
                                <PonentesCom :ponentes="ponentes" />
                            </div>
                            <div v-if="cargarRubricaPresencial" class="col-md-3 d-flex flex-column align-items-center">
                                <EventoCom :fecha="infoSala.fecha" :horaInicio="infoSala.hora_inicio"
                                    :horaFin="infoSala.hora_fin" :sala="infoSala.numero_sala" />
                            </div>
                            <div v-if="cargarRubricaPresencial" class="col-md-3 d-flex flex-column align-items-center">
                                <SuplentesCom :idProyecto="proyecto.id_proyecto" :idEtapa="proyecto.id_etapa"
                                    :tipo="tipo" :evaluadores="evaluadores" :ponentes="ponentes" />
                            </div>
                            <!-- Botones -->
                            <div class="col-lg-12 mt-4 ">
                                <div class="row justify-content-center">
                                    <div v-if="cargarRubricaPresencial" class="col-4">
                                        <button type="button" class="btn btn-sm btn-warning font-weight-bold w-100"
                                            @click="openModal">
                                            Añadir Presentación
                                        </button>
                                    </div>
                                    <div v-if="cargarRubricaPresencial" class="col-4">
                                        <a :href="urlPresentacionGuardada" target="_blank"
                                            class="btn btn-sm btn-warning font-weight-bold w-100">
                                            Ver Presentación
                                        </a>
                                    </div>
                                    <div class="col-4">
                                        <a :href="proyecto.url_propuesta_escrita" target="_blank"
                                            class="btn btn-sm btn-warning font-weight-bold w-100">
                                            Ver Proyecto
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </template>
                        <template v-else>
                            <div class="col-md-12">
                                <p>Cargando datos, por favor espere...</p>
                            </div>
                        </template>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal para ingresar la URL de la presentación -->
        <div class="modal fade" id="presentationModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
            aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2 class="modal-title" id="exampleModalLabel">Añadir URL de Presentación</h2>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
                            style="font-size: 0.75rem; padding: 0.25rem; width: 1.5rem; height: 1.5rem;"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="guardarPresentacion">
                            <div class="form-group">
                                <label for="urlPresentacion">URL de la Presentación</label>
                                <input type="url" class="form-control" id="urlPresentacion" v-model="urlPresentacion"
                                    placeholder="https://example.com/presentacion" required>
                            </div>
                            <div class="text-center">
                                <button type="submit" class="btn btn-warning">Guardar</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <div class="accordion pt-4 mt-3" id="accordionExample">
            <div class="card p-2">
                <div id="headingOne">
                    <button class="btn btn-block toggle-button collapsed rubrica-btn" type="button"
                        data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false"
                        aria-controls="collapseOne">
                        Respuestas calificación virtual
                    </button>
                </div>
                <div id="collapseOne" class="collapse mt-5" aria-labelledby="headingOne"
                    data-bs-parent="#accordionExample">
                    <div v-if="evaluadoresObtenidos == 'True'">
                        <RubricaCom :proyecto="proyecto" :id_evaluador="id_evaluador1" :etapa="'Virtual'" />
                    </div>
                </div>
            </div>
            <div v-if="cargarRubricaPresencial" class="card p-2">
                <div id="headingTwo">
                    <button class="btn btn-block toggle-button collapsed rubrica-btn" type="button"
                        data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false"
                        aria-controls="collapseTwo">
                        Respuestas calificación presencial (1)
                    </button>
                </div>
                <div id="collapseTwo" class="collapse mt-5" aria-labelledby="headingTwo"
                    data-bs-parent="#accordionExample">
                    <div v-if="evaluadoresObtenidos == 'True'">
                        <RubricaCom v-if="cargarRubricaPresencial" :proyecto="proyecto" :id_evaluador="id_evaluador2"
                            :etapa="'Presencial'" />
                    </div>
                </div>
            </div>
            <div v-if="cargarRubricaPresencial" class="card p-2">
                <div id="headingThree">
                    <button class="btn btn-block toggle-button collapsed rubrica-btn" type="button"
                        data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false"
                        aria-controls="collapseThree">
                        Respuestas calificación presencial (2)
                    </button>
                </div>
                <div id="collapseThree" class="collapse mt-5" aria-labelledby="headingThree"
                    data-bs-parent="#accordionExample">
                    <div v-if="evaluadoresObtenidos == 'True'">
                        <RubricaCom v-if="cargarRubricaPresencial" :proyecto="proyecto" :id_evaluador="id_evaluador3"
                            :etapa="'Presencial'" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import EvaluadoresCom from './EvaluadoresCom.vue';
import EventoCom from './EventoCom.vue';
import PonentesCom from './PonentesCom.vue';
import SuplentesCom from './SuplentesCom.vue';
import RubricaCom from './RubricaCom.vue';
import { useToastUtils } from '@/utils/toast';
import { obtenerEvaluadoresProyecto, obtenerPonentesProyecto, obtenerInfoSalaProyecto, insertarOActualizarUrlPresentacion, obtenerUrlPresentacionProyecto } from '../../../../../services/delegadoService';

export default {
    name: 'DetalleProyecto',
    props: {
        proyecto: {
            type: Object,
            required: true
        },
    },
    components: {
        EvaluadoresCom,
        PonentesCom,
        EventoCom,
        SuplentesCom,
        RubricaCom,
    },
    setup(props) {
        const { showSuccessToast, showErrorToast, showInfoToast } = useToastUtils();

        const cargarRubricaVirtual = ref(false);
        const cargarRubricaPresencial = ref(false);
        const evaluadores = ref({ virtual: [], presencial: [] });
        const id_evaluador1 = ref(0);
        const id_evaluador2 = ref(0);
        const id_evaluador3 = ref(0);
        const evaluadoresObtenidos = ref('False');
        const ponentes = ref([]);
        const infoSala = ref({
            fecha: '',
            hora_inicio: '',
            hora_fin: '',
            numero_sala: ''
        });
        const rubricas = ref([]);
        const tituloProyecto = ref('');
        const ponentesProyecto = ref('');
        const universidadProyecto = ref('');
        const puntajeTotal = ref(0);
        const urlPresentacionGuardada = ref('');
        const urlPresentacion = ref('');
        const suplente = ref({});
        const tipo = ref('');
        const isLoading = ref(true);

        // console.log('Estado del proyecto:', props.proyecto.estado_calificacion);

        // Función para obtener los evaluadores del proyecto
        const fetchEvaluadores = async (id_proyecto) => {
            try {
                const id_etapa = props.proyecto.id_etapa;
                if (id_etapa == 2) {
                    await fetchUrlPresentacion(props.proyecto.id_proyecto);
                    const dataEvaluadorVirtual = await obtenerEvaluadoresProyecto(id_proyecto, id_etapa);
                    evaluadores.value.virtual = dataEvaluadorVirtual;
                    id_evaluador1.value = evaluadores.value.virtual[0].id_usuario;
                    evaluadoresObtenidos.value = 'True';
                } else {
                    const dataEvaluadorVirtual = await obtenerEvaluadoresProyecto(id_proyecto, 2);
                    evaluadores.value.virtual = dataEvaluadorVirtual;
                    id_evaluador1.value = evaluadores.value.virtual[0].id_usuario;
                    const dataEvaluadorPresencial = await obtenerEvaluadoresProyecto(id_proyecto, 1);
                    evaluadores.value.presencial = dataEvaluadorPresencial;
                    if (evaluadores.value.presencial.length <= 1) {
                        id_evaluador2.value = evaluadores.value.presencial[0].id_usuario;
                    } else if (evaluadores.value.presencial.length > 1) {
                        id_evaluador2.value = evaluadores.value.presencial[0].id_usuario;
                        id_evaluador3.value = evaluadores.value.presencial[1].id_usuario;
                    } else {
                        showErrorToast("Error al obtener evaluadores.");
                    }
                    evaluadoresObtenidos.value = 'True';
                }
            } catch (error) {
                console.error('Error al obtener evaluadores:', error);
            }
        };

        // Función para obtener los ponentes del proyecto
        const fetchPonentes = async (id_proyecto) => {
            try {
                const data = await obtenerPonentesProyecto(id_proyecto);
                ponentes.value = data;
            } catch (error) {
                console.error('Error al obtener ponentes:', error);
            }
        };

        // Función para obtener informacion de sala para un proyecto
        const fetchInfoSala = async (id_proyecto) => {
            try {
                const data = await obtenerInfoSalaProyecto(id_proyecto);
                infoSala.value = data;
            } catch (error) {
                console.error('Error al obtener la información de la sala:', error);
            }
        };

        // Función para guardar la presentación
        const guardarPresentacion = async () => {
            try {
                await insertarOActualizarUrlPresentacion(props.proyecto.id_proyecto, urlPresentacion.value);
                showSuccessToast('Presentación guardada/actualizada correctamente.');
                urlPresentacionGuardada.value = urlPresentacion.value;
                $('#presentationModal').modal('hide');
            } catch (error) {
                showErrorToast('Error al guardar la presentación. Por favor, intenta nuevamente.');
            }
        };

        // Función para obtener presentación
        const fetchUrlPresentacion = async (id_proyecto) => {
            try {
                const response = await obtenerUrlPresentacionProyecto(id_proyecto);
                urlPresentacionGuardada.value = response.data;
            } catch (error) {
                console.log('Error al obtener la URL de la presentación.');
            }
        };

        // Función para cargar todos los datos del proyecto
        const fetchAllData = async () => {
            try {
                // Cargar evaluadores y ponentes en paralelo
                const evaluadoresPromise = fetchEvaluadores(props.proyecto.id_proyecto);
                const ponentesPromise = fetchPonentes(props.proyecto.id_proyecto);

                // Si está en etapa 1, cargar info de sala y URL de presentación
                let salaPromise, presentacionPromise;
                if (props.proyecto.id_etapa == 1) {
                    salaPromise = fetchInfoSala(props.proyecto.id_proyecto);
                    presentacionPromise = fetchUrlPresentacion(props.proyecto.id_proyecto);
                }

                // Ejecutar todas las promesas de carga de datos en paralelo
                await Promise.all([evaluadoresPromise, ponentesPromise, salaPromise, presentacionPromise]);

                // Configurar la rúbrica según los evaluadores
                if (evaluadores.value.virtual.length > 0 || evaluadores.value.presencial.length > 0) {
                    if (props.proyecto.id_etapa == 2) {
                        cargarRubricaVirtual.value = true;
                        cargarRubricaPresencial.value = false;
                    } else {
                        cargarRubricaPresencial.value = true;
                        cargarRubricaVirtual.value = true;
                    }
                }
            } catch (error) {
                showErrorToast('Error al cargar la información del proyecto.');
            } finally {
                isLoading.value = false;
            }
        };

        const openModal = () => {
            urlPresentacion.value = '';
            $('#presentationModal').modal('show');
        };

        onMounted(() => {
            fetchAllData();
        });

        return {
            cargarRubricaVirtual,
            cargarRubricaPresencial,
            evaluadores,
            id_evaluador1,
            id_evaluador2,
            id_evaluador3,
            ponentes,
            infoSala,
            rubricas,
            tituloProyecto,
            ponentesProyecto,
            universidadProyecto,
            puntajeTotal,
            urlPresentacion,
            urlPresentacionGuardada,
            suplente,
            evaluadoresObtenidos,
            tipo,
            fetchAllData,
            guardarPresentacion,
            openModal,
            isLoading,
        };
    },

};
</script>


<style scoped>
.btn_regresar:hover {
    cursor: pointer;
    color: #007bff;
}

.btn_regresar {
    padding: 8px 16px;
    border: 2px solid transparent;
    transition: background-color 0.3s ease, border-color 0.3s ease;
    display: inline-flex;
    align-items: center;
}

.btn_regresar:hover {
    background-color: rgba(0, 0, 0, 0.05);
    border-color: #000;
    cursor: pointer;
}

.btn_regresar svg {
    transition: transform 0.3s ease;
}

.btn_regresar:hover svg {
    transform: translateX(-4px);
}

.row.my-4 {
    border: 1px solid lightgray;
    padding: 10px;
}

.custom-shadow {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.toggle-button {
    background-color: #f8f9fa;
}

.card {
    margin-bottom: 10px;
}

.button-container {
    gap: 20px;
    margin-bottom: 20px;
}

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

.toggle-button {
    text-align: left;
    width: 100%;
    padding: 10px;
    border: none;
    background: none;
    color: #000;
    cursor: pointer;
}

.toggle-button:hover {
    background-color: #e0e0e0;
}

.feature {
    display: flex;
    flex-direction: column;
    align-items: start;
    margin-bottom: 15px;
}

.toggle-button {
    text-align: center;
    padding: 5px 20px;
    width: 100%;
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

@media only screen and (max-width: 767px) {
    .accordion {
        display: block;
    }
}
</style>