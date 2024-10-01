from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.proyecto_convocatoria import ProyectoConvocatoriaCreate

def get_convocatoria_en_curso(db: Session):
    try:
        sql = text("SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso' LIMIT 1")
        result = db.execute(sql).fetchone()
        if result:
            return result[0]
        else:
            raise HTTPException(status_code=404, detail="No hay convocatorias en curso.")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener la convocatoria en curso.")

def create_proyecto_convocatoria(db: Session, proyecto_convocatoria: ProyectoConvocatoriaCreate):
    try:
        id_convocatoria = get_convocatoria_en_curso(db)

        sql_query = text(
            """
            INSERT INTO proyectos_convocatoria (id_proyecto, id_convocatoria) 
            VALUES (:id_proyecto, :id_convocatoria);
            """
        )

        params = {
            "id_proyecto": proyecto_convocatoria.id_proyecto,
            "id_convocatoria": id_convocatoria
        }

        db.execute(sql_query, params)
        db.commit()
        return True

    except IntegrityError as e:
        db.rollback()
        if 'Duplicate entry' in str(e.orig):
            raise HTTPException(status_code=400, detail="El proyecto ya está registrado en la convocatoria.")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad al asociar el proyecto a la convocatoria.")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al asociar el proyecto a la convocatoria.")
