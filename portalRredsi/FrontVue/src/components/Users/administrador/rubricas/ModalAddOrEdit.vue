<template>
  <!--Modal de añadir item-->
  <div
    class="modalCabecero modal fade show"
    data-bs-backdrop="static" 
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content rounded-st-1 shadow-lg modal-responsive">
        <div class="modal-header p-4 shadow w-100">
          <i class="fas fa-list icon"></i>
          <h1 class="modal-title fs-5" id="staticBackdropLabel">
            Item Rúbrica
          </h1>
          <button
            type="button"
            class="btn-close"
            @click="closeModal()"
          ></button>
        </div>
        <div class="modal-body">
          <form action="" id="formAdd" @submit.prevent="save()">
            <div class="row">
              <div class="col-md-6 mb-4">
                <label for="titulo" class="form-label"
                  >Título
                  <span class="text-danger fw-bold">*</span>
                </label>
                <input
                  type="text"
                  id="titulo"
                  name="titulo"
                  required="required"
                  class="form_modal form-control"
                  v-model="itemActual.titulo"
                />
              </div>
              <div class="col-md-6 mb-4">
                <label for="valor_maximo" class="form-label"
                  >Valor máximo
                  <span class="text-danger fw-bold">*</span>
                </label>
                <input
                  type="number"
                  id="valor_maximo"
                  name="valor_maximo"
                  required="required"
                  class="form_modal form-control"
                  v-model="itemActual.valor_max"
                />
              </div>
              <div class="col-md-12 mb-4">
                <label for="descripcion" class="form-label"
                  >Descripción
                  <span class="text-danger fw-bold">*</span>
                </label>
                <textarea
                  id="descripcion"
                  name="descripcion"
                  required="required"
                  class="form_textArea form-control"
                  v-model="itemActual.componente"
                ></textarea>
              </div>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="btn" data-bs-dismiss="modal" @click="closeModal()">
            Cerrar
          </button>
          <button class="btn" type="submit" form="formAdd">Guardar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { updateItems } from "@/services/administradorService";
import { InsertItems } from "@/services/administradorService";
import { defineEmits, reactive } from "vue";
import { useToastUtils } from "@/utils/toast";

const {showSuccessToast } = useToastUtils();

const props = defineProps({
  infoModalEditar: {
    type: Object,
    default: null,
    validator(value) {
      return (
        typeof (value.id_item_rubrica === "number" || value.id_item_rubrica === null)&&
        typeof (value.id_rubrica === "number" || value.id_rubrica === null) &&
        typeof (value.titulo === "string" || value.titulo === null) &&
        typeof (value.componente === "number" || value.componente === null) &&
        typeof (value.valor_max === "string" || value.valor_max === null)
      );
    },
  },
});

const emit = defineEmits(["close", "actualizarRubrica", "newRubricAdded"]);

//Propiedad auxiliar para guardar el id del item
const id_item_rubrica = props.infoModalEditar.id_item_rubrica;

//Objeto reactivo para almacenar los cambios que se realicen
const itemActual = reactive({
  id_rubrica: props.infoModalEditar.id_rubrica,
  titulo: props.infoModalEditar.titulo,
  componente: props.infoModalEditar.componente,
  valor_max: props.infoModalEditar.valor_max,
});

//Método para cerrar el modal
const closeModal = () => {
  emit("close");
};

//Método para emitir el evento a la rubrica
const actualizar = () => {
  emit("actualizarRubrica", { id_item_rubrica, itemActual });
};

const newRubricAdded = (nuevo_item) => emit("newRubricAdded", nuevo_item);

//Método para hacer el guardado, cerrar modal y disparar el método que emitira
const save = async () => {
  if (id_item_rubrica == null) {
    const { data } = await InsertItems(itemActual);
    const { data: id_item_rubrica } = data;
    newRubricAdded({ id_item_rubrica, ...itemActual });
    
    if(data.success == true){
      showSuccessToast("Se registró con éxito");
    }
    
  } else {
    const itemActualizado = await updateItems(id_item_rubrica, itemActual);

    if(itemActualizado.data.success){
      showSuccessToast("Se editó con éxito");
    }
    actualizar();
  }
  closeModal();
};
</script>

<style scoped>
.modalCabecero {
  display: block;
}
textarea {
  color: black;
}
.modal-header {
  border: 1px solid yellow;
}
.form_modal {
  border: 1px solid rgb(190, 190, 190);
  border-radius: 5px;
}
.form_textArea {
  border: 1px solid rgb(190, 190, 190);
  width: 100%;
  height: 100%;
  border-radius: 5px;
}
.form_textArea:focus {
  border: 1px solid rgb(150, 149, 149);
  box-shadow: 0 0 5px 2px rgba(230, 230, 207, 0.8);
  outline: none;
  border-radius: 3px;
}
.form_modal:focus {
  border: 1px solid rgb(150, 149, 149);
  box-shadow: 0 0 5px 2px rgba(230, 230, 207, 0.8);
  outline: none;
  border-radius: 3px;
}
label {
  font-size: 20px;
  font-weight: bold;
  color: black;
  width: 100%;
  text-align: start;
}
i {
  font-size: 30px;
  margin-right: 8px;
  color: rgb(255, 182, 6);
}
.btn {
  background-color: rgb(255, 182, 6);
  font-weight: 700;
}
.btn:focus {
  border: none;
  box-shadow: none;
  color: #494949;
  background-color: rgb(255, 182, 6);
}
@media only screen and (min-width: 500px) and (max-width: 768px) {
  .modal-dialog {
    min-width: 50%;
  }
}
</style>
