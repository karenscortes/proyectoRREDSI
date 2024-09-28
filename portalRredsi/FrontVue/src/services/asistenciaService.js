import api from './api';

// Función para subir un archivo relacionado con una transacción
export const uploadFileData = async (file) => {
    try {
      const formData = new FormData();
      formData.append('file', file);
  
      const response = await api.post(`/transaction/upload-file/`, formData, {
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