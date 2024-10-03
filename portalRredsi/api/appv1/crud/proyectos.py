from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException

from core.utils import generate_Contraseña, generate_project_id, generate_user_id_int

def check_existing_user(db: Session, celular: str, correo: str):
    """ Verifica si ya existe un usuario con el mismo celular o correo """
    existing_user = db.execute(text("""
        SELECT id_usuario FROM usuarios WHERE celular = :celular OR correo = :correo
    """), {"celular": celular, "correo": correo}).fetchone()
    return existing_user is not None

def insert_user(db: Session, user_data, rol: int):
    """ Inserta un usuario en la tabla usuarios y maneja la duplicidad. """
    
    if check_existing_user(db, user_data['celular'], user_data['correo']):
        raise HTTPException(status_code=400, detail="El celular o correo ya está registrado")
    
    user_id = generate_user_id_int()  # Generar un ID único para el usuario
    password = generate_Contraseña()  # Generar una contraseña segura

    sql_user = text("""
        INSERT INTO usuarios (id_usuario, id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) 
        VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :clave, :estado)
    """)
    
    db.execute(sql_user, {
        "id_usuario": user_id,
        "id_rol": rol,
        "id_tipo_documento": user_data['id_tipo_documento'],
        "documento": user_data['documento'],
        "nombres": user_data['nombres'],
        "apellidos": user_data['apellidos'],
        "celular": user_data['celular'],
        "correo": user_data['correo'],
        "clave": password,
        "estado": "inactivo"
    })
    db.commit()
    return user_id

def insert_autor(db: Session, autor_data, project_id: int):
    """ Inserta un autor en la tabla autores, vinculado al proyecto. """
    sql_autor = text("""
        INSERT INTO autores (nombre, id_proyecto) 
        VALUES (:nombre, :id_proyecto)
    """)
    db.execute(sql_autor, {
        "nombre": autor_data.nombre,
        "id_proyecto": project_id
    })

def insert_full_project(db: Session, project_data, tutor_data, ponente_data, autores_data, ponente_opcional_data=None):
    """ Inserta un proyecto completo con tutor, ponente, ponente opcional, autores y asociación a una convocatoria. """
    try:
        db.begin()  # Iniciar la transacción

        # 1. Insertar el proyecto
        project_id = generate_project_id()  # Generar un ID único para el proyecto
        sql_proyecto = text("""
            INSERT INTO proyectos (id_proyecto, id_institucion, id_modalidad, id_area_conocimiento, titulo, estado_asignacion, programa_academico, grupo_investigacion, linea_investigacion, nombre_semillero, url_propuesta_escrita, url_aval) 
            VALUES (:id_proyecto, :id_institucion, :id_modalidad, :id_area_conocimiento, :titulo, 'pendiente', :programa_academico, :grupo_investigacion, :linea_investigacion, :nombre_semillero, :url_propuesta_escrita, :url_aval)
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
            "nombre_semillero": project_data.nombre_semillero,
            "url_propuesta_escrita": project_data.url_propuesta_escrita,
            "url_aval": project_data.url_aval
        })

        # 2. Insertar tutor
        tutor_id = insert_user(db, tutor_data, rol=4)

        # 3. Insertar ponente principal
        ponente_id = insert_user(db, ponente_data, rol=5)

        # 4. Insertar ponente opcional si existe
        ponente_opcional_id = None
        if ponente_opcional_data:
            ponente_opcional_id = insert_user(db, ponente_opcional_data, rol=5)

        # 5. Insertar autores
        for autor in autores_data:
            insert_autor(db, autor, project_id)

        # 6. Obtener convocatoria activa
        convocatoria = db.execute(text("SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso' LIMIT 1")).fetchone()
        if not convocatoria:
            raise HTTPException(status_code=404, detail="No se encontró una convocatoria en curso")

        # 7. Insertar el proyecto en la convocatoria
        db.execute(text("INSERT INTO proyectos_convocatoria (id_proyecto, id_convocatoria) VALUES (:id_proyecto, :id_convocatoria)"), {
            "id_proyecto": project_id,
            "id_convocatoria": convocatoria.id_convocatoria
        })

        # 8. Obtener la etapa "Virtual"
        etapa = db.execute(text("SELECT id_etapa FROM etapas WHERE nombre = 'Virtual' LIMIT 1")).fetchone()
        if not etapa:
            raise HTTPException(status_code=404, detail="No se encontró la etapa 'Virtual'")

        # 9. Insertar participantes en la tabla de participantes_proyecto
        insert_participante_proyecto(db, tutor_id, etapa.id_etapa, project_id, convocatoria.id_convocatoria, "tutor")
        insert_participante_proyecto(db, ponente_id, etapa.id_etapa, project_id, convocatoria.id_convocatoria, "ponente")

        # Insertar ponente opcional si existe
        if ponente_opcional_id:
            insert_participante_proyecto(db, ponente_opcional_id, etapa.id_etapa, project_id, convocatoria.id_convocatoria, "ponente")

        db.commit()  # Confirmar la transacción

        return {"id_proyecto": project_id}

    except Exception as e:
        db.rollback()  # Realiza rollback si ocurre algún error
        raise HTTPException(status_code=500, detail=str(e))

def insert_participante_proyecto(db: Session, user_id: int, etapa_id: int, project_id: int, convocatoria_id: int, rol: str):
    """ Inserta un participante (tutor o ponente) en la tabla participantes_proyecto. """
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
