import api from './api';

// Función para subir un archivo relacionado con una transacción
export const uploadFileData = async (file) => {
    try {
      const formData = new FormData();
      formData.append('file', file);
  
      const response = await api.post(`/admin/upload-excel/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data', // Solo es necesario este header
        }
      });
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };


  // Función para obtener todos los asistentes
export const getAttendeesByPage = async (page = 1, pageSize = 10) => {
  try {
    const response = await api.get(`/admin/get-all-attendees/?page=${page}&page_size=${pageSize}`, {
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

// Función para editar asistente
export const updateAttendees = async (id_usuario, newData) => {
  try {
      const url = `/admin/update-attendee/${id_usuario}/`;
      const response = await api.put(url, newData,{
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