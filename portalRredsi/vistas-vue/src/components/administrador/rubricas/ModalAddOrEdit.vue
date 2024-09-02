<template>
  <!--Modal de añadir item-->
  <div
    class="modalCabecero modal fade show"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content rounded-st-1 shadow-lg modal-responsive">
        <div class="modal-header p-4 shadow w-100">
          <i class="fas fa-list icon"></i>
          <h1 class="modal-title fs-5" id="staticBackdropLabel">Item Rúbrica</h1>
          <button
            type="button"
            class="btn-close"
            @click="closeModal()"
          ></button>
        </div>
        <div class="modal-body">
          <form action="">
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
                  class="form_modal form-control" v-model="tituloItem"
                />
              </div>
              <div class="col-md-6 mb-4">
                <label for="valor_maximo" class="form-label"
                  >Valor máximo
                  <span class="text-danger fw-bold">*</span>
                </label>
                <input
                  type="text"
                  id="valor_maximo"
                  name="valor_maximo"
                  required="required"
                  class="form_modal form-control" v-model="valorMax"
                />
              </div>
              <div class="col-md-12 mb-4">
                <label for="descripcion" class="form-label "
                  >Descripción
                  <span class="text-danger fw-bold">*</span>
                </label>
                <textarea
                  id="descripcion"
                  name="descripcion"
                  required="required"
                  class="form_textArea form-control" v-model="descripcion"
                ></textarea>
              </div>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="btn" data-bs-dismiss="modal" @click="closeModal()">Cerrar</button>
          <button class="btn" data-bs-dismiss="modal">Guardar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
export default{
  props:{
    infoModalEditar: {
      type: Object,  
      default: null,
      validator(value){
        return(
          (typeof value.p_idItem === 'number' || value.p_idItem == null) &&
          typeof value.p_tituloItem === 'string' &&
          typeof value.p_valorMax === 'number' &&
          typeof value.p_descripcion === 'string'
        );
      }
    }
  },
  emits: ['close'],
  setup(props, {emit}){
    const closeModal = ()=>{
      emit('close');
    }
    const tituloItem = ref (props.infoModalEditar.p_tituloItem);
    const valorMax = ref(props.infoModalEditar.p_valorMax);
    const descripcion = ref(props.infoModalEditar.p_descripcion);
    return{tituloItem,valorMax,descripcion,closeModal};
  }
}
</script>

<style scoped>
.modalCabecero{
  display: block;
}
textarea{
  color: black
}
.modal-dialog {
  max-width: 50%;
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
label{
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
.btn{
  background-color: rgb(255, 182, 6);
  font-weight: 700;
}
.btn:focus{
  border: none;
  box-shadow: none;
  color: #494949;
  background-color: rgb(255, 182, 6);
}
@media only screen and (min-width: 500px) and (max-width: 768px) {
  .modal-dialog {
    min-width: 97%;
  }
}
</style>
