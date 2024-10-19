<template>
  <tr class="text-center">
    <td>{{ infoDelegado.nombres}} {{ infoDelegado.apellidos }}</td>
    <td>{{ infoDelegado.nombre_institucion }}</td>
    <td>
      <div class="form-check form-switch">
        <!-- Mostrar el spinner cuando el cambio de estado está en proceso -->
        <SpinnerGlobal v-if="loading" />
        
        <input
          v-else
          class="form-check-input td_check"
          :checked="infoDelegado.estado == 'activo'"
          @change="cambiarEstado()"
          type="checkbox"
          id="estado"
        />
      </div>
    </td>
    <td class="text-center">
      <a
        href="#"
        class="btn-sm font-weight-bold text-dark"
        type="button"
        @click="openModal()"
      >
        <i class="far fa-address-card h4"></i>
      </a>
    </td>
  </tr>
</template>

<script setup>
import { ref } from 'vue';
import SpinnerGlobal from '../../../UI/SpinnerGlobal.vue';

const props = defineProps({
  infoDelegado: {
    type: Object,
    required: true,
    validator(value) {
      return (
        typeof value.id_usuario === 'number' &&
        typeof value.nombres === 'string' &&
        typeof value.apellidos === 'string' &&
        typeof value.tipo_documento === 'string' &&
        typeof value.documento === 'string' &&
        typeof value.nombre_institucion === 'string' &&
        typeof value.primer_area === 'string' &&
        typeof value.segunda_area === 'string' &&
        typeof value.url_titulo === 'string' &&
        typeof value.estado  === 'string' &&
        typeof value.celular === 'string' &&
        typeof value.correo === 'string' 
      );
    },
  },
  index: {
    type: Number,
    required: true
  }
})

// Definir el estado de carga
const loading = ref(false);

// Definiendo los eventos que emitirán al componente padre. 
const emit = defineEmits(["open", "check"]);

const openModal = () => emit("open", props.infoDelegado);

const cambiarEstado = async () => {
  loading.value = true; // Activar el spinner
  try {
    // Emitir el evento 'check' para cambiar el estado del delegado
    await emit("check", props.index);
  } catch (error) {
    console.error("Error al cambiar el estado del delegado", error);
  } finally {
    loading.value = false; // Desactivar el spinner
  }
};
</script>

<style>
.form-check {
  padding-left: 2.5rem;
}
.form-check-input {
  border: 1px solid rgb(187, 187, 187);
}
.form-check-input:focus {
  border: 1px solid rgb(187, 187, 187);
}
</style>
