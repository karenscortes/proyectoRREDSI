import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getAllModalidades = async () => {
  try {
    const response = await api.get('/modalidades/get-all-modalidades/');
    console.log('Modalidades obtenidas:', response.data); // Depuración: Imprime los datos obtenidos
    return response;
  } catch (error) {
    console.error('Error al obtener las modalidades:', error); // Depuración: Captura cualquier error
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
