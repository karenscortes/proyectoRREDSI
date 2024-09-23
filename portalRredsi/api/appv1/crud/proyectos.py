from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.proyecto import  ProyectoCreate
from core.utils import generate_project_id

def create_project_sql(db: Session, proyecto: ProyectoCreate,url_propuesta_escrita=str,url_aval=str):
    try:
        # Insertar datos en la tabla `proyectos`
        sql_query_proyecto = text(
            """
            INSERT INTO proyectos (
                id_proyecto,id_institucion, id_modalidad, id_area_conocimiento, titulo, programa_academico, 
                grupo_investigacion, linea_investigacion, nombre_semillero, url_propuesta_escrita, url_aval
            ) VALUES (
                :id_proyecto,:id_institucion, :id_modalidad, :id_area_conocimiento, :titulo,  :programa_academico,
                :grupo_investigacion, :linea_investigacion, :nombre_semillero, :url_propuesta_escrita, :url_aval
            );
            """
        )

        # Parámetros para la tabla `proyectos`
        params_proyecto = {
            "id_proyecto": generate_project_id(),
            "id_institucion": proyecto.id_institucion,
            "id_modalidad": proyecto.id_modalidad,
            "id_area_conocimiento": proyecto.id_area_conocimiento,
            "titulo": proyecto.titulo,  # estado inicial del proyecto
            "programa_academico": proyecto.programa_academico,
            "grupo_investigacion": proyecto.grupo_investigacion,
            "linea_investigacion": proyecto.linea_investigacion,
            "nombre_semillero": proyecto.nombre_semillero,
            "url_propuesta_escrita": url_propuesta_escrita,
            "url_aval": url_aval
        }

        # Ejecutar inserción en la tabla `proyectos`
        db.execute(sql_query_proyecto, params_proyecto)
        db.commit()

        return True  # Retorna True si la inserción fue exitosa

    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear proyecto: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID del proyecto ya está en uso")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad al crear el proyecto")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear proyecto: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor al crear el proyecto")
