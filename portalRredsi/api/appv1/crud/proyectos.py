from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.proyecto import  ProyectoCreate
from appv1.schemas.usuario import UserCreate
from core.security import get_hashed_password
from core.utils import generate_user_id_int

def create_user_tutor_project(db: Session, usuario: UserCreate):

    try:
        sql_query = text(
        "INSERT INTO usuarios (id_usuario,id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, :estado);"
        )
        params = {
            "id_usuario": generate_user_id_int(),
            "id_rol": 4,
            "id_tipo_documento": usuario.id_tipo_documento,
            "documento": usuario.documento,
            "nombres": usuario.nombres,
            "apellidos": usuario.apellidos,
            "celular": usuario.celular,
            "correo": usuario.correo,
            "passhash": get_hashed_password(usuario.clave),
            "estado":"inactivo"
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear usuario: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'for key \'mail\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear usuario")
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear usuario: {e}")
        print("Error ", e)
        raise HTTPException(status_code=500, detail="Error. No hay Integridad de datos")
    
def create_user_ponente_project(db: Session, usuario: UserCreate):

    try:
        sql_query = text(
        "INSERT INTO usuarios (id_usuario,id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, :estado);"
        )
        params = {
            "id_usuario": generate_user_id_int(),
            "id_rol": 5,
            "id_tipo_documento": usuario.id_tipo_documento,
            "documento": usuario.documento,
            "nombres": usuario.nombres,
            "apellidos": usuario.apellidos,
            "celular": usuario.celular,
            "correo": usuario.correo,
            "passhash": get_hashed_password(usuario.clave),
            "estado":"inactivo"
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear usuario: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'for key \'mail\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear usuario")
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear usuario: {e}")
        print("Error ", e)
        raise HTTPException(status_code=500, detail="Error. No hay Integridad de datos")

def create_project_sql(db: Session, proyecto: ProyectoCreate):
    try:
        # Insertar datos en la tabla `proyectos`
        sql_query_proyecto = text(
            """
            INSERT INTO proyectos (
                id_institucion, id_modalidad, id_area_conocimiento, titulo, programa_academico, 
                grupo_investigacion, linea_investigacion, nombre_semillero, url_propuesta_escrita, url_aval
            ) VALUES (
                :id_institucion, :id_modalidad, :id_area_conocimiento, :titulo,  :programa_academico,
                :grupo_investigacion, :linea_investigacion, :nombre_semillero, :url_propuesta_escrita, :url_aval
            );
            """
        )

        # Parámetros para la tabla `proyectos`
        params_proyecto = {
            "id_institucion": proyecto.id_institucion,
            "id_modalidad": proyecto.id_modalidad,
            "id_area_conocimiento": proyecto.id_area_conocimiento,
            "titulo": proyecto.titulo,  # estado inicial del proyecto
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
