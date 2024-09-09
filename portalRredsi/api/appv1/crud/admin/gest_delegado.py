# Crear un usuario
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
      
from sqlalchemy import text

from appv1.models.usuario import Usuario


def get_delegados_activos(db: Session):
    try:
        return  db.query(Usuario).all()  
    except SQLAlchemyError as e:
        print(f"Error al buscar los delegados: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar los delegados")


