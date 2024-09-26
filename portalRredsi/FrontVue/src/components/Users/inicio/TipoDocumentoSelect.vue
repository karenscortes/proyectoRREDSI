<template>
  <div class="form-group">
    <select class="form-control" id="tipoDocumentoSelect" v-model="selectedTipoDocumento" @change="updateTipoDocumento">
      <!-- Mostrar el nombre, pero el value es el ID -->
      <option v-for="tipo in tiposDocumento" :key="tipo.id_tipo_documento" :value="tipo.id_tipo_documento">
        {{ tipo.nombre }}
      </option>
    </select>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getAllTiposDocumento } from '@/services/tipoDocumentoService';

export default {
  props: {
    modelValue: {
      type: Number, // Usamos Number porque el ID es un número
      default: null,
    },
  },
  setup(props, { emit }) {
    const tiposDocumento = ref([]);
    const selectedTipoDocumento = ref(props.modelValue);

    // Obtener tipos de documento de la API
    const fetchTiposDocumento = async () => {
      try {
        const response = await getAllTiposDocumento();
        tiposDocumento.value = response.data; // Cargar los tipos de documento
      } catch (error) {
        console.error('Error al obtener los tipos de documento:', error);
      }
    };

    // Emitir el ID del tipo de documento cuando cambia la selección
    const updateTipoDocumento = () => {
      emit('update:modelValue', selectedTipoDocumento.value); // Emitir el ID seleccionado
    };

    // Cargar los tipos de documento cuando se monta el componente
    onMounted(fetchTiposDocumento);

    return {
      tiposDocumento,
      selectedTipoDocumento,
      updateTipoDocumento,
    };
  },
};
</script>

<style scoped>
/* Puedes agregar estilos aquí */
</style>
