import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getAllAreasConocimiento = async () => {
  try {
    const response = await api.get('/areasConocimientos/get-all-areasConocimiento/');
    console.log('Áreas de conocimiento obtenidas:', response.data); // Depuración: Imprime los datos obtenidos
    return response;
  } catch (error) {
    console.error('Error al obtener las áreas de conocimiento:', error); // Depuración: Captura cualquier error
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
