# Crear un usuario
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.models.usuario import Usuario
from appv1.schemas.UsuarioEvaluador import EvaluadorCreate
from core.security import get_hashed_password, verify_token
from core.utils import generate_user_id_int
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.usuario import UserResponse

from db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Crear un usuario
def create_evaluador_sql(db: Session, evaluador: EvaluadorCreate):

    try:
        sql_query = text(
        "INSERT INTO usuarios (id_usuario,id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, :estado);"
        )
        params = {
            "id_usuario": generate_user_id_int(),
            "id_rol":1,
            "id_tipo_documento": evaluador.id_tipo_documento,
            "documento": evaluador.documento,
            "nombres": evaluador.nombres,
            "apellidos": evaluador.apellidos,
            "celular": evaluador.celular,
            "correo": evaluador.correo,
            "passhash": get_hashed_password(evaluador.clave),
            "estado":"activo"
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear usuario: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID de usuario ya está en uso")
            if 'for key \'mail\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear usuario")
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear usuario: {e}")
        print("Error ", e)
        raise HTTPException(status_code=500, detail="Error. No hay Integridad de datos")
    
    
# Consultar un usuario por su email
def get_user_by_email(db: Session, p_mail: str):
    try:
        sql = text("SELECT * FROM usuarios WHERE correo = :mail")
        result = db.execute(sql, {"mail": p_mail}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar usuario por email: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario por email")