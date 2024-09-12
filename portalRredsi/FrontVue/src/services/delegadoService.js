import api from './api'; 

// Función para obtener proyectos sin asignar
export const proyectosSinAsignar = async (page = 1, pageSize = 10) => {
    try {
        const response = await api.get(`/proyectosSinAsignar/get-all-unassiggned-Projects/?page=${page}&page_size=${pageSize}`, {
            headers: {
                'Authorization': `Bearer` // Incluye el token de autenticación
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
            throw error;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

// Función para obtener Posibles evaluadores para un proyecto
export const obtenerPosiblesEvaluadores = async (id_area_conocimiento,id_institucion) => {
    try {
        const response = await api.get(`/asignarProyectoEtapaVirtual/get-posibles-evaluadores/?area_conocimiento=${id_area_conocimiento}&id_institucion=${id_institucion}`, {
            headers: {
                'Authorization': `Bearer` // Incluye el token de autenticación
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

// Función para obtener la lista de evaluadores para un proyectos en caso de que no hayan recomendados
export const obtenerListaEvaluadores = async () => {
    try {
        const response = await api.get(`/listaEvaluadores/get-all-evaluators/`, {
            headers: {
                'Authorization': `Bearer` // Incluye el token de autenticación
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

// Función para obtener id de area de conocimiento
export const obtenerIdAreaConocimiento = async (area_conocimiento) => {
    try {
        const response = await api.get(`/asignarProyectoEtapaVirtual/get-id-area-conocimiento/?nombre_area=${area_conocimiento}`, {
            headers: {
                'Authorization': `Bearer` // Incluye el token de autenticación
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

// Función para obtener id de institucion
export const obtenerIdInstitucion = async (institucion) => {
    try {
        const response = await api.get(`/asignarProyectoEtapaVirtual/get-id-institucion/?nombre_institucion=${institucion}`, {
            headers: {
                'Authorization': `Bearer` // Incluye el token de autenticación
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

//Asistencia
export const asistenciaEvento = async (page= 1, page_size = 10) => {
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

//Numeros de sala
export const obtenerSalasPorConvocatoria = async (page = 1, page_size = 10) => {
    try {
        const response = await api.get(`/get-salas-por-convocatoria/?page=${page}&page_size=${page_size}`, {
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
export const actualizarAsistencia = async (id_asistencia, id_usuario, asistencia) => {
    try {
        const response = await api.put(`/update-asistencia/`, {
            id_asistente: id_asistencia,
            id_usuario: id_usuario,
            asistencia: asistencia
        }, {
            headers: {
                'Authorization': `Bearer YOUR_TOKEN_HERE`
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






