<template>
  <div class="container">
    <div class="row mb-5 mt-2">
      <!-- Titulo Principal -->
      <div class="col">
        <div class="section_title text-center">
          <h1>Gestionar Cuentas Delegados</h1>
        </div>
      </div>
    </div>

    <!-- Spinner global mientras se cargan los delegados -->
    <div v-if="loading" class="text-center my-5">
      <SpinnerGlobal />
    </div>

    <!-- Mostrar el contenido solo cuando no esté cargando -->
    <div v-else>
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
                        placeholder="Nombre o documento"
                      />
                    </div>
                    <div class="col-md-2 col-4">
                      <button
                        class="btn btn-dark w-100 font-weight-bold"
                        @click="buscar()"
                      >
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
                  >
                    <i class="fas fa-plus extra-bold-icon"></i>
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
              <!-- Componente hijo: RowTableDelegado -->
              <RowTableDelegado
                v-for="(delegado, index) in ArrayDelegados"
                :key="index"
                :index="index"
                :infoDelegado="delegado"
                @open="showModalDetail($event)"
                @check="cambiarEstadoCheckboxDelegado($event)"
              />
            </tbody>
          </table>
        </div>
      </div>

      <!-- Paginador -->
      <PaginatorBody
        :totalPages="total_pages"
        @page-changed="handlePaginate($event)"
      />
      
      <!-- Modal de agregar delegado -->
      <ModalAdd @close="closeModalAdd()" v-if="isModalOpenAdd"></ModalAdd>
      
      <!-- Modal de detalle de delegado -->
      <ModalDetalle
        v-if="isModalOpenEdit"
        @closeModalDetail="closeModalDetail()"
        :infoModal="infoModalDetail"
      ></ModalDetalle>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref, reactive } from "vue";
import { useToastUtils } from '@/utils/toast'; 
import RowTableDelegado from "../components/Users/administrador/gest_delegado/RowTableDelegado.vue";
import SpinnerGlobal from "@/components/UI/SpinnerGlobal.vue"; 
import ModalAdd from "../components/Users/administrador/gest_delegado/ModalAdd.vue";
import ModalDetalle from "../components/Users/administrador/gest_delegado/ModalDetalle.vue";
import PaginatorBody from "../components/UI/PaginatorBody.vue";
import { getDelegatesAll } from "@/services/administradorService";
import { updateStatusDelegate } from "@/services/administradorService";
import { getDelegateByNameOrDocument} from "@/services/administradorService";

const { showErrorToast, showInfoToast } = useToastUtils();

//Propiedades para manejar la apertura del modal
const isModalOpenEdit = ref(false);
const isModalOpenAdd = ref(false);

//Propiedad para definir la pagina actual, para el servicio y el total de paginas para enviar al paginador
const page = ref(1);
const total_pages = ref(0);

// Propiedad para controlar la carga de la lista de delegados
const loading = ref(true); // Iniciar como 'true' porque estamos cargando los datos

//Propiedad para guardar la busqueda
const busqueda = ref("");

//Popriedad para guardar el estado del delegado, esta se llenara cuando el td de la tabla emita el evento(saber si esta activo o inactivo)
const estadoActualDelegado = ref("");

//Array que almacena la info que necesitamos en cada td, para recorrerla e irla enviando
const ArrayDelegados = reactive([]);

//Objeto de prueba, para enviarle la informacion del delegado al modal de detalle
const infoModalDetail = reactive({});

//Objeto que almacena la configuracion del paginador.
const configPagination = reactive({});

//Funcion que se ejecuta cuando se emite un evento desde el td, recibe el nuevo estado, cada que se hace algún cambio.
const cambiarEstadoCheckboxDelegado = (index) => {
  estadoActualDelegado.value =
  ArrayDelegados[index].estado == "activo" ? "inactivo" : "activo";
  ArrayDelegados[index].estado = estadoActualDelegado.value;
  const estado = estadoActualDelegado.value;
  const id_delegado = ArrayDelegados[index].id_usuario;
  actualizarEstado(id_delegado, estado);
};

//Función que se ejecuta cuando se cambia la pagina desde el paginador.
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
  ArrayDelegados.splice(0, ArrayDelegados.length);
  users.forEach(function (delegado, i) {
    const infoDelegado = {
      id_usuario: delegado.id_usuario,
      nombres: delegado.nombres,
      apellidos: delegado.apellidos,
      nombre_institucion:
      delegado.detalles_institucionales[0].institucion.nombre,
      primer_area: delegado.detalles_institucionales[0].primer_area.nombre,
      segunda_area: delegado.detalles_institucionales[0].segunda_area.nombre,
      url_titulo: delegado.titulos_academicos[0].url_titulo,
      estado: delegado.estado,
      tipo_documento: delegado.tipo_documento.nombre,
      documento: delegado.documento,
      celular: delegado.celular,
      correo: delegado.correo,
    };
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

//Función para abrir modal detalle
const showModalDetail = (infoDelegado) => {
  infoModalDetail.value = infoDelegado;
  isModalOpenEdit.value = true;
};

//Función para cerrar modal detalle
const closeModalDetail = () => {
  isModalOpenEdit.value = false;
};

//Funcion para actualizar el estado del delegado
const actualizarEstado = async (id_delegado, estado) => {
  try {
    const response = await updateStatusDelegate(id_delegado, estado);
    return response;
  } catch (error) {
    console.error("Error al actualizar el estado: ", error);
    alert("Error al actualizar el estado del delegado");
  }
};

// Función para buscar delegados
const buscar = async () => {
  loading.value = true; // Mostrar spinner mientras busca
  try {
    if (busqueda.value !== "") {
      const response = await getDelegateByNameOrDocument(busqueda.value);
      configPagination.value.users = [response.data];
      configPagination.value.total_pages = 1;
      configPagination.value.total_users = 1;
      modificarArrayDelegados();
      busqueda.value = "";
    } else {
      await fetchAllDelegates();
    }
  } catch (error) {
    showErrorToast("Error al buscar el delegado.");
  } finally {
    loading.value = false; // Esconder spinner
  }
};

// Función para cargar los delegados
const fetchAllDelegates = async () => {
  loading.value = true; // Mostrar el spinner
  try {
    const response = await getDelegatesAll(page.value);
    total_pages.value = response.data.total_pages;
    configPagination.value = response.data;
    modificarArrayDelegados();
  } catch (error) {
    showErrorToast("Error al cargar los delegados.");
  } finally {
    loading.value = false; // Ocultar el spinner una vez se carguen los datos
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
