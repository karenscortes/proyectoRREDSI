<template>
  <div class="container mt-5">
    <div>
      <!--Titulo principal-->
      <div>
        <h1 class="titulo_principal d-flex justify-content-start">
          {{ tituloPrincipal }}
        </h1>
      </div>
      <div
        class="contenedor_principal d-flex justify-content-between flex-lg-row flex-column-reverse"
      >
        <!-- Tabla -->
        <div class="table-responsive w-sm-100 w-md-100 w-lg-75">
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
                v-for="(item, index) in infoItems"
                :key="index"
                :infoItem="item"
                @editarItem="onEditModal($event)"
              >
              </ItemTBody>
              <!-- row btn añadir item-->
              <tr class="tr_item_rubrica">
                <td class="td_boton text-center" colspan="3">
                  <button class="boton_añadir" @click="showModal()">
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
              <CardTipo :infoCard="card"> </CardTipo>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--Sesion de modales-->
    <ModalAdd
      v-if="isModalOpen"
      @close="closeModal()"
      :infoModalEditar="infoModalEditar"
    ></ModalAdd>
    <ModalDelete></ModalDelete>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { getRubricsAll } from "@/services/administradorService";
import { reactive } from "vue";
import { ref } from "vue";
import ModalDelete from "../components/Users/administrador/rubricas/ModalDelete.vue";
import ModalAdd from "../components/Users/administrador/rubricas/ModalAdd.vue";
import CardTipo from "../components/Users/administrador/rubricas/CardTipo.vue";
import ItemTBody from "../components/Users/administrador/rubricas/ItemTBody.vue";
import FootTable from "../components/Users/administrador/rubricas/FootTable.vue";
import ItemThead from "../components/Users/administrador/rubricas/ItemThead.vue";

const isModalOpen = ref(false);
//Titulo contenedor principal
const tituloPrincipal = "Gestionar rúbricas";

//info para enviar al modal(Editar)
const infoModalEditar = reactive({
  id_item_rubrica: null,
  titulo: "",
  valor_max: null,
  componente: "",
});

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

//info items rubrica
const infoItems = reactive([]);

//info para la card
const infoCards = reactive([
  {
    image: "rubrica.png",
    altImage: "Esto es un ejemplo",
    idModalidad: 1,
    modalidadProyecto: "Poster",
    idFase: 1,
    faseProyecto: "Presencial",
  },
  {
    image: "rubrica.png",
    altImage: "Esto es un ejemplo",
    idModalidad: 1,
    modalidadProyecto: "Poster",
    idFase: 1,
    faseProyecto: "Presencial",
  },
  {
    image: "rubrica.png",
    altImage: "Esto es un ejemplo",
    idModalidad: 1,
    modalidadProyecto: "Poster",
    idFase: 1,
    faseProyecto: "Presencial",
  },
  {
    image: "rubrica.png",
    altImage: "Esto es un ejemplo",
    idModalidad: 1,
    modalidadProyecto: "Poster",
    idFase: 1,
    faseProyecto: "Presencial",
  },
]);

//Evento cambiar valores modal por info actual
const onEditModal = (informacionTr) => {
  infoModalEditar.id_item_rubrica = informacionTr.id_item_rubrica;
  infoModalEditar.titulo = informacionTr.titulo;
  infoModalEditar.valor_max = informacionTr.valor_max;
  infoModalEditar.componente = informacionTr.componente;
  showModal();
};

//Evento para cerrar el modal
const closeModal = () => {
  infoModalEditar.id_item_rubrica = null;
  infoModalEditar.titulo = "";
  infoModalEditar.valor_max = null;
  infoModalEditar.componente = "";
  isModalOpen.value = false;
};

//Evento para abrir el modal
const showModal = () => {
  isModalOpen.value = true;
};
const fetchAllRubrics = async () => {
  try {
    const response = await getRubricsAll();
    const primerRubrica = response.data[0].items_rubrica;
    primerRubrica.forEach(function (item, i) {
      infoItems[i] = item; 
    });
  } catch (error) {
    console.error("Error al obtener rubricas: ", error);
    alert("Error al obtener las rúbricas");
  }
};
onMounted(() => {
  fetchAllRubrics();
});
</script>

<style scoped>
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
  height: 60vh;
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
