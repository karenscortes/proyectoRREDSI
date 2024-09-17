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

// Función para modificar el rol de un usuario
export const updateUserRole = async (userId, newRoleId) => {
    try {
        const response = await api.put('/superadmin/update-role/', {
            user_id: userId,
            new_role_id: newRoleId
        });
        return response.data; // Retorna el resultado del servidor (booleano)
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

// Funcion para obtener el historial de actividades por administrador
export const getActivityHistoryByAdmin = async (userId) => {
    try {
            const response = await api.get(`/superadmin/get-activity-history/${userId}/`);
            return response.data; // Retorna el historial de actividades
    } catch (error) {
        if (error.response) {

            throw error.response.data;
        } else {
            throw new Error('Error de red o de servidor');
        }       
    }
};        