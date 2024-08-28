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
        <!-- tabla -->
        <div class="table-responsive w-sm-100 w-md-100 w-lg-75">
          <table class="display table text-dark table-bordered-dark">
            <thead class="thead_table">
              <!--Imput thead-->
              <ItemThead></ItemThead>
              <ItemThead></ItemThead>
              <ItemThead></ItemThead>
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
              <ItemTBody></ItemTBody>
              <ItemTBody></ItemTBody>
              <ItemTBody></ItemTBody>
              <ItemTBody></ItemTBody>
              <!--Btn añadir item-->
              <tr class="tr_item_rubrica">
                <td class="td_boton text-center" colspan="3">
                  <button
                    data-bs-toggle="modal"
                    data-bs-target="#modalAñadirItem"
                    class="boton_añadir"
                  >
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
        <div class="scroll-div border border-1 border-dark rounded-1">
          <h2 class="tipo_formato d-flex justify-content-center">
            Elije uno de los formatos
          </h2>
          <!--Aqui van las cards-->
          <div class="row text-center">
            <div
              class="col_card col-lg-12 col-md-6 col-6 d-flex justify-content-md-center justify-content-center"
            >
              <CardTipo></CardTipo>
            </div>

            <div
              class="col_card col-lg-12 col-md-6 col-6 d-flex justify-content-md-center justify-content-center"
            >
              <CardTipo></CardTipo>
            </div>
            <div
              class="col_card col-lg-12 col-md-6 col-6 d-flex justify-content-md-center justify-content-center mb-2"
            >
              <CardTipo></CardTipo>
            </div>
            <div
              class="col_card col-lg-12 col-md-6 col-6 d-flex justify-content-md-center justify-content-center mb-2"
            >
              <CardTipo></CardTipo>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--Btn regresar, Btn editar-->
    <div class="cont_boton d-flex justify-content-center mt-3 w-lg-75">
      <button class="btn boton pl-5 pr-5 mx-auto">Regresar</button>
      <button class="btn boton pl-5 pr-5 mx-auto">Editar</button>
    </div>
    <ModalAdd></ModalAdd>
    <ModalDelete></ModalDelete>
  </div>
</template>

<script>
import CardTipo from "./CardTipo.vue";
import ItemTBody from "./ItemTBody.vue";
import ItemThead from "./ItemThead.vue";
import FootTable from "./FootTable.vue"
import ModalAdd from "./ModalAdd.vue";
import ModalDelete from "./ModalDelete.vue";

export default {
  setup() {
    const tituloPrincipal = "Gestionar rúbricas";
    return { tituloPrincipal };
  },
  components: {
    CardTipo,
    ItemTBody,
    ItemThead,
    FootTable,
    ModalAdd,
    ModalDelete,
  },
};
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
  margin-left: 25%;
  font-weight: 600;
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
  padding-left: 24px;
  padding-right: 24px;
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
.titulo_rubrica{
	font-size: 18px; font-weight: bold;
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
    margin-left: 22%;
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
