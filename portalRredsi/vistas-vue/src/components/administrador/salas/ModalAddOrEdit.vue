<template>
  <!--Modal editar sala-->
  <div
    class="modalCabecero modal fade show"
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
            @click="closeModal()"
          >
            <span aria-hidden="true">&times;</span>
          </button>
          <h3 class="modal-title mt-5 font-weight-bold" id="modalLabel">
            Gestionar Sala
          </h3>
        </div>
        <div class="modal-body mt-3">
          <form>
            <!--Select Área-->
            <div class="form-group row justify-content-center">
              <label
                for="areaSelect"
                class="col-6 col-form-label text-right font-weight-bold"
                >Asignar nueva área:</label
              >
              <div class="col-6">
                <select v-model="idAreaConocimiento" class="form-select text-dark p-1 w-100" id="areaSelect">
                  <option :value="null" disabled>Seleccionar el área</option>
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
            <!--Select delegado-->
            <div class="form-group row justify-content-center">
              <label
                for="delegadoSelect"
                class="col-6 col-form-label text-right font-weight-bold"
                >Asignar nuevo delegado:</label
              >
              <div class="col-6">
                <select
                  v-model="idDelegado"
                  class="form-select text-dark p-1 w-100"
                  id="delegadoSelect"
                >
                  <option :value="null" selected>Seleccionar delegado</option>
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
            <!--input asignar num sala(cuando es crear)-->
            <div class="form-group row justify-content-center mb-5" v-if="!idSala">
              <label
                for="asignarNumSala"
                class="col-6 col-form-label text-right font-weight-bold"
                >Asignar Nº de sala:</label
              >
              <div class="col-6">
                <input
                  type="text"
                  class="form-control form-control-sm w-100"
                  id="asignarNumSala"
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
    //Objeto que se recibe para cuando se va a editar
    infoEditar: {
      type: Object,
      default: null,
      validator(value) {
        return(
          (typeof value.p_idDelegado === "number" || value.p_idDelegado === null) &&
          (typeof value.p_idSala === "number" || value.p_idSala === null) &&
          (typeof value.p_idAreaConocimiento === "number" || value.p_idAreaConocimiento === null)
        )
      },
    },
  },
  //Evento para cerrar modal
  emits: ['close'],
  setup(props,{emit}) {
    const closeModal = ()=>{
      emit('close');
    }

    //Lista de areas de conocimiento
    const arrayAreasConocimiento = reactive([
      {
        id: "1",
        nombre: "Sistemas",
      },
      {
        id: "2",
        nombre: "Medicina",
      },
      {
        id: "3",
        nombre: "Ciencias Humanas",
      },
    ]);

    //Lista delegados
    const arrayDelegados = reactive([
      {
        id: "1",
        nombre: "Lucia Pelaez",
      },
      {
        id: "2",
        nombre: "Juan Pablo",
      },
      {
        id: "3",
        nombre: "Milena",
      },
    ]);
    
    //Propiedades en las que se guardara la info(v-model)
    const idAreaConocimiento = ref(props.infoEditar.p_idAreaConocimiento);
    const idDelegado = ref(props.infoEditar.p_idDelegado);
    const idSala = ref(props.infoEditar.p_idSala);

    return { 
      arrayAreasConocimiento,
      arrayDelegados,
      idAreaConocimiento,
      idDelegado,
      idSala,
      closeModal,
    };
  }
};
</script>
<style scoped>
.modalCabecero{
  display: block;
}
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
input{
  font-size: 1rem; 
}
</style>
