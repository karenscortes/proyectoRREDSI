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
          <button
            type="button"
            class="close mr-3 mt-3"
            @click="closeModal()"
          >
            <span aria-hidden="true">&times;</span>
          </button>
          <h3 class="modal-title mt-5" id="modalLabel">{{infoModal.p_nombres}} {{ infoModal.p_apellidos }}</h3>
        </div>
        <div class="modal-body mt-3">
          <div class="row mx-auto justify-content-center">
            <div class="col-6 text-dark font-weight-bold">
              Tipo de Documento:
            </div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="tipo_documento">{{ infoModal.p_tipoDocumento }}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Documento:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.p_documento}}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Nombre Completo:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.p_nombres }} {{ infoModal.p_apellidos}}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">
              Area de conocimiento:
            </div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.p_areaConocimiento }}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Institución:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.p_institucion }}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Teléfono:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.p_telefono }}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Correo:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.p_correo}}</span>
            </div>

            <div class="text-center mt-3">
              <a
                href="/constancia_NotasAprendiz.pdf"
                class="btn btn-warning"
                target="_blank"
              >
                Ver Títulos
              </a>
            </div>
          </div>
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
          typeof id_delegado === 'number' &&
          typeof value.nombres === 'string' &&
          typeof value.apellidos === 'string' &&
          typeof tipo_documento === 'string' &&
          typeof value.documento === 'string' &&
          typeof (value.id_institucion === 'string' || value.id_institucion === null) &&
          typeof (value.id_primera_area_conocimiento === 'string' || value.id_primera_area_conocimiento === null) &&
          typeof (value.id_segunda_area_conocimiento === 'string' || value.id_segunda_area_conocimiento === null) &&
          typeof (value.url_titulo === 'string'|| value.url_titulo === null) &&
          typeof value.estado  === 'string' &&
          typeof value.celular === 'string' &&
          typeof value.correo === 'string' 
        );
      }
    }
  },
  emits: ["closeModalDetail"],
  setup(props, { emit }) {
    const closeModal = () => {
      emit("closeModalDetail");
    };
    return { closeModal};
  },
};
</script>
<style>
.modalCabecero {
  display: block;
}
</style>
