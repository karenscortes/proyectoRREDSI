# Crear un usuario
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.models.usuario import Usuario
from appv1.schemas.usuario import UserCreate, UserResponse, UserUpdate
from core.security import get_hashed_password, verify_token
from core.utils import generate_user_id_int
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.usuario import UserResponse

from db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Crear un usuario
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
            "celular": usuario.celular,
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
# Consultar un usuario por su email y validar si está activo
# Consultar un usuario por su email y validar si está activo
def get_user_by_email(db: Session, p_mail: str):
    try:
        sql = text("SELECT * FROM usuarios WHERE correo = :mail")
        result = db.execute(sql, {"mail": p_mail}).fetchone()

        # Validar si el usuario existe
        if not result:
            raise HTTPException(status_code=404, detail="El correo no está registrado, por favor crear cuenta")

        # Validar si el usuario está activo
        if result.estado != 'activo':
            raise HTTPException(status_code=403, detail="Usuario no autorizado")
        
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar usuario por email: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario por email")


# Consultar un usuario por su documento
def get_user_by_documento(db: Session, p_documento: str):
    try:
        sql = text("SELECT * FROM usuarios WHERE documento = :doc")
        result = db.execute(sql, {"doc": p_documento}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar usuario por email: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario por email")

def get_user_by_id(db: Session, user_id: int) -> UserResponse:
    try:
        sql = text("SELECT * FROM usuarios WHERE id_usuario = :user_id")
        result = db.execute(sql, {"user_id": user_id}).fetchone()

        if result is None:
            return None
        
        # Crear el objeto UserResponse basado en el resultado de la consulta
        user_data = {
            "id_usuario": result.id_usuario,
            "id_rol": result.id_rol,
            "id_tipo_documento": result.id_tipo_documento,
            "documento": result.documento,
            "nombres": result.nombres,
            "apellidos": result.apellidos,
            "celular": result.celular,
            "correo": result.correo,
            "estado": result.estado
        }
        return UserResponse(**user_data)

    except SQLAlchemyError as e:
        print(f"Error al buscar usuario por ID: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario por ID")


# Obtener info actual de la persona logueada
def get_institutional_details(db: Session, id_usuario: int):
    try:
        # Segunda consulta para obtener los detalles institucionales
        sql_detalles_institucionales = text("""
            SELECT id_institucion, semillero, grupo_investigacion, 
                id_primera_area_conocimiento, id_segunda_area_conocimiento
            FROM detalles_institucionales
            WHERE id_usuario = :user_id
        """)

        result_detalles = db.execute(sql_detalles_institucionales, {"user_id": id_usuario}).fetchone()

        if result_detalles is None:
            return None

        return result_detalles

    except SQLAlchemyError as e:
        print(f"Error al obtener información del usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener información del usuario")


def update_password(db: Session, correo: str, new_password: str):
    try:
        # Hash el nuevo password
        hashed_password = get_hashed_password(new_password)
        # Actualizar el nuevo password en base de datos
        sql_query = text("UPDATE usuarios SET clave = :clave WHERE correo = :correo")
        params = { "clave": hashed_password, "correo": correo }
        # Ejecutar la consulta de actualización
        db.execute(sql_query, params)
        # Confirmar los cambios
        db.commit()
        return True

    except SQLAlchemyError as e:
        db.rollback()  # Deshacer los cambios si ocurre un error
        print(f"Error al actualizar password: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar password")
    
def update_user(db: Session, id_usuario: int, usuario: UserUpdate):
    try:
        # Crear un diccionario con solo los campos que se proporcionan para la actualización
        update_data = {}
        
        if usuario.id_tipo_documento is not None:
            update_data["id_tipo_documento"] = usuario.id_tipo_documento
        if usuario.nombres is not None:
            update_data["nombres"] = usuario.nombres
        if usuario.apellidos is not None:
            update_data["apellidos"] = usuario.apellidos
        if usuario.celular is not None:
            update_data["celular"] = usuario.celular
        if usuario.correo is not None:
            update_data["correo"] = usuario.correo
        if usuario.clave is not None:  # Actualizar contraseña si se proporciona
            hashed_password = get_hashed_password(usuario.clave) 
            update_data["clave"] = hashed_password

        # Verifica si hay datos para actualizar
        if not update_data:
            raise HTTPException(status_code=400, detail="No se proporcionaron datos para actualizar")

        # Ejecuta la actualización con SQLAlchemy ORM
        db.query(Usuario).filter(Usuario.id_usuario == id_usuario).update(update_data)
        db.commit()

        return True

    except IntegrityError as e:
        db.rollback()
        print(f"Error de integridad de datos al actualizar usuario: {e}")
        raise HTTPException(status_code=400, detail="Error de integridad de datos al actualizar usuario.")

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al actualizar usuario: {e}")
        raise HTTPException(status_code=500, detail="Error interno al actualizar usuario.")


