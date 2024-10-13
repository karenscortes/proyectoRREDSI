<template>
  <div
    class="modalCabecero modal fade show"
    id="delegateInformation"
    tabindex="-1"
    aria-labelledby="modalLabel"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div
        class="modal-content border border-dark border-5 rounded-5 text-dark"
      >
        <div class="text-center">
          <button type="button" class="close mr-3 mt-3" @click="closeModal()">
            <span aria-hidden="true">&times;</span>
          </button>
          <h3 class="modal-title mt-5 fs-3" id="modalLabel">
            {{ infoModal.value.nombres }} {{ infoModal.value.apellidos }}
          </h3>
        </div>
        <div class="modal-body mt-3 text-center">
          <div class="row mx-auto justify-content-center">
            <div class="col-12 mb-3">
              <label for="tipo_document" class="form-label fw-bold mb-2 fs-6"
                >Tipo de Documento:</label
              >
              <span class="text-dark fs-6" style="margin-left: 10px">{{
                infoModal.value.tipo_documento
              }}</span>
            </div>
            <div class="col-12 mb-3">
              <label for="document" class="form-label fw-bold mb-2 fs-6"
                >Documento:</label
              >
              <span class="text-dark fs-6">{{
                infoModal.value.documento
              }}</span>
            </div>
            <div class="col-12 mb-3">
              <label for="institucion" class="form-label fw-bold mb-2 fs-6"
                >Institución:</label
              >
              <span class="text-dark fs-6">{{
                infoModal.value.nombre_institucion
              }}</span>
            </div>
            
            <div class="col-12 mb-3">
              <label for="celular" class="form-label fw-bold mb-2 fs-6"
                >Teléfono:</label
              >
              <span class="text-dark fs-6">{{
                infoModal.value.celular
              }}</span>
            </div>

            <div class="col-12 mb-3">
              <label for="correo" class="form-label fw-bold mb-2 fs-6"
                >Correo:</label
              >
              <span class="text-dark fs-6">{{
                infoModal.value.correo  
              }}</span>
            </div>

            <div class="col-12 mb-3">
              <label for="primer_area" class="form-label fw-bold mb-2 fs-6"
                >Primer área:</label
              >
              <span class="text-dark fs-6">{{
                infoModal.value.primer_area
              }}</span>
            </div>
            
            <div class="col-12 mb-3" v-if="infoModal.value.segunda_area">
              <label for="segunda_Area" class="form-label fw-bold mb-2 fs-6"
                >Segunda área:</label
              >
              <span class="text-dark fs-6">{{
                infoModal.value.segunda_area
              }}</span>
            </div>

            <div class="text-center mt-3">
              <a
                :href="infoModal.value.url_titulo"
                class="btn btn-warning"
                target="_blank"
                >Ver Títulos</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    infoModal: {
      type: Object,
      required: true,
      validator(value) {
        const actualValue = value.value;
        return (
          typeof actualValue.id_usuario === "number" &&
          typeof actualValue.nombres === "string" &&
          typeof actualValue.apellidos === "string" &&
          typeof actualValue.tipo_documento === "string" &&
          typeof actualValue.documento === "string" &&
          typeof actualValue.nombre_institucion === "string" &&
          typeof actualValue.primer_area === "string" &&
          typeof (
            actualValue.segunda_area === "string" &&
            actualValue.segunda_area === null
          ) &&
          typeof actualValue.url_titulo === "string" &&
          typeof actualValue.estado === "string" &&
          typeof actualValue.celular === "string" &&
          typeof actualValue.correo === "string"
        );
      },
    },
  },
  emits: ["closeModalDetail"],
  setup(props, { emit }) {
    const closeModal = () => {
      emit("closeModalDetail");
    };
    return { closeModal };
  },
};
</script>
<style>
.modalCabecero {
  display: block;
}
span{
  margin-left: 5px;
}
@media only screen and (min-width: 500px) and (max-width: 768px) {
  .modal-dialog {
    min-width: 50%;
  }
}
</style>
