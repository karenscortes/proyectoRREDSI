<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-user-group fa-1.5x text-dark mb-3"></i>
        </div>
        <h2 class="text-dark text-left font-weight-bold">
            Suplentes
            <i type="button" class="fa-regular fa-square-plus fa-lg text-dark" @click="openModal"></i>
        </h2>

        <p class="text-dark text-left">
            Tipo: {{ nuevoTipo }} <br>
            Nombre: {{ suplenteSeleccionado ? `${suplenteSeleccionado.nombres} ${suplenteSeleccionado.apellidos}` : ''
            }}
        </p>

        <div v-if="isModalOpen" class="modal">
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="modal-title">Agregar Suplente</h2>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
                        style="font-size: 0.75rem; padding: 0.25rem; width: 1.5rem; height: 1.5rem;">
                        <span @click="closeModal">&times;</span>
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

                    <div class="form-group">
                        <label for="suplente">Seleccionar Suplente (por nombre):</label>
                        <select v-model="suplenteSeleccionado" id="suplente" class="form-control custom-select">
                            <option value="" disabled selected>Seleccionar Suplente</option>
                            <option v-for="(suplente, index) in suplentes" :key="index" :value="suplente">
                                {{ suplente.nombres }} {{ suplente.apellidos }}
                            </option>
                        </select>
                    </div>
                    <div class="button-container text-center">
                        <button class="btn btn-warning font-weight-bold btn-lg" @click="addSuplente">Añadir</button>
                    </div>
                </div>
            </div>
        </div>
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
        id_suplente: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            isModalOpen: false,
            suplentes: [],
            nuevoTipo: '',
            suplenteSeleccionado: null,
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
                this.suplentes = await obtenerAsistentesSuplentes(1); 
                console.log("Suplentes obtenidos:", this.suplentes);
            } catch (error) {
                this.showErrorToast("Error al obtener los asistentes:");
            }
        },
        async fetchProyectoConvocatoria() {
            try {
                const response = await obtenerProyectoConvocatoria(this.idProyecto);
                this.idProyectoConvocatoria = response.data.proyecto_convocatoria.id_proyecto_convocatoria;
                console.log("ID Proyecto Convocatoria:", this.idProyectoConvocatoria);
            } catch (error) {
                this.showErrorToast("Error al obtener el proyecto convocatoria:");
            }
        },
        async fetchSuplentesSeleccionados() {
            try {
                
                const suplenteData = await obtenerSuplentes(this.id_suplente, this.idProyecto, this.tipo_usuario);
                if (suplenteData && suplenteData.length > 0) {    
                    this.suplenteSeleccionado = suplenteData[0];
                    this.nuevoTipo = suplenteData[0].tipo_usuario;
                    console.log("Suplente seleccionado:", this.suplenteSeleccionado);
                } else {
                    console.warn("No se encontraron suplentes para el id_suplente:", this.id_suplente);
                    this.showInfoToast("No hay suplentes asignados a este proyecto.");
                }
            } catch (error) {
                console.error("Error al obtener los suplentes seleccionados:", error);
                // this.showErrorToast("Error al obtener los suplentes seleccionados."); 
            }
        },

        async addSuplente() {
            try {
                await insertarSuplente(
                    this.suplenteSeleccionado.id_usuario,
                    this.idEtapa,
                    this.idProyecto,
                    this.idProyectoConvocatoria,
                    this.nuevoTipo
                );

                this.showSuccessToast("Suplente insertado con éxito");
                this.$emit('suplenteSeleccionado', {
                    suplente: this.suplenteSeleccionado,
                    tipo: this.nuevoTipo
                });
                this.resetForm();
                this.closeModal();
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
        console.log("ID Suplente en mounted:", this.id_suplente);
        await this.fetchSuplentesSeleccionados();
    }
};
</script>



<style scoped>
h2 {
    font-size: 0.8rem;
    margin-bottom: 2px;
}

.modal {
    display: block;
    /* Mostrar el modal */
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
    margin: 10% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 40%;
    max-width: 500px;
}

.close {
    color: #aaa;
    font-size: 28px;
    font-weight: bold;
    float: right;
    cursor: pointer;
}

.close:hover,
.close:focus {
    color: #000;
    text-decoration: none;
}

select {
    display: block;
    width: 100%;
    max-height: 200px;
    overflow-y: auto;
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
</style>
