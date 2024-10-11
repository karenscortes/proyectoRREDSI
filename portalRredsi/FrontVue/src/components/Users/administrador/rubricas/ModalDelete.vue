<template>
  <!--Modal confirmación eliminar rúbrica-->
  <div
    class="modalCabecero modal fade show"
    id="modalEliminar"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
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
import { reactive, onMounted} from "vue";
import { useToastUtils } from '@/utils/toast'; 

const { showErrorToast, showWarningToast, showSuccessToast} = useToastUtils();
const props = defineProps({
  infoModalEliminar: {
    type: Object,
    default:null,
    validator(value) {
      return (
        typeof value.id_item_rubrica === "number" &&
        typeof value.id_rubrica === 'number'
      );
    }
  }
  
});

//Info para mandarle a la rúbrica y que actualice su vista
const infoBorrar = reactive({
  'id_rubrica': props.infoModalEliminar.id_rubrica, 
  'id_item_rubrica': props.infoModalEliminar.id_item_rubrica,
});

//Definimos los eventos a emitir
const emit = defineEmits(['close', 'actualizarRubrica']);

//Método para cerrar el evento 
const closeModal = () => {
  emit('close'); 
}

//Método que emitira el evento a la rubrica
const actualizar = ()=>{
  emit('actualizarRubrica', infoBorrar); 
}

//Función para eliminar item, cerrar modal y disparar el método que emitira a la rubrica
const save = async () => {
  const aux_id_item = props.infoModalEliminar.id_item_rubrica;  
  const result = await deleteItems(aux_id_item);
  closeModal();
  actualizar(); 
  if(result.data.success == true){
    showSuccessToast("Se eliminó con éxito");
  }else{
    showErrorToast("No se pudó realizar esta acción, intenta de nuevo");
  }
}

onMounted(() => {
  showWarningToast('Cuidado, esta acción no se puede deshacer');
});

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
