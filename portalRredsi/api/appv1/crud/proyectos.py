from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.proyecto import  ProyectoCreate

def create_project_sql(db: Session, proyecto: ProyectoCreate):
    try:
        # Insertar datos en la tabla `proyectos`
        sql_query_proyecto = text(
            """
            INSERT INTO proyectos (
                id_institucion, id_modalidad, id_area_conocimiento, titulo, estado, programa_academico, 
                grupo_investigacion, linea_investigacion, nombre_semillero, url_propuesta_escrita, url_aval
            ) VALUES (
                :id_institucion, :id_modalidad, :id_area_conocimiento, :titulo, :estado, :programa_academico,
                :grupo_investigacion, :linea_investigacion, :nombre_semillero, :url_propuesta_escrita, :url_aval
            );
            """
        )

        # Parámetros para la tabla `proyectos`
        params_proyecto = {
            "id_institucion": proyecto.id_institucion,
            "id_modalidad": proyecto.id_modalidad,
            "id_area_conocimiento": proyecto.id_area_conocimiento,
            "titulo": proyecto.titulo,
            "estado": "pendiente",  # estado inicial del proyecto
            "programa_academico": proyecto.programa_academico,
            "grupo_investigacion": proyecto.grupo_investigacion,
            "linea_investigacion": proyecto.linea_investigacion,
            "nombre_semillero": proyecto.nombre_semillero,
            "url_propuesta_escrita": proyecto.url_propuesta_escrita,
            "url_aval": proyecto.url_aval
        }

        # Ejecutar inserción en la tabla `proyectos`
        db.execute(sql_query_proyecto, params_proyecto)
        db.commit()

        # Obtener el ID del proyecto recién creado
        id_proyecto = db.execute(text("SELECT LAST_INSERT_ID()")).scalar()

        # Insertar autores en la tabla `autores`
        sql_query_autores = text(
            "INSERT INTO autores (nombre, id_proyecto) VALUES (:nombre, :id_proyecto);"
        )

        for autor in proyecto.autores:
            db.execute(sql_query_autores, {"nombre": autor, "id_proyecto": id_proyecto})

        # Insertar tutores y ponentes en la tabla `usuarios` y asociarlos al proyecto
        sql_query_usuarios = text(
            """
            INSERT INTO usuarios (nombre, apellido, correo, telefono, tipo) 
            VALUES (:nombre, :apellido, :correo, :telefono, :tipo)
            ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id);
            """
        )

        sql_query_participantes = text(
            """
            INSERT INTO participantes_proyecto (id_usuario, id_etapa, id_proyecto, id_proyecto_convocatoria) 
            VALUES (:id_usuario, :id_etapa, :id_proyecto, :id_proyecto_convocatoria);
            """
        )

        # Insertar información personal de tutores y ponentes
        for participante in proyecto.participantes:
            # Insertar o actualizar usuario en la tabla `usuarios`
            usuario_params = {
                "nombre": participante.nombre,
                "apellido": participante.apellido,
                "correo": participante.correo,
                "telefono": participante.telefono,
                "tipo": participante.tipo,  # Ejemplo: "tutor" o "ponente"
            }
            db.execute(sql_query_usuarios, usuario_params)

            # Obtener el ID del usuario (nuevo o existente)
            id_usuario = db.execute(text("SELECT LAST_INSERT_ID()")).scalar()

            # Asociar el usuario al proyecto
            db.execute(sql_query_participantes, {
                "id_usuario": id_usuario,
                "id_etapa": participante.id_etapa,
                "id_proyecto": id_proyecto,
                "id_proyecto_convocatoria": proyecto.id_proyecto_convocatoria
            })

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
