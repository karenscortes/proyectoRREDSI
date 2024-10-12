import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

// Función para crear un usuario
export const createUser = async (id_tipo_documento, documento, nombres, apellidos, celular, correo, clave) => {
  try {
    const response = await api.post('/evaluadores/create', {
      id_tipo_documento,
      documento,        // Número de documento
      nombres,          // Nombres del usuario
      apellidos,        // Apellidos del usuario
      celular,          // Número de teléfono
      correo,           // Correo electrónico
      clave             // Contraseña
    });
    
    return response; // Retorna la respuesta de la API
  } catch (error) {
    if (error.response) {
      console.error('Error en la respuesta de la API:', error.response.data);
      throw error.response.data; // Devuelve el error que envía la API
    } else {
      console.error('Error de red o de servidor:', error.message);
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para obtener el usuario actual
export const getCurrentUser = async () => {
  try {
    const token = localStorage.getItem('token');  // Asume que tu token está almacenado en el localStorage
    if (!token) {
      throw new Error('Token de autenticación no encontrado. Inicia sesión nuevamente.');
    }

    const response = await api.get('/users/me', {
      headers: {
        Authorization: `Bearer ${token}`,  // Usa el token que extraes
      },
    });

    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('Error en la respuesta de la API:', error.response.status, error.response.data);
    } else if (error.request) {
      console.error('No se recibió respuesta del servidor:', error.request);
    } else {
      console.error('Error durante la solicitud:', error.message);
    }
    throw error;
  }
};

// Función para actualizar el perfil del usuario
export const updateUserProfile = async (userId, userData) => {
  try {
    const response = await api.put('/users/update/', 
      ...userData,
      userId, // Aquí se desglosan los datos del perfil que se quieren actualizar
      {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Asegúrate de obtener el token correctamente
        }
      });
    return response.data; // Retorna el mensaje de éxito
  } catch (error) {
    if (error.response) {
      // Manejar el error que proviene del servidor
      throw error.response.data;
    } else {
      // Manejar errores de red u otros errores no relacionados con la API
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función consultar los detalles institucionales de un usuario loguegado
export const getInstitutionalDetails = async () => {
  try {
      const url = `/users/me/get_institutional_details/
`;
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