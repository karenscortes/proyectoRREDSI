import api from './api';

// Servicio para insertar un proyecto
export const insertarProyecto = async (id_institucion, id_modalidad, id_area_conocimiento, titulo, programa_academico, grupo_investigacion, linea_investigacion, nombre_semillero, propuesta_escrita, aval) => {
    try {
        const formData = new FormData();
        formData.append('id_institucion', id_institucion);
        formData.append('id_modalidad', id_modalidad);
        formData.append('id_area_conocimiento', id_area_conocimiento);
        formData.append('titulo', titulo);
        formData.append('programa_academico', programa_academico);
        formData.append('grupo_investigacion', grupo_investigacion);
        formData.append('linea_investigacion', linea_investigacion);
        formData.append('nombre_semillero', nombre_semillero);
        formData.append('propuesta_escrita', propuesta_escrita);
        formData.append('aval', aval);

        const response = await api.post('/projects/create', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error.response;  // Devuelve el error de la API
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

// Servicio para insertar un participante en un proyecto
export const insertarParticipanteProyecto = async (id_usuario, id_proyecto, id_proyectos_convocatoria) => {
    try {
        const response = await api.post('/participanteProyecto/create', {
            id_usuario: id_usuario,
            id_proyecto: id_proyecto,
            id_proyectos_convocatoria: id_proyectos_convocatoria
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error.response;  // Devuelve el error de la API
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

// Servicio para agregar un proyecto a una convocatoria
export const agregarProyectoConvocatoria = async (id_proyecto) => {
    try {
        const response = await api.post('/proyectosConvocatorias/create', {
            id_proyecto: id_proyecto,
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error.response;  // Devuelve el error de la API
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};
