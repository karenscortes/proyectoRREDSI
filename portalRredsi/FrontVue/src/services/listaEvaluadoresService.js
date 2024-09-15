import api from './api'; 

// Función para obtener la lista de evaluadores
export const obtenerListaEvaluadores = async (page = 1, page_size = 10) => {
    try {
        const response = await api.get(`/listaEvaluadores/get-all-evaluators/?page=${page}&page_size=${page_size}
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

// Función para actualizar el estado de un evalaudor
export const actualizarEstadoEvaluador = async (id_evaluador, estado) => {
    try {
        const response = await api.put(`/listaEvaluadores/update-evaluator-status/?id_evaluador=${id_evaluador}&estado=${estado}
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