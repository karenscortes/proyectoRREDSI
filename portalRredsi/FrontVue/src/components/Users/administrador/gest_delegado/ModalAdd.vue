<template>
  <div
    class="modalCabecero modal fade show"
    id="createAccount"
    tabindex="-1"
    aria-labelledby="modalLabel"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div
        class="modal-content border border-dark border-5 rounded-5 text-dark"
      >
        <div class="text-center">
          <button type="button" class="close mr-3 mt-3" @click="closeModal()">
            <span>&times;</span>
          </button>
          <h3 class="modal-title mt-4 mb-3 text-center" id="modalLabel">
            Crear Cuenta de Delegado
          </h3>
        </div>
        <div class="modal-body">
          <form action="" id="formAdd" @submit.prevent="save()">
            <div class="row">
              <!-- Select para Tipo de Documento -->
              <div class="col-md-6 mb-4">
                <label for="id_tipo_documento" class="form-label"
                  >Tipo de Documento
                  <span class="text-danger fw-bold">*</span>
                </label>
                <select
                  class="form-select"
                  id="id_tipo_documento"
                  v-model="user.id_tipo_documento"
                  required
                >
                  <option :value="null" disabled selected>
                    Tipo de documento
                  </option>
                  <option
                    class="option"
                    v-for="(tipo, index) in arrayDocuments"
                    :key="index"
                    :value="tipo.id_tipo_documento"
                  >
                    {{ tipo.nombre }}
                  </option>
                </select>
              </div>

              <!-- Documento -->
              <div class="col-md-6 mb-4">
                <label for="documento" class="form-label"
                  >Documento
                  <span class="text-danger fw-bold">*</span>
                </label>
                <input
                  type="text"
                  id="documento"
                  class="form-control"
                  v-model="user.documento"
                  required
                />
              </div>

              <!-- Nombres -->
              <div class="col-md-6 mb-4">
                <label for="nombres" class="form-label"
                  >Nombres
                  <span class="text-danger fw-bold">*</span>
                </label>
                <input 
                  type="text" 
                  id="nombres" 
                  class="form-control" 
                  v-model="user.nombres" 
                  required 
                />
              </div>

              <!-- Apellidos -->
              <div class="col-md-6 mb-4">
                <label for="apellidos" class="form-label"
                  >Apellidos
                  <span class="text-danger fw-bold">*</span>
                </label>
                <input
                  type="text"
                  id="apellidos"
                  class="form-control"
                  v-model="user.apellidos"
                  required
                />
              </div>

              <!-- Celular -->
              <div class="col-md-6 mb-4">
                <label for="celular" class="form-label"
                  >Celular
                  <span class="text-danger fw-bold">*</span>
                </label>
                <input 
                  type="tel" 
                  id="celular" 
                  class="form-control" 
                  v-model="user.celular"
                  required 
                />
              </div>

              <!-- Correo -->
              <div class="col-md-6 mb-4">
                <label for="correo" class="form-label"
                  >Correo Electrónico
                  <span class="text-danger fw-bold">*</span>
                </label>
                <input 
                  type="email" 
                  id="correo" 
                  class="form-control" 
                  v-model="user.correo"
                  required 
                />
              </div>

              <!-- Botón de Enviar -->
              <div class="col-12 text-center">
                <button
                  type="submit"
                  class="btn btn-warning w-50"
                  form="formAdd"
                >
                  Guardar
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { reactive, ref } from "vue";
import { onMounted } from "vue";
import { getAllDocumentsType } from "../../../../services/administradorService";
import { createDelegate } from "../../../../services/administradorService";
import { useToastUtils } from '@/utils/toast'; 

const { showErrorToast, showSuccessToast} = useToastUtils();

//array para almacenar variedas de tipos de documento
const arrayDocuments = reactive([]);  

//objeto para almacenar los valores de los inputs
const user = reactive({
  id_rol: 2,
  id_tipo_documento: null,
  documento: "",
  nombres: "",
  apellidos: "",
  celular: "",
  correo: "",
  estado: "activo",
  clave: "",
});

//Función para 
const fetchAllDocumentsTypes = async () => {
  try {
    const documents_types = await getAllDocumentsType();
    arrayDocuments.splice(0, arrayDocuments.length, ...documents_types.data);
    return documents_types
  } catch (error) {
    showErrorToast("Ocurrió un error al obtener los tipos de documento. Por favor, vuelve a intentarlo.");
  }
};

//función para crear delegado
const save = async () => {
  if(user.id_tipo_documento !== null){
    closeModal(); 
    const userCreate = await createDelegate(user);
    showSuccessToast("Se registró con éxito.");
  }else{
    showErrorToast("Por favor, ingrese un tipo de documento.");
  }
  
};

onMounted(() => {
  fetchAllDocumentsTypes();
});

//Emitir evento para notificarle a rúbrica que debe cerrar el modal
const emit = defineEmits(["close"]);
const closeModal = () => {
  emit("close");
};

</script>
<style>
.modalCabecero {
  display: block;
}
</style>
