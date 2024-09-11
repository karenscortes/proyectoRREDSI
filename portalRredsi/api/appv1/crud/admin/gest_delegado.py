# Crear un usuario
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
      
from sqlalchemy import text

from appv1.models.rol import Rol
from appv1.models.usuario import Estados, Usuario


def get_delegados_activos(db: Session):
    try:
        result = db.query(Usuario).filter(
        Usuario.estado == Estados.activo,
        Usuario.rol.has(Rol.nombre == "Delegado") 
).all()
        return  result
    except SQLAlchemyError as e:
        print(f"Error al buscar los delegados: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar los delegados")


