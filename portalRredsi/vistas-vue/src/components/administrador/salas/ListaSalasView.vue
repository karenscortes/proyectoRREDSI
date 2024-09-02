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
            v-model="busqueda"
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
import ModalAdd from "./ModalAddOrEdit.vue";
import { reactive } from "vue";
import { ref } from "vue";
export default {
  setup() {
    //Variable para gestionar la apertura del modal
    const isModalOpen = ref(false); 

    //Propiedad para guardar la busqueda
    const busqueda = ref(""); 

    //Lista con la Info de cada sala que se enviara a cada tr
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

    //Objeto que se enviara al modal
    const infoModal = reactive({
      p_idDelegado: null,
      p_idSala: null,
      p_idAreaConocimiento: null,
    });

    //Evento para limpiar los campos y cerrrar el modal
    const closeModal = () => {
      infoModal.p_idDelegado = null;
      infoModal.p_idSala = null;
      infoModal.p_idAreaConocimiento = null; 
      isModalOpen.value = false;
    }

    //Evento para abrir el modal
    const showModal = () => {
      isModalOpen.value = true;
    }

    //Evento que se dispara al escuchar el evento del tr
    const onModal = infoSala => { 
      infoModal.p_idDelegado = infoSala.p_idDelegado; 
      infoModal.p_idSala = infoSala.p_idSala;
      infoModal.p_idAreaConocimiento = infoSala.p_idAreaConocimiento; 
      showModal();  
    }
    return {infoSalas,infoModal,busqueda,isModalOpen, closeModal,showModal,onModal};
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
