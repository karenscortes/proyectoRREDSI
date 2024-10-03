<template>
    <div v-if="rubrica" class="rubrica-detalle-container">
      <h2 class="text-center mb-4">{{ rubrica.titulo_rubrica }}</h2>
  
      <!-- Información del proyecto -->
      <div class="info mb-4">
        <table class="table table-bordered table-striped">
          <tr>
            <th>Título:</th>
            <td>{{ rubrica.titulo_proyecto || 'No disponible' }}</td>
          </tr>
          <tr>
            <th>Ponente(s):</th>
            <td>{{ rubrica.ponentes || 'No disponible' }}</td>
          </tr>
          <tr>
            <th>Universidad:</th>
            <td>{{ rubrica.universidad_proyecto || 'No disponible' }}</td>
          </tr>
        </table>
      </div>
  
      <!-- Tabla de componentes de la rúbrica -->
      <table class="table table-bordered mt-3">
        <thead class="custom-table-header">
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
      <div class="evaluador-info mt-4 p-3 rounded">
        <h5 class="evaluador-title mb-3">Información del Evaluador</h5>
        <p><strong>Nombre del Evaluador:</strong> {{ rubrica.evaluador.nombre_evaluador }}</p>
        <p><strong>Cédula:</strong> {{ rubrica.evaluador.cedula_evaluador }}</p>
        <p><strong>Universidad:</strong> {{ rubrica.evaluador.universidad_evaluador }}</p>
        <p><strong>Email:</strong> {{ rubrica.evaluador.email_evaluador }}</p>
        <p><strong>Celular:</strong> {{ rubrica.evaluador.celular_evaluador }}</p>
      </div>
  
      <div class="text-center mt-4">
        <button class="btn btn-secondary" @click="volver">Volver</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      rubrica: {
        type: Object,
        required: true,
      }
    },
    methods: {
      volver() {
        this.$emit('volver');
      }
    }
  }
  </script>
  
  <style scoped>
  .rubrica-detalle-container {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    margin: 20px;
  }
  
  .custom-table-header {
    background-color: #ffc107; /* Color de encabezado de tabla personalizado */
    color: #333333; /* Color del texto del encabezado */
  }
  
  .evaluador-info {
    background-color: #f0f0f0; /* Fondo más claro para la sección del evaluador */
    padding: 20px;
    border-radius: 8px;
  }
  
  .evaluador-title {
    color: #ffc107; /* Cambiar solo el color del título a naranja */
    font-weight: bold; /* Negrita solo en el título */
    font-size: 1.0rem; /* Aumentar solo el tamaño del título */
  }
  
  h2 {
    color: #333333;
  }
  
  h5 {
    color: #ff9800; /* Cambiar solo el color del subtítulo */
  }
  
  .btn-secondary {
    background-color: #ffc107; /* Color del botón "Volver" */
    border-color: #ffc107;
    color: #fff;
  }
  </style>
  