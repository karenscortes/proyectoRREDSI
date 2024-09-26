<template>
    <div class="form-group">
      <select class="form-control" id="modalidadSelect" v-model="selectedModalidad" @change="updateModalidad">
        <!-- Mostrar el nombre, pero el value es el ID -->
        <option v-for="modalidad in modalidades" :key="modalidad.id_modalidad" :value="modalidad.id_modalidad">
          {{ modalidad.nombre }}
        </option>
      </select>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { getAllModalidades } from '@/services/modalidadService';
  
  export default {
    props: {
      modelValue: {
        type: Number, // Usamos Number porque el ID es un número
        default: null,
      },
    },
    setup(props, { emit }) {
      const modalidades = ref([]);
      const selectedModalidad = ref(props.modelValue);
  
      // Obtener modalidades de la API
      const fetchModalidades = async () => {
        try {
          const response = await getAllModalidades();
          modalidades.value = response.data; // Cargar las modalidades
        } catch (error) {
          console.error('Error al obtener las modalidades:', error);
        }
      };
  
      // Emitir el ID de la modalidad cuando cambia la selección
      const updateModalidad = () => {
        emit('update:modelValue', selectedModalidad.value); // Emitir el ID seleccionado
      };
  
      // Cargar las modalidades cuando se monta el componente
      onMounted(fetchModalidades);
  
      return {
        modalidades,
        selectedModalidad,
        updateModalidad,
      };
    },
  };
  </script>
  
  <style scoped>
  /* Puedes agregar estilos aquí */
  </style>
  