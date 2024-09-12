import api from './api';

// Función para obtener todas las rubricas
export const getRubricsAll = async () => {
    try {
        const response = await api.get(`/admin/all-rubrics/`, {
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

// Función para editar itemsRubrica
export const updateItems = async ($id_item_rubrica, item_nuevo) => {
  try {
      const response = await api.put(`/admin/update-items/?id_item=${$id_item_rubrica}&item_nuevo=${item_nuevo}/`,{
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