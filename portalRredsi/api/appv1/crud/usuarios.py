# Crear un usuario
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.usuario import UserCreate, UserUpdate
from core.security import get_hashed_password
from core.utils import generate_user_id_int
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def create_user_sql(db: Session, usuario: UserCreate):

    try:
        sql_query = text(
        "INSERT INTO usuarios (id_usuario,id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado) VALUES (:id_usuario, :id_rol, :id_tipo_documento, :documento, :nombres, :apellidos, :celular, :correo, :passhash, :estado);"
        )
        params = {
            "id_usuario": generate_user_id_int(),
            "id_rol": usuario.id_rol,
            "id_tipo_documento": usuario.id_tipo_documento,
            "documento": usuario.documento,
            "nombres": usuario.nombres,
            "apellidos": usuario.apellidos,
            "celular": usuario.nombres,
            "correo": usuario.correo,
            "passhash": get_hashed_password(usuario.clave),
            "estado":usuario.estado
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

# Consultar un usuario por su ID
def get_user_by_id(db: Session, user_id: int):
    sql = text("SELECT * FROM usuarios WHERE id_usuario = :user_id")
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
    

def update_user_profile(db: Session, id_usuario: int, usuario: UserUpdate):
    try:
        # Inicia la consulta SQL para actualizar los datos del usuario
        sql = "UPDATE usuarios SET "
        params = {"id_usuario": id_usuario}
        updates = []
        
        # Actualización de la tabla usuarios
        if usuario.id_tipo_documento:
            updates.append("id_tipo_documento = :id_tipo_documento")
            params["id_tipo_documento"] = usuario.id_tipo_documento
        if usuario.nombres:
            updates.append("nombres = :nombres")
            params["nombres"] = usuario.nombres
        if usuario.apellidos:
            updates.append("apellidos = :apellidos")
            params["apellidos"] = usuario.apellidos
        if usuario.celular:
            updates.append("celular = :celular")
            params["celular"] = usuario.celular
        if usuario.correo:
            updates.append("correo = :correo")
            params["correo"] =usuario.correo
        sql += ", ".join(updates) + " WHERE id_usuario = :id_usuario"
        
        sql = text(sql)
        
        db.execute(sql, params)
        db.commit()

        return True
    except IntegrityError as e:
        db.rollback()
        print(f"Error al actualizar usuario: {e}")
        if 'for key' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. El dato ya está registrado.")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad de datos al actualizar usuario.")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al actualizar usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar usuario")
