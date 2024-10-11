<template>
  <div class="form-group">
      <select class="form-control" id="tipoDocumentoSelect" v-model="selectedTipoDocumento" @change="updateTipoDocumento">
          <option v-for="tipo in tiposDocumento" :key="tipo.id_tipo_documento" :value="tipo.id_tipo_documento">
              {{ tipo.nombre }}
          </option>
      </select>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import { getAllTiposDocumento } from '@/services/TipoDocumentoService';  // Supongo que esta es la ruta del servicio

export default {
    props: {
        selectedTipoDocumento: {
            type: Number,
            default: null,
        },
    },
    setup(props, { emit }) {
        const tiposDocumento = ref([]);
        const selectedTipoDocumento = ref(props.selectedTipoDocumento);

        // Obtener tipos de documento de la API
        const fetchTiposDocumento = async () => {
            try {
                const response = await getAllTiposDocumento();
                tiposDocumento.value = response.data;
            } catch (error) {
                console.error('Error al obtener los tipos de documento:', error);
            }
        };

        // Emitir el evento tipo-documento-selected cuando cambie selectedTipoDocumento
        const updateTipoDocumento = () => {
            emit('tipo-documento-selected', selectedTipoDocumento.value);
        };

        // Obtener tipos de documento cuando el componente se monta
        onMounted(fetchTiposDocumento);

        // Usar watch para observar cambios en props.selectedTipoDocumento
        watch(
            () => props.selectedTipoDocumento,
            (newTipoDocumento) => {
                selectedTipoDocumento.value = newTipoDocumento;
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

