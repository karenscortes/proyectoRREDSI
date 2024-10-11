from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_all_institucionEducativa(db: Session):
    try:
        sql = text("SELECT * FROM instituciones ")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar areas de conocimiento: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar las instituciones")