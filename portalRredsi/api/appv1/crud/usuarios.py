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
    
    
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy import text

def update_user(db: Session, user_id: int, usuario: UserUpdate):
    try:
        sql = "UPDATE usuarios SET "
        params = {"id_usuario": user_id}
        updates = []
        
        if usuario.nombres:
            updates.append("nombres = :nombres")
            params["nombres"] = usuario.nombres
        if usuario.apellidos:
            updates.append("apellidos = :apellidos")
            params["apellidos"] = usuario.apellidos
        if usuario.tipo_documento:
            updates.append("id_tipo_documento = :tipo_documento")
            params["tipo_documento"] = usuario.tipo_documento
        if usuario.documento:
            updates.append("documento = :documento")
            params["documento"] = usuario.documento
        if usuario.correo:
            updates.append("correo = :correo")
            params["correo"] = usuario.correo
        if usuario.clave:
            updates.append("clave = :clave")
            params["clave"] = usuario.clave
        if usuario.id_institucion:
            updates.append("id_institucion = :id_institucion")
            params["id_institucion"] = usuario.id_institucion
        if usuario.grupo_investigacion:
            updates.append("grupo_investigacion = :grupo_investigacion")
            params["grupo_investigacion"] = usuario.grupo_investigacion
        if usuario.nombre_semillero:
            updates.append("nombre_semillero = :nombre_semillero")
            params["nombre_semillero"] = usuario.nombre_semillero
        if usuario.titulo_pregrado:
            updates.append("titulo_pregrado = :titulo_pregrado")
            params["titulo_pregrado"] = usuario.titulo_pregrado
        if usuario.titulo_especializacion:
            updates.append("titulo_especializacion = :titulo_especializacion")
            params["titulo_especializacion"] = usuario.titulo_especializacion
        if usuario.titulo_maestria:
            updates.append("titulo_maestria = :titulo_maestria")
            params["titulo_maestria"] = usuario.titulo_maestria
        if usuario.titulo_doctorado:
            updates.append("titulo_doctorado = :titulo_doctorado")
            params["titulo_doctorado"] = usuario.titulo_doctorado
        if usuario.id_area_conocimiento:
            updates.append("id_primera_area_conocimiento = :id_area_conocimiento")
            params["id_area_conocimiento"] = usuario.id_area_conocimiento
        if usuario.otra_area_conocimiento:
            updates.append("id_segunda_area_conocimiento = :otra_area_conocimiento")
            params["otra_area_conocimiento"] = usuario.otra_area_conocimiento
        
        sql += ", ".join(updates) + " WHERE id_usuario = :id_usuario"
        
        sql = text(sql)
        
        db.execute(sql, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()
        if 'for key' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. Integridad de datos violada")
        else:
            raise HTTPException(status_code=400, detail="Error. Conflicto de datos al actualizar usuario")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error interno del servidor al actualizar usuario")
