<template>
  <!--Modal editar sala-->
  <div
    class="modal fade"
    id="modalSala"
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
            Gestionar Sala
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
                <select class="form-select text-dark p-1 w-100" id="areaSelect">
                  <option selected>Seleccionar área</option>
                  <option
                    v-for="(area, index) in arrayAreasConocimiento"
                    :key="index"
                    :value="area.id"
                  >
                    {{ area.nombre }}
                  </option>
                </select>
              </div>
            </div>
            <div class="form-group row justify-content-center">
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
                  <option selected>Seleccionar delegado</option>
                  <option
                    class="option"
                    v-for="(delegado, index) in arrayDelegados"
                    :key="index"
                    :value="delegado.id"
                  >
                    {{ delegado.nombre }}
                  </option>
                </select>
              </div>
            </div>
            <div class="form-group row justify-content-center mb-5">
              <label
                for="colFormLabelSm"
                class="col-6 col-form-label text-right font-weight-bold"
                >Asignar Nº de sala:</label
              >
              <div class="col-6">
                <input
                  type="text"
                  class="form-control form-control-sm w-100"
                  id="colFormLabelSm"
                  style="font-size: 1rem"
                />
              </div>
            </div>
            <div class="text-center">
              <button type="submit" class="btn btn-warning font-weight-bold">
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
import { reactive } from "vue";
import { ref } from "vue";
export default {
  props: {
    infoEditar: {
      type: Object,
      default: null,
      validator(value) {
        return (
          typeof value.p_idDelegado === "number" &&
          typeof value.p_delegado === "string" &&
          typeof value.p_idSala === "number" &&
          typeof value.p_numSala === "string" &&
          typeof value.p_idAreaConocimiento === "number" &&
          typeof value.p_areaConocimiento === "string"
        );
      },
    },
  },
  setup(props) {
    const arrayAreasConocimiento = reactive([
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
    ]);

    const arrayDelegados = reactive([
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
    ]);
    
    const areaConocimiento = ref(props.infoEditar.p_areaConocimiento);
    const delegado = ref(props.infoEditar.p_delegado);
    const numSala = ref(props.infoEditar.p_descripcion);

    return { arrayAreasConocimiento,arrayDelegados,areaConocimiento,delegado,numSala};
  }
};
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
.button {
  font-size: 1rem;
  padding: 0.3rem 1.5rem;
}
</style>
