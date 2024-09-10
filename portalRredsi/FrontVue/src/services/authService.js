import api from './api'; 

// Función para manejar el inicio de sesión
export const login = async () => {
  try {
    const response = await api.get(`/proyectosSinAsignar/get-all-unassiggned-Projects/`, {
        headers: {
            'Authorization': `Bearer` // Incluye el token de autenticación
        }
    });
    return response;
} catch (error) {
    if (error.response) {
        throw error; // Lanza el error para que lo maneje el store
    } else {
        throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
}
};