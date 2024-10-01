from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session

def insert_participante_proyecto(db: Session, id_usuario: int, id_etapa: int, id_proyecto: int, tipo_participante: str, id_proyectos_convocatoria: int):
    try:
        sql_query = text(
            """
            INSERT INTO participantes_proyecto (id_usuario, id_etapa, id_proyecto, tipo_participante, id_proyectos_convocatoria) 
            VALUES (:id_usuario, :id_etapa, :id_proyecto, :tipo_participante, :id_proyectos_convocatoria);
            """
        )

        params = {
            "id_usuario": id_usuario,
            "id_etapa": id_etapa,
            "id_proyecto": id_proyecto,
            "tipo_participante": tipo_participante,
            "id_proyectos_convocatoria": id_proyectos_convocatoria
        }

        db.execute(sql_query, params)
        db.commit()
        return True

    except IntegrityError as e:
        db.rollback()
        if 'Duplicate entry' in str(e.orig):
            raise HTTPException(status_code=400, detail="El participante ya está registrado en el proyecto.")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad al insertar el participante.")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al insertar el participante en el proyecto.")
