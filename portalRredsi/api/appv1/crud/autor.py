from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.autores import AutorCreate

def create_autor_project(db: Session, autor: AutorCreate, id_proyecto: int):
    try:
        sql_query = text(
            """
            INSERT INTO autores (nombre, id_proyecto) 
            VALUES (:nombre, :id_proyecto);
            """
        )

        params = {
            "nombre": autor.nombre,
            "id_proyecto": id_proyecto
        }

        db.execute(sql_query, params)
        db.commit()
        return True

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al crear autor")
