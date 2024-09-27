<template>
    <!-- Contenido principal -->
    <div class="become">
        <div class="container">
            <div class="row row-eq-height">
                <div class="col-lg-6 order-2 order-lg-1">
                    <div class="become_title">
                        <h1>Bienvenido al portal RREDSI</h1>
                    </div>
                    <p class="become_text">RREDSI es una red reconocida por su impacto en el desarrollo de proyectos de innovación y tecnología. A lo largo de los años, nuestros evaluadores han desempeñado un rol clave en garantizar la calidad y relevancia de los proyectos presentados. Su capacidad para analizar y proporcionar retroalimentación precisa ha contribuido significativamente al éxito de cada convocatoria. Los logros obtenidos demuestran el compromiso y la excelencia en cada evaluación realizada. RREDSI sigue avanzando como un motor de progreso para la ciencia y la innovación en Colombia. ¿Que esperas para unirte?</p>
                    <!-- Postulacion -->
                    <div class="become_button text-center trans_200">
                        <a href="#" type="button" data-bs-toggle="modal"
                        data-bs-target="#postulacionEvaluador">Postularme</a>
                    </div>
                </div>
                <div class="col-lg-6 order-1 order-lg-2">
                    <div class="become_image">
                        <img src="../assets/img/become.jpg" alt="img">
                    </div>
                </div>
                
            </div>
        </div>
    </div>
    <!-- Fin del contenido principal -->


    <!-- Modal postulacion -->
    <div class="modal fade" id="postulacionEvaluador" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border border-dark border-5 rounded-5 text-dark">
                <div class="modal-header text-center">
                    <h3 class="modal-title mt-3 w-100 fs-4  mr-1" id="modalLabel">Formulario de Postulación</h3>
                    <button type="button" class="btn-close mr-1 mt-3" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body mt-3">
                    <div class="row justify-content-center text-start">
                        <!-- Jornadas -->
                        <div class="col-5 text-dark font-weight-bold px-3 fs-6">Participación jornada virtual:</div>
                        <div class="col-5 mb-3 px-3">
                            <select v-model="etapa_virtual" class="form-select">
                                <option value="">Seleccionar</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                            </select>
                        </div>

                        <div class="col-5 text-dark font-weight-bold px-3 fs-6 mt-2">Participación jornada presencial:</div>
                        <div class="col-5 mb-3 px-3 mt-2">
                            <select v-model="etapa_presencial" class="form-select">
                                <option value="">Seleccionar</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                            </select>
                        </div>

                       
                        <div class="col-5 text-dark font-weight-bold px-3 fs-6 mt-2"  v-if="etapa_presencial === '1'">Disponibilidad en la mañana:</div>
                        <div class="col-5 mb-3 px-3 mt-2">
                            <select v-model="jornada_manana" class="form-select" v-if="etapa_presencial === '1'">
                                <option value="">Seleccionar</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                            </select>
                        </div>

                        <div class="col-5 text-dark font-weight-bold px-3 fs-6 mt-2"  v-if="etapa_presencial === '1'">Disponibilidad en la tarde:</div>
                        <div class="col-5 mb-3 px-3 mt-2" v-if="etapa_presencial === '1'">
                            <select v-model="jornada_tarde" class="form-select">
                                <option value="">Seleccionar</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                            </select>
                        </div>
                        

                        <!-- Botón para enviar -->
                        <div class="col-12 text-center mt-4 mb-2">
                            <button @click="enviarPostulacion"  class="btn btn-warning text-white">Enviar Postulación</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { insertarPostulacionEvaluador } from '../services/evaluadorService'; 
import { useAuthStore } from '@/store';
import { useToastUtils } from '@/utils/toast'; 

const { showSuccessToast, showErrorToast, showWarningToast} = useToastUtils();

export default {
    data() {
        return {
            id_evaluador: null,
            etapa_virtual: '',
            etapa_presencial: '',
            jornada_manana: '',
            jornada_tarde: '',
            postulacionExitosa: false 
        };
    },
    watch: {
        // Observamos cambios en etapa_presencial para actualizar los campos de jornada
        etapa_presencial(newVal) {
            if (newVal === '1') {
                // Si selecciona asistencia presencial, restablecemos los valores de jornada a vacíos
                this.jornada_manana = '';
                this.jornada_tarde = '';
            } else {
                // Si selecciona no presencial, asignamos 0 a los campos de jornada
                this.jornada_manana = '0';
                this.jornada_tarde = '0';
            }
        }
    },
    methods: {
        async enviarPostulacion() {
            // Verificamos que los campos obligatorios estén completos
            if (this.etapa_virtual === '' || this.etapa_presencial === '') {
                showWarningToast('Por favor, complete todos los campos antes de enviar.');
                return;
            }

            // Si se selecciona la etapa presencial, validamos que los campos de jornada estén completos
            if (this.etapa_presencial === '1' && (this.jornada_manana === '' || this.jornada_tarde === '')) {
                showWarningToast('Por favor, complete los campos de disponibilidad para la jornada presencial.');
                return;
            }
            
            try {
                const authStore = useAuthStore();
                const user = authStore.user;

                const postulacionData = {
                    id_evaluador: user.id_usuario,  
                    etapa_virtual: parseInt(this.etapa_virtual), 
                    etapa_presencial: parseInt(this.etapa_presencial),
                    jornada_manana: parseInt(this.jornada_manana),
                    jornada_tarde: parseInt(this.jornada_tarde)
                };

                // Intentar enviar la postulación
                const response = await insertarPostulacionEvaluador(postulacionData);
                console.log('Postulación exitosa', response.data);

                this.postulacionExitosa = true;  
                showSuccessToast('Postulación enviada exitosamente. Espera una respuesta en los proximos días...');
                $('#postulacionEvaluador').modal('hide'); // Cierra el modal

             
            } catch (error) {
                // Si el error es "Ya existe una postulación para este evaluador y convocatoria"
                if (error.response && error.response.data && error.response.data.detail === "Ya existe una postulación para este evaluador y convocatoria") {
                    showErrorToast('Ya te postulaste para esta convocatoria, espera una respuesta en los próximos días...');
                    $('#postulacionEvaluador').modal('hide'); // Cierra el modal
                } else {
                    // Manejo de otros errores
                    console.error('Error al insertar postulación:', error.message);
                    showErrorToast('Error al insertar postulación');
                    $('#postulacionEvaluador').modal('hide'); // Cierra el modal
                }
            }
        },
    },
    mounted() {
        const authStore = useAuthStore();
        this.id_evaluador = authStore.user.id_usuario;  
    }
};
</script>


<style scoped> 
    .become
    {
        width: 100%;
        padding-bottom: 163px;
    }
    .become_title h1
    {
        display: block;
        color: #1a1a1a;
        font-weight: 500;
        padding-top: 24px;
    }
    .become_title h1::before
    {
        display: block;
        position: absolute;
        top: 0;
        left: 0;
        width: 55px;
        height: 4px;
        content: '';
        background: #ffb606;
    }
    .become_text
    {
        font-weight: 500;
        font-size: 14px;
        color: #a5a5a1;
        margin-top: 48px;
        margin-bottom: 0px;
    }
    .become_button
    {
        width: 188px;
        height: 53px;
        background: #ffb606;
        margin-top: 37px;
    }
    .become_button a
    {
        display: block;
        font-size: 16px;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 53px;
    }
    .become_button:hover
    {
        box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }
    .become_image
    {
        width: 100%;
        margin-top: 85px;
    }
    .become_image img
    {
        width: 100%;
    }

    .btn-close{

        width: 8px;
        height: 8px;
    }

    /* Media query para pantallas pequeñas */
    @media (max-width: 990px) {
        .become_image {
            margin-top: 1px; 
        }
        
        .become_text {
            margin-top: 30px; 
        }
        .become_title {
            margin-top: 40px; 
        }
    }
</style>