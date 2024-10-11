import api from './api';  // Instancia Axios con la URL base configurada

export const createProject = async (datosProyecto, datosTutor, datosPonente, ponenteOpcional, autores) => {
  try {
    const formData = new FormData();

    // Proyecto
    formData.append('id_institucion', datosProyecto.institucion_educativa);
    formData.append('id_modalidad', datosProyecto.modalidad);
    formData.append('id_area_conocimiento', datosProyecto.area_conocimiento);
    formData.append('titulo', datosProyecto.titulo);
    formData.append('programa_academico', datosProyecto.programa_academico);
    formData.append('grupo_investigacion', datosProyecto.grupo_investigacion || '');
    formData.append('linea_investigacion', datosProyecto.linea_investigacion || '');
    formData.append('nombre_semillero', datosProyecto.nombre_semillero || '');

    // Archivos
    formData.append('url_propuesta_escrita', datosProyecto.propuesta_escrita);  // Archivo de propuesta escrita
    formData.append('url_aval', datosProyecto.aval);  // Archivo de aval

    // Tutor
    formData.append('tutor_id_tipo_documento', datosTutor.tipo_documento);
    formData.append('tutor_documento', datosTutor.numero_documento);
    formData.append('tutor_nombres', datosTutor.nombres);
    formData.append('tutor_apellidos', datosTutor.apellidos);
    formData.append('tutor_celular', datosTutor.celular);
    formData.append('tutor_correo', datosTutor.correo);

    // Ponente 1
    formData.append('ponente1_id_tipo_documento', datosPonente.tipo_documento);
    formData.append('ponente1_documento', datosPonente.numero_documento);
    formData.append('ponente1_nombres', datosPonente.nombres);
    formData.append('ponente1_apellidos', datosPonente.apellidos);
    formData.append('ponente1_celular', datosPonente.celular);
    formData.append('ponente1_correo', datosPonente.correo);

    // Ponente 2 (opcional)
    if (
      ponenteOpcional.nombres && 
      ponenteOpcional.apellidos && 
      ponenteOpcional.numero_documento && 
      ponenteOpcional.celular && 
      ponenteOpcional.correo
    ) {
      formData.append('ponente2_id_tipo_documento', ponenteOpcional.tipo_documento);
      formData.append('ponente2_documento', ponenteOpcional.numero_documento);
      formData.append('ponente2_nombres', ponenteOpcional.nombres);
      formData.append('ponente2_apellidos', ponenteOpcional.apellidos);
      formData.append('ponente2_celular', ponenteOpcional.celular);
      formData.append('ponente2_correo', ponenteOpcional.correo);
    }

    // Autores
    const autoresNombres = autores.map(autor => autor.nombre).join(', ');
    formData.append('autores', autoresNombres);

    // Enviar la solicitud a la API
    const response = await api.post('/projects/projects/create-project', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    return response;
  } catch (error) {
    if (error.response && error.response.data && error.response.data.detail) {
      // Usar el mensaje de error específico proporcionado por la API
      throw new Error(error.response.data.detail);
    } else {
      // Error genérico si no hay detalles en la respuesta
      throw new Error('No se pudo conectar con el servidor. Inténtelo de nuevo.');
    }
  }
};
