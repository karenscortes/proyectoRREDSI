import api from './api'; // Importa tu instancia de Axios con la baseURL configurada

export const registrarProyecto = async (datosProyecto, datosTutor, datosPonente, ponenteOpcional, autores) => {
  try {
    const formData = new FormData();

    // Agrega todos los datos del proyecto
    formData.append('id_institucion', datosProyecto.institucion_educativa);
    formData.append('id_modalidad', datosProyecto.modalidad);
    formData.append('id_area_conocimiento', datosProyecto.area_conocimiento);
    formData.append('titulo', datosProyecto.titulo);
    formData.append('programa_academico', datosProyecto.programa_academico);
    formData.append('grupo_investigacion', datosProyecto.grupo_investigacion);
    formData.append('linea_investigacion', datosProyecto.linea_investigacion);

    // Si existen los archivos, los agregamos
    if (datosProyecto.propuesta_escrita) {
      formData.append('url_propuesta_escrita', datosProyecto.propuesta_escrita);
    }
    if (datosProyecto.aval) {
      formData.append('url_aval', datosProyecto.aval);
    }

    // Agrega los datos del tutor
    formData.append('tutor_id_tipo_documento', datosTutor.tipo_documento);
    formData.append('tutor_documento', datosTutor.numero_documento);
    formData.append('tutor_nombres', datosTutor.nombres);
    formData.append('tutor_apellidos', datosTutor.apellidos);
    formData.append('tutor_celular', datosTutor.celular);
    formData.append('tutor_correo', datosTutor.correo);

    // Agrega los datos del primer ponente
    formData.append('ponente1_id_tipo_documento', datosPonente.tipo_documento);
    formData.append('ponente1_documento', datosPonente.numero_documento);
    formData.append('ponente1_nombres', datosPonente.nombres);
    formData.append('ponente1_apellidos', datosPonente.apellidos);
    formData.append('ponente1_celular', datosPonente.celular);
    formData.append('ponente1_correo', datosPonente.correo);

    // Si existe el segundo ponente, lo agregamos
    if (ponenteOpcional) {
      formData.append('ponente2_id_tipo_documento', ponenteOpcional.tipo_documento);
      formData.append('ponente2_documento', ponenteOpcional.numero_documento);
      formData.append('ponente2_nombres', ponenteOpcional.nombres);
      formData.append('ponente2_apellidos', ponenteOpcional.apellidos);
      formData.append('ponente2_celular', ponenteOpcional.celular);
      formData.append('ponente2_correo', ponenteOpcional.correo);
    }

    // Agrega la lista de autores uno por uno
    autores.forEach((autor, index) => {
      formData.append(`autores[${index}]`, autor.nombre);
    });

    // Enviamos la solicitud POST con multipart/form-data
    const response = await api.post('/projects/create-project', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('Error en la respuesta de la API:', error.response);
      throw error.response.data;
    } else {
      console.error('Error de red o de servidor:', error);
      throw new Error('Error de red o de servidor');
    }
  }
};
