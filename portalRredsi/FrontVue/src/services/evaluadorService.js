import api from './api'; 

// Función para obtener los proyectos asignados
export const obtenerProyectosAsignados = async (idUsuario, page = 1, pageSize = 10) => {
  try {
    const response = await api.get('/obtenerProyectosEvaluador/obtener-proyectos-asignados-paginados/', {
      params: {
        id_usuario: idUsuario,
        page: page,
        page_size: pageSize
      }
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error; // Lanza el error para que lo maneje el store
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};


// Función para obtener los proyectos asignados
export const obtenerProyectosPorEstado = async (estado_evaluacion, idUsuario, page = 1, pageSize = 10) => {
  try {
    const response = await api.get('/obtenerProyectosEvaluador/obtener-proyectos-por-estado-paginados/', {
      headers: {
        'Authorization': `Bearer` // Incluye el token de autenticación
      },
      params: {
        estado_evaluacion: estado_evaluacion,
        id_usuario: idUsuario,
        page: page,
        page_size: pageSize
      }
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error; // Lanza el error para que lo maneje el store
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};

// Servicio para obtener los datos para calificar un proyecto
export const obtenerDatosParaCalificarProyecto = async (idProyecto, idUsuario) => {
  try {
    const response = await api.get('/obtenerProyectosEvaluador/obtener-datos-para-calificar-proyecto/', {
      params: {
        id_proyecto: idProyecto,
        id_usuario: idUsuario
      }
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      throw error; // Lanza el error para que lo maneje el componente
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};


// Función para insertar una postulación de evaluador
export const insertarPostulacionEvaluador = async (postulacionData) => {
  try {
    const response = await api.post('/postulacionEvaluador/insertar-postulacion-evaluador/', postulacionData, {
      headers: {
        'Authorization': `Bearer`, // Incluye el token de autenticación
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error; // Lanza el error para que lo maneje el store o componente
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};