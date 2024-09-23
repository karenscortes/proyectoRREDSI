from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.autores import AutorCreate
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def create_autor_sql(db: Session, autor: AutorCreate):

    try:
        sql_query = text(
        "INSERT INTO autores (nombre,id_proyecto) VALUES (:nombre,:id_proyecto);"
        )
        params = {
            "nombre": autor.nombre,
            "id_proyecto": autor.id_proyecto,
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear autor: {e}")
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear autor: {e}")
        print("Error ", e)
        raise HTTPException(status_code=500, detail="Error. No hay Integridad de datos")