<template>
  <div class="container pt-5">
    <!--Titulo principal-->
    <div class="row mb-5 mt-2">
      <div class="col">
        <div class="section_title text-center">
          <h1>Gestionar Salas</h1>
        </div>
      </div>
    </div>
    <!-- Opción añadir sala y buscador -->
    <div class="row mb-4">
      <div
        class="col-12 divloco col-md-6 d-flex justify-content-start mb-3 mb-md-0"
      >
        <button
          class="btn btn-warning w-sm-100 w-75 font-weight-bold"
          type="button"
          @click="showModal()"
        >
          Crear sala
        </button>
      </div>
      <div class="col-12 col-md-6 d-flex justify-content-end">
        <div class="d-flex w-100">
          <input
            type="text"
            id="busqueda"
            class="form-control mr-2"
            placeholder="Buscar..."
          />
          <button class="btn btn-warning font-weight-bold">Buscar</button>
        </div>
      </div>
    </div>

    <!-- Tabla -->
    <div class="table-responsive tablaloca">
      <table
        id="basic-datatables"
        class="display table table-striped table-hover text-dark"
      >
        <thead>
          <tr>
            <th>Número de sala</th>
            <th>Area de conocimiento</th>
            <th>Delegado asignado</th>
            <th>Editar</th>
          </tr>
        </thead>
        <tbody>
          <!--RowTableSala(componente)-->
          <RowTableSala
            v-for="(sala, index) in infoSalas"
            :key="index"
            :infoSala="sala"
            @editarRow="onModal($event)"
          ></RowTableSala>
        </tbody>
      </table>
    </div>
    <ModalAdd v-if="isModalOpen" :infoEditar="infoModal" @close="closeModal()"></ModalAdd>
  </div>
</template>

<script>
import RowTableSala from "./RowTableSala.vue";
import ModalAdd from "./ModalAdd.vue";
import { reactive } from "vue";
import { ref } from "vue";
export default {
  setup() {
    const isModalOpen = ref(false); 
    const infoSalas = reactive([  
      {
        p_idDelegado: 1,
        p_delegado: "Lucia Perez",
        p_idSala: 1,
        p_numSala: "132435s",
        p_idAreaConocimiento: 1,
        p_areaConocimiento: "Sistemas",
      },
      {
        p_idDelegado: 2,
        p_delegado: "Juan Pablo",
        p_idSala: 2,
        p_numSala: "132756s",
        p_idAreaConocimiento: 2,
        p_areaConocimiento: "Medicina",
      },
      {
        p_idDelegado: 3,
        p_delegado: "Milena",
        p_idSala: 3,
        p_numSala: "132345",
        p_idAreaConocimiento: 3,
        p_areaConocimiento: "Ciencias Humanas",
      },
    ])

    const infoModal = reactive({
      p_idDelegado: null,
      p_delegado: "",
      p_idSala: null,
      p_numSala: "",
      p_idAreaConocimiento: null,
      p_areaConocimiento: "",
    });

    const closeModal = () => {
      infoModal.p_idDelegado = null;
      infoModal.p_delegado = ""; 
      infoModal.p_idSala = null;
      infoModal.p_numSala = "";
      infoModal.p_idAreaConocimiento = null; 
      infoModal.p_areaConocimiento = ""; 
      isModalOpen.value = false;
    }

    const showModal = () => {
      isModalOpen.value = true;
    }

    const onModal = infoSala => { 
      infoModal.p_idDelegado = infoSala.p_idDelegado;
      infoModal.p_delegado = infoSala.p_delegado; 
      infoModal.p_idSala = infoSala.p_idSala;
      infoModal.p_numSala = infoSala.p_numSala;
      infoModal.p_idAreaConocimiento = infoSala.p_idAreaConocimiento; 
      infoModal.p_areaConocimiento = infoSala.p_areaConocimiento; 
      isModalOpen.value = true; 
    }
    return {infoSalas,infoModal,onModal,isModalOpen, closeModal,showModal};
  },
  components: {
    RowTableSala,
    ModalAdd,
  },
};
</script>
<style scoped>
thead {
  background: rgb(255, 182, 6);
}
h1{
  color: black;
}
</style>
