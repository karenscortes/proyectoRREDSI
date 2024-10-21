<template>
  <div class="rubrica-container ">
    <!-- Verifica si hay una rúbrica seleccionada -->
    <div v-if="rubricaSeleccionada">
      <!-- Pasamos los datos al componente de detalle -->
      <rubrica-detalle
        :rubrica="rubricaSeleccionada"
        @volver="volverBusqueda"
      />
    </div>

    <!-- Si no hay rúbrica seleccionada, muestra la búsqueda -->
    <div v-else class="buscar-rubricas">
      <h2 class="text-center mb-4">Consultar evaluaciones</h2>

      <!-- Mostrar mensaje de error si existe -->
      <div v-if="error" class="alert alert-danger">
        {{ error }}
      </div>

      <!-- Input para el ID del proyecto -->
      <div class="row justify-content-center mb-4">
        <div class="col-md-5">
          <label for="id_proyecto" class="form-label"
            >Código del Proyecto:</label
          >
          <input
            v-model="id_proyecto"
            class="form-control"
            placeholder="Ingresa el código del proyecto"
          />
        </div>
        <div class="col-md-3 align-self-end">
          <button class="btn" @click="buscarRubricas">
            Buscar
          </button>
        </div>
      </div>

      <!-- Lista de rúbricas calificadas -->
      <div v-if="rubricas.length > 0" class="mt-5">
        <h3 class="text-center">Evaluaciones disponibles:</h3>
        <ul class="list-group">
          <li
            class="list-group-item d-flex justify-content-between align-items-center"
            v-for="rubrica in rubricas"
            :key="rubrica.id_rubrica"
          >
            <div>
              <span
                >Puntaje evaluación:
                <strong>{{ rubrica.puntaje_aprobacion }}</strong></span
              ><br />
              <span
                >Estado:
                <strong class="text-warning">{{
                  rubrica.estado_proyecto
                }}</strong></span
              >
              <br />
            </div>
            <button
              class="btn"
              @click="verDetalleRubrica(rubrica)"
            >
              Visualizar
            </button>
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
import { useToastUtils } from "@/utils/toast"; // Importamos las alertas
import { obtenerRubricasCalificadas } from "@/services/rubricasCalificadas";
import RubricaDetalle from "./Rubricas_detalle.vue";

export default {
  components: {
    RubricaDetalle,
  },
  data() {
    return {
      id_proyecto: "", // Solo se utiliza ID Proyecto
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
        this.error = "Por favor ingresa el codigo del proyecto.";
        this.loading = false;
        showErrorToast("Por favor ingresa el codigo del proyecto"); // Mostramos una alerta de error
        return;
      }

      try {
        const response = await obtenerRubricasCalificadas(this.id_proyecto);

        console.log("Datos recibidos:", response); // Verificar los datos recibidos

        if (response && response.rubricas_calificadas) {
          this.rubricas = response.rubricas_calificadas;
          this.titulo_proyecto = response.titulo_proyecto;
          this.ponentes = response.ponentes;
          this.universidad_proyecto = response.universidad_proyecto;
          showSuccessToast("Rúbricas encontradas con éxito"); // Mostramos alerta de éxito
        } else {
          this.error = "No se encontraron rúbricas para el proyecto.";
          showErrorToast("No se encontraron rúbricas para el proyecto");
        }
      } catch (error) {
        console.error("Error al buscar las rúbricas:", error);
        this.error = error.message;
        showErrorToast("No existen rubricas con este codigo del proyecto");
      } finally {
        this.loading = false;
      }
    },
    verDetalleRubrica(rubrica) {
      console.log("Detalles de la rúbrica seleccionada:", rubrica);

      // Combina los datos generales del proyecto con la rúbrica seleccionada
      this.rubricaSeleccionada = {
        ...rubrica,
        titulo_proyecto: this.titulo_proyecto,
        ponentes: this.ponentes,
        universidad_proyecto: this.universidad_proyecto,
      };
    },
    volverBusqueda() {
      this.rubricaSeleccionada = null;
    },
  },
};
</script>

<style scoped>
.rubrica-container {
  margin-top: 50px;
  border: none;
}

.buscar-rubricas {
  background-color: #ffffff;
  padding: 20px;
}

h2,
h3,
label,
span,
strong {
  font-weight: bold; /* Negrita para los textos */
  color: #000000;
}

.btn {
  color: rgb(255, 182, 6);
  color: #000000;
  font-size: medium;
}

.btn:hover:hover {
  background-color: rgb(0, 0, 0);
  color: white;
}

</style>
