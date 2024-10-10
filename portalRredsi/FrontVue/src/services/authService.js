import api from './api';
import { useToastUtils } from '@/utils/toast'; // Importar la librería de utilidades de notificación

// Función para manejar el inicio de sesión
export const login = async (username, password) => {
  const { showErrorToast } = useToastUtils(); // Inicializar las alertas

  try {
    // Enviar solicitud de inicio de sesión
    const response = await api.post('/access/token', new URLSearchParams({
      grant_type: '',
      username,
      password,
      scope: '',
      client_id: '',
      client_secret: ''
    }), {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });

    // Retornar la respuesta de la API
    return response;

  } catch (error) {
    // Manejar errores de la solicitud
    if (error.response) {
      const status = error.response.status;

      // Mostrar un mensaje de error adecuado en el frontend usando las alertas personalizadas
      if (status === 404) {
        showErrorToast('El correo no está registrado, por favor crear cuenta.'); // Correo no encontrado
      } else if (status === 403) {
        showErrorToast('El usuario no está autorizado, comuníquese con el administrador.');
      } else if (status === 401) {
        showErrorToast('Información incorrecta, verifica tu email o contraseña.');
      } else if (status === 500) {
        showErrorToast('Error del servidor. Intenta de nuevo más tarde.');
      } else {
        showErrorToast(`Ingresa los datos para iniciar sesión.`);
      }

      throw error; // Lanza el error para que lo maneje el store

    } else {
      // Manejar errores de red
      showErrorToast('Error de red o de servidor');
      throw new Error('Error de red o de servidor');
    }
  }
};


export const requestResetCode = async (email) => {
  try {
    const response = await api.post(`/access/request-reset-code?email=${encodeURIComponent(email)}`, '', {
      headers: {
        'accept': 'application/json'
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

// Función para verificar código y actualizar contraseña
export const changePassword = async (email, newPassword, code) => {
  try {
    const response = await api.post('/access/change-password', {
      email,
      new_password: newPassword,
      code
    }, {
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json'
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