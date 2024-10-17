from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel

from appv1.schemas.usuario import UserResponse

# Asumiendo que tienes el esquema UserResponse
def get_user_by_documento(db: Session, documento: str):
    try:
        sql = text("SELECT * FROM usuarios WHERE documento = :documento")
        result = db.execute(sql, {"documento": documento}).fetchone()
        
        if result is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Aquí puedes mapear el resultado a un esquema Pydantic como UserResponse si es necesario
        return UserResponse(**dict(result))
    
    except SQLAlchemyError as e:
        print(f"Error al buscar usuario por número de documento: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario")
