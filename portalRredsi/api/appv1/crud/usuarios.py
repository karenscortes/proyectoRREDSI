# Crear un usuario
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.usuario import UserCreate
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
    
    
def update_user_profile(db: Session, user_id: int, usuario: UserUpdate):
    try:
        # Inicia la consulta SQL para actualizar los datos del usuario
        sql = "UPDATE usuarios SET "
        params = {"user_id": user_id}
        updates = []
        
        # Actualización de la tabla usuarios
        if 'nombres' in user_data:
            updates.append("nombres = :nombres")
            params["nombres"] = user_data['nombres']
        if 'apellidos' in user_data:
            updates.append("apellidos = :apellidos")
            params["apellidos"] = user_data['apellidos']
        if 'correo' in user_data:
            updates.append("correo = :correo")
            params["correo"] = user_data['correo']
        if 'clave' in user_data:
            updates.append("clave = :clave")
            params["clave"] = user_data['clave']

        # Genera las partes de la consulta SQL
        if updates:
            sql += ", ".join(updates) + " WHERE id_usuario = :user_id"
            sql = text(sql)
            db.execute(sql, params)

        # Actualización de detalles institucionales
        if 'institucion' in user_data or 'grupo_investigacion' in user_data or 'semillero' in user_data:
            sql_institucional = "UPDATE detalles_institucionales SET "
            params_institucional = {"user_id": user_id}
            updates_institucional = []

            if 'institucion' in user_data:
                updates_institucional.append("id_institucion = :id_institucion")
                params_institucional["id_institucion"] = user_data['institucion']
            if 'grupo_investigacion' in user_data:
                updates_institucional.append("grupo_investigacion = :grupo_investigacion")
                params_institucional["grupo_investigacion"] = user_data['grupo_investigacion']
            if 'semillero' in user_data:
                updates_institucional.append("semillero = :semillero")
                params_institucional["semillero"] = user_data['semillero']

            if updates_institucional:
                sql_institucional += ", ".join(updates_institucional) + " WHERE id_usuario = :user_id"
                sql_institucional = text(sql_institucional)
                db.execute(sql_institucional, params_institucional)

        # Actualización de títulos académicos
        if 'titulos_academicos' in user_data:
            for titulo in user_data['titulos_academicos']:
                sql_titulo = """
                INSERT INTO titulos_academicos (nivel, nombre_titulo, url_titulo, id_usuario)
                VALUES (:nivel, :nombre_titulo, :url_titulo, :user_id)
                ON DUPLICATE KEY UPDATE nombre_titulo = VALUES(nombre_titulo), url_titulo = VALUES(url_titulo)
                """
                params_titulo = {
                    "nivel": titulo['nivel'],
                    "nombre_titulo": titulo['nombre_titulo'],
                    "url_titulo": titulo['url_titulo'],
                    "user_id": user_id
                }
                db.execute(text(sql_titulo), params_titulo)

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