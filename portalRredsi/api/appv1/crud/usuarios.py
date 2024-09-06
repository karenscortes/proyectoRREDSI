# Crear un usuario
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.usuario import UserCreate
from core.security import get_hashed_password
from core.utils import generate_user_id, generate_user_id_int
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def create_user_sql(db: Session, usuario: UserCreate):

    try:
        sql_query = text(
        "INSERT INTO usuarios (id_usuario,id_rol, correo, clave, estado) VALUES (:user_id, :rol, :mail, :passhash, :status);"
        )
        params = {
            "user_id": generate_user_id_int(),
            "rol": usuario.id_rol,
            "mail": usuario.correo,
            "passhash": get_hashed_password(usuario.clave),
            "status":'activo'
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
        sql = text("SELECT * FROM usuarios WHERE mail = :mail")
        result = db.execute(sql, {"mail": p_mail}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar usuario por email: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario por email")

# Consultar un usuario por su ID
def get_user_by_id(db: Session, user_id: str):
    sql = text("SELECT * FROM users WHERE user_id = :user_id")
    result = db.execute(sql, {"user_id": user_id}).fetchone()
    return result

def update_password(db: Session, email: str, new_password: str):
    try:
        # Hash el nuevo password
        hashed_password = get_hashed_password(new_password)
        # Actualizar el nuevo password en base de datos
        sql_query = text("UPDATE users SET passhash = :passhash WHERE mail = :mail")
        params = { "passhash": hashed_password, "mail": email }
        # Ejecutar la consulta de actualización
        db.execute(sql_query, params)
        # Confirmar los cambios
        db.commit()
        return True

    except SQLAlchemyError as e:
        db.rollback()  # Deshacer los cambios si ocurre un error
        print(f"Error al actualizar password: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar password")