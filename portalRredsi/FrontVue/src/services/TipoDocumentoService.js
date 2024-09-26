import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getAllTiposDocumento = async () => {
  try {
    const response = await api.get('/tipo_identificacion/get-all-identificacion/');
    console.log('Tipos de documento obtenidos:', response.data); // Depuración: Imprime los datos obtenidos
    return response;
  } catch (error) {
    console.error('Error al obtener los tipos de documento:', error); // Depuración: Captura cualquier error
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
