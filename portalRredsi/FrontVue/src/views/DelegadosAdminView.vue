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
              @open="showModalDetail($event)"
              @check="cambiarEstadoCheckboxDelegado($event)"
            >
            </RowTableDelegado>
          </tbody>
        </table>
      </div>
    </div>
    <PaginatorBody
      :totalPages="total_pages"
      @page-changed="handlePaginate($event)"
    ></PaginatorBody>
    <ModalAdd @close="closeModalAdd()" v-if="isModalOpenAdd"></ModalAdd>
    <ModalDetalle
      v-if="isModalOpenEdit"
      @closeModalDetail="closeModalDetail()"
      :infoModal="infoModalDetail"
    ></ModalDetalle>
  </div>
</template>
<script setup>
import { onMounted, ref, reactive } from 'vue';
import RowTableDelegado from "../components/Users/administrador/gest_delegado/RowTableDelegado.vue";
import ModalAdd from "../components/Users/administrador/gest_delegado/ModalAdd.vue";
import ModalDetalle from "../components/Users/administrador/gest_delegado/ModalDetalle.vue";
import PaginatorBody from "../components/UI/PaginatorBody.vue";
import { getDelegatesAll } from "@/services/administradorService";

const isModalOpenEdit = ref(false);
const isModalOpenAdd = ref(false);
const page = ref(1);
const total_pages = ref(0);

const busqueda = ref("");
const estadoActualDelegado = ref("");

const cambiarEstadoCheckboxDelegado = (index) => {
  estadoActualDelegado.value =
    ArrayDelegados[index].p_estado == "activo" ? "inactivo" : "activo";
  ArrayDelegados[index].p_estado = estadoActualDelegado.value;
};
const handlePaginate = async(pagina) => {
  page.value = pagina;
  const newPage = await fetchAllDelegates(page.value);
  console.log("Soy respuesta desde rubrica paginador")
  total_pages.value = newPage.data.total_pages;
  console.log(total_pages.value);
  console.log(newPage.data.users);
};

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

const infoModalDetail = reactive({
  p_idDelegado: null,
  p_tipoDocumento: "",
  p_documento: "",
  p_nombres: "",
  p_apellidos: "",
  p_areaConocimiento: "",
  p_institucion: "",
  p_telefono: "",
  p_correo: "",
});

const showModalAdd = () => {
  isModalOpenAdd.value = true;
};
const closeModalAdd = () => {
  isModalOpenAdd.value = false;
};

const showModalDetail = (infoDelegado) => {
  infoModalDetail.p_idDelegado = infoDelegado.p_idDelegado;
  infoModalDetail.p_tipoDocumento = infoDelegado.p_tipoDocumento;
  infoModalDetail.p_documento = infoDelegado.p_documento
  infoModalDetail.p_nombres = infoDelegado.p_nombres;
  infoModalDetail.p_apellidos = infoDelegado.p_apellidos;
  infoModalDetail.p_areaConocimiento = infoDelegado.p_areaConocimiento;
  infoModalDetail.p_institucion = infoDelegado.p_institucion;
  infoModalDetail.p_telefono = infoDelegado.p_telefono;
  infoModalDetail.p_correo = infoDelegado.p_correo;
  isModalOpenEdit.value = true;
};

const closeModalDetail = () => {
  isModalOpenEdit.value = false;
};

const fetchAllDelegates = async () => {
  try {
    const response = await getDelegatesAll(page.value);
    total_pages.value = response.data.total_pages;
    console.log(response)
    return response
  } catch (error) {
    console.error("Error al obtener los delegados: ", error);
    alert("Error al obtener los delegados");
  }
};
onMounted(() => {
  fetchAllDelegates();
});
</script>
<style scoped>
.btn {
  background-color: rgb(43, 43, 43);
}
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
