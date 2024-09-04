from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

def get_proyectos_por_etapa(db: Session):
    try:
        sql = text("SELECT * FROM proyectos JOIN participantes_proyecto ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  JOIN etapas ON participantes_proyecto.id_etapa = etapas.id_etapa WHERE etapas.nombre = 'presencial' AND participantes_proyecto.id_datos_personales = 5")
        # params = {
        #     "nombre_etapa": nombre_etapa
        # }
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por etapa: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos por etapa")

# "SELECT * FROM participantes_proyecto JOIN etapas ON participantes_proyecto.id_etapa = etapas.id_etapa WHERE etapas.nombre = :nombre_etapa"
