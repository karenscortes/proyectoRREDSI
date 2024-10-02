import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getAllModalidades = async () => {
  try {
    const response = await api.get('/modalidades/get-all-modalidades/');
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
