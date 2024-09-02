from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

# Consultar todos los administradores
def get_all_admin(db: Session):
    try:
        sql = text("SELECT * FROM usuarios WHERE id_rol = 3")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar administradores: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar administradores")