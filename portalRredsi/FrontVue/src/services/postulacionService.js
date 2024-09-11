import api from './api';

// Función para obtener todos las postulaciones con paginación
export const getApplicationsByPage = async (page = 1, pageSize = 10) => {
    try {
      const response = await api.get(`/postulaciones/get-all-applications/?page=${page}&page_size=${pageSize}`, {
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

// Función para obtener los certificados
export const getCertificatesById = async (id_evaluador) => {
    try {
      const response = await api.get(`/postulaciones/get-certificates-by-id/?id_usuario=${encodeURIComponent(id_evaluador)}`);
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; 
      } else {
        throw new Error('Error de red o de servidor'); 
      }
    }
};

// Función para actualizar estado de postulación
export const updateApplication = async (id_evaluador,estado) => {
    try {
      const response = await api.put(`/postulaciones/update-application-status/?id_evaluador=${id_evaluador}&estado=${estado}`);
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; 
      } else {
        throw new Error('Error de red o de servidor'); 
      }
    }
};