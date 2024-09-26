<template>
  <div class="form-group">
    <label for="tipoDocumentoSelect">Seleccione un tipo de documento</label>
    <select class="form-control" id="tipoDocumentoSelect" v-model="selectedTipoDocumento" @change="updateTipoDocumento">
      <option v-for="tipo in tiposDocumento" :key="tipo.id_tipo_documento" :value="tipo.nombre">
        {{ tipo.nombre }}
      </option>
    </select>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import { getAllTiposDocumento } from '@/services/tipoDocumentoService';

export default {
  props: {
    modelValue: {
      type: String,
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
        tiposDocumento.value = response.data;
        console.log('Tipos de documento cargados:', tiposDocumento.value); // Depuración: Verifica si los tipos de documento están cargando
      } catch (error) {
        console.error('Error al obtener los tipos de documento:', error);
      }
    };

    // Emitir el evento cuando cambie el tipo de documento
    const updateTipoDocumento = () => {
      emit('update:modelValue', selectedTipoDocumento.value);
    };

    // Obtener tipos de documento cuando el componente se monta
    onMounted(fetchTiposDocumento);

    // Usar watch para observar cambios en props.modelValue
    watch(
      () => props.modelValue,
      (newTipo) => {
        selectedTipoDocumento.value = newTipo;
      },
      { immediate: true }
    );

    return {
      tiposDocumento,
      selectedTipoDocumento,
      updateTipoDocumento,
    };
  },
};
</script>

<style scoped>
/* Estilos opcionales */
</style>
