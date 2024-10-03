<template>
  <div class="rubrica-container container">
    <!-- Verifica si hay una rúbrica seleccionada -->
    <div v-if="rubricaSeleccionada">
      <!-- Pasamos los datos al componente de detalle -->
      <rubrica-detalle :rubrica="rubricaSeleccionada" @volver="volverBusqueda" />
    </div>

    <!-- Si no hay rúbrica seleccionada, muestra la búsqueda -->
    <div v-else class="buscar-rubricas">
      <h2 class="text-center">Buscar Rúbricas Calificadas</h2>

      <!-- Mostrar mensaje de error si existe -->
      <div v-if="error" class="alert alert-danger">
        {{ error }}
      </div>

      <!-- Input para el ID del tutor y proyecto -->
      <div class="row justify-content-center mb-4">
        <div class="col-md-6">
          <label for="id_tutor" class="form-label">ID Tutor:</label>
          <input v-model="id_tutor" class="form-control" placeholder="Ingresa el ID del tutor" />
        </div>
      </div>

      <div class="row justify-content-center mb-4">
        <div class="col-md-6">
          <label for="id_proyecto" class="form-label">ID Proyecto:</label>
          <input v-model="id_proyecto" class="form-control" placeholder="Ingresa el ID del proyecto" />
        </div>
      </div>

      <div class="text-center">
        <button class="btn btn-dark" @click="buscarRubricas">Buscar</button>
      </div>

      <!-- Lista de rúbricas calificadas -->
      <div v-if="rubricas.length > 0" class="mt-5">
        <h3 class="text-center">Rúbricas Calificadas:</h3>
        <ul class="list-group">
          <li class="list-group-item d-flex justify-content-between align-items-center" v-for="rubrica in rubricas" :key="rubrica.id_rubrica">
            {{ rubrica.titulo_rubrica }}
            <button class="btn btn-outline-primary" @click="verDetalleRubrica(rubrica)">Visualizar</button>
          </li>
        </ul>
      </div>

      <!-- Mensaje cuando no se encuentran rúbricas -->
      <div v-else-if="!loading" class="mt-5 text-center">
        <p>No se encontraron rúbricas calificadas</p>
      </div>

      <!-- Mensaje de carga -->
      <div v-if="loading" class="mt-5 text-center">
        <p>Cargando rúbricas...</p>
      </div>
    </div>
  </div>
</template>

<script>
import { obtenerRubricasCalificadas } from '@/services/rubricasCalificadas';
import RubricaDetalle from './Rubricas_detalle.vue';

export default {
  components: {
    RubricaDetalle,
  },
  data() {
    return {
      id_tutor: '',
      id_proyecto: '',
      rubricas: [],
      rubricaSeleccionada: null,
      titulo_proyecto: null,
      ponentes: null,
      universidad_proyecto: null,
      error: null,
      loading: false,
    };
  },
  methods: {
    async buscarRubricas() {
      this.error = null;
      this.loading = true;
      if (!this.id_tutor && !this.id_proyecto) {
        this.error = 'Por favor ingresa un ID de tutor o un ID de proyecto.';
        this.loading = false;
        return;
      }

      try {
        const response = await obtenerRubricasCalificadas(this.id_tutor, this.id_proyecto);
        
        console.log('Datos recibidos:', response); // Verificar los datos recibidos

        this.rubricas = response.rubricas_calificadas;
        this.titulo_proyecto = response.titulo_proyecto;
        this.ponentes = response.ponentes;
        this.universidad_proyecto = response.universidad_proyecto;
      } catch (error) {
        console.error('Error al buscar las rúbricas:', error);
        this.error = error.message || 'Error desconocido al buscar las rúbricas.';
      } finally {
        this.loading = false;
      }
    },
    verDetalleRubrica(rubrica) {
      console.log('Detalles de la rúbrica seleccionada:', rubrica);
      
      // Combina los datos generales del proyecto con la rúbrica seleccionada
      this.rubricaSeleccionada = {
        ...rubrica,
        titulo_proyecto: this.titulo_proyecto,
        ponentes: this.ponentes,
        universidad_proyecto: this.universidad_proyecto
      };
    },
    volverBusqueda() {
      this.rubricaSeleccionada = null;
    }
  }
};
</script>

<style scoped>
.rubrica-container {
  margin-top: 90px;
  padding-top: 90px;
}

.buscar-rubricas {
  background-color: #f4f4f4;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #333333;
}

.btn-primary {
  background-color: #888585;
  border-color: #000000;
}

.btn-outline-primary {
  border-color: #000000;
  color: #292828;
}
</style>
