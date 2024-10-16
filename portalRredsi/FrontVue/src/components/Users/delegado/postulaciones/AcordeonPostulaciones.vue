<template>
    <!-- Acordeón para cada evaluador -->
    <div class="accordion-item">
        <h2 class="accordion-header row align-items-center">
            <div class="col-8 col-md-10">
                <button class="accordion-button collapsed row align-items-center" type="button"
                    data-bs-toggle="collapse" :data-bs-target="`#flush-collapse${evaluator.id_evaluador}`" aria-expanded="false"
                    :aria-controls="`flush-collapse${evaluator.id_evaluador}`">
                    <div class="col-8">
                        <h4 class="h5 m-0">{{ evaluator.nombres}} {{evaluator.apellidos}}</h4>
                    </div>
                </button>
            </div>
            <div class="col-4 col-md-2 d-flex ">
                <div >
                    <a href="#" @click="updateStatus(evaluator,'rechazada')">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960"
                            width="24px" fill="#00000"  class="icono1">
                            <path
                                d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z" />
                        </svg>
                    </a>
                </div>
                <div class="ms-3">
                    <a href="#" @click="updateStatus(evaluator,'aceptada')">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960"
                            width="24px" fill="#00000"  class="icono2">
                            <path
                                d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                        </svg>
                    </a>
                </div>
            </div>
        </h2>
        <div :id="`flush-collapse${evaluator.id_evaluador}`" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
            <div class="accordion-body col-10 pl-0 text-dark text-start">
                <div class="row mt-4">
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Institución:</strong></p>
                        <p class="text-dark">{{ evaluator.nombre_institucion }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Área de conocimiento:</strong></p>
                        <p class="text-dark">{{ evaluator.area_conocimiento }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Área de conocimiento secundaria:</strong></p>
                        <p class="text-dark">{{ evaluator.otra_area}}</p>
                    </div>
                </div>
                <div class="row mt-4">
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Teléfono:</strong></p>
                        <p class="text-dark">{{ evaluator.celular }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="text-dark"><strong>Correo electrónico:</strong></p>
                        <p class="text-dark">{{ evaluator.correo }}</p>
                    </div>
                    <div class="col-md-2 col-12">
                        <p class="text-dark"><strong>Etapa:</strong></p>
                        <p v-if="evaluator.etapa_virtual && evaluator.etapa_presencial" class="text-dark"> Virtual y
                            presencial</p>
                        <p v-else class="text-dark">{{ evaluator.etapa_virtual ? "Virtual" : "Presencial" }}</p>

                    </div>
                    <div v-if="evaluator.etapa_virtual && evaluator.etapa_presencial || evaluator.etapa_presencial"
                        class="col-md-2 col-12">
                        <p class="text-dark"><strong>Jornada:</strong></p>
                        <p v-if="evaluator.jornada_manana && evaluator.jornada_tarde" class="text-dark"> Mañana y tarde
                        </p>
                        <p v-else class="text-dark">{{ evaluator.jornada_manana ? "Mañana" : "Tarde" }}</p>
                    </div>
                </div>
                <div class="row mt-4 justify-content-center">
                    <div class="col-md-4 col-12">
                        <a @click="openModal(evaluator)"
                            class="btn w-100 mb-3">Visualizar
                            Títulos</a>
                    </div>
                </div>
            </div>
        </div>


        <!-- Modal -->
        <div class="modal fade" :id="`modal_titulos_${evaluator.id_evaluador}`" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content border border-dark border-5 rounded-5">
                    <div class="row text-center justify-content-end mt-2">
                        <div class="col-2">
                            <button type="button" class="btn-close justify-contet-end" data-bs-dismiss="modal"
                                aria-label="Close"></button>
                        </div>
                        <div class="col-12">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Programas Académicos <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00000"><path d="M480-120 200-272v-240L40-600l440-240 440 240v320h-80v-276l-80 44v240L480-120Zm0-332 274-148-274-148-274 148 274 148Zm0 241 200-108v-151L480-360 280-470v151l200 108Zm0-241Zm0 90Zm0 0Z"/></svg></h1>
                        </div>
                    </div>
                    <div class="modal-body">
                        <div class="list-group">
                            <a v-for="(certificate,index) in certificates"  :key="index" :href="'https://proyectorredsi-whpk.onrender.com/'+certificate.url_titulo" class="list-group-item list-group-item-action" target="_blank">{{certificate.nivel}}</a>
                        </div>
                    </div>
                    <div class="row justify-content-center mb-2">
                        <button type="button" class="btn btn-dark fw-bold col-4 text-center" data-bs-dismiss="modal">Cerrar</button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import { getCertificatesById, updateApplication} from '@/services/postulacionService';
import { useToastUtils } from '@/utils/toast';
export default {
    name: "AcordeonPostulaciones",
    props: {
        evaluator: Object,
    },
    data(){
        return{
            certificates:[]
        }
    },
    methods: {
        ... useToastUtils(),
        notifyParent(){
            this.$emit('notify');
        },

        async updateStatus(evaluator,estado) {
            try {
                await updateApplication(evaluator.id_evaluador, estado);
                if(estado == 'rechazada'){
                    this.showSuccessToast('La postulación se rechazó exitosamente.');
                }else{
                    this.showSuccessToast('La postulación se aceptó exitosamente.');
                }
                
                this.notifyParent();
            } catch (error) {
                this.showErrorToast('Error al procesar postulación.')
            }
        },
        
        async openModal(evaluator) {
            try {
                this.certificates = [];
                const response = await getCertificatesById(evaluator.id_evaluador);
                if(response.data.length > 0){
                    this.certificates = response.data; 
                    $(`#modal_titulos_${evaluator.id_evaluador}`).modal('show'); // Abre el modal
                }else{
                    this.showInfoToast('El postulado no cuenta con titulación.');   
                }
               
            } catch (error) {
                this.showErrorToast('Error al consultar titulación.')
            }
        },
    }
};
</script>


<style scoped>
.accordion-button:not(.collapsed) {
    background-color: rgb(255, 182, 6);
    color: #000;
}

.accordion-button {
    color: #000;
}

.accordion-button::after {
    filter: invert(0);
}

.icono1:hover{ 
    fill:#f50c0c ;
}

.icono2:hover{
    fill:#12d336 ;
}

.btn-visualizar{
    border: 0;
    color: #000;
}
</style>