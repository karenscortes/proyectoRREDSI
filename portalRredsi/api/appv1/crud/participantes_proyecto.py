from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.participantes_proyecto import  participanteProyectoCreate

def create_participantes_proyecto(db: Session, participante_proyecto: participanteProyectoCreate):

    try:
        sql_query = text(
        "INSERT INTO participantes_proyecto(id_usuario,id_etapa, id_proyecto, id_proyectos_convocatoria) VALUES (:id_usuario,:id_etapa, :id_proyecto, :id_proyectos_convocatoria);"
        )
        params = {

            "id_usuario": participante_proyecto.id_usuario,
            "id_etapa": 2,
            "id_proyecto": participante_proyecto.id_proyecto,
            "id_proyectos_convocatoria": participante_proyecto.id_proyectos_convocatoria,
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear Participante Proyecto: {e}")
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear Participante Proyecto: {e}")
        print("Error ", e)
        raise HTTPException(status_code=500, detail="Error. No hay Integridad de datos")