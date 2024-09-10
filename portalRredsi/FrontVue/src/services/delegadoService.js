import api from './api'; 

// Proyectos sin asignar
export const proyectosSinAsignar = async () => {
    try {
        const response = await api.get('/proyectosSinAsignar/get-all-unassiggned-Projects/', {
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

//Asistencia
export const asistenciaEvento = async (page= 1, page_size = 10,) => {
    try {
        const response = await api.get(`asistencia/get-all-asistentes/?page=${page}&page_size=${page_size}`, {
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

