<template>
  <div class="container mt-5 pt-5">
    <h1 class="mb-4">Consulta tus Rúbricas Calificadas</h1>

    <!-- Buscador bonito con margin-top 5 y padding-top 5 -->
    <div class="search-container mb-4">
      <input v-model="searchTerm" class="form-control mb-2" placeholder="Ingresa ID Tutor o ID Proyecto" />
      <button class="btn btn-primary" @click="buscarRubricas">Buscar</button>
    </div>

    <!-- Muestra varias rúbricas -->
    <div v-if="proyectos.length > 0">
      <!-- Recorremos los proyectos obtenidos -->
      <div v-for="(proyecto, index) in proyectos" :key="index" class="rubrica mb-4 p-3 shadow-sm rounded border">
        <!-- Información del proyecto -->
        <div class="row mb-3">
          <div class="col-md-4">
            <label for="titulo"><strong>Título:</strong></label>
            <input type="text" class="form-control" v-model="proyecto.titulo_proyecto" readonly />
          </div>
          <div class="col-md-4">
            <label for="ponentes"><strong>Ponente(s):</strong></label>
            <input type="text" class="form-control" v-model="proyecto.ponentes" readonly />
          </div>
          <div class="col-md-4">
            <label for="universidad"><strong>Universidad:</strong></label>
            <input type="text" class="form-control" v-model="proyecto.universidad_proyecto" readonly />
          </div>
        </div>

        <!-- Ciclo para mostrar todas las rúbricas calificadas de cada proyecto -->
        <div v-for="(rubrica, idx) in proyecto.rubricas_calificadas" :key="idx" class="rubrica-calificada mt-3">
          <h5 class="mt-3"><strong>Etapa:</strong> {{ rubrica.etapa.nombre_etapa }}</h5>

          <!-- Tabla de rúbrica con ítems calificados -->
          <table class="table table-bordered mt-3">
            <thead class="thead-light">
              <tr>
                <th>Componentes</th>
                <th>Max Valor</th>
                <th>Calificación</th>
                <th>Observaciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in rubrica.items_rubrica" :key="item.id_item_rubrica">
                <td>{{ item.titulo_item }}</td>
                <td>{{ item.valor_max }}</td>
                <td>{{ item.calificacion }}</td>
                <td>{{ item.observacion }}</td>
              </tr>
            </tbody>
          </table>

          <!-- Información del evaluador -->
          <div class="mt-3">
            <p><strong>Nombre del Evaluador:</strong> {{ rubrica.evaluador.nombre_evaluador }}</p>
            <p><strong>Cédula:</strong> {{ rubrica.evaluador.cedula_evaluador }}</p>
            <p><strong>Universidad:</strong> {{ rubrica.evaluador.universidad_evaluador }}</p>
            <p><strong>Email:</strong> {{ rubrica.evaluador.email_evaluador }}</p>
            <p><strong>Celular:</strong> {{ rubrica.evaluador.celular_evaluador }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Si no se encuentran proyectos -->
    <p v-else>No se encontraron rúbricas calificadas.</p>
  </div>
</template>

<script>
import { obtenerRubricasCalificadas } from '@/services/rubricasCalificadas';

export default {
  data() {
    return {
      searchTerm: '', // Término de búsqueda
      proyectos: [], // Lista de proyectos obtenidos
    };
  },
  methods: {
    async buscarRubricas() {
      try {
        const idNumber = Number(this.searchTerm); // Convertimos el ID a número
        const response = await obtenerRubricasCalificadas(idNumber, idNumber); // Llamamos al servicio de API
        
        console.log("Respuesta de la API:", response.data); // Para verificar lo que devuelve la API
        
        // Asignar la respuesta a proyectos
        if (response.data) {
          this.proyectos = [response.data]; // Guardamos los proyectos en la lista
        } else {
          this.proyectos = [];
          alert("No se encontraron rúbricas calificadas.");
        }
      } catch (error) {
        console.error('Error al obtener las rúbricas:', error);
        alert('Hubo un error al intentar obtener las rúbricas.');
      }
    },
  },
};
</script>

<style scoped>
/* Mejora del diseño general */
.search-container {
  display: flex;
  align-items: center;
}

.search-container input {
  padding: 10px;
  font-size: 16px;
  width: 300px;
  margin-right: 10px;
  border-radius: 5px;
}

.search-container button {
  padding: 10px 20px;
  font-size: 16px;
}

/* Estilo del contenedor de rúbricas */
.rubrica {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Tabla de componentes */
table {
  width: 100%;
  border-collapse: collapse;
}

thead th {
  background-color: #f8f9fa;
}
</style>
