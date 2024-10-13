<template>
    <div class="feature">
        <div class="icon-custom text-center">
            <i class="fa-solid fa-user-group fa-3x"></i>
        </div>
        <h2 class="text-left font-weight-bold text-yellow">
            Suplentes
            <i type="button" class="fa-regular fa-square-plus fa-1x text-yellow" @click="openModal"></i>
        </h2>

        <!-- Suplentes Ponentes -->
        <div v-if="suplentesPonentes.length > 0">
            <span class="text-left font-weight-bold">Suplentes Ponentes</span>
            <p class="text-dark suplente-details text-left" v-for="suplente in suplentesPonentes"
                :key="suplente.nombres">
                {{ suplente.nombres }} {{ suplente.apellidos }}
            </p>
        </div>

        <!-- Suplentes Evaluadores -->
        <div v-if="suplentesEvaluadores.length > 0">
            <span class="text-left font-weight-bold">Suplentes Evaluadores</span>
            <p class="text-dark suplente-details text-left" v-for="suplente in suplentesEvaluadores"
                :key="suplente.nombres">
                {{ suplente.nombres }} {{ suplente.apellidos }}
            </p>
        </div>

        <!-- Modal para agregar suplente -->
        <transition name="modal-fade">
            <div v-if="state.isModalOpen" class="modal" @click.self="closeModal">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2 class="modal-title">Agregar Suplente</h2>
                        <button type="button" class="btn-close" @click="closeModal" aria-label="Close">
                            <span>&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="form-group">
                            <label for="tipo">Tipo:</label>
                            <select v-model="state.nuevoTipo" id="tipo" class="form-control custom-select">
                                <option value="" disabled selected>Seleccionar Tipo</option>
                                <option value="suplenteEvaluador">Suplente Evaluador</option>
                                <option value="suplentePonente">Suplente Ponente</option>
                            </select>
                        </div>
                        <div class="form-group" v-if="state.nuevoTipo === 'suplentePonente'">
                            <label for="ponente">Seleccionar Ponente a reemplazar:</label>
                            <select v-model="state.evaluadorSeleccionado" id="ponente"
                                class="form-control custom-select">
                                <option value="" disabled selected>Seleccionar Ponente</option>
                                <option v-for="(ponente, index) in ponentes" :key="index" :value="ponente.id_usuario">
                                    {{ ponente.nombres }} {{ ponente.apellidos }}
                                </option>
                            </select>
                        </div>
                        <div class="form-group" v-else>
                            <label for="evaluador">Seleccionar Evaluador a reemplazar:</label>
                            <select v-model="state.evaluadorSeleccionado" id="evaluador"
                                class="form-control custom-select">
                                <option value="" disabled selected>Seleccionar Evaluador</option>
                                <option v-for="(evaluador, index) in evaluadores.presencial" :key="index"
                                    :value="evaluador.id_usuario"
                                    :disabled="esEvaluadorDesactivado(evaluador.id_usuario)">
                                    {{ evaluador.nombres }} {{ evaluador.apellidos }}
                                </option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="suplente">Seleccionar Suplente:</label>
                            <select v-model="state.suplenteSeleccionado" id="suplente"
                                class="form-control custom-select">
                                <option value="" disabled selected>Seleccionar Suplente</option>
                                <option v-for="(asistente, index) in state.asistentes" :key="index"
                                    :value="asistente.id_usuario">
                                    {{ asistente.nombres }} {{ asistente.apellidos }}
                                </option>
                            </select>
                        </div>
                        <div class="button-container text-center">
                            <button class="btn btn-warning font-weight-bold btn-lg" @click="addSuplente"
                                :disabled="isCalificado">Añadir</button>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import { reactive, onMounted, computed } from 'vue';
import { useToastUtils } from '@/utils/toast';
import { obtenerAsistentesSuplentes, insertarSuplente, obtenerProyectoConvocatoria, obtenerSuplentes } from '../../../../../services/delegadoService';

export default {
    name: 'SuplentesCom',
    props: {
        idProyecto: {
            type: Number,
            required: true
        },
        idEtapa: {
            type: Number,
            required: true
        },
        proyecto: {
            type: Object,
            required: true
        },
        isCalificado: {
            type: Boolean,
            required: true
        },
        evaluadores: Array,
        ponentes: Array,
    },
    setup(props, { emit }) {
        const state = reactive({
            isModalOpen: false,
            suplentes: [],
            suplentesPonentes: [],
            suplentesEvaluadores: [],
            asistentes: [],
            nuevoTipo: '',
            suplenteSeleccionado: null,
            evaluadorSeleccionado: null,
            idProyectoConvocatoria: null,
            evaluadoresDesactivados: []
        });

        const { showSuccessToast, showErrorToast } = useToastUtils();

        const suplentesPonentes = computed(() => {
            return state.suplentes.filter(suplente => suplente.tipo_usuario === 'suplentePonente');
        });

        const suplentesEvaluadores = computed(() => {
            return state.suplentes.filter(suplente => suplente.tipo_usuario === 'suplenteEvaluador');
        });

        const esEvaluadorDesactivado = (idUsuario) => {
            return state.evaluadoresDesactivados.includes(idUsuario);
        };

        const openModal = async () => {
            state.isModalOpen = true;
            try {
                await fetchAsistentes();
                await fetchProyectoConvocatoria();
            } catch (error) {
                state.isModalOpen = false;
            }
        };

        const closeModal = () => {
            state.isModalOpen = false;
        };

        const fetchAsistentes = async () => {
            try {
                state.asistentes = await obtenerAsistentesSuplentes(1);
            } catch (error) {
                showErrorToast("Error al obtener los asistentes:");
            }
        };

        const fetchProyectoConvocatoria = async () => {
            try {
                const response = await obtenerProyectoConvocatoria(props.idProyecto);
                state.idProyectoConvocatoria = response.data.proyecto_convocatoria.id_proyecto_convocatoria;
            } catch (error) {
                showErrorToast("Error al obtener el proyecto convocatoria:");
            }
        };

        const fetchSuplentes = async () => {
            try {
                const suplenteData = await obtenerSuplentes(props.idProyecto, state.tipo_usuario);
                state.evaluadoresDesactivados = [];
                state.suplentes = suplenteData;
                state.suplentesEvaluadores.forEach(suplente => {
                    if (!state.evaluadoresDesactivados.includes(suplente.id_usuario)) {
                        state.evaluadoresDesactivados.push(suplente.id_usuario);
                    }
                });
            } catch (error) {
                console.error("Error al obtener los suplentes seleccionados:", error);
            }
        };

        const addSuplente = async () => {
            if (state.suplenteSeleccionado === state.evaluadorSeleccionado) {
                showErrorToast("Debe seleccionar un suplente diferente al evaluador.");
                return;
            }
            try {
                await insertarSuplente(
                    state.suplenteSeleccionado,
                    props.idEtapa,
                    props.idProyecto,
                    state.idProyectoConvocatoria,
                    state.nuevoTipo,
                    state.evaluadorSeleccionado
                );
                showSuccessToast("Suplente insertado con éxito");
                state.evaluadoresDesactivados.push(state.evaluadorSeleccionado);
                await fetchSuplentes(); 

                resetForm();
                closeModal();
            } catch (error) {
                showErrorToast("Error al agregar suplente:");
            }
        };

        const resetForm = () => {
            state.nuevoTipo = '';
            state.suplenteSeleccionado = null;
            state.evaluadorSeleccionado = null;
        };

        onMounted(async () => {
            await fetchSuplentes();
        });

        return {
            state,
            suplentesPonentes,
            suplentesEvaluadores,
            openModal,
            closeModal,
            fetchAsistentes,
            fetchProyectoConvocatoria,
            fetchSuplentes,
            addSuplente,
            resetForm,
            esEvaluadorDesactivado
        };
    }
};
</script>



<style scoped>
.icon-custom {
    color: #ffb606;
    margin-bottom: 0.5rem;
}

.text-yellow {
    color: #ffb606;
}

h2 {
    font-size: 1.1rem;
    margin-bottom: 3px;
}

.suplente-details {
    font-size: 0.8rem;
    color: #000;
}

.text-left {
    text-align: left;
}

p {
    margin-bottom: 0.2rem;
}

.modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #888;
    width: 40%;
    max-width: 500px;
    transition: transform 0.3s ease-in-out;
    transform: translateY(0);
}

button.btn-close {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    margin-left: auto;
    color: #333;
}

.button-container {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}

button.btn-lg {
    padding: 6px 12px;
    font-size: 1rem;
    width: 25%;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.modal-fade-enter,
.modal-fade-leave-to {
    opacity: 0;
    transform: translateY(-30px);
}
</style>
