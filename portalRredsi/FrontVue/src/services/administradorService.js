import api from './api';

// Funcion para crear convocatoria
export const createConvocatoria = async (nombre, fecha_inicio, fecha_fin, estado) => {
  try {
    const url = `/admin/crear-convocatoria`;
    const payload = { nombre, fecha_inicio, fecha_fin, estado };
    console.log('Enviando payload:', payload); // Verifica qué se está enviando
    const response = await api.post(url, payload, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      }
    });
    return response;
  } catch (error) {
    console.error('Error en el servicio createConvocatoria:', error);
    if (error.response) {
      throw error.response.data; // Enviar el mensaje de error exacto si el servidor lo provee
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Servicio para la programación de fases
export const programarFase = async (id_fase, id_convocatoria, fecha_inicio, fecha_fin) => {
  try {
    const url = `/admin/crear-programacion-fase`;
    const payload = { id_fase, id_convocatoria, fecha_inicio, fecha_fin };
    console.log('Enviando payload para programar fase:', payload); // Verifica qué se está enviando
    const response = await api.post(url, payload, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      }
    });
    return response;
  } catch (error) {
    console.error('Error en el servicio programarFase:', error);
    if (error.response) {
      throw error.response.data; // Enviar el mensaje de error exacto si el servidor lo provee
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para obtener todos los admins con paginación
export const getConvocatoriasByPage = async (page = 1, pageSize = 5) => {
  try {
      const response = await api.get(`/convocatorias/verconvocatorias/?page=${page}&page_size=${pageSize}`);
      return response.data;  // Acceder a los datos de la respuesta
  } catch (error) {
      if (error.response) {
          throw error.response.data;  // Devuelve el error original de la API
      } else {
          throw new Error('Error de red o de servidor');
      }
  }
};


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

// Función para crear item 
export const InsertItems = async (new_item) => {
  try {
      const url = `/admin/create-items/`;
      const response = await api.post(url, new_item,{
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
export const updateItems = async (id_item_rubrica, item_nuevo) => {
  try {
      const url = `/admin/update-items/${id_item_rubrica}/`;
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

// Función para eliminar item
export const deleteItems = async (id_item_rubrica) => {
  try {
      const url = `/admin/delete-items/${id_item_rubrica}/`;
      const response = await api.post(url, {
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

// Función consultar delegados paginados
export const getDelegatesAll = async (page = 1, page_size = 10) => {
  try {
      const url = `/admin/all-delegates/?page=${page}&page_size=${page_size}`;
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

// Función consultar las reas de conocimiento
export const getAreasConocimiento = async () => {
  try {
      const url = `/generales/get_areas_conocimiento/`;
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

// Función para crear sala
export const addSala = async (p_id_usuario,p_area_conocimento,p_numero_sala,p_nombre_sala) => {
  try {
      const url = `/admin/crear-sala/`;
      const response = await api.post(url, {
          id_usuario: p_id_usuario,
          area_conocimento: p_area_conocimento,
          numero_sala: p_numero_sala,
          nombre_sala: p_nombre_sala
        },
        {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
          },
        }
      
    );
    return response;
  } catch (error) {
    if (error.response) {
      throw error;
    } else {
      throw new Error('Error de red o de servidor'); 
    }
  }
};

// Función para actualizar sala
export const updateSala = async (p_id_sala,p_id_usuario,p_area_conocimento,p_numero_sala,p_nombre_sala) => {
  try {
      const url = `/admin/salas/${p_id_sala}`;
      const response = await api.put(url, {
          id_usuario: p_id_usuario,
          area_conocimento: p_area_conocimento,
          numero_sala: p_numero_sala,
          nombre_sala: p_nombre_sala
        },
        {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
          },
        }
      
    );
    return response;
  } catch (error) {
    if (error.response) {
      throw error;
    } else {
      throw new Error('Error de red o de servidor'); 
    }
  }
};