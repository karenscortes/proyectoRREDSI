<template>
  <div
    class="modalCabecero modal fade show"
    id="createAccount"
    tabindex="-1"
    aria-labelledby="modalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div
        class="modal-content border border-dark border-5 rounded-5 text-dark"
      >
        <div class="text-center">
          <button type="button" class="close mr-3 mt-3" @click="closeModal()">
            <span aria-hidden="true">&times;</span>
          </button>
          <h3 class="modal-title mt-5" id="modalLabel">
            Crear Cuenta de Delegado
          </h3>
        </div>
        <div class="modal-body mt-3">
          <form>
            <div class="form-group row justify-content-center">
              <label
                for="email"
                class="col-1 col-form-label col-form-label-sm"
                >Email:
              </label>
              <div class="col-5">
                <input
                  type="email"
                  class="form-control form-control-sm"
                  id="email"
                  v-model="correo"
                  placeholder="usuario@gmail.com"
                />
              </div>
              <label
                for="email"
                class="col-1 col-form-label col-form-label-sm"
                >nombre:
              </label>
              <div class="col-5">
                <input
                  type="email"
                  class="form-control form-control-sm"
                  id="email"
                  v-model="correo"
                  placeholder="usuario@gmail.com"
                />
              </div>
            </div>
            <div class="text-center">
              <button type="submit" class="btn btn-warning font-weight-bold">
                Crear
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref } from 'vue';

export default {
  emits: ["close"],
  setup(props, { emit }) {
    const correo = ref("");

    const closeModal = () => {
      emit("close");
    };
    return {closeModal, correo};
  },
};
</script>
<style>
.modalCabecero {
  display: block;
}
</style>
