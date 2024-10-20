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

// Función para obtener la convocatoria en curso
export const getConvocatoriaEnCurso = async () => {
  try {
    const url = `/admin/convocatoria-en-curso`; // Ajusta la ruta según tu backend
    const response = await api.get(url, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Token de autenticación
      }
    });
    return response.data; // Retorna los datos de la convocatoria en curso
  } catch (error) {
    console.error('Error en el servicio getConvocatoriaEnCurso:', error);
    if (error.response) {
      throw error.response.data; // Retorna el mensaje de error exacto si el servidor lo provee
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};


// Servicio para la programación de múltiples fases
export const programarFases = async (programacionesFases) => {
  try {
    const url = `/admin/crear-programaciones-fases`;

    // Verifica qué payload se está enviando
    console.log('Enviando payload para programar fases:', programacionesFases);

    const response = await api.post(url, programacionesFases, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      }
    });

    return response.data; // Devolver solo los datos de la respuesta
  } catch (error) {
    console.error('Error en el servicio programarFases:', error);

    // Diferenciar errores del servidor y otros tipos de errores
    if (error.response) {
      // Error del servidor, lanzar el mensaje del servidor
      throw error.response.data;
    } else if (error.request) {
      // Error de red (la solicitud se hizo pero no hubo respuesta)
      throw new Error('No se recibió respuesta del servidor. Verifica tu conexión de red.');
    } else {
      // Otro tipo de error (algo ocurrió al hacer la solicitud)
      throw new Error('Error al configurar la solicitud.');
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

// Función para obtener todos los admins con paginación
export const getProgramacionFasesByPage = async (page = 1, pageSize = 5) => {
  try {
      const response = await api.get(`/convocatorias/programacion-fases-activa/?page=${page}&page_size=${pageSize}`);
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

// Función para editar item
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
      const url = `/admin/update-status-items/${id_item_rubrica}/`;
      const response = await api.put(url, {
        estado: "inactivo"
      },{
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

// Función para buscar documento y nombre
export const getDelegateByNameOrDocument = async (busqueda) => {
  try {
      const url = `/admin/delegates/${busqueda}/`;
      const response = await api.get(url,{
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

// Función para crear delegado
export const createDelegate = async (user) => {
  try {
      const url = `/admin/create-delegates/`;
      const response = await api.post(url, user,{
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
}

// Obtener todos los tipos de documento
export const getAllDocumentsType= async (user) => {
  try {
      const url = `/admin/all_type_documents/`;
      const response = await api.get(url,{
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
}

//Función para actualizar estado delegado
export const updateStatusDelegate = async (id_delegado, estado) => {
  try{
    const url = `/admin/update-delegate-status/${id_delegado}/`;
      const response = await api.put(url, 
      {
        estado: estado
      },
      {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` 
      }
    });
    return response;
  }catch(error){
    if (error.response) {
      throw error;
    } else {
      throw new Error('Error de red o de servidor'); 
    }
  }
}

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