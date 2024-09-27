import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getCurrentUser = async () => {
    try {
      const token = localStorage.getItem('token');
      if (!token) {
        throw new Error('Token de autenticación no encontrado. Inicia sesión nuevamente.');
      }
  
      console.log('Token:', token);
  
      const response = await api.get('/users/me', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
  
      console.log('Respuesta de la API:', response); // Agrega este console.log
  
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

// Nueva función para actualizar el perfil 
export const updateUserProfile = async (userId, userData) => {
    try {
        const response = await api.put('/users/update/', {
            user_id: userId,
            userData // Aquí se desglosan los datos del perfil que se quieren actualizar
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

export const registerUser = async (idTipoDocumento, documento, nombres, apellidos, celular, correo, clave) => {
  try {
    // Enviar solicitud de registro a la API
    const response = await api.post('/evaluadores/create', {
      id_tipo_documento: idTipoDocumento, // ID del tipo de documento
      documento: documento,
      nombres: nombres,
      apellidos: apellidos,
      celular: celular,
      correo: correo,
      clave: clave
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    // Retornar la respuesta de la API
    return response;
  } catch (error) {
    // Manejar errores de la solicitud
    if (error.response) {
      throw error; // Lanza el error de la API
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};