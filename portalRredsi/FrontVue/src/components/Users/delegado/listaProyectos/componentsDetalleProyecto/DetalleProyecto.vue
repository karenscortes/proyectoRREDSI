<template>
    <div class="container mt-5">
        <div class="row mb-2 mt-2">
            <div class="col">
                <div class="section_title text-center">
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
        <div class="why-choose-section ">
            <div class="container">
                <div class="row justify-content-between">
                    <div class="col-lg-6 order-2 order-lg-1">
                        <div class="section-title mt-4 text-left">
                            <h2>Información del proyecto</h2>
                        </div>
                        <div class="row my-4 gy-3">
                            <!-- Ponentes -->
                            <div class="col-6 col-md-6">
                                <PonentesCom :ponentes="ponentes" />
                            </div>
                            <!-- Evaluadores -->
                            <div class="col-6 col-md-6">
                                <EvaluadoresCom :evaluadores="evaluadores" :id_etapa="proyecto.id_etapa" />
                            </div>
                            <!-- Evento -->
                            <div v-if="cargarRubricaPresencial" class="col-6 col-md-6 mt-3">
                                <EventoCom :fecha="infoSala.fecha" :horaInicio="infoSala.hora_inicio"
                                    :horaFin="infoSala.hora_fin" :sala="infoSala.numero_sala" />
                            </div>
                            <!-- Suplentes -->
                            <div v-if="cargarRubricaPresencial" class="col-6 col-md-6 mt-3">
                                <SuplentesCom :idProyecto="proyecto.id_proyecto" :idEtapa="proyecto.id_etapa"
                                    :tipo="tipo" :evaluadores="evaluadores" :ponentes="ponentes"
                                />
                            </div>
                        </div>
                        <!-- Botones -->
                        <div class="row">
                            <div v-if="cargarRubricaPresencial" class="col-4">
                                <button type="button" class="btn btn-sm btn-warning font-weight-bold w-100 " title="Añadir Presentación"
                                    @click="openModal">
                                    <i class="fa-solid fa-plus"></i>
                                </button>
                            </div>
                            <div v-if="cargarRubricaPresencial" class="col-4">
                                <form :action="urlPresentacion" target="_blank">
                                    <button type="submit" class="btn btn-sm btn-warning font-weight-bold w-100" title="Ver Presentación">
                                        <i class="fa-solid fa-eye"></i>
                                    </button>
                                </form>
                            </div>
                            <div class="col-4">
                                <a :href="proyecto.url_propuesta_escrita" target="_blank"
                                    class="btn btn-sm btn-warning font-weight-bold w-100" title="Ver Proyecto">
                                    <i class="fa-solid fa-file-pdf"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    <!-- Imagen del detalle -->
                    <div class="col-lg-6 order-1 order-lg-2">
                        <div class="img-wrap mt-5 ">
                            <img src="../../../../../assets/img/course_5.jpg" class="img-fluid shadow-lg detail-image" />
                        </div>
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
                        <i style="margin-right: 10px;" class="fa-solid fa-check fa-lg"></i>
                        Respuesta rúbrica 1
                    </button>
                </div>
                <div id="collapseOne" class="collapse mt-5" aria-labelledby="headingOne"
                    data-bs-parent="#accordionExample">
                    <RubricaCom :proyecto="proyecto" 
                        :id_evaluador="id_evaluador1" :etapa="'Virtual'" />
                </div>
            </div>
            <div v-if="cargarRubricaPresencial" class="card p-2">
                <div id="headingTwo">
                    <button class="btn btn-block toggle-button collapsed rubrica-btn" type="button"
                        data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false"
                        aria-controls="collapseTwo">
                        <i style="margin-right: 10px;" class="fa-solid fa-check fa-lg"></i>
                        Respuesta rúbrica 2
                    </button>
                </div>
                <div id="collapseTwo" class="collapse mt-5" aria-labelledby="headingTwo"
                    data-bs-parent="#accordionExample">
                    <RubricaCom v-if="cargarRubricaPresencial" :proyecto="proyecto"
                        :id_evaluador="id_evaluador2" :etapa="'Presencial'" />
                </div>
            </div>
            <div v-if="cargarRubricaPresencial"  class="card p-2">
                <div id="headingThree">
                    <button class="btn btn-block toggle-button collapsed rubrica-btn" type="button"
                        data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false"
                        aria-controls="collapseThree">
                        <i style="margin-right: 10px;" class="fa-solid fa-x fa-lg"></i>
                        Respuesta rúbrica 3
                    </button>
                </div>
                <!-- <div id="collapseThree" class="collapse mt-5" aria-labelledby="headingThree"
                    data-bs-parent="#accordionExample">
                    <RubricaCom v-if="cargarRubricaPresencial" :proyecto="proyecto" 
                        :id_evaluador="id_evaluador3" :etapa="'presencial'" />
                    <h4 class="text-center text-dark mt-4 mb-4">Respaldo</h4>
                    <div class="custom-file-upload mx-auto">
                        <input type="file" id="comprobante_pago" name="comprobante_pago" />
                        <label for="comprobante_pago" class="upload-label">
                            <i class="fas fa-cloud-upload-alt"></i>
                            Selecciona un archivo
                        </label>
                    </div>
                </div> -->
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
import { obtenerEvaluadoresProyecto, obtenerPonentesProyecto, obtenerInfoSalaProyecto, insertarUrlPresentacion, obtenerUrlPresentacionProyecto } from '../../../../../services/delegadoService';

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
        const urlPresentacion = ref('');
        const suplente = ref({});
        const tipo = ref('');

        // Función para obtener los evaluadores del proyecto
        const fetchEvaluadores = async (id_proyecto) => {
            try {
                const id_etapa = props.proyecto.id_etapa;
                if (id_etapa == 2) {
                    const dataEvaluadorVirtual = await obtenerEvaluadoresProyecto(id_proyecto, id_etapa);
                    evaluadores.value.virtual = dataEvaluadorVirtual;
                    id_evaluador1.value = evaluadores.value.virtual[0].id_usuario;
                } else {
                    const dataEvaluadorVirtual = await obtenerEvaluadoresProyecto(id_proyecto, 2);
                    evaluadores.value.virtual = dataEvaluadorVirtual;
                    id_evaluador1.value = evaluadores.value.virtual[0].id_usuario;
                    const dataEvaluadorPresencial = await obtenerEvaluadoresProyecto(id_proyecto, 1);
                    evaluadores.value.presencial = dataEvaluadorPresencial;
                    if (evaluadores.value.presencial.length > 0) {
                        id_evaluador2.value = evaluadores.value.presencial[0].id_usuario;
                    } else if (evaluadores.value.presencial.length > 1) {
                        id_evaluador3.value = evaluadores.value.presencial[1].id_usuario;
                    }
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

        // Función para obtener presentación
        const fetchUrlPresentacion = async (id_proyecto) => {
            try {
                const response = await obtenerUrlPresentacionProyecto(id_proyecto);
                urlPresentacion.value = response.data.url_presentacion;
            } catch (error) {
                console.log('Error al obtener la URL de la presentación.');
            }
        };

        // Función para renderizar la vista
        const fetchAllData = async () => {
            try {
                await fetchEvaluadores(props.proyecto.id_proyecto);
                await fetchPonentes(props.proyecto.id_proyecto);
                if (props.proyecto.id_etapa == 1) {
                    await fetchInfoSala(props.proyecto.id_proyecto);
                    await fetchUrlPresentacion(props.proyecto.id_proyecto);
                }

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
                console.error('Error al cargar los datos del proyecto:', error);
                showErrorToast('Error al cargar los datos del proyecto.');
            }
        };

        const guardarPresentacion = async () => {
            try {
                await insertarUrlPresentacion(props.proyecto.id_proyecto, urlPresentacion.value);
                showInfoToast('Presentación guardada correctamente.');
                $('#presentationModal').modal('hide');
            } catch (error) {
                console.error('Error al guardar la URL de la presentación:', error);
                showErrorToast('Error al guardar la presentación. Por favor, intenta nuevamente.');
            }
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
            suplente,
            tipo,
            fetchAllData,
            guardarPresentacion,
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

.button-container {
    gap: 20px;
    margin-bottom: 20px;
}

.detail-image {
    max-width: 90%;
    border-radius: 8px;
    margin-top: 20px;
}

.rubrica-btn {
    padding: 8px 15px;
    font-size: 0.875rem;
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