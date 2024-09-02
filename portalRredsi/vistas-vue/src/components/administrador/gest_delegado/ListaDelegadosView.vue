<template>
  <div class="container pt-5">
    <div class="row mb-5 mt-2">
      <!--Titulo Principal-->
      <div class="col">
        <div class="section_title text-center">
          <h1>Gestionar Cuentas Delegados</h1>
        </div>
      </div>
    </div>
    <div class="row justify-content-center">
      <!-- tabla -->
      <div class="table-responsive row d-flex justify-content-center">
        <table class="display table table-striped table-hover text-dark">
          <thead class="text-center">
            <tr class="cabecero">
              <th class="thTable" colspan="3">
                <!-- Buscador -->
                <div class="row justify-content-start">
                  <div class="col-md-5 col-6">
                    <input
                      type="text"
                      id="busqueda"
                      v-model="busqueda"
                      class="form-control"
                      placeholder="Buscar..."
                    />
                  </div>
                  <div class="col-md-2 col-4">
                    <button class="btn btn-dark w-100 font-weight-bold">
                      Buscar
                    </button>
                  </div>
                </div>
              </th>
              <th class="thTable">
                <a
                  class="btn-sm font-weight-bold text-dark"
                  @click="showModalAdd()"
                  type="button"
                  ><i class="fas fa-plus extra-bold-icon"></i>
                </a>
              </th>
            </tr>
            <tr>
              <th>Usuario</th>
              <th>Institucion</th>
              <th>Estado</th>
              <th>Perfil</th>
            </tr>
          </thead>
          <tbody class="text-center">
            <RowTableDelegado
              v-for="(delegado, index) in ArrayDelegados"
              :key="index"
              :index="index"
            :infoDelegado="delegado"
            @open="showModalEdit()" @check="cambiarEstadoCheckboxDelegado($event)">
            </RowTableDelegado>
          </tbody>
        </table>
      </div>
    </div>
    <ModalAdd @close="closeModalAdd()" v-if="isModalOpenAdd"></ModalAdd>
    <ModalDetalle v-if="isModalOpenEdit" @closeModalDetail="closeModalEdit()"></ModalDetalle>
  </div>
</template>
<script>
import { ref } from "vue";
import { reactive } from "vue";
import RowTableDelegado from "./RowTableDelegado.vue";
import ModalAdd from "./ModalAdd.vue";
import ModalDetalle from "./ModalDetalle.vue";

export default {
  setup() {
    const isModalOpenEdit = ref(false); 
    const isModalOpenAdd = ref(false); 

    const busqueda = ref("");
    const estadoActualDelegado = ref("");

    const cambiarEstadoCheckboxDelegado = index => {
      estadoActualDelegado.value = ArrayDelegados[index].p_estado == 'activo' ? 'inactivo' : 'activo';
      ArrayDelegados[index].p_estado = estadoActualDelegado.value;
    }

    const ArrayDelegados = reactive([
      {
        p_idDelegado: 1,
        p_nombres: "Emanuel",
        p_apellidos: "Echeverri",
        p_institucion: "SENA",
        p_estado: "inactivo",
        p_tipoDocumento: "Cédula",
        p_documento: "123456",
        p_areaConocimiento: "Sistemas",
        p_telefono: "12332456",
        p_correo: "Ema@gmail.com",
      },
      {
        p_idDelegado: 2,
        p_nombres: "Luis",
        p_apellidos: "Duarte",
        p_institucion: "SENA",
        p_estado: "activo",
        p_tipoDocumento: "Cédula",
        p_documento: "234567",
        p_areaConocimiento: "Artes visuales",
        p_telefono: "12332456",
        p_correo: "Luis@gmail.com",
      },
      {
        p_idDelegado: 1,
        p_nombres: "Nicol",
        p_apellidos: "Martinez",
        p_institucion: "SENA",
        p_estado: "activo",
        p_tipoDocumento: "Cédula",
        p_documento: "123456",
        p_areaConocimiento: "Contabilidad",
        p_telefono: "12332456",
        p_correo: "Nicol@gmail.com",
      },
    ]);
    
    const infoModalEdit= ref({

    }); 

    const showModalAdd = () =>{
      isModalOpenAdd.value = true;
    }
    const closeModalAdd = () =>{
      isModalOpenAdd.value = false; 
    }

    const showModalEdit = () =>{
      isModalOpenEdit.value = true;
    }
    const closeModalEdit = () =>{
      isModalOpenEdit.value = false; 
    }
    return { 
    busqueda, 
    ArrayDelegados,
    infoModalEdit,
    isModalOpenEdit,
    isModalOpenAdd,
    closeModalEdit, 
    showModalEdit, 
    closeModalAdd,
    showModalAdd, 
    cambiarEstadoCheckboxDelegado,
    };
  },
  components: {
    RowTableDelegado,
    ModalAdd,
    ModalDetalle,
  },
};
</script>
<style scoped>
.thTable {
  background-color: rgb(255, 182, 6);
}
.extra-bold-icon {
  font-size: 26px;
  color: black;
  text-shadow: 1px 1px 0 black, -1px -1px 0 black, -1px 1px 0 black,
    1px -1px 0 black;
}
h1 {
  color: black;
}
</style>
