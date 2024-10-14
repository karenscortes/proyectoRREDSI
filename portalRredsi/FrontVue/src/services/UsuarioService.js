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
    const url = `/users/update/${encodeURIComponent(userId)}/`;
    const response = await api.put(url,userData,
    {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` 
      }
    });
      return response.data; 
  } catch (error) {
    if (error.response) {
      throw error.response.data;
    } else {
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
    if (response.data === null)
      return null;
    return response;
  } catch (error) {
    if (error.response) {
      throw error;
    } else {
      throw new Error('Error de red o de servidor'); 
    }
  }
};

// Función para actualizar el perfil del usuario
export const resetPassword = async (curPass, Newpass, email) => {
  try {

    const formData = new FormData();
    formData.append('email', email);
    formData.append('current_password', curPass);
    formData.append('new_password', Newpass);

    const response = await api.put('/users/update-password/',formData,     
    {
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json'
      }
    });
      return response; 
  } catch (error) {
    if (error.response) {
      throw error.response.data;
    } else {
      throw new Error('Error de red o de servidor');
    }   
  }
};

// Función para actualizar los datos institucionales
export const updateInstitutionalData = async (userId,Data) => {
  try {
    const url = `/users/update-institutional-data/${encodeURIComponent(userId)}/`;
    const response = await api.put(url,Data,
    {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
      }
    });
    
    return response.data; 
  } catch (error) {
    if (error.response) {
      throw error.response.data;
    } else {
      throw new Error('Error de red o de servidor');
    }
    
  }
};

// Función para crear un registro de datos institucionales
export const createInstitutionalData = async (Data) => {
  try {
    const response = await api.post('/users/create-institutional-data/', Data, {
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json'  
      }
    });
    return response; // Retorna la respuesta de la API
  } catch (error) {
    if (error.response) {
      throw error.response.data; // Devuelve el error que envía la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};


// Función para insertar archivos de los titulos academicos
export const insertCertificatesFiles = async (userId,pregradoFile,especializacionFile,maestriaFile,doctoradoFile) => {
  try {
    console.log("entróoo")
    const formData = new FormData();

    if(pregradoFile){
      formData.append('pregradoFile', pregradoFile);
    }
    
    if(especializacionFile){
      formData.append('especializacionFile', especializacionFile);
    }
    
    if(maestriaFile){
      formData.append('maestriaFile', maestriaFile);
    }
    
    if(doctoradoFile){
      formData.append('doctoradoFile', doctoradoFile);
    }
    
    
    const url = `/users/upload-certificates/${encodeURIComponent(userId)}/`;
    const response = await api.put(url,formData,{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response; // Retorna la respuesta de la API
  } catch (error) {
    if (error.response) {
      throw error.response.data; // Devuelve el error que envía la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para crear registros de titulos academicos
export const createUpdateRecords = async (userId,data) => {
  try {    
    const url = `/users/create-certificates-records/${encodeURIComponent(userId)}/`;
    const response = await api.post(url,data,{
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json'   
      }
    });
    return response; // Retorna la respuesta de la API
  } catch (error) {
    if (error.response) {
      throw error.response.data; // Devuelve el error que envía la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
