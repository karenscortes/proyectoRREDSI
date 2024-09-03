from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

def get_proyectos_por_etapa(db: Session, nombre_etapa: str):
    try:
        sql = text("SELECT * FROM participantes_proyecto JOIN etapas ON participantes_proyecto.id_etapa = etapas.id_etapa WHERE etapas.nombre = :nombre_etapa")
        params = {
            "nombre_etapa": nombre_etapa
        }
        result = db.execute(sql, params).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por etapa: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos por etapa")