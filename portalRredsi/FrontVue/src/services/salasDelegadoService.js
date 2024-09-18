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