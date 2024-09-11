from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.delegado.asignacionProyectoEtapaVirtual import AsignarProyectoEtapaUno


def asignar_proyecto_etapa_virtual(db: Session, asignacion: AsignarProyectoEtapaUno ):
    try:
        sql = text("""INSERT INTO participantes_proyecto (id_usuario, id_proyecto, id_etapa, id_proyecto_convocatoria) 
                        VALUES (:id_us, :id_p, :id_etp, :id_pc)""")
        
        params={
            "id_us": asignacion.id_usuario,
            "id_p": asignacion.id_proyecto,
            "id_etp": asignacion.id_etapa,
            "id_pc": asignacion.id_proyecto_convocatoria,
        }
        result = db.execute(sql,params)
        db.commit()
        return result
    
    except IntegrityError as e:
        db.rollback()
        print(f"Error al asignar proyecto: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El evaluador ya esta asignado ya esta asignado a este proyecto")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al asignar proyecto")
        
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al asignar proyecto: {e}")
        raise HTTPException(status_code=500, detail="Error al asignar proyecto")
    
    
def get_convocatoria_actual_por_proyecto(db: Session, id_proyecto: int):
    try:
        sql = text("""SELECT * FROM proyectos_convocatoria 
                        JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria  
                        WHERE proyectos_convocatoria.id_proyecto = :id_p 
                        AND convocatorias.estado = 'en curso'
                    """)
        result = db.execute(sql, {"id_p": id_proyecto}).fetchone()
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar proyecto en una convocatoria activa")
        raise HTTPException(status_code=404, detail="Error al buscar proyecto en una convocatoria activa")
    
    return result

def get_posibles_evaluadores_para_proyecto(db: Session, id_area_conocimiento: str, id_institucion: int):
    try:
        sql = text("""
            SELECT usuarios.* 
            FROM detalles_institucionales 
            JOIN usuarios ON detalles_institucionales.id_usuario = usuarios.id_usuario 
            JOIN areas_conocimiento ON detalles_institucionales.id_primera_area_conocimiento = areas_conocimiento.id_area_conocimiento 
            WHERE detalles_institucionales.id_institucion != :id_i 
            AND areas_conocimiento.nombre LIKE :ac 
            AND (usuarios.id_rol = 1 OR usuarios.id_rol = 2)
            AND usuarios.estado = 'activo'
        """)
        
        # Preparar los parámetros con comodines para LIKE
        params = {
            "ac": f'%{id_area_conocimiento}%',  # Incluir los comodines % aquí
            "id_i": id_institucion
        }
        result = db.execute(sql, params).fetchall()
        
        return result
    
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar evaluadores")
        raise HTTPException(status_code=404, detail="Error al buscar evaluadores")