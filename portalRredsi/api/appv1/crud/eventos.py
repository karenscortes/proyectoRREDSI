
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from requests import Session
from sqlalchemy import text


def get_eventos_activos(db: Session):
    try:
        sql = text("SELECT * FROM eventos WHERE estado = 'activo'")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar eventos activos: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar eventos activos")