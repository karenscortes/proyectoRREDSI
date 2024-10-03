<template>
    <div class="event_items container"> <!-- Aumentar el padding top para evitar interferencia con el menú -->
      <!-- Mostrar mensaje de carga -->
      <div v-if="loading" class="text-center my-3">Cargando eventos...</div>
  
      <!-- Mostrar mensaje de error -->
      <div v-if="error" class="text-danger text-center my-3">{{ error }}</div>
  
      <!-- Renderizar eventos cuando estén disponibles -->
      <div v-if="events.length > 0">
        <div class="row event_item" v-for="(event, index) in orderedEventsByDate" :key="index">
          <div class="col">
            <div class="row d-flex flex-row align-items-center justify-content-between">
              <!-- Fecha de inicio en el cuadro con borde naranja -->
              <div class="col-lg-2 order-lg-1 order-2">
                <div class="event_date d-flex flex-column align-items-center justify-content-center">
                  <div class="event_day">{{ getDay(event.fecha_inicio) }}</div>
                  <div class="event_month">{{ getMonth(event.fecha_inicio) }}</div>
                </div>
              </div>
  
              <!-- Detalles del evento -->
              <div class="col-lg-6 order-lg-2 order-3">
                <div class="event_content">
                  <div class="event_name">
                    <a class="trans_200" href="#">
                      <!-- Cambiar Ponencias a Evento presencial -->
                      {{ event.nombre_fase === 'Ponencias' ? 'Evento presencial' : event.nombre_fase }}
                    </a>
                  </div>
                  <div class="event_location">{{ event.nombre_etapa }}</div>
                  <p>Evento programado desde {{ event.fecha_inicio }} hasta {{ event.fecha_fin }}.</p>
                </div>
              </div>
  
              <!-- Imagen del evento -->
              <div class="col-lg-4 order-lg-3 order-1">
                <div class="event_image">
                  <img :src="getImageForEvent(event.nombre_fase, event.nombre_etapa, index)" alt="Imagen del evento" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { getEvents } from '@/services/programacionFases';
  
  export default {
    data() {
      return {
        events: [],
        loading: true,
        error: null,
      };
    },
    computed: {
      orderedEventsByDate() {
        // Ordenar los eventos por fecha de inicio (ascendente)
        return this.events.sort((a, b) => {
          return new Date(a.fecha_inicio) - new Date(b.fecha_inicio);
        });
      },
    },
    methods: {
      getDay(date) {
        const correctedDate = new Date(date);
        correctedDate.setMinutes(correctedDate.getMinutes() + correctedDate.getTimezoneOffset());
        return correctedDate.getUTCDate();
      },
      getMonth(date) {
        const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
        const correctedDate = new Date(date);
        correctedDate.setMinutes(correctedDate.getMinutes() + correctedDate.getTimezoneOffset());
        return months[correctedDate.getUTCMonth()];
      },
      getImageForEvent(nombre_fase, nombre_etapa, index) {
        // Ciclo de imágenes para que no se repitan y usar una imagen distinta para la segunda sección
        const images = [
          new URL('@/assets/img/event_1.jpg', import.meta.url).href,
          new URL('@/assets/img/event_2.jpg', import.meta.url).href,
          new URL('@/assets/img/event_3.jpg', import.meta.url).href,
        ];
  
        // Para la segunda sección (índice 1) se asegura una imagen diferente
        if (index === 1) {
          return images[1]; // Imagen para la segunda sección
        }
  
        // Retornar la imagen basada en el índice del evento para evitar que se repitan
        return images[index % images.length];
      },
    },
    async created() {
      try {
        this.events = await getEvents();
      } catch (error) {
        this.error = 'Error al cargar los eventos';
      } finally {
        this.loading = false;
      }
    },
  };
  </script>
  
  <style scoped>
  
  .event_item {
    margin-bottom: 30px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    padding: 15px;
    border-radius: 8px;
  }
  
  .event_date {
    color: #ffa500; /* Naranja */
    border: 2px solid #ffa500; /* Borde naranja */
    font-weight: bold;
    padding: 10px;
    border-radius: 8px;
    text-align: center;
    font-size: 24px;
    width: 100px;
    height: 100px;
    margin: 0 auto; /* Centrar el cuadro */
    margin-bottom: 10px;
  }
  
  .event_day {
    font-size: 36px;
    font-weight: bold;
  }
  
  .event_month {
    font-size: 18px;
  }
  
  .event_content {
    padding: 10px 0;
  }
  
  .event_image img {
    width: 100%;
    height: auto;
    border-radius: 8px;
  }
  
  .event_name {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .event_location {
    color: gray;
    font-size: 16px;
  }
  </style>
  