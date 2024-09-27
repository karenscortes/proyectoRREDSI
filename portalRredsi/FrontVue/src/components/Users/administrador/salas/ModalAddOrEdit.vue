<template>
  <!--Modal editar sala-->
  <div class="modalCabecero modal fade show" id="modalSala" tabindex="-1" aria-labelledby="modalLabel"
    aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content border border-dark border-5 rounded-5 text-dark">
        <div class="text-center">
          <button type="button" class="close mr-3 mt-3" @click="closeModal()">
            <span aria-hidden="true">&times;</span>
          </button>
          <h3 class="modal-title mt-5 font-weight-bold" id="modalLabel">
            Gestionar Sala
          </h3>
        </div>
        <div class="modal-body mt-3">
          <form @submit.prevent="AddOrEdit">
            <!--Select Área-->
            <div class="form-group row justify-content-center">
              <label for="areaSelect" class="col-6 col-form-label text-right font-weight-bold">Asignar nueva
                área:</label>
              <div class="col-6">
                <select v-model="idAreaConocimiento" class="form-select text-dark p-1 w-100" id="areaSelect" required>
                  <option :value="null" disabled>Seleccionar el área</option>
                  <option v-for="(area, index) in arrayAreasConocimiento" :key="index"
                    :value="area.p_id_area_conocimiento">
                    {{ area.p_nombre }}
                  </option>
                </select>
              </div>
            </div>
            <!--Select delegado-->
            <div class="form-group row justify-content-center">
              <label for="delegadoSelect" class="col-6 col-form-label text-right font-weight-bold">Asignar nuevo
                delegado:</label>
              <div class="col-6">
                <select v-model="idDelegado" class="form-select text-dark p-1 w-100" id="delegadoSelect" required>
                  <option :value="null" selected>Seleccionar delegado</option>
                  <option class="option" v-for="(delegado, index) in arrayDelegados" :key="index" :value="delegado.id_delegado">
                    {{ delegado.nombres }} {{ delegado.apellidos }}
                  </option>
                </select>
              </div>
            </div>
            <div class="form-group row justify-content-center mb-3">
              <label for="asignarNumSala" class="col-6 col-form-label text-right font-weight-bold">Asignar Nº de
                sala:</label>
              <div class="col-6">
                <input type="text" class="form-control form-control-sm w-100" id="asignarNumSala" v-model="num_sala" required/>
              </div>
            </div>
            <div class="form-group row justify-content-center mb-5">
              <label for="asignarNombreSala" class="col-6 col-form-label text-right font-weight-bold">Asignar nombre de
                sala:</label>
              <div class="col-6">
                <input type="text" class="form-control form-control-sm w-100" id="asignarNumSala" v-model="nombre_sala" required />
              </div>
            </div>
            <div class="text-center">
              <button type="submit" class="btn btn-warning font-weight-bold">
                Guardar Cambios
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { reactive, watch } from "vue";
import { ref } from "vue";
import { addSala, updateSala } from "@/services/administradorService"
import { useToastUtils } from '@/utils/toast';

export default {
  props: {
    //Objeto que se recibe para cuando se va a editar
    infoEditar: {
      type: Object,
      default: null,
      validator(value) {
        return (
          (typeof value.p_idDelegado === "number" || value.p_idDelegado === null) &&
          (typeof value.p_idSala === "number" || value.p_idSala === null) &&
          (typeof value.p_numSala === "string" || value.p_numSala === null) &&
          (typeof value.p_nombre_sala === "string" || value.p_nombre_sala === null) &&
          (typeof value.p_idAreaConocimiento === "number" || value.p_idAreaConocimiento === null) &&
          Array.isArray(value.p_posiblesAreasConocimiento) &&
          Array.isArray(value.arrayDelegados)
        )
      },
    },
  },
  //Evento para cerrar modal
  emits: ['close'],
  setup(props, { emit }) {
    const closeModal = () => {
      emit('close');
    }

    //Propiedades para la alerta
    const { showSuccessToast, showErrorToast } = useToastUtils();


    const mostrarAlerta = () =>{
      isOpen.value = true;
    }

    //Lista de areas de conocimiento
    const arrayAreasConocimiento = reactive([]);
    watch(
      () => props.infoEditar.p_posiblesAreasConocimiento,
      (newVal) => {
        if (Array.isArray(newVal)) {
          arrayAreasConocimiento.splice(0, arrayAreasConocimiento.length, ...newVal);
        }
      },
      { immediate: true }
    );
    
    //Lista delegados
    const arrayDelegados = reactive([]);

    watch(
      () => props.infoEditar.p_lista_delegados,
      (newVal) => {
        if (Array.isArray(newVal)) {
          arrayDelegados.splice(0, arrayDelegados.length, ...newVal);
        }
      },
      { immediate: true }
    );
    console.log(arrayDelegados)

    //Propiedades en las que se guardara la info(v-model)
    const idAreaConocimiento = ref(props.infoEditar.p_idAreaConocimiento);
    const idDelegado = ref(props.infoEditar.p_idDelegado);
    const idSala = ref(props.infoEditar.p_idSala);
    const num_sala = ref(props.infoEditar.p_numSala);
    const nombre_sala = ref(props.infoEditar.p_nombre_sala);

    //Funcion para crear sala
    const crearSala = async (p_id_delegado,p_id_area_conocimiento,p_numero_sala,p_nombre_sala)=>{
      try {
        await addSala(p_id_delegado,p_id_area_conocimiento,p_numero_sala,p_nombre_sala);

        // ALERTA DE CREACION DE SALA EXITOSA
        showSuccessToast("La sala se ha creado exitosamente");
      } catch (error) {
        // ALERTA SI FALLA LA CREACION DE SALA EXITOSA
        showErrorToast("La sala no se ha podido crear, intenta de nuevo más tarde...");
      }
    }

    //Funcion para crear sala
    const actualizarSala = async (idSala,p_id_delegado,p_id_area_conocimiento,p_numero_sala,p_nombre_sala)=>{
      try {
        await updateSala(idSala,p_id_delegado,p_id_area_conocimiento,p_numero_sala,p_nombre_sala);
        
        // ALERTA PARA LA ACTUALIZACION DE SALA EXITOSA
        showSuccessToast("La sala se ha actualizado con exito");
      } catch (error) {
        // ALERTA SI FALLA LA ACTUALIZACION DE SALA
        showErrorToast("La sala no se ha podido actualizar, intenta de nuevo más tarde...");
      }
    }

    // Funcion para editar o crear la sala seleccionada una vez se envie el formulario
    const AddOrEdit = () => {
      if (props.infoEditar.p_idSala != null) {
        actualizarSala(idSala.value, idDelegado.value, idAreaConocimiento.value, num_sala.value, nombre_sala.value );
      } else {
        crearSala(idDelegado.value, idAreaConocimiento.value, num_sala.value, nombre_sala.value );
      }
    }

    return {
      arrayAreasConocimiento,
      arrayDelegados,
      idAreaConocimiento,
      idDelegado,
      idSala,
      closeModal,
      num_sala,
      AddOrEdit,
      nombre_sala,
      mostrarAlerta
    };
  },
};
</script>
<style scoped>
.modalCabecero {
  display: block;
}

.modal-title {
  font-size: 1.5rem;
  color: #333;
}

label {
  font-size: 1.2rem;
  color: #444;
  display: inline-block;
  white-space: nowrap;
}

.form-select {
  font-size: 1rem;
}

.form-select:focus {
  box-shadow: 0 0 5px yellow;
  border: 1px solid yellow;
}

.btn-guardar {
  font-size: 1rem;
  padding: 0.3rem 1.5rem;
}

.button {
  font-size: 1rem;
  padding: 0.3rem 1.5rem;
}

input {
  font-size: 1rem;
}
</style>
