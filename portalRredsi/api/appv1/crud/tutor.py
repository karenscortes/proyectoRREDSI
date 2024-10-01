from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.tutor import UserTutorCreate
from core.utils import generate_user_id_int, generate_Contraseña

def create_user_tutor_project(db: Session, tutor: UserTutorCreate):
    try:
        sql_query = text(
            """
            INSERT INTO usuarios (id_usuario, id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) 
            VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, :estado);
            """
        )

        params = {
            "id_usuario": generate_user_id_int(),
            "id_rol": 4,  # Rol de tutor
            "id_tipo_documento": tutor.id_tipo_documento,
            "documento": tutor.documento,
            "nombres": tutor.nombres,
            "apellidos": tutor.apellidos,
            "celular": tutor.celular,
            "correo": tutor.correo,
            "passhash": generate_Contraseña(),
            "estado": "inactivo"
        }

        db.execute(sql_query, params)
        db.commit()
        return True

    except IntegrityError as e:
        db.rollback()
        if 'Duplicate entry' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad al crear el tutor")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error interno del servidor al crear el tutor")
