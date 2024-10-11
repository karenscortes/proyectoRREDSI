<template>
  <div class="form-group">
      <select class="form-control" id="institucionesSelect" v-model="selectedInstitucion" @change="updateInstitucion">
          <option v-for="institucion in instituciones" :key="institucion.id_institucion" :value="institucion.id_institucion">
              {{ institucion.nombre }}
          </option>
      </select>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import { getAllInstituciones } from '@/services/institucionesService';  // Asegúrate de tener el servicio configurado para obtener las instituciones

export default {
  props: {
      selectedInstitucion: {
          type: Number,
          default: null,
      },
  },
  setup(props, { emit }) {
      const instituciones = ref([]);
      const selectedInstitucion = ref(props.selectedInstitucion);

      // Obtener instituciones de la API
      const fetchInstituciones = async () => {
          try {
              const response = await getAllInstituciones(); // Cambia esto según cómo esté configurada tu API
              instituciones.value = response.data;
          } catch (error) {
              console.error('Error al obtener las instituciones:', error);
          }
      };

      // Emitir el evento institucion-selected cuando cambie selectedInstitucion
      const updateInstitucion = () => {
          emit('institucion-selected', selectedInstitucion.value);
      };

      // Obtener instituciones cuando el componente se monta
      onMounted(fetchInstituciones);

      // Usar watch para observar cambios en props.selectedInstitucion
      watch(
          () => props.selectedInstitucion,
          (newInstitucion) => {
              selectedInstitucion.value = newInstitucion;
          },
          { immediate: true }
      );

      return {
          instituciones,
          selectedInstitucion,
          updateInstitucion,
      };
  },
};
</script>

<style scoped>
/* Estilos opcionales */
</style>
