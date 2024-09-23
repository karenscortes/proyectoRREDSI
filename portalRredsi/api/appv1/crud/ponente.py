from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.ponente import UserPonenteCreate
from core.utils import generate_Contraseña, generate_user_id_int

def create_user_ponente_project(db: Session, ponente: UserPonenteCreate):

    try:
        sql_query = text(
        "INSERT INTO usuarios (id_usuario,id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, :estado);"
        )
        params = {
            "id_usuario": generate_user_id_int(),
            "id_rol": 5,
            "id_tipo_documento": ponente.id_tipo_documento,
            "documento": ponente.documento,
            "nombres": ponente.nombres,
            "apellidos": ponente.apellidos,
            "celular": ponente.celular,
            "correo": ponente.correo,
            "passhash":generate_Contraseña(),
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