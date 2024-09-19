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