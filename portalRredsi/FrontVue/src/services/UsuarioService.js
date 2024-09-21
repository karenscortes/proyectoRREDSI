import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

// Servicio para obtener un usuario por su ID (incluyendo token para autenticación)
export const getUserById = async (userId) => {
    try {
        // Obtenemos el token desde el localStorage
        const token = localStorage.getItem('token');

        if (!token) {
            throw new Error('Token de autenticación no encontrado. Inicia sesión nuevamente.');
        }

        const response = await fetch(`/users/get-user/${userId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}` // Enviamos el token en la cabecera
            }
        });

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error('Usuario no encontrado');
            } else {
                throw new Error('Error al obtener el usuario');
            }
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al obtener el usuario:', error);
        throw new Error('Error de red o de servidor');
    }
};


// Nueva función para actualizar el perfil 
export const updateUserProfile = async (userId, userData) => {
    try {
        const response = await api.put('/users/update/', {
            user_id: userId,
            userData // Aquí se desglosan los datos del perfil que se quieren actualizar
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