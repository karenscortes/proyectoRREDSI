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
          <h3 class="modal-title mt-5" id="modalLabel">{{infoModal.value.nombres}} {{infoModal.value.apellidos}}</h3>
        </div>
        <div class="modal-body mt-3">
          <div class="row mx-auto justify-content-center">
            <div class="col-6 text-dark font-weight-bold">
              Tipo de Documento:
            </div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="tipo_documento">{{ infoModal.value.tipo_documento }}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Documento:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="documento">{{ infoModal.value.documento}}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Institución:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.value.nombre_institucion }}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Teléfono:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.value.celular }}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Correo:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="conocimiento">{{ infoModal.value.correo}}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">Primer area:</div>
            <div class="col-6 border mb-3">
              <span class="text-dark" id="primer_area">{{ infoModal.value.primer_area }}</span>
            </div>
            <div class="col-6 text-dark font-weight-bold">
              Segunda area:
            </div>
            <div class="col-6 border mb-3" v-if="infoModal.value.segunda_area">
              <span class="text-dark" id="segunda_area">{{ infoModal.value.segunda_area }}</span>
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
      required: true,
      validator(value){
        const actualValue = value.value;
        return(
          typeof actualValue.id_usuario === 'number' &&
          typeof actualValue.nombres === 'string' &&
          typeof actualValue.apellidos === 'string' &&
          typeof actualValue.tipo_documento === 'string' &&
          typeof actualValue.documento === 'string' &&
          typeof actualValue.nombre_institucion === 'string' &&
          typeof actualValue.primer_area === 'string' &&
          typeof (actualValue.segunda_area === 'string' && actualValue.segunda_area === null) &&
          typeof actualValue.url_titulo === 'string' &&
          typeof actualValue.estado  === 'string' &&
          typeof actualValue.celular === 'string' &&
          typeof actualValue.correo === 'string' 
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
