from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from appv1.models.rol import Rol
from appv1.models.usuario import Estados, Usuario
from appv1.schemas.usuario import UserCreate
from core.utils import generate_user_id_int
from core.security import get_hashed_password
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

#Obtener todos los delegados en estado activo
def get_delegados_activos_paginated(db: Session, page, page_size):
    try:
        offset = (page - 1) * page_size
        users = db.query(Usuario).filter(
        Usuario.estado == Estados.activo, 
        Usuario.rol.has(Rol.nombre == "Delegado")).order_by(Usuario.nombres.asc()).limit(page_size).offset(offset).all()
        if users is None:
            raise HTTPException(status_code=404, detail="No hay delegados activos")
        
        total_users = db.query(Usuario).filter(Usuario.estado == Estados.activo, 
        Usuario.rol.has(Rol.nombre == "Delegado")).count()

        # Calcular el número total de páginas
        total_pages = (total_users + page_size - 1) // page_size
        return users, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar los delegados activos: {e}")
        raise HTTPException(status_code=500, detail="Error. No hay integridad de datos")

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
        raise HTTPException(status_code=500, detail="Error. No hay integridad de datos")

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
    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear usuario: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID de usuario ya está en uso")
            if 'for key \'mail\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear usuario")
    except SQLAlchemyError as e:
        print(f"Error al crear el usuario: {e}")
        raise HTTPException(status_code=500, detail="Error. No hay integridad de datos")


