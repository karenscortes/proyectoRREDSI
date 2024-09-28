<template>
    <div class="modal fade" id="modalEditar" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
    aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog" style="max-width: 50%;">
            <div class="modal-content rounded-st-1 shadow-lg modal-responsive">
                <div class="modal-header p-4 shadow w-100" style="border: 1px solid yellow;">
                    <i class="fas fa-edit icon"></i>
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Editar asistente</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="updateInfo()">
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="nombres" class="form-label">
                                    Nombres
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="text" id="nombres" v-model="infoModal.nombres" class="form_modal form-control" required>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="apellidos" class="form-label">
                                    Apellidos
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="text" id="apellidos" v-model="infoModal.apellidos" class="form_modal form-control" required>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="celular" class="form-label">
                                    Celular
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="text" id="celular" v-model="infoModal.celular" class="form_modal form-control" required>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="correo" class="form-label">
                                    correo
                                    <span class="text-danger fw-bold">*</span>
                                </label>
                                <input type="email" id="correo" v-model="infoModal.correo" class="form_modal form-control" required>
                            </div>
                            <div class=" col-md-12  mb-2">
                                <label for="comprobante_pago" class="form-label d-flex justify-content-center">
                                    Lista de Asistentes: 
                                </label>
                                <div class="custom-file-upload mx-auto">
                                    <label for="comprobante_pago" class="upload-label">
                                        <input type="file" id="comprobante_pago" name="comprobante_pago" class="d-none d-print-block" @change="onFileChange"/>
                                        <i class="fas fa-cloud-upload-alt"></i>
                                        Selecciona un archivo
                                    </label>
                                </div> 
                            </div>
                            <div class="d-flex justify-content-center" style="border: 1px solid yellow;">
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

export default {
  props:{
    infoModal: {
      type: Object,  
      default: null,
      validator(value){
        return(
          typeof id_usuario === 'number' &&
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
  emits: ["closeModalDetail"],
  setup(props, { emit }) {

    const closeModal = () => {
      emit("closeModalDetail");
    };

    const updateInfo = () => {
      
    };
    return { 
        closeModal,
        updateInfo
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
</style>