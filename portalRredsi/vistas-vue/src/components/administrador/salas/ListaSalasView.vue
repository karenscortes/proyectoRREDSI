<template>
  <div class="container pt-5">
    <div class="row mb-5 mt-2">
      <div class="col">
        <div class="section_title text-center">
          <h1>Gestionar Salas</h1>
        </div>
      </div>
    </div>
    <!-- Buscador y añadir sala -->
    <div class="row mb-4">
      <div
        class="col-12 divloco col-md-6 d-flex justify-content-start mb-3 mb-md-0"
      >
        <button
          class="btn btn-warning w-sm-100 w-75 font-weight-bold"
          data-toggle="modal"
          data-target="#addSalaModal"
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
         <RowTableSala v-for="(item, index) in salas" :key="index"></RowTableSala>
        </tbody>
      </table>
    </div>
    <ModalAddSala></ModalAddSala>
    <ModalEditSala></ModalEditSala>
  </div>
</template>

<script>
import RowTableSala from './RowTableSala.vue';
import ModalAddSala from './ModalAddSala.vue';
import ModalEditSala from './ModalEditSala.vue';
export default{
    setup(){
        const salas = [1, 2, 3, 4];
        return{salas,}
    },
    components:{
        RowTableSala,
        ModalAddSala, 
        ModalEditSala,
    }
};
</script>
<style scoped>
    thead{
        background: rgb(255, 182, 6);
    }
</style>