import api from './api'; 

// Función para obtener proyectos sin asignar
export const proyectosSinAsignar = async (page = 1, pageSize = 2) => {
    try {
        const response = await api.get(`/proyectosSinAsignar/get-all-unassiggned-Projects/?page=${page}&page_size=${pageSize}`, {
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

// Función para obtener autores de un proyecto
export const obtenerAutoresProyecto = async (id_proyecto) => {
    try {
        const response = await api.get(`/proyectosSinAsignar/get-all-authors?id_proyecto=${id_proyecto}`, {
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