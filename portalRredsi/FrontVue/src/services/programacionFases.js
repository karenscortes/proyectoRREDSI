import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getEvents = async () => {
  try {
    const response = await api.get('/fases/get-phase-dates/');
    return response.data; // Devolver solo los datos de la respuesta
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
