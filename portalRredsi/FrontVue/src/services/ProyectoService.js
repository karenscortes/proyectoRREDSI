import api from './api';

// Función para crear un nuevo proyecto
export const createProject = async (projectData) => {
  try {
    const response = await api.post('/projects/create', {
      id_institucion: projectData.institucion_educativa,
      id_modalidad: projectData.modalidad,
      id_area_conocimiento: projectData.area_conocimiento,
      titulo: projectData.titulo,
      programa_academico: projectData.programa_academico,
      grupo_investigacion: projectData.grupo_investigacion,
      linea_investigacion: projectData.linea_investigacion,
      nombre_semillero: projectData.nombre_semillero
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para subir archivos relacionados con un proyecto
export const uploadProjectFile = async (projectId, file, fileType) => {
  try {
    const formData = new FormData();
    formData.append('file', file);

    const response = await api.post(`/projects/upload-file/${projectId}?type=${fileType}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para asociar el proyecto a una convocatoria
export const addProjectToCall = async (projectId, callId) => {
  try {
    const response = await api.post('/proyectosConvocatorias/create', {
      id_proyecto: projectId,
      id_convocatoria: callId
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para agregar un participante a un proyecto
export const addProjectParticipant = async (projectId, userId, callProjectId) => {
  try {
    const response = await api.post('/participanteProyecto/create', {
      id_usuario: userId,
      id_proyecto: projectId,
      id_proyectos_convocatoria: callProjectId
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
