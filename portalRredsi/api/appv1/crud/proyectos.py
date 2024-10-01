from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy import text
from core.utils import generate_project_id


def insert_full_project(db: Session, project_data, tutor_data, ponente_data, ponente_opcional_data=None):
    """
    Función para insertar un proyecto completo con tutor, ponente, autores y asociación a una convocatoria.
    """
    try:
        # Comienza la transacción
        db.begin()

        # 1. Insertar el proyecto y generar un ID único
        project_id = generate_project_id()
        sql_proyecto = text("""
            INSERT INTO proyectos (id_proyecto, id_institucion, id_modalidad, id_area_conocimiento, titulo, estado_asignacion, estado_calificacion, programa_academico, grupo_investigacion, linea_investigacion, url_propuesta_escrita, url_aval) 
            VALUES (:id_proyecto, :id_institucion, :id_modalidad, :id_area_conocimiento, :titulo, 'pendiente', 'P_virtual', :programa_academico, :grupo_investigacion, :linea_investigacion, :url_propuesta_escrita, :url_aval)
        """)

        db.execute(sql_proyecto, {
            "id_proyecto": project_id,
            "id_institucion": project_data.id_institucion,
            "id_modalidad": project_data.id_modalidad,
            "id_area_conocimiento": project_data.id_area_conocimiento,
            "titulo": project_data.titulo,
            "programa_academico": project_data.programa_academico,
            "grupo_investigacion": project_data.grupo_investigacion,
            "linea_investigacion": project_data.linea_investigacion,
            "url_propuesta_escrita": project_data.url_propuesta_escrita,
            "url_aval": project_data.url_aval
        })

        # 2. Insertar tutor
        tutor_id = insert_user(db, tutor_data, rol=4)

        # 3. Insertar ponente
        ponente_id = insert_user(db, ponente_data, rol=5)

        # 4. Insertar ponente opcional si existe
        if ponente_opcional_data:
            ponente_opcional_id = insert_user(db, ponente_opcional_data, rol=5)

        # 5. Obtener la convocatoria en curso
        convocatoria = db.execute(text("SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso' LIMIT 1")).fetchone()
        if not convocatoria:
            raise HTTPException(status_code=404, detail="No se encontró una convocatoria en curso")

        # 6. Insertar proyecto en la convocatoria
        db.execute(text("INSERT INTO proyectos_convocatoria (id_proyecto, id_convocatoria) VALUES (:id_proyecto, :id_convocatoria)"), {
            "id_proyecto": project_id,
            "id_convocatoria": convocatoria["id_convocatoria"]
        })

        # 7. Obtener la etapa virtual
        etapa = db.execute(text("SELECT id_etapa FROM etapas WHERE nombre = 'Virtual' LIMIT 1")).fetchone()
        if not etapa:
            raise HTTPException(status_code=404, detail="No se encontró la etapa virtual")

        # 8. Insertar participantes en la tabla de participantes_proyecto
        insert_participante_proyecto(db, tutor_id, etapa["id_etapa"], project_id, convocatoria["id_convocatoria"], "tutor")
        insert_participante_proyecto(db, ponente_id, etapa["id_etapa"], project_id, convocatoria["id_convocatoria"], "ponente")

        # Insertar ponente opcional si está presente
        if ponente_opcional_data:
            insert_participante_proyecto(db, ponente_opcional_id, etapa["id_etapa"], project_id, convocatoria["id_convocatoria"], "ponente")

        # Confirmar la transacción
        db.commit()

        return {"id_proyecto": project_id}

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad: " + str(e))
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error en la base de datos: " + str(e))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def insert_user(db: Session, user_data, rol: int):
    """
    Inserta un usuario en la tabla usuarios.
    """
    sql_user = text("""
        INSERT INTO usuarios (id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado)
        VALUES (:id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, 'hashed_password', 'inactivo')
    """)
    db.execute(sql_user, {
        "id_rol": rol,
        "id_tipo_documento": user_data.id_tipo_documento,
        "documento": user_data.documento,
        "nombres": user_data.nombres,
        "apellidos": user_data.apellidos,
        "celular": user_data.celular,
        "correo": user_data.correo
    })

    user_id = db.execute(text("SELECT LAST_INSERT_ID()")).fetchone()[0]
    return user_id


def insert_participante_proyecto(db: Session, user_id: int, etapa_id: int, project_id: int, convocatoria_id: int, rol: str):
    """
    Inserta un participante (tutor/ponente) en la tabla participantes_proyecto.
    """
    sql_participante = text("""
        INSERT INTO participantes_proyecto (id_usuario, id_etapa, id_proyecto, id_proyectos_convocatoria, rol) 
        VALUES (:id_usuario, :id_etapa, :id_proyecto, :id_proyectos_convocatoria, :rol)
    """)
    db.execute(sql_participante, {
        "id_usuario": user_id,
        "id_etapa": etapa_id,
        "id_proyecto": project_id,
        "id_proyectos_convocatoria": convocatoria_id,
        "rol": rol
    })
