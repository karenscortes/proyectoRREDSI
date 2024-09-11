<template>
  <!--Modal editar sala-->
  <div
    class="modal fade"
    id="editSala"
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
          <h3 class="modal-title mt-5 font-weight-bold" id="modalLabel">
            Editar sala
          </h3>
        </div>
        <div class="modal-body mt-3">
          <form>
            <div class="row justify-content-center">
              <!-- Contenedor para Asignar nueva área -->
              <div class="col-md-6">
                <div class="form-group row">
                  <label
                    for="areaSelect"
                    class="col-sm-6 col-form-label text-right font-weight-bold"
                  >
                    Asignar nueva área:
                  </label>
                  <div class="col-sm-6">
                    <select class="form-select text-dark p-1" id="areaSelect">
                      <option selected>Seleccionar área</option>
                      <option value="1">Ciencias matemáticas</option>
                      <option value="2">Industria y comercio</option>
                    </select>
                  </div>
                </div>
              </div>

              <!-- Contenedor para Asignar nuevo delegado -->
              <div class="col-md-6">
                <div class="form-group row">
                  <label
                    for="evaluadorSelect"
                    class="col-sm-6 col-form-label text-right font-weight-bold"
                  >
                    Asignar nuevo delegado:
                  </label>
                  <div class="col-sm-6">
                    <select class="form-select text-dark" id="evaluadorSelect">
                      <option selected>Seleccionar evaluador</option>
                      <option value="1">Rigoberto Urán</option>
                      <option value="2">Sancho Sánchez</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>

            <!-- Botón para guardar cambios -->
            <div class="text-center mt-3">
              <button
                type="submit"
                class="btn-guardar btn btn-warning font-weight-bold"
              >
                Guardar Cambios
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script></script>
<style scoped>
.modal-title {
  font-size: 1.5rem;
  color: #333;
}
label {
  font-size: 1.2rem;
  color: #444;
  display: inline-block;
}
.form-select {
  font-size: 1rem;
  width: 100%;
}
.btn-guardar {
  font-size: 1rem;
  padding: 0.3rem 1.5rem;
}
</style>
