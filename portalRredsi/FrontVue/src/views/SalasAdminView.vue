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
      <div class="col-12 divloco col-md-6 d-flex justify-content-start mb-3 mb-md-0">
        <button class="btn btn-warning w-sm-100 w-75 font-weight-bold" type="button" @click="showModal()">
          Crear sala
        </button>
      </div>
      <div class="col-12 col-md-6 d-flex justify-content-end">
        <div class="d-flex w-100">
          <input type="text" id="busqueda" v-model="busqueda" class="form-control mr-2" placeholder="Buscar..." />
          <button class="btn btn-warning font-weight-bold">Buscar</button>
        </div>
      </div>
    </div>

    <!-- Tabla -->
    <div class="table-responsive tablaloca">
      <table id="basic-datatables" class="display table table-striped table-hover text-dark">
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
          <RowTableSala v-for="(sala, index) in infoSalas" :key="index" :infoSala="sala" @editarRow="onModal($event)">
          </RowTableSala>
        </tbody>
      </table>
    </div>
    <ModalAddOrEdit v-if="isModalOpen" :infoEditar="infoModal" @close="closeModal()"></ModalAddOrEdit>

    <!-- Componente del paginador  -->
    <PaginatorBody :totalPages="totalPages" @page-changed="cambiarPagina" v-if="totalPages > 1"  />
  </div>
</template>

<script>
import { reactive } from "vue";
import { ref } from "vue";
import RowTableSala from '../components/Users/administrador/salas/RowTableSala.vue';
import ModalAddOrEdit from '../components/Users/administrador/salas/ModalAddOrEdit.vue';
import { obtenerSalas } from '@/services/delegadoService';
import PaginatorBody from "../components/UI/PaginatorBody.vue";
import { getAreasConocimiento } from '@/services/administradorService'

export default {
  setup() {
    //Variable para gestionar la apertura del modal
    const isModalOpen = ref(false);

    //Propiedad para guardar la busqueda
    const busqueda = ref("");
    const infoSalas = reactive([])
    let posiblesAreasConocimiento = reactive([])
    let totalPages = ref(0);

    // Funcion para obtener las salas
    const obtenerInfoSalas = async (p_pagina_Actual) => {
      
      // Limpia la lista de salas
      infoSalas.length = 0;

      // Obtiene las salas de la página actual
      const salasObtenidas = await obtenerSalas(p_pagina_Actual);
      
      // Obtengo las posibles áreas de conocimiento en la primera carga de la pagina para que no vuelva a cargar un vez se abara el modal
      const datos_area_conocimiento = await getAreasConocimiento();
      datos_area_conocimiento.data.forEach((area) => {
        posiblesAreasConocimiento.push({
          p_nombre: area.nombre,
          p_id_area_conocimiento: area.id_area_conocimiento
        });
      });

      // Obtiene el total de paginas
      totalPages.value = salasObtenidas.data.total_pages;

      // Agrega las nuevas salas obtenidas a infoSalas
      salasObtenidas.data.salas.forEach((sala) => {
        infoSalas.push({
          p_idDelegado: sala.id_usuario,
          p_delegado: sala.nombres_delegado,
          p_idSala: sala.id_sala,
          p_numSala: sala.numero_sala,
          p_idAreaConocimiento: sala.id_area_conocimiento,
          p_areaConocimiento: sala.nombre_area_conocimiento,
          p_posiblesAreasConocimiento: posiblesAreasConocimiento
        });
      });

      return infoSalas;
    }

    //Objeto que se enviara al modal
    const infoModal = reactive({
      p_idDelegado: null,
      p_idSala: null,
      p_idAreaConocimiento: null,
      p_posiblesAreasConocimiento: posiblesAreasConocimiento
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

    // cambiar la pagina en el componente paginador
    const cambiarPagina= (pagina)=>{
      obtenerInfoSalas(pagina);
    }

    return { infoSalas, infoModal, busqueda, isModalOpen, closeModal, showModal, onModal, obtenerInfoSalas, totalPages,cambiarPagina };
  },
  components: {
    RowTableSala,
    ModalAddOrEdit,
    PaginatorBody
  },
  mounted() {
    this.obtenerInfoSalas();  //Obtener la información de las salas al cargar la página
  }
};
</script>
<style scoped>
thead {
  background: rgb(255, 182, 6);
}

h1 {
  color: black;
}
</style>
