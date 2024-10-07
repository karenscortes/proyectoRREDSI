import api from './api'; 

// Función para obtener cantidad de postulaciones de una convocatoria activa
export const obtenerCantidadPostulaciones = async () => {
    try {
        const response = await api.get(`/generales/get_cantidad_postulaciones/`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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

// Función para obtener cantidad de postulaciones de una convocatoria activa
export const obtenerCantidadProyectosAsignados = async () => {
    try {
        const response = await api.get(`/generales/get_cantidad_proyectos_asignados/`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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

// Función para obtener cantidad la url de una presentación de un proyecto
export const obtenerUrlPresentacionProyecto = async (id_proyecto) => {
    try {
        const response = await api.get(`/salas/get-presentacion-proyecto/?id_proyecto=${id_proyecto}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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

// Función para obtener proyectos sin asignar
export const proyectosSinAsignar = async (page = 1, pageSize = 10) => {
    try {
        const response = await api.get(`/proyectosSinAsignar/get-all-unassiggned-Projects/?page=${page}&page_size=${pageSize}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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

// Función para obtener proyecto convocatoria
export const obtenerProyectoConvocatoria = async (id_proyecto) => {
    try {
        const response = await api.get(`/asignarProyectoEtapaVirtual/obtener-proyecto-convocatoria/?id_proyecto=${id_proyecto}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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

// Función para asignar proyecto etapa virtual
export const asignarProyectoEtapaVirtual = async (datosAsignacion) => {
    try {
        const response = await api.post(`/asignarProyectoEtapaVirtual/asignar-proyecto-etapa-uno/`,datosAsignacion, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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

// Función para obtener id de un evaluador por su documento
export const obtenerIdEvaluador = async (documento) => {
    try {
        const response = await api.get(`/listaEvaluadores/get-evaluator-by-document/?documento=${documento}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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

// Función para obtener id de un evaluador por su documento
export const actualizarEstadoProyecto = async (id_proyecto) => {
    try {
        const response = await api.put(`/asignarProyectoEtapaVirtual/update-estado-proyecto/?id_proyecto=${id_proyecto}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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


export const obtenerConvocatoria = async () => {
    try {
        const response = await api.get('/asistencia/get-convocatoria-actual/', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        return response.data; 
    } catch (error) {
        if (error.response) {
            throw error.response.data; 
        } else {
            throw new Error('Error de red o de servidor'); 
        }
    }
};


//Asistencia
export const asistenciaEvento = async (page= 1, page_size = 10) => {
    try {
        const response = await api.get(`/asistencia/get-all-asistentes/?page=${page}&page_size=${page_size}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}` 
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
        const response = await api.get(`/asistencia/get-asistentes-por-sala/?numero_sala=${numero_sala}&page=${page}&page_size=${page_size}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}` 
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

// Salas por convocatoria en curso
export const obtenerSalas = async (page= 1, page_size=9) => {
    try {
        const response = await api.get(`/salas/get-salas-por-convocatoria/?page=${page}&page_size=${page_size}`,{
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}` 
            }  
        });
        return response;
    } catch (error) {
        if(error.response){
            throw error;
        }else {
            throw new Error('Error al obtener las salas');
        }
    }
};

// Asistentes por rol (participantes, evaluadores)
export const obtenerAsistentesPorRol = async (rol, page = 1, page_size = 10) => {
    try {
        const response = await api.get(`asistencia/get-asistentes-por-rol/${rol}?page=${page}&page_size=${page_size}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
export const actualizarAsistencia = async (id_asistente, id_usuario, asistencia) => {
    try {
        const response = await api.put(`/asistencia/update-asistencia/?id_asistente=${id_asistente}&id_usuario=${id_usuario}&asistencia=${asistencia}`, {
            id_asistente: id_asistente,
            id_usuario: id_usuario,
            asistencia: asistencia
        }, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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


// Todos los Proyectos 
export const obtenerListaProyectos = async (nombreEtapa, page = 1, pageSize = 10) => {
    try {
        const response = await api.get(`listaProyectos/obtener-proyectos-por-etapa-paginados/?nombre_etapa=${nombreEtapa}&page=${page}&page_size=${pageSize}`, {
            params: {
                nombre_etapa: nombreEtapa,
                page: page,
                page_size: pageSize
            }
        });
        return response.data;
    } catch (error) {
        if (error.response) {
            throw error; // Lanza el error para que lo maneje el store
        } else {
            throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
    }
};

//Filtros proyectos por estado (pendientes / calificados)
export const obtenerProyectosPorEstado = async (nombreEtapa, estado_calificacion, page = 1, pageSize = 10) => {
    try {
        const response = await api.get(`/listaProyectos/obtener-proyectos-por-estado/?nombre_etapa=${nombreEtapa}&estado_calificacion=${estado_calificacion}&page=${page}&page_size=${pageSize}`, {
            headers: {
            'Authorization': `Bearer` // Incluye el token de autenticación
            },
        params: {
            nombre_etapa: nombreEtapa,
            estado_calificacion: estado_calificacion,
            page: page,
            page_size: pageSize
        }
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error; 
        } else {
            throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
    }
};

//Función para obtener las fechas de las fases en las que se hacen las Asignaciones
export const obtenerFechasAsignaciones = async () => {
    try {
      const response = await api.get(`/proyectosSinAsignar/get-assignment-dates/`);
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; 
      } else {
        throw new Error('Error de red o de servidor'); 
      }
    }
};

//Función para obtener evaluadores de un proyecto por etapa
export const obtenerEvaluadoresProyecto = async (id_proyecto, id_etapa) => {
    try {
        const response = await api.get(`/detalleProyecto/participantes-etapa/?id_proyecto=${id_proyecto}&id_etapa=${id_etapa}`, {
            headers: {
                'Authorization': `Bearer` 
            },
            
        });
        return response.data; 
    } catch (error) {
        if (error.response) {  
            throw error;  
        } else {  
            throw new Error('Error de red o de servidor');
        }
    }
};

//Función para obtener ponentes de un proyecto
export const obtenerPonentesProyecto = async (id_proyecto) => {
    try {
        const response = await api.get(`/detalleProyecto/ponentes-proyecto/?id_proyecto=${id_proyecto}`, {
            headers: {
                'Authorization': `Bearer` 
            },
            
        });
        return response.data; 
    } catch (error) {
        if (error.response) {
            throw error; 
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

//Función para obtener datos de sala para presentación de un proyecto
export const obtenerInfoSalaProyecto = async (id_proyecto) => {
    try {
        const response = await api.get(`detalleProyecto/datos-sala-proyecto/?id_proyecto=${id_proyecto}` , {
            headers: {
                'Authorization': `Bearer` 
            },
        });
        return response.data
    }catch (error) {
        if (error.response) {
            throw error; 
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

//Función para obtener datos de rúbirca calificada
export const obtenerRubricaCalificada = async (id_proyecto, id_usuario) => {
    try {
        const response = await api.get(`/obtenerProyectosEvaluador/obtener-datos-del-proyecto-calificado/?id_proyecto=${id_proyecto}&id_usuario=${id_usuario}` , {
            headers: {
                'Authorization': `Bearer` 
            },
        });
        return response.data
    }catch (error) {
        if (error.response) {
            throw error; 
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

//Función para obtener los asistentes de un evento (suplentes)
export const obtenerAsistentesSuplentes = async (id_convocatoria) => {
    try {
        const response = await api.get(`/detalleProyecto/asistentes-evento/?id_convocatoria=${id_convocatoria}`, {
            headers: {
                'Authorization': `Bearer` 
            },
        });
        return response.data       
    }catch (error){
        if (error.response) {
            throw error;
        }else {
            throw new Error('Error del red o de servidor')
        }
    }
};

//Funcion para insertar suplente
export const insertarSuplente = async(id_usuario, id_etapa, id_proyecto, id_proyectos_convocatoria, tipo_usuario) => {
    try {
        const response = await api.post(`detalleProyecto/insertar-suplentes/?id_usuario=${id_usuario}&id_etapa=${id_etapa}&id_proyecto=${id_proyecto}&id_proyectos_convocatoria=${id_proyectos_convocatoria}&tipo_usuario=${tipo_usuario}`, {
            headers: {
                'Authorization': `Bearer` 
            },
        });
        return response.data;
    } catch (error) {
        if (error.response) {
            throw error;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};


//Función insertar url presentación
export const insertarUrlPresentacion = async (id_proyecto, url_presentacion) => {
    try {
        const response = await api.post(`detalleProyecto/insertar-url-presentacion/?id_proyecto=${id_proyecto}&url_presentacion=${url_presentacion} `, {
            headers: {
                'Authorization': `Bearer` 
            },
        });
    }catch (error) {
        if (error.response) {
            throw error;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};





