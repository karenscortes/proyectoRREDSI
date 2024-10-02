import api from './api';  // Asegúrate de tener configurada tu instancia Axios

// Función para obtener las rúbricas calificadas
export const obtenerRubricasCalificadas = async (id_tutor, id_proyecto) => {
  try {
    const params = {};
    if (id_tutor) params.id_tutor = id_tutor;
    if (id_proyecto) params.id_proyecto = id_proyecto;

    const response = await api.get('/proyectosConvocatorias/proyectosConvocatorias/rubricas-calificadas', { params });
    
    console.log('Datos recibidos:', response.data);  // Asegúrate de que la API devuelve los datos correctos
    return response.data;  // Este debería ser el objeto con los datos del proyecto y las rúbricas
  } catch (error) {
    if (error.response) {
      throw error.response.data || error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
