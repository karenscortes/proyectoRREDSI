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
          <h3
            class="modal-title mt-5 font-weight-bold"
            id="modalLabel"
          >
            Editar sala
          </h3>
        </div>
        <div class="modal-body mt-3">
          <form>
            <div class="form-group row justify-content-center">
              <label
                for="areaSelect"
                class="col-6 col-form-label text-right font-weight-bold"
                >Asignar nueva área:</label
              >
              <div class="col-6">
                <select
                  class="form-select text-dark p-1 w-100"
                  id="areaSelect"
                >
                  <option selected>Seleccionar área</option>
                  <option v-for="(area, index) in areasConocimiento" :key="index" :value="area.id">{{ area.nombre }}</option>
                </select>
              </div>
            </div>
            <div class="form-group row justify-content-center mb-5">
              <label
                for="evaluadorSelect"
                class="col-6 col-form-label text-right font-weight-bold"
                >Asignar nuevo delegado:</label
              >
              <div class="col-6">
                <select
                  class="form-select text-dark p-1 w-100"
                  id="evaluadorSelect"
                >
                  <option selected>Seleccionar evaluador</option>
                  <option class="option" v-for="(evaluador, index) in evaluadores" :key="index" :value="evaluador.id">{{evaluador.nombre }}</option>
                </select>
              </div>
            </div>
            <div class="text-center">
              <button type="submit" class="btn btn-warning font-weight-bold"
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
<script>
import { reactive } from 'vue';
export default {
  setup (){
    const areasConocimiento = reactive([
      {
        id: "1",
        nombre: "Sistemas",
      },
      {
        id: "2",
        nombre: "Sistemas",
      },
      {
        id: "3",
        nombre: "Sistemas",
      },
    ])

    const evaluadores = reactive([
      {
        id: "1",
        nombre: "Lucia Pelaez",
      },
      {
        id: "2",
        nombre: "Lucia Pelaez",
      },
      {
        id: "3",
        nombre: "Lucia Pelaez",
      },
    ])

    return{areasConocimiento, evaluadores}
  }
}
</script>
<style scoped>
.modal-title {
  font-size: 1.5rem;
  color: #333;
}
label {
  font-size: 1.2rem;
  color: #444;
  display: inline-block;
  white-space: nowrap;
}
.form-select {
  font-size: 1rem;
}
.form-select:focus {
  box-shadow: 0 0 5px yellow;
  border: 1px solid yellow;
}
.btn-guardar {
  font-size: 1rem;
  padding: 0.3rem 1.5rem;
}
.button{
font-size: 1rem; 
padding: 0.3rem 1.5rem;
}
</style>
