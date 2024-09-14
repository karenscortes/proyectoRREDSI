<template>
  <!--Modal confirmación eliminar rúbrica-->
  <div
    class="modalCabecero modal fade show"
    id="modalEliminar"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered" style="max-width: 25%">
      <div class="modal-content rounded-st-1 shadow-lg modal-responsiven">
        <button
          type="button"
          class="btn-close"
          @click="closeModal()"
        ></button>
        <div class="modal-body">
          <form action="">
            <div class="row">
              <div class="col-md-12 mb-4">
                <h2 class="mensaje_body text-center">
                  ¿Seguro que quieres eliminar este ítem?
                </h2>
              </div>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="btn mx-auto" @click="closeModal()">Cancelar</button>
          <button class="btn mx-auto" @click="save()">Aceptar</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import {deleteItems} from "@/services/administradorService";
const props = defineProps({
  id_item_rubrica: {
    type: Number,
    required: true,
  },
});

const emit = defineEmits(['close', 'actualizarRubrica']);
const closeModal = () => {
  emit('close'); 
}

const actualizar = (id_item)=>{
  emit('actualizarRubrica', id_item); 
}
const save = () => {
  const aux_id_item = props.id_item_rubrica;  
  const result = deleteItems(aux_id_item); 
  closeModal();
  actualizar(aux_id_item); 
  console.log(aux_id_item);
}
</script>
<style scoped>
.modalCabecero{
  display: block;
}
.btn-close {
  margin-left: auto;
}
.mensaje_body {
  font-size: 24px;
  color: black;
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
.modal-footer {
  border: 1px solid yellow;
}
@media only screen and (min-width: 500px) and (max-width: 768px) {
  .modal-dialog {
    min-width: 97%;
  }
}
</style>
