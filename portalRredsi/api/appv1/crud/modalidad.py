from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
def get_all_modalidades(db: Session):
    try:
        sql = text("SELECT * FROM modalidades ")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar tipo de modalidad: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar tipo de modalidad")