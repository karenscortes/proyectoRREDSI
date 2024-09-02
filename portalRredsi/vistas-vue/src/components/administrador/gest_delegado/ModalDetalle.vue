<template>
  <div
    class="modal fade"
    id="delegateInformation"
    tabindex="-1"
    aria-labelledby="modalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div
        class="modal-content border border-dark border-5 rounded-5 text-dark"
      >
        <div class="text-center">
          <button
            type="button"
            class="close mr-3 mt-3"
            data-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
          <h3 class="modal-title mt-5" id="modalLabel">Emmanuel Echeverry</h3>
        </div>
        <div class="modal-body mt-3">
          <div class="row mx-auto justify-content-center">
            <div class="col-5 text-dark font-weight-bold">
              Tipo de Documento:
            </div>
            <div class="col-5 border mb-3">
              <span class="text-dark" id="conocimiento">Cedula</span>
            </div>
            <div class="col-5 text-dark font-weight-bold">Documento:</div>
            <div class="col-5 border mb-3">
              <span class="text-dark" id="conocimiento">2102156348</span>
            </div>
            <div class="col-5 text-dark font-weight-bold">Nombre Completo:</div>
            <div class="col-5 border mb-3">
              <span class="text-dark" id="conocimiento">Maria Luisa</span>
            </div>
            <div class="col-5 text-dark font-weight-bold">
              Area de conocimiento:
            </div>
            <div class="col-5 border mb-3">
              <span class="text-dark" id="conocimiento">Sistemas</span>
            </div>
            <div class="col-5 text-dark font-weight-bold">Institución:</div>
            <div class="col-5 border mb-3">
              <span class="text-dark" id="conocimiento">SENA</span>
            </div>
            <div class="col-5 text-dark font-weight-bold">Teléfono:</div>
            <div class="col-5 border mb-3">
              <span class="text-dark" id="conocimiento">3204562023</span>
            </div>
            <div class="col-5 text-dark font-weight-bold">Correo:</div>
            <div class="col-5 border mb-3">
              <span class="text-dark" id="conocimiento">maria60@gmail.com</span>
            </div>

            <div class="text-center mt-3">
              <a
                href="../delegado/pruebas_documentos/constancia_NotasAprendiz.pdf"
                class="btn btn-outline-primary"
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
