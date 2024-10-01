import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

// Servicio para obtener las rúbricas calificadas por id_tutor o id_proyecto
export const obtenerRubricasCalificadas = async (id_tutor = null, id_proyecto = null) => {
  try {
    // Construimos la URL para la API
    let url = '/proyectosConvocatorias/proyectosConvocatorias/rubricas-calificadas/?';
    
    if (id_tutor) url += `id_tutor=${id_tutor}`;
    if (id_proyecto) url += `${id_tutor ? '&' : ''}id_proyecto=${id_proyecto}`;

    // Realizamos la petición GET a la API
    const response = await api.get(url);

    return response; // Devolvemos la respuesta completa
  } catch (error) {
    if (error.response) {
      // Si hay un error en la respuesta, lo devolvemos
      throw error.response;
    } else {
      // En caso de error de red o servidor
      throw new Error('Error de red o de servidor');
    }
  }
};
