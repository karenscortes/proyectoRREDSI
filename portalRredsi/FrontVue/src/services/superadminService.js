import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

// Función para obtener todos los admins con paginación
export const getAdminsByPage = async (page = 1, pageSize = 10) => {
    try {
        const response = await api.get(`/superadmin/get-all-admins/?page=${page}&page_size=${pageSize}`);
        return response.data;  // Acceder a los datos de la respuesta
    } catch (error) {
        if (error.response) {
            throw error.response.data;  // Devuelve el error original de la API
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};
