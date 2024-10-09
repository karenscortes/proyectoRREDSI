<template>
  <div class="container">
    <div>
      <!--Titulo principal-->
      <div class="row mb-5 mt-2">
        <div class="col">
          <div class="section_title text-center">
            <h1>Gestionar rúbricas</h1>
          </div>
        </div>
      </div>
      <div
        class="contenedor_principal d-flex justify-content-between flex-lg-row flex-column-reverse"
      >
        <!-- Tabla -->
        <div class="table w-sm-100 w-md-100 w-lg-75 h-30">
          <table
            class="display table text-dark table-bordered-dark"
            id="basic-datatables"
          >
            <thead class="thead_table">
              <!--Imput thead-->
              <ItemThead
                v-for="(imput, index) in infoImputs"
                :key="index"
                :infoImputs="imput"
              >
              </ItemThead>
              <!--Cabecero titulos-->
              <tr class="tr_rubrica">
                <td class="titulo_rubrica text-center">Componentes</td>
                <td></td>
                <td></td>
                <td class="titulo_rubrica">Max valor</td>
                <td class="titulo_rubrica text-center">Calificación</td>
                <td class="titulo_rubrica text-center" colspan="3">
                  Observaciones
                </td>
              </tr>
            </thead>
            <tbody>
              <!--item rubrica-->
              <ItemTBody
                v-for="item in infoItems"
                :key="item.id_item_rubrica"
                :infoItem="item"
                @eliminarItem = "onDeleteModal($event)"
                @editarItem="onEditModal($event)"
              >

              </ItemTBody>
              <!-- row btn añadir item-->
              <tr class="tr_item_rubrica">
                <td class="td_boton text-center" colspan="3">
                  <button class="boton_añadir" @click="showModalEdit()">
                    Añadir
                  </button>
                </td>

                <td class="td_valor_max"></td>
                <td class="td_calificacion"></td>
                <td class="td_observacion"></td>
              </tr>
              <!--foot rubrica-->
              <FootTable></FootTable>
            </tbody>
          </table>
        </div>
        <!--Contenedor card (tipos rúbricas)-->
        <div class="scroll-div border border-1 border-dark rounded-1 pb-2">
          <h2 class="tipo_formato d-flex justify-content-center">
            Elije uno de los formatos
          </h2>
          <!--Aqui van las cards-->
          <div class="row text-center">
            <div
              class="col_card col-lg-12 col-md-6 col-6 d-flex justify-content-md-center justify-content-center"
              v-for="(card, index) in infoCards"
              :key="index"
            >
              <CardTipo :infoCard="card" :infoImage="infoImageCards" @cardSeleccionada="onCardSeleccionada($event)"> </CardTipo>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--Sesion de modales-->
    <ModalAdd
      v-if="isModalEditOpen"
      @close="closeEditModal()"
      :infoModalEditar="infoModalEditarOrAdd"
      @actualizarRubrica="actualizarItemEdit($event)"
      @newRubricAdded="nuevoItem($event)"
    ></ModalAdd>
    <ModalDelete 
    v-if="isModalDeleteOpen" 
    :infoModalEliminar="infoModalEliminar" 
    @close="CloseDeleteModal()"
    @actualizarRubrica="actualizarItemDelete($event)">
    </ModalDelete>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { getRubricsAll } from "@/services/administradorService";
import { reactive } from "vue";
import { ref } from "vue";
import ModalDelete from "../components/Users/administrador/rubricas/ModalDelete.vue";
import ModalAdd from "../components/Users/administrador/rubricas/ModalAddOrEdit.vue";
import CardTipo from "../components/Users/administrador/rubricas/CardTipo.vue";
import ItemTBody from "../components/Users/administrador/rubricas/ItemTBody.vue";
import FootTable from "../components/Users/administrador/rubricas/FootTable.vue";
import ItemThead from "../components/Users/administrador/rubricas/ItemThead.vue";

//arreglo con las rubricas 
const arrayRubricas = reactive([]);
//Propiedades para manejar la apertura de los modales
const isModalEditOpen = ref(false);
const isModalDeleteOpen = ref(false); 

//Propiedad para guardar el id_item que se eliminara
const infoModalEliminar  = ref({});

//Titulo h1 del contenedor principal
const tituloPrincipal = "Gestionar rúbricas";

//info imputs del Thead
const infoImputs = reactive([
  {
    p_name_imput: "titulo",
    p_id: "titulo",
    p_titulo: "Título:",
  },
  {
    p_name_imput: "ponente",
    p_id: "ponente",
    p_titulo: "Ponente(es):",
  },
  {
    p_name_imput: "universidad",
    p_id: "universidad",
    p_titulo: "Universidad:",
  },
]);

//info para enviar al modal(Editar)
const infoModalEditarOrAdd = reactive({
  id_item_rubrica: null,
  id_rubrica: null,
  titulo: "",
  valor_max: null,
  componente: "",
});

//info para los items rubrica
const infoItems = reactive([]);

//info image card 
const infoImageCards = reactive({
  image: "rubrica.png",
  altImage: "Esto es un ejemplo",
});

//info para la card
const infoCards = reactive([]);

//Método para recorrer items de cualquier rubrica que le pasemos por parametros(array_items)
const recorrerItemsRubrica = (arrayItems) => {
  infoItems.splice(0, infoItems.length)
  arrayItems.forEach(function (item, i) {
    infoItems[i] = item;
  });
} 

//Método para actualizar rubrica con la card(rubrica) seleccionada
const onCardSeleccionada = (id_rubrica) =>{
  const itemsRubricaActual = buscarItemsRubricaSeleccionada(id_rubrica);
  infoModalEditarOrAdd.id_rubrica = id_rubrica;
  recorrerItemsRubrica(itemsRubricaActual);
}

//Método para buscar item de la rubrica seleccionada en las cards 
const buscarItemsRubricaSeleccionada = (id_rubrica)=>{
  const arrayItemsActual = reactive([]); 
  arrayRubricas.forEach(function (rubricActual,i) {
    if(rubricActual.id_rubrica == id_rubrica){
      arrayItemsActual.splice(0,arrayItemsActual.length, ... rubricActual.items_rubrica);
    }
  });
  return arrayItemsActual;
} 
//Método para abrir el modal de editar
const showModalEdit = () => {
  isModalEditOpen.value = true;
};

//Método para cambiar la información del modal editar por info actual y abrir modal de editar
const onEditModal = (informacionTr) => {
  infoModalEditarOrAdd.id_rubrica = informacionTr.id_rubrica; 
  infoModalEditarOrAdd.id_item_rubrica = informacionTr.id_item_rubrica;
  infoModalEditarOrAdd.titulo = informacionTr.titulo;
  infoModalEditarOrAdd.valor_max = informacionTr.valor_max;
  infoModalEditarOrAdd.componente = informacionTr.componente;
  showModalEdit();
};

//Método para cerrar el modal de editar y limpiar los campos
const closeEditModal = () => {
  infoModalEditarOrAdd.id_item_rubrica = null;
  infoModalEditarOrAdd.titulo = "";
  infoModalEditarOrAdd.valor_max = null;
  infoModalEditarOrAdd.componente = "";
  isModalEditOpen.value = false;
};

//Método para cambiar el valor del id_item que se enviara y abrir el modal de eliminar
const onDeleteModal = (objectEliminar) => {
  infoModalEliminar.value = objectEliminar;
  isModalDeleteOpen.value = true; 
};

//Método para cerrar el modal de eliminar
const CloseDeleteModal = () =>{
  isModalDeleteOpen.value = false; 
}

//Método para actualizar los items cuando se haya eliminado uno
const actualizarItemDelete = (infoEliminar)=>{

  const idx_rubric = arrayRubricas.findIndex( rubrica => rubrica.id_rubrica === infoEliminar.id_rubrica );
  const idx_itemRubric = arrayRubricas[idx_rubric].items_rubrica.findIndex( item => infoEliminar.id_item_rubrica === item.id_item_rubrica );
  if(idx_rubric > -1 && idx_itemRubric > -1 ){
    arrayRubricas[idx_rubric].items_rubrica.splice(idx_itemRubric,1)
    infoItems.splice(idx_itemRubric,1);
  }
}

//Método para actualizar los items cuando se haya editado
const actualizarItemEdit = ({id_item_rubrica, itemActual})=>{
  infoItems.forEach(function (item, i) {
    if(item.id_item_rubrica == id_item_rubrica){
      infoItems[i] = itemActual; 
      infoItems[i].id_item_rubrica = id_item_rubrica;
    }
  });
}

//Método para recorrer items de la primer rubrica(la de por defecto)
const itemsPrimerRubrica  =  async () => {
  const primerRubrica = arrayRubricas[0];
  const itemsRubrica = primerRubrica.items_rubrica;
  infoModalEditarOrAdd.id_rubrica = primerRubrica.id_rubrica;
  itemsRubrica.forEach(function (item, i) {
    infoItems[i] = item;
  });
}

//Método para recorrer todas las rubricas y llenar el array que se enviara a las cards(Para que se listen en cards)
const rubricas = () => {
  arrayRubricas.forEach(function (rubricActual,i) {
    const objectInfoCard = {
      'nombreModalidad': rubricActual.modalidad.nombre, 
      'nombreEtapa': rubricActual.etapa.nombre,
      'id_rubrica': rubricActual.id_rubrica,
    }
    infoCards[i] = objectInfoCard; 
  });
}

const nuevoItem = (item)=>{
  const idx_rubric = arrayRubricas.findIndex( rubrica => rubrica.id_rubrica === item.id_rubrica );
  if(idx_rubric > -1){
    arrayRubricas[idx_rubric].items_rubrica.push(item)
    infoItems.push(item);
  }
}

//Utilizando el servicio para traer todas las rubricas
const fetchAllRubrics = async () => {
  try {
    const response = await getRubricsAll();
    arrayRubricas.splice(0, arrayRubricas.length, ...response.data);
    itemsPrimerRubrica(); 
    rubricas(); 
  } catch (error) {
    console.error(error);
    alert("Error al obtener las rúbricas");
  }
};
onMounted(() => {
  fetchAllRubrics();
});
</script>

<style scoped>
.table {
  max-height: 750px;
  overflow-y: auto;
}

.boton_añadir {
  border: none;
  width: 150px;
  height: 30px;
  background-color: rgb(255, 182, 6);
  border-radius: 5px;
  font-weight: 700;
  font-size: 17px;
}
.titulo_principal {
  color: black;
}
.contenedor_principal {
  gap: 20px;
}
.tr_rubrica {
  border-bottom: 1px solid black;
}
.td_boton {
  vertical-align: middle;
}
.tr_item_rubrica {
  border-bottom: 1px solid black;
}

.tr_item_rubrica > td {
  border-right: 1px solid black;
}

.table-bordered-dark {
  border: 1px solid black;
}
.scroll-div {
  height: 73vh;
  overflow-y: auto;
  overflow-x: hidden;
}

.col_card {
  padding-left: 19px;
  padding-right: 19px;
  padding-top: 10px;
}
.boton {
  padding-left: 10px;
  padding-right: 10px;
  border: none;
  height: 40px;
  min-width: 14rem;
  width: 20%;
  font-weight: 700;
  font-size: 20px;
  color: black;
  border-radius: 5px;
  background-color: rgb(255, 182, 6);
}
.btn:hover {
  color: #494949;
  background-color: rgb(255, 182, 6);
}
.tipo_formato {
  color: black;
  font-weight: bold;
  font-style: italic;
  font-size: 16px;
}
.titulo_rubrica {
  font-size: 18px;
  font-weight: bold;
}

::-webkit-scrollbar {
  width: 13px;
}

::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background-color: rgb(255, 212, 128);
  border-radius: 10px;
  border: 2px solid #ffffff;
}

::-webkit-scrollbar-thumb:hover {
  background-color: rgb(255, 200, 100);
}

@media only screen and (min-width: 500px) and (max-width: 768px) {
  .modal-dialog {
    min-width: 97%;
  }
  .scroll-div {
    width: 100%;
  }

  .card {
    width: 100%;
  }

  .tablaloca {
    width: 100%;
  }

  .titulo_principal {
    margin-left: 10%;
  }
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .cont_boton {
    width: 100%;
  }
  .scroll-div {
    width: 100%;
  }

  .card {
    width: 75%;
  }

  .tablaloca {
    width: 100%;
  }
  .titulo_principal {
    margin-left: 23%;
  }
}

@media only screen and (min-width: 992px) and (max-width: 1366px) {
  .cont_boton {
    width: 74%;
  }

  .scroll-div {
    width: 25%;
    position: sticky;
    top: 1%;
    bottom: 10%;
  }

  .titulo_principal {
    margin-left: 17%;
  }
}

@media only screen and (min-width: 1200px) and (max-width: 2612px) {
  .cont_boton {
    width: 79%;
  }
  .titulo_principal {
    margin-left: 25%;
  }
}

@media only screen and (min-width: 992px) and (max-width: 1199px) {
  .scroll-div {
    position: sticky;
    top: 1%;
    bottom: 20%;
  }

  .tipo_formato {
    font-size: 15px;
  }

  .table-responsive {
    width: 75%;
  }

  .tablaloca {
    width: 100%;
  }
}

@media only screen and (min-width: 1367px) and (max-width: 2612px) {
  .scroll-div {
    width: 25%;
    position: sticky;
    top: 1%;
    bottom: 20%;
  }
  .table-responsive {
    width: 100%;
  }
  .btnloco {
    padding-left: 50px;
    padding-right: 50px;
  }
}
</style>
