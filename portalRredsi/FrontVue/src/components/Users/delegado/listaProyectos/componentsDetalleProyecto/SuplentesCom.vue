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
                <span class="close" @click="closeModal">&times;</span>
                <h4>Agregar Suplente</h4>

                <div class="form-group">
                    <label for="tipo">Tipo:</label>
                    <select v-model="nuevoTipo" id="tipo" class="form-control">
                        <option value="" disabled selected>Seleccionar Tipo</option>
                        <option v-for="(tipo, index) in tiposSuplentes" :key="index" :value="tipo">
                            {{ tipo }}
                        </option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="suplente">Seleccionar Suplente (por nombre):</label>
                    <select v-model="suplenteSeleccionado" id="suplente" class="form-control">
                        <option value="" disabled selected>Seleccionar Suplente</option>
                        <option v-for="(suplente, index) in suplentes" :key="index" :value="suplente">
                            {{ suplente.nombres }} {{ suplente.apellidos }}
                        </option>
                    </select>
                </div>

                <button class="btn btn-warning font-weight-bold" @click="addSuplente">Añadir</button>
            </div>
        </div>
    </div>
</template>

<script>
    import { useToastUtils } from '@/utils/toast';
    import { obtenerAsistentesSuplentes, insertarSuplente, obtenerProyectoConvocatoria } from '../../../../../services/delegadoService';

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
                tiposSuplentes: ['evaluador', 'suplenteEvaluador', 'ponente', 'suplentePonente', 'tutor'],
                nuevoTipo: '',
                suplenteSeleccionado: null,
                idProyectoConvocatoria: null
            };
        },
        setup() {
            const { showSuccessToast, showErrorToast, showInfoToast } = useToastUtils();
            return { showSuccessToast, showErrorToast, showInfoToast };
        },
        methods: {
            async openModal() {
                this.isModalOpen = true;
                await this.fetchAsistentes();
                await this.fetchProyectoConvocatoria();
            },
            closeModal() {
                this.isModalOpen = false;
            },
            async fetchAsistentes() {
                try {
                    this.suplentes = await obtenerAsistentesSuplentes(1);
                } catch (error) {
                    console.error("Error al obtener los asistentes:", error);
                }
            },
            async fetchProyectoConvocatoria() {
                try {
                    const response = await obtenerProyectoConvocatoria(this.idProyecto);
                    if (response) {
                        this.idProyectoConvocatoria = response.data.proyecto_convocatoria.id_proyecto_convocatoria;
                    } else {
                        console.error("No se encontró proyecto convocatoria para el ID del proyecto:", this.idProyecto);
                    }
                } catch (error) {
                    console.error("Error al obtener el proyecto convocatoria:", error);
                }
            },
            async addSuplente() {
                
                console.log("Datos del suplente seleccionado:", this.suplenteSeleccionado);
                console.log("ID Proyecto:", this.idProyecto);
                console.log("ID Etapa:", this.idEtapa);
                console.log("ID Proyecto Convocatoria:", this.idProyectoConvocatoria);
                console.log("Tipo de Suplente:", this.nuevoTipo);

                try {
                    await insertarSuplente(
                        this.suplenteSeleccionado.id_usuario,
                        this.idEtapa,
                        this.idProyecto,
                        this.idProyectoConvocatoria,
                        this.nuevoTipo
                    );

                    alert("Suplente insertado con éxito");
                    this.$emit('suplenteSeleccionado', {
                        suplente: this.suplenteSeleccionado,
                        tipo: this.nuevoTipo
                    });

                    this.resetForm();
                    this.closeModal();
                } catch (error) {
                    console.error("Error al agregar suplente:", error);
                    alert("Error al insertar el suplente. Por favor, intenta nuevamente.");
                }
            }
        },
        mounted(){
            this.suplentes.id_usuario = this.id_suplente;
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
    width: 50%;
    max-width: 600px;
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
</style>
