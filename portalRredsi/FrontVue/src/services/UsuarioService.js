import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente





// Nueva función para actualizar el perfil 
export const updateUserProfile = async (userId, userData) => {
    try {
        const response = await api.put('/users/update/', {
            user_id: userId,
            ...userData // Aquí se desglosan los datos del perfil que se quieren actualizar
        });
        return response.data; // Retorna el mensaje de éxito
    } catch (error) {
        if (error.response) {
            // Manejar el error que proviene del servidor
            throw error.response.data;
        } else {
            // Manejar errores de red u otros errores no relacionados con la API
            throw new Error('Error de red o de servidor');
        }
    }
};