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
import { onMounted, ref, reactive } from "vue";
import RowTableDelegado from "../components/Users/administrador/gest_delegado/RowTableDelegado.vue";
import ModalAdd from "../components/Users/administrador/gest_delegado/ModalAdd.vue";
import ModalDetalle from "../components/Users/administrador/gest_delegado/ModalDetalle.vue";
import PaginatorBody from "../components/UI/PaginatorBody.vue";
import { getDelegatesAll } from "@/services/administradorService";

//Propiedades para manejar la apertura del modal
const isModalOpenEdit = ref(false);
const isModalOpenAdd = ref(false);

//Propiedad para definir la pagina actual, para el servicio y el total de paginas para enviar al paginador
const page = ref(1);
const total_pages = ref(0);

//Propiedad para guardar la busqueda
const busqueda = ref("");

//Popriedad para guardar el estado del delegado, esta se llenara cuando el td de la tabla emita el evento(saber si esta activo o inactivo)
const estadoActualDelegado = ref("");

//Array que almacena la info que necesitamos en cada td, para recorrerla e irla enviando
const ArrayDelegados = reactive([]);

//Objeto de prueba, para enviarle la informacion del delegado al modal de detalle
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

//Objeto que almacena la configuracion del paginador, es decir, la respuesta que nos da el endPoint,
//el array de usuarios, la pagina actual, la cantidad de paginas, etc... 
//esto con el fin de ir actualizando la información para que el array funcione de manera adecuada. 
//Se llena cada que el paginador emita el evento de cambio de pagina, ya sea previous o next
const configPagination = reactive({});

//Funcion que se ejecuta cuando se emite un evento desde el td, recibe el nuevo estado, cada que se hace algún cambio. 
//Se encarga de actualizar ese estado en el array 
const cambiarEstadoCheckboxDelegado = (index) => {
  estadoActualDelegado.value = ArrayDelegados[index].p_estado == "activo" ? "inactivo" : "activo";
  ArrayDelegados[index].p_estado = estadoActualDelegado.value;
};

//Función que se ejecuta cuando se cambia la pagina desde el paginador, es decir, cuando el paginador nos emite por medio del evento
//Su funcionalidad es recibir la pagina actual, para poder actualizar nuestra propiedad page, hacer la petición, para que el 
//endPoint nos devuelva el data con los respectivos campos(la misma respuesta de siempre) 
const handlePaginate = async (pagina) => {
  page.value = pagina;
  const newPage = await fetchAllDelegates(page.value);
  total_pages.value = newPage.data.total_pages;
  configPagination.value = await newPage.data;
  modificarArrayDelegados();
};

//Función que se ejecutara cada que el paginador emita un cambio de pagina, se encarga de actualizar el array con la nueva información
const modificarArrayDelegados = () => {
  const users = configPagination.value.users;
  users.forEach(function (delegado, i) {
    const infoDelegado = {
      id_usuario: delegado.id_usuario,
      nombres: delegado.nombres,
      apellidos: delegado.apellidos,
      nombre_institucion: delegado.detalles_institucionales[0].id_institucion,
      primer_area: delegado.detalles_institucionales[0].primer_area.nombre,
      segunda_area: delegado.detalles_institucionales[0].segunda_area.nombre,
      url_titulo: delegado.titulos_academicos[0].url_titulo,
      estado: delegado.estado,
      tipo_documento: delegado.tipo_documento.nombre,
      documento: delegado.documento,
      celular: delegado.celular,
      correo: delegado.correo,
    }
    ArrayDelegados[i] = infoDelegado;
  });
};

//Función que cambia el valor de la propiedad para que el modal de agregar se pueda abrir
const showModalAdd = () => {
  isModalOpenAdd.value = true;
};

//Función que cambia el valor de la propiedad para que el modal de agregar se cierre
const closeModalAdd = () => {
  isModalOpenAdd.value = false;
};

//Función que se ejecutara cuando el td emita que le dieron click al btn de abrir modal detalle, 
//esta modifica el objeto con la info que se enviara al modal detalle(también era prueba)
//el td puede devolver toda la info completa(ya que la tiene), se instancia un objeto global vacio y se llena con la info recibida.
const showModalDetail = (infoDelegado) => {
  infoModalDetail.p_idDelegado = infoDelegado.p_idDelegado;
  infoModalDetail.p_tipoDocumento = infoDelegado.p_tipoDocumento;
  infoModalDetail.p_documento = infoDelegado.p_documento;
  infoModalDetail.p_nombres = infoDelegado.p_nombres;
  infoModalDetail.p_apellidos = infoDelegado.p_apellidos;
  infoModalDetail.p_areaConocimiento = infoDelegado.p_areaConocimiento;
  infoModalDetail.p_institucion = infoDelegado.p_institucion;
  infoModalDetail.p_telefono = infoDelegado.p_telefono;
  infoModalDetail.p_correo = infoDelegado.p_correo;
  isModalOpenEdit.value = true;
};

//Función para cerrar modal detalle 
const closeModalDetail = () => {
  isModalOpenEdit.value = false;
};

//Función para utilizar el servicio, hacer la petición y actualizar las respectivas propiedades.
const fetchAllDelegates = async () => {
  try {
    const response = await getDelegatesAll(page.value);
    total_pages.value = response.data.total_pages;
    configPagination.value = response.data;
    modificarArrayDelegados();
    return response;
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
