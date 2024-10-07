<template>
  <div class="rubrica-container container">
    <!-- Verifica si hay una rúbrica seleccionada -->
    <div v-if="rubricaSeleccionada">
      <!-- Pasamos los datos al componente de detalle -->
      <rubrica-detalle :rubrica="rubricaSeleccionada" @volver="volverBusqueda" />
    </div>

    <!-- Si no hay rúbrica seleccionada, muestra la búsqueda -->
    <div v-else class="buscar-rubricas">
      <h2 class="text-center mb-4">Consultar Rúbricas Calificadas</h2>

      <!-- Mostrar mensaje de error si existe -->
      <div v-if="error" class="alert alert-danger">
        {{ error }}
      </div>

      <!-- Input para el ID del proyecto -->
      <div class="row justify-content-center mb-4">
        <div class="col-md-6">
          <label for="id_proyecto" class="form-label">ID Proyecto:</label>
          <input v-model="id_proyecto" class="form-control" placeholder="Ingresa el codigo del proyecto" />
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
            <div>
              <strong>{{ rubrica.titulo_rubrica }}</strong> <br/>
              <span>Estado: <strong>{{ rubrica.estado_proyecto }}</strong></span> <br/>
              <span>Puntaje de Aprobación: <strong>{{ rubrica.puntaje_aprobacion }}</strong></span>
            </div>
            <button class="btn btn-outline-secondary" @click="verDetalleRubrica(rubrica)">Visualizar</button>
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
import { useToastUtils } from '@/utils/toast'; // Importamos las alertas
import { obtenerRubricasCalificadas } from '@/services/rubricasCalificadas';
import RubricaDetalle from './Rubricas_detalle.vue';

export default {
  components: {
    RubricaDetalle,
  },
  data() {
    return {
      id_proyecto: '', // Solo se utiliza ID Proyecto
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
      // Reiniciar las variables antes de buscar nuevas rúbricas
      this.rubricas = [];
      this.rubricaSeleccionada = null;
      this.titulo_proyecto = null;
      this.ponentes = null;
      this.universidad_proyecto = null;
      this.error = null;

      const { showSuccessToast, showErrorToast } = useToastUtils(); // Obtenemos los métodos de las alertas

      // Comienza el proceso de búsqueda
      this.loading = true;

      if (!this.id_proyecto) {
        this.error = 'Por favor ingresa el codigo del proyecto.';
        this.loading = false;
        showErrorToast('Por favor ingresa el codigo del proyecto'); // Mostramos una alerta de error
        return;
      }

      try {
        const response = await obtenerRubricasCalificadas(this.id_proyecto);

        console.log('Datos recibidos:', response); // Verificar los datos recibidos

        if (response && response.rubricas_calificadas) {
          this.rubricas = response.rubricas_calificadas;
          this.titulo_proyecto = response.titulo_proyecto;
          this.ponentes = response.ponentes;
          this.universidad_proyecto = response.universidad_proyecto;
          showSuccessToast('Rúbricas encontradas con éxito'); // Mostramos alerta de éxito
        } else {
          this.error = 'No se encontraron rúbricas para el proyecto.';
          showErrorToast('No se encontraron rúbricas para el proyecto');
        }
      } catch (error) {
        console.error('Error al buscar las rúbricas:', error);
        this.error = error.message;
        showErrorToast('No existen rubricas con este codigo del proyecto');
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
  margin-top: 10px;
  padding-top: 10px;
}

.buscar-rubricas {
  background-color: #f4f4f4;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border: 1px solid #ccc; /* Borde del background */
}

h2, h3, label, span, strong {
  font-weight: bold; /* Negrita para los textos */
  color: #000000;
}

.btn-outline-secondary {
  border-color: #6c757d;
  color: #000000;
}

.btn-outline-secondary:hover {
  background-color: #6c757d;
  color: #000000;
}
</style>
