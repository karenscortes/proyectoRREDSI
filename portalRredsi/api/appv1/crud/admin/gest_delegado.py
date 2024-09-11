from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from appv1.models.rol import Rol
from appv1.models.usuario import Estados, Usuario
from appv1.schemas.usuario import UserCreate
from core.utils import generate_user_id_int
from core.security import get_hashed_password

#Obtener todos los delegados en estado activo
def get_delegados_activos(db: Session):
    try:
        result = db.query(Usuario).filter(
        Usuario.estado == Estados.activo, Usuario.rol.has(Rol.nombre == "Delegado")).all()
        if result is None:
            raise HTTPException(status_code=404, detail="No hay delegados activos")
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar los delegados activos: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar delegados activos")


#Obtener delegado por numero de documento
def get_delegados_by_document(doc: str, db: Session,):
    try:
        result = db.query(Usuario).filter(
        Usuario.documento == doc, Usuario.rol.has(Rol.nombre == "Delegado")).first()
        if result is None:
            raise HTTPException(status_code=404, detail="No se encontro el delegado")    
        return result    
    except SQLAlchemyError as e:
        print(f"Error al buscar los delegados: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar el delegado")


#Crear delegado
def create_delegado(user: UserCreate, db: Session):
    try:
        nuevo_usuario = Usuario(
            id_usuario = generate_user_id_int(),
            id_rol = user.id_rol, 
            id_tipo_documento = user.id_tipo_documento,
            documento = user.documento, 
            nombres = user.nombres, 
            apellidos = user.apellidos, 
            celular = user.celular, 
            correo = user.correo, 
            clave = get_hashed_password(user.clave)
        )
        db.add(nuevo_usuario)
        db.commit()
        return True
    except SQLAlchemyError as e:
        print(f"Error al buscar los delegados: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar los delegados")


