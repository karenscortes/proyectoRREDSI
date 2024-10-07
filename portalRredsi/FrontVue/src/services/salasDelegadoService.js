import api from './api'; 

// Sala asignada a un delegado especifico
export const obtenerDatosSalaAsignada = async (id_usuario_logueado) => {
    try {
        const response = await api.get(`/salas/verificar-sala-asignada/?id_usuario=${id_usuario_logueado}`, {
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


// FUNCION PARA OBTENER LOS PONENTES RELACIONADOS A UN PROYECTO
export const obtenerPonentesProyecto = async (id_proyecto) => {
    try {
        const response = await api.get(`/salas/get-ponentes-proyecto/?id_proyecto=${id_proyecto}`, {
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

// FUNCION PARA OBTENER LOS PROYECTOS QUE NO HAN SIDO ASIGNADOS EN LA ETAPA PRESENCIAL
export const obetnerProyectosSinAsignarEtapaPresencial = async () => {
    try {
        const response = await api.get(`/salas/get-proyectos-sin-asignar-etapa-presencial/`, {
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

// FUNCION PARA OBTENER LOS POSIBLES EVALUADORES EN LA ETAPA PRESENCIAL
export const obtenerPosiblesEvaluadoresEtapaPresencial = async (id_area_conocimiento,id_institucion) => {
    try {
        const response = await api.get(`/salas/get-posibles-evaluadores-etapa-presencial/?id_area_conocimiento=${id_area_conocimiento}&id_institucion=${id_institucion}
`, {
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

// FUNCION PARA OBTENER DETALLE DE UNA SALA ESPECIFICA
export const obtenerDetalleSala = async (id_sala) => {
    try {
        const response = await api.get(`/salas/get-detalle-sala/?id_sala=${id_sala}`, {
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

// FUNCION PARA ASIGNAR EVALUADORES PARA QUE EVALUEN UN PROYECTO EN UNA SALA ESPECIFICA
export const asignarEvaluadoresEtapaPresencial = async (id_evaluador_1,id_evaluador_2,id_proyecto,id_proyecto_convocatoria,id_sala,fecha,hora_inicio,hora_fin) => {
    try {
        const response = await api.post(`/salas/asignar-evaluadores-etapa-presencial/?id_evaluador_1=${id_evaluador_1}&id_evaluador_2=${id_evaluador_2}&id_proyecto=${id_proyecto}&id_proyecto_convocatoria=${id_proyecto_convocatoria}&id_sala=${id_sala}&fecha=${fecha}&hora_inicio=${hora_inicio}&hora_fin=${hora_fin}
`, {
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

// FUNCION PARA OBTENER DATOS DE UN PROYECTO POR ID
export const obtenerDatosProyecto = async (id_proyecto) => {
    try {
        const response = await api.get(`/generales/get_proyecto_by_id/?id_proyecto=${id_proyecto}
`, {
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

// FUNCION PARA ACTUALIZAR LA FECHA Y HORARIO DE DETALLE SALA DATOS DE UN PROYECTO POR ID
export const actualizarHorarioAsignado = async (p_id_sala,p_id_proyecto_convocatoria,p_fecha,p_hora_inicio,p_hora_fin) => {
    try {
        const response = await api.put(`/salas/actualizar-horario/?id_sala=${p_id_sala}&id_proyecto_convocatoria=${p_id_proyecto_convocatoria}&fecha=${p_fecha}&hora_inicio=${p_hora_inicio}&hora_fin=${p_hora_fin}

`, {
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