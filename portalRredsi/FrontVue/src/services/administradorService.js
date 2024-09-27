import api from './api';

// Función para crear una nueva convocatoria
export const createConvocatoria = async (convocatoria) => {
  try {
    const url = `/admin/crear-convocatoria`;
    const response = await api.post(url, convocatoria, {
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

// Función para agregar una nueva etapa
export const addEtapa = async (idConvocatoria, nombre) => {
  try {
    const url = `/admin/convocatoria/${idConvocatoria}/etapas`;
    const response = await api.post(url, { nombre }, {
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

// Función para agregar una nueva fase
export const addFase = async (idEtapa, nombre) => {
  try {
    const url = `/admin/etapas/${idEtapa}/fases`;
    const response = await api.post(url, { nombre }, {
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

// Función para obtener fases por etapa
export const getFases = async (idEtapa) => {
  try {
    const url = `/admin/etapas/${idEtapa}/fases`;
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

// Función para editar una etapa
export const modifyEtapa = async (idEtapa, nombre) => {
  try {
    const url = `/admin/etapas/${idEtapa}`;
    const response = await api.put(url, { nombre }, {
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

// Función para editar una fase
export const modifyFase = async (idFase, nombre) => {
  try {
    const url = `/admin/fases/${idFase}`;
    const response = await api.put(url, { nombre }, {
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