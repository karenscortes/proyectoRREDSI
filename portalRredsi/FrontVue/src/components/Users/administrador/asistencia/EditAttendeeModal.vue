<template>
    <div class="modal fade  show" id="modalEditar" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
    aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered bg-transparent" style="max-width: 50%;">
            <div class="modal-content border border-dark border-5 rounded-5 text-dark shadow-lg modal-responsive">
                <div class="modal-header px-4 shadow w-100 rounded-5 rounded-bottom" >
                    <i class="fas fa-edit icon"></i>
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Editar asistente</h1>
                    <button type="button" class="close fs-2" @click="closeModal()">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="updateInfo()">
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="nombres" class="form-label">
                                    Nombres
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="text" id="nombres" v-model="editableData.nombres" class="form_modal form-control" required>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="apellidos" class="form-label">
                                    Apellidos
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="text" id="apellidos" v-model="editableData.apellidos" class="form_modal form-control" required>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="celular" class="form-label">
                                    Celular
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="text" id="celular" v-model="editableData.celular" class="form_modal form-control" required>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="correo" class="form-label">
                                    correo
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="email" id="correo" v-model="editableData.correo" class="form_modal form-control" required>
                            </div>
                            <div class=" col-md-12  mb-2">
                                <label for="correo" class="form-label">
                                    Comprobate Pago (Url):
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="text" id="correo" v-model="editableData.url_comprobante_pago" class="form_modal form-control" required>
                            </div>
                            <div class="d-flex justify-content-center">
                                <button class="btn boton pl-5 pr-5 mx-auto" type="submit">Actualizar Datos</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { updateAttendees } from '@/services/asistenciaService';
import { reactive } from "vue";
import { useToastUtils } from '@/utils/toast';
export default {
  props:{
    infoModal: {
      type: Object,  
      default: null,
      validator(value){
        return(
          typeof value.id_usuario === 'number' &&
          typeof value.documento === 'string' &&
          typeof value.nombres === 'string' &&
          typeof value.apellidos === 'string' &&
          typeof value.celular === 'string' &&
          typeof value.correo === 'string' &&
          typeof value.url_comprobante_pago === 'string'  
        );
      }
    }
  },
  emits: ["closeEditModal"],
  setup(props, { emit }) {
    const { showErrorToast,showSuccessToast} = useToastUtils();

    const editableData = reactive({
        nombres: props.infoModal.nombres,
        apellidos: props.infoModal.apellidos,
        celular: props.infoModal.celular,
        correo: props.infoModal.correo,
        url_comprobante_pago: props.infoModal.url_comprobante_pago,
    });

    const closeModal = () => {
      emit("closeEditModal");
    };
    
    const updateInfo = async() => {
        try {
            if (editableData.nombres !== props.infoModal.nombres || editableData.apellidos !== props.infoModal.apellidos ||
                editableData.celular !== props.infoModal.celular || editableData.correo !== props.infoModal.correo ||
                editableData.url_comprobante_pago !== props.infoModal.url_comprobante_pago) 
            {
                console.log("entró");
                const response = await updateAttendees(props.infoModal.id_usuario, editableData);
                showSuccessToast(response.data.message);

            }else{
                showErrorToast("Error al intentar Actualizar.");
            }
        } catch (error) {
            showErrorToast("Error al actualizar Asistente.");
        }
    };
    return { 
        closeModal,
        updateInfo,
        editableData,
    };
  },
};
</script>
<style scoped>

.form-control{
	height: 35px;
	border: 1px solid black;
}

.form_modal{
	border: 1px solid rgb(190, 190, 190);
}

#modalEditar {
  display: block;
}


.modal-header .icon {
	color:rgb(255, 182, 6);
	font-size: 2rem;
	margin-right: 10px;
}

.modal-header{
	color: #000000;
	font-size: 2rem;
	margin-right: 10px;
}

label{
	font-size: 15px;
	font-weight: bold;
	color: black;
}
</style>
