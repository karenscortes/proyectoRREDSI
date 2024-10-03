import api from './api';
import { useToastUtils } from '@/utils/toast'; // Importar la librería de utilidades de notificación

// Función para manejar el inicio de sesión
export const login = async (username, password) => {
  const { showErrorToast } = useToastUtils(); // Inicializar las alertas

  try {
    // Enviar solicitud de inicio de sesión
    const response = await api.post('/access/token', new URLSearchParams({
      username,
      password,
    }), {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });

    // Retornar los datos si la solicitud fue exitosa
    return response.data;

  } catch (error) {
    // Manejar errores de la solicitud
    if (error.response) {
      const status = error.response.status;
      const errorMessage = error.response.data.detail;

      // Mostrar un mensaje de error adecuado en el frontend usando las alertas personalizadas
      if (status === 404) {
        showErrorToast('El correo no está registrado,por favor crear cuenta.'); // Mensaje cuando el correo no está en la base de datos
      } else if (status === 403) {
        showErrorToast('El usuario no está autorizado, comuniquese con el administrador');
      } else if (status === 401) {
        showErrorToast('Información incorrecta, verifica tu email o contraseña.');
      } else if (status === 500) {
        showErrorToast('Error del servidor. Intenta de nuevo más tarde.');
      } else {
        showErrorToast(`Error desconocido: ${status}. Intenta de nuevo.`);
      }

    } else if (error.request) {
      showErrorToast('No se recibió respuesta del servidor. Verifica tu conexión a internet.');
    } else {
      showErrorToast(`Error en la solicitud: ${error.message}`);
    }

    throw error;
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