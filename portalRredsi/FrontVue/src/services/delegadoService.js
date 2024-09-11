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

// Asistentes por sala
export const obtenerAsistentesPorSala = async (numero_sala, page = 1, page_size = 10) => {
    try {
        const response = await api.get(`asistencia/get-asistentes-por-sala/${numero_sala}?page=${page}&page_size=${page_size}`, {
            headers: {
                'Authorization': `Bearer` // Incluye el token si es necesario
            }
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};


// Asistentes por rol (participantes, evaluadores)
export const obtenerAsistentesPorRol = async (rol, page = 1, page_size = 10) => {
    try {
        const response = await api.get(`asistencia/get-asistentes-por-rol/${rol}?page=${page}&page_size=${page_size}`, {
            headers: {
                'Authorization': `Bearer`
            }
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

//Asistentes por documento
export const obtenerAsistentePorDocumento = async (documento) => {
    try {
        const response = await api.get(`asistencia/get-asistente-por-cedula/${documento}`, {
            headers: {
                'Authorization': `Bearer`
            }
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

//Actualizar asistencia (check)
export const actualizarAsistencia = async (documento, asistencia) => {
    try {
        const response = await api.patch(`asistencia/update-asistencia/${documento}`, { asistencia }, {
            headers: {
                'Authorization': `Bearer`
            }
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};




