<template>
    <div class="form-group">
      <select class="form-control" id="areaConocimientoSelect" v-model="selectedAreaConocimiento" @change="updateAreaConocimiento">
        <!-- Mostrar el nombre, pero el value es el ID -->
        <option v-for="area in areasConocimiento" :key="area.id_area_conocimiento" :value="area.id_area_conocimiento">
          {{ area.nombre }}
        </option>
      </select>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { getAllAreasConocimiento } from '@/services/areasConocimientoService';
  
  export default {
    props: {
      modelValue: {
        type: Number, // Usamos Number porque el ID es un número
        default: null,
      },
    },
    setup(props, { emit }) {
      const areasConocimiento = ref([]);
      const selectedAreaConocimiento = ref(props.modelValue);
  
      // Obtener áreas de conocimiento de la API
      const fetchAreasConocimiento = async () => {
        try {
          const response = await getAllAreasConocimiento();
          areasConocimiento.value = response.data; // Cargar las áreas de conocimiento
        } catch (error) {
          console.error('Error al obtener las áreas de conocimiento:', error);
        }
      };
  
      // Emitir el ID del área de conocimiento cuando cambia la selección
      const updateAreaConocimiento = () => {
        emit('update:modelValue', selectedAreaConocimiento.value); // Emitir el ID seleccionado
      };
  
      // Cargar las áreas de conocimiento cuando se monta el componente
      onMounted(fetchAreasConocimiento);
  
      return {
        areasConocimiento,
        selectedAreaConocimiento,
        updateAreaConocimiento,
      };
    },
  };
  </script>
  
  <style scoped>
  /* Puedes agregar estilos aquí */
  </style>
  