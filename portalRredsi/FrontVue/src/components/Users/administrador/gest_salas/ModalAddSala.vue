<template>
  <!-- Modal añadir sala -->
  <div
    class="modal fade"
    id="addSala"
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
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
          <h3
            class="modal-title mt-5 font-weight-bold"
            id="modalLabel"
            style="font-size: 1.5rem; color: #333"
          >
            Añadir sala
          </h3>
        </div>
        <div class="modal-body mt-3">
          <form>
            <div class="form-group row justify-content-center">
              <label
                for="areaSelect"
                class="col-6 col-form-label text-right font-weight-bold"
                style="font-size: 1.2rem; color: #444; white-space: nowrap"
                >Área de conocimiento:</label
              >
              <div class="col-6 pr-5">
                <select
                  class="form-select text-dark p-1"
                  id="areaSelect"
                  style="font-size: 1rem"
                >
                  <option selected>Seleccionar Área</option>
                  <option value="1">Ciencias matemáticas</option>
                  <option value="2">Industria y comercio</option>
                </select>
              </div>
            </div>
            <div class="form-group row justify-content-center">
              <label
                for="evaluadorSelect"
                class="col-6 col-form-label text-right font-weight-bold"
                style="font-size: 1.2rem; color: #444; white-space: nowrap"
                >Asignar nuevo delegado:</label
              >
              <div class="col-6 pr-5">
                <select
                  class="form-select text-dark p-1"
                  id="evaluadorSelect"
                  style="font-size: 1rem"
                >
                  <option selected>Seleccionar evaluador</option>
                  <option value="1">Rigoberto Urán</option>
                  <option value="2">Sancho Sánchez</option>
                </select>
              </div>
            </div>
            <div class="form-group row justify-content-center mb-5">
              <label
                for="colFormLabelSm"
                class="col-6 col-form-label text-right font-weight-bold"
                style="font-size: 1.2rem; color: #444; white-space: nowrap"
                >Asignar Nº de sala:</label
              >
              <div class="col-6 pr-5">
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="colFormLabelSm"
                  style="font-size: 1rem"
                />
              </div>
            </div>
            <div class="text-center">
              <button
                type="submit"
                class="btn btn-warning font-weight-bold"
                style="font-size: 1rem; padding: 0.3rem 1.5rem"
              >
                Añadir sala
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
