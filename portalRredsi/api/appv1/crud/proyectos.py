from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from appv1.schemas.proyecto import ParticipanteCreate, ProyectoCreate
from core.utils import generate_Contraseña, generate_project_id, generate_user_id_int

def create_full_project(db: Session, proyecto: ProyectoCreate, tutor: ParticipanteCreate, ponente1: ParticipanteCreate, ponente2: Optional[ParticipanteCreate] = None):
    try:
        # **Paso 1: Inserción del proyecto**
        project_id = generate_project_id()

        project_sql = text(
            "INSERT INTO proyectos (id_proyecto, id_institucion, id_modalidad, id_area_conocimiento, titulo, "
            "estado_asignacion, estado_calificacion, programa_academico, grupo_investigacion, linea_investigacion, "
            "nombre_semillero, url_propuesta_escrita, url_aval) "
            "VALUES (:id_proyecto, :id_institucion, :id_modalidad, :id_area_conocimiento, :titulo, "
            "'pendiente', 'P_virtual', :programa_academico, :grupo_investigacion, :linea_investigacion, "
            ":nombre_semillero, :url_propuesta_escrita, :url_aval)"
        )

        project_params = {
            "id_proyecto": project_id,
            "id_institucion": proyecto.id_institucion,
            "id_modalidad": proyecto.id_modalidad,
            "id_area_conocimiento": proyecto.id_area_conocimiento,
            "titulo": proyecto.titulo,
            "programa_academico": proyecto.programa_academico,
            "grupo_investigacion": proyecto.grupo_investigacion,
            "linea_investigacion": proyecto.linea_investigacion,
            "nombre_semillero": proyecto.nombre_semillero,
            "url_propuesta_escrita": proyecto.url_propuesta_escrita,
            "url_aval": proyecto.url_aval,
        }

        db.execute(project_sql, project_params)

        # **Paso 2: Obtener la convocatoria en curso**
        convocatoria_sql = text(
            "SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso' LIMIT 1"
        )
        convocatoria = db.execute(convocatoria_sql).fetchone()

        if not convocatoria:
            raise HTTPException(status_code=404, detail="No hay convocatoria en curso")
        
        convocatoria_id = convocatoria[0]

        # **Paso 3: Insertar en proyectos_convocatoria**
        proyecto_convocatoria_sql = text(
            "INSERT INTO proyectos_convocatoria (id_proyecto, id_convocatoria) VALUES (:id_proyecto, :id_convocatoria)"
        )
        db.execute(proyecto_convocatoria_sql, {"id_proyecto": project_id, "id_convocatoria": convocatoria_id})

        proyecto_convocatoria_id = db.execute(text("SELECT LAST_INSERT_ID()")).fetchone()[0]

        # **Paso 4: Inserción del tutor**
        try:
            tutor_id = generate_user_id_int()

            tutor_sql = text(
                "INSERT INTO usuarios (id_usuario, id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) "
                "VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, 'inactivo')"
            )

            tutor_params = {
                "id_usuario": tutor_id,
                "id_rol": 4,  # Rol de tutor
                "id_tipo_documento": tutor.id_tipo_documento,
                "documento": tutor.documento,
                "nombres": tutor.nombres,
                "apellidos": tutor.apellidos,
                "celular": tutor.celular,
                "correo": tutor.correo,
                "passhash": generate_Contraseña(),
            }

            db.execute(tutor_sql, tutor_params)
        except IntegrityError as e:
            db.rollback()  # Rollback en caso de error de tutor
            if 'correo' in str(e.orig):
                raise HTTPException(status_code=400, detail="El correo del tutor ya está registrado.")
            elif 'documento' in str(e.orig):
                raise HTTPException(status_code=400, detail="El documento del tutor ya está registrado.")
            elif 'celular' in str(e.orig):
                raise HTTPException(status_code=400, detail="El número de celular del tutor ya está registrado.")
            else:
                raise HTTPException(status_code=400, detail=f"Error de integridad del tutor: {str(e)}")

        # **Paso 5: Inserción del primer ponente**
        try:
            ponente1_id = generate_user_id_int()

            ponente1_sql = text(
                "INSERT INTO usuarios (id_usuario, id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) "
                "VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, 'inactivo')"
            )

            ponente1_params = {
                "id_usuario": ponente1_id,
                "id_rol": 5,  # Rol de ponente
                "id_tipo_documento": ponente1.id_tipo_documento,
                "documento": ponente1.documento,
                "nombres": ponente1.nombres,
                "apellidos": ponente1.apellidos,
                "celular": ponente1.celular,
                "correo": ponente1.correo,
                "passhash": generate_Contraseña(),
            }

            db.execute(ponente1_sql, ponente1_params)
        except IntegrityError as e:
            db.rollback()  # Rollback en caso de error de ponente1
            if 'correo' in str(e.orig):
                raise HTTPException(status_code=400, detail="El correo del primer ponente ya está registrado.")
            elif 'documento' in str(e.orig):
                raise HTTPException(status_code=400, detail="El documento del primer ponente ya está registrado.")
            elif 'celular' in str(e.orig):
                raise HTTPException(status_code=400, detail="El número de celular del primer ponente ya está registrado.")
            else:
                raise HTTPException(status_code=400, detail=f"Error de integridad del primer ponente: {str(e)}")

        # **Paso 6: Inserción del segundo ponente (si existe)**
        if ponente2:
            try:
                ponente2_id = generate_user_id_int()

                ponente2_sql = text(
                    "INSERT INTO usuarios (id_usuario, id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) "
                    "VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, 'inactivo')"
                )

                ponente2_params = {
                    "id_usuario": ponente2_id,
                    "id_rol": 5,  # Rol de ponente
                    "id_tipo_documento": ponente2.id_tipo_documento,
                    "documento": ponente2.documento,
                    "nombres": ponente2.nombres,
                    "apellidos": ponente2.apellidos,
                    "celular": ponente2.celular,
                    "correo": ponente2.correo,
                    "passhash": generate_Contraseña(),
                }

                db.execute(ponente2_sql, ponente2_params)
            except IntegrityError as e:
                db.rollback()  # Rollback en caso de error de ponente2
                if 'correo' in str(e.orig):
                    raise HTTPException(status_code=400, detail="El correo del segundo ponente ya está registrado.")
                elif 'documento' in str(e.orig):
                    raise HTTPException(status_code=400, detail="El documento del segundo ponente ya está registrado.")
                elif 'celular' in str(e.orig):
                    raise HTTPException(status_code=400, detail="El número de celular del segundo ponente ya está registrado.")
                else:
                    raise HTTPException(status_code=400, detail=f"Error de integridad del segundo ponente: {str(e)}")

        # **Paso 7: Insertar participantes_proyecto**
        etapa_virtual_sql = text(
            "SELECT id_etapa FROM etapas WHERE nombre = 'virtual' LIMIT 1"
        )
        etapa_virtual = db.execute(etapa_virtual_sql).fetchone()
        if not etapa_virtual:
            raise HTTPException(status_code=404, detail="No se encontró la etapa 'virtual'")

        etapa_virtual_id = etapa_virtual[0]

        # Insertar tutor en participantes_proyecto
        insert_participante_proyecto(db, tutor_id, etapa_virtual_id, project_id, proyecto_convocatoria_id, "tutor")

        # Insertar primer ponente en participantes_proyecto
        insert_participante_proyecto(db, ponente1_id, etapa_virtual_id, project_id, proyecto_convocatoria_id, "ponente")

        # Insertar segundo ponente en participantes_proyecto (si existe)
        if ponente2:
            insert_participante_proyecto(db, ponente2_id, etapa_virtual_id, project_id, proyecto_convocatoria_id, "ponente")

        # **Paso 8: Inserción de autores uno por uno**
        for autor in proyecto.autores:
            try:
                # Cada autor se inserta como un registro separado
                autor_sql = text("INSERT INTO autores (nombre, id_proyecto) VALUES (:nombre, :id_proyecto)")
                db.execute(autor_sql, {"nombre": autor.nombre, "id_proyecto": project_id})  # Se inserta cada autor con su nombre y el id del proyecto
            except IntegrityError as e:
                db.rollback()  # En caso de error, hacer rollback
                raise HTTPException(status_code=400, detail=f"Error al insertar el autor {autor.nombre}: {str(e)}")

        # Retornar solo el ID del proyecto
        return {"project_id": project_id}

    except SQLAlchemyError as e:
        db.rollback()  # Rollback en caso de error general
        raise HTTPException(status_code=500, detail="Error en la base de datos")


def insert_participante_proyecto(db: Session, user_id: int, etapa_id: int, project_id: int, proyecto_convocatoria_id: int, tipo_usuario: str):
    participante_proyecto_sql = text(
        "INSERT INTO participantes_proyecto (id_usuario, id_etapa, id_proyecto, id_proyectos_convocatoria, tipo_usuario) "
        "VALUES (:id_usuario, :id_etapa, :id_proyecto, :id_proyectos_convocatoria, :tipo_usuario)"
    )
    db.execute(participante_proyecto_sql, {
        "id_usuario": user_id,
        "id_etapa": etapa_id,
        "id_proyecto": project_id,
        "id_proyectos_convocatoria": proyecto_convocatoria_id,
        "tipo_usuario": tipo_usuario
    })
