<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-user-group fa-1.5x text-dark mb-3"></i>
        </div>
        <h2 class="text-dark text-left font-weight-bold">
            Suplentes
            <i type="button" class="fa-regular fa-square-plus fa-lg text-dark" @click="openModal"></i>
        </h2>

        <p class="text-dark text-left" v-for="suplente in suplentes" :key="suplente.nombres">
            {{ suplente.nombres }} {{ suplente.apellidos }} <strong>{{ suplente.tipo_usuario }}</strong>
        </p>
        
        <!-- Modal para agregar suplente -->
        <transition name="modal-fade">
            <div v-if="isModalOpen" class="modal" @click.self="closeModal">
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
                            <select v-model="nuevoTipo" id="tipo" class="form-control custom-select">
                                <option value="" disabled selected>Seleccionar Tipo</option>
                                <option value="suplenteEvaluador">Suplente Evaluador</option>
                                <option value="suplentePonente">Suplente Ponente</option>
                            </select>
                        </div>
                        <div class="form-group" v-if="nuevoTipo === 'suplentePonente'">
                            <label for="suplente">Seleccionar Ponente a reemplazar :</label>
                            <select v-model="evaluadorSeleccionado" id="evaluador" class="form-control custom-select">
                                <option value="" disabled selected>Seleccionar Ponente</option>
                                <option v-for="(ponente, index) in ponentes" :key="index" :value="ponente.id_usuario">
                                    {{ ponente.nombres }} {{ ponente.apellidos }}
                                </option>
                            </select>
                        </div>
                        <div class="form-group" v-else>
                            <label for="suplente">Seleccionar Evaluador a reemplazar :</label>
                            <select v-model="evaluadorSeleccionado" id="evaluador" class="form-control custom-select">
                                <option value="" disabled selected>Seleccionar Evaluador</option>
                                <option v-for="(evaluador, index) in evaluadores.presencial" :key="index" :value="evaluador.id_usuario">
                                    {{ evaluador.nombres }} {{ evaluador.apellidos }}
                                </option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="asistente">Seleccionar Suplente (por nombre):</label>
                            <select v-model="suplenteSeleccionado" id="asistente" class="form-control custom-select">
                                <option value="" disabled selected>Seleccionar Suplente</option>
                                <option v-for="(asistente, index) in asistentes" :key="index" :value="asistente.id_usuario">
                                    {{ asistente.nombres }} {{ asistente.apellidos }}
                                </option>
                            </select>
                        </div>
                        <div class="button-container text-center">
                            <button class="btn btn-warning font-weight-bold btn-lg" @click="addSuplente">Añadir</button>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
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
        evaluadores: Array,
        ponentes: Array,
    },
    data() {
        return {
            isModalOpen: false,
            suplentes: [],
            asistentes: [],
            nuevoTipo: '',
            suplenteSeleccionado: null,
            evaluadorSeleccionado: null,
            idProyectoConvocatoria: null,
            tipo_usuario: ''
        };
    },
    setup() {
        const { showSuccessToast, showErrorToast } = useToastUtils();
        return { showSuccessToast, showErrorToast };
    },
    methods: {
        async openModal() {
            this.isModalOpen = true;
            try {
                await this.fetchAsistentes();
                await this.fetchProyectoConvocatoria();
            } catch (error) {
                this.isModalOpen = false;
            }
        },
        closeModal() {
            this.isModalOpen = false;
        },
        async fetchAsistentes() {
            try {
                this.asistentes = await obtenerAsistentesSuplentes(1);
            } catch (error) {
                this.showErrorToast("Error al obtener los asistentes:");
            }
        },
        async fetchProyectoConvocatoria() {
            try {
                const response = await obtenerProyectoConvocatoria(this.idProyecto);
                this.idProyectoConvocatoria = response.data.proyecto_convocatoria.id_proyecto_convocatoria;
            } catch (error) {
                this.showErrorToast("Error al obtener el proyecto convocatoria:");
            }
        },
        async fetchSuplentes() {
            try {
                const suplenteData = await obtenerSuplentes(this.idProyecto, this.tipo_usuario);
                this.suplentes = suplenteData;
            } catch (error) {
                console.error("Error al obtener los suplentes seleccionados:", error);
            }
        },

        async addSuplente() {
            try {
                await insertarSuplente(
                    this.suplenteSeleccionado,
                    this.idEtapa,
                    this.idProyecto,
                    this.idProyectoConvocatoria,
                    this.nuevoTipo,
                    this.evaluadorSeleccionado
                );
                this.showSuccessToast("Suplente insertado con éxito");
                this.resetForm();
                this.closeModal();
                this.fetchSuplentes();
            } catch (error) {
                this.showErrorToast("Error al agregar suplente:");
            }
        },
        resetForm() {
            this.nuevoTipo = '';
            this.suplenteSeleccionado = null;
        }
    },
    async mounted() {
        await this.fetchSuplentes();
    }
};
</script>

<style scoped>
h2 {
    font-size: 0.8rem;
    margin-bottom: 2px;
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

/* Transiciones dinámicas */
.modal-fade-enter-active, .modal-fade-leave-active {
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.modal-fade-enter, .modal-fade-leave-to /* .modal-fade-leave-active en Vue 2 */ {
    opacity: 0;
    transform: translateY(-30px);
}
</style>
