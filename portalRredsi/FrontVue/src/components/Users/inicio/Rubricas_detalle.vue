<template>
  <div v-if="rubrica" class="rubrica-detalle-container">
    <h2 class="text-center mb-4">{{ rubrica.titulo_rubrica }}</h2>
  
    <!-- Información del proyecto -->
    <div class="info mb-4">
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>Título del Proyecto:</th>
            <td>{{ rubrica.titulo_proyecto || 'No disponible' }}</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th>Ponente(s):</th>
            <td>{{ rubrica.ponentes || 'No disponible' }}</td>
          </tr>
          <tr>
            <th>Universidad:</th>
            <td>{{ rubrica.universidad_proyecto || 'No disponible' }}</td>
          </tr>
          <tr>
            <th>Estado del Proyecto:</th>
            <td>{{ rubrica.estado_proyecto || 'No disponible' }}</td>
          </tr>
          <tr>
            <th>Puntaje:</th>
            <td>{{ rubrica.puntaje_aprobacion || 'No disponible' }}</td>
          </tr>
        </tbody>
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

h2 {
  color: #333333;
}

.btn-secondary {
  background-color: #ffc107; /* Color del botón "Volver" */
  border-color: #000000;
  color: #000000;
}
</style>
