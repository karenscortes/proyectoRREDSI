import api from './api';  // Asegúrate de tener configurada tu instancia Axios

// Función para obtener las rúbricas calificadas por proyecto
export const obtenerRubricasCalificadas = async (id_proyecto) => {
  try {
    const params = { id_proyecto };  // Asegúrate de que el parámetro se está pasando correctamente

    // Verificar la ruta correcta de la API
    const response = await api.get('/proyectosConvocatorias/proyectosConvocatorias/rubricas-calificadas', { params });
    
    console.log('Datos recibidos en el servicio:', response.data);  // Verificar los datos que devuelve la API
    return response.data;  // Devolver los datos completos de la API
  } catch (error) {
    console.error('Error en el servicio:', error);  // Captura el error en la consola
    if (error.response) {
      throw error.response.data || error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
