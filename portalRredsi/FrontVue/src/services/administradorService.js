import api from './api';

// Función para obtener todas las rubricas
export const getRubricsAll = async () => {
    try {
        const url = `/admin/all-rubrics/`;
        const response = await api.get(url, {
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
      const url = `/admin/update-items/${$id_item_rubrica}/`;
      const response = await api.put(url, item_nuevo,{
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