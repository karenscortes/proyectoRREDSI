from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.proyecto_convocatoria import ProyectoConvocatoriaCreate

# Consultar el ID de la convocatoria que está en curso
def get_convocatoria_en_curso(db: Session):
    try:
        sql = text("SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso' LIMIT 1")
        result = db.execute(sql).fetchone()
        if result:
            return result[0]  # Accedemos al primer elemento de la tupla
        else:
            raise HTTPException(status_code=404, detail="No hay convocatorias en curso.")
    except SQLAlchemyError as e:
        print(f"Error al obtener la convocatoria en curso: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener convocatoria en curso.")


# Crear un proyecto_convocatoria
def create_proyecto_convocatoria(db: Session, proyecto_convocatoria: ProyectoConvocatoriaCreate):
    try:
        # Obtener la convocatoria en curso
        id_convocatoria = get_convocatoria_en_curso(db)

        # Crear la entrada en la tabla proyectos_convocatoria
        sql_query = text(
            "INSERT INTO proyectos_convocatoria (id_proyecto, id_convocatoria) "
            "VALUES (:id_proyecto, :id_convocatoria)"
        )
        params = {
            "id_proyecto": proyecto_convocatoria.id_proyecto,
            "id_convocatoria": id_convocatoria,
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad
        print(f"Error al crear proyecto_convocatoria: {e}")
        if 'Duplicate entry' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. El proyecto ya está registrado en la convocatoria.")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay integridad de datos al crear proyecto_convocatoria.")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al crear proyecto_convocatoria: {e}")
        raise HTTPException(status_code=500, detail="Error al crear proyecto_convocatoria.")
