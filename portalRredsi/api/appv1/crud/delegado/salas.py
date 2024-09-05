# Crear un usuario
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.delegado.salas import AsignarProyectoSala



def asignar_proyecto_a_sala(db: Session, asignacion: AsignarProyectoSala ):
    try:
        sql = text("INSERT INTO detalle_sala (id_sala, id_proyecto_convocatoria, fecha, hora_inicio, hora_fin) VALUES (:id_sala, :id_proyecto_convocatoria, :fecha, :hora_inicio, :hora_fin)")
        
        params={
            "id_sala": asignacion.id_sala,
            "id_proyecto_convocatoria": asignacion.id_proyecto_convocatoria,
            "fecha": asignacion.fecha,
            "hora_inicio": asignacion.hora_inicio,
            "hora_fin": asignacion.hora_fin
        }
        result = db.execute(sql,params)
        db.commit()
        return result
    
    except IntegrityError as e:
        db.rollback()
        print(f"Error al asignar proyecto a sala: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID de proyecto ya esta asignado ")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al asignar proyecto")
        
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al asignar proyecto: {e}")
        raise HTTPException(status_code=500, detail="Error al asignar proyecto")
    
    
def get_salas(db: Session):
    try:
        sql = text("SELECT * FROM salas")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar salas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar salas")
    
    
def get_salas_por_convocatoria(db: Session, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("SELECT * FROM salas JOIN detalle_sala ON salas.id_sala = detalle_sala.id_sala JOIN proyectos_convocatoria ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria WHERE convocatorias.estado = 'en curso' LIMIT :page_size OFFSET :offset ")
        
        params ={
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql,params).mappings().all()
        
        # Obtener el número total de usuarios
        count_sql = text("SELECT COUNT(*) FROM salas JOIN detalle_sala ON salas.id_sala = detalle_sala.id_sala JOIN proyectos_convocatoria ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria WHERE convocatorias.estado = 'en curso'")
        total_salas = db.execute(count_sql).scalar()

        # Calcular el número total de páginas
        total_pages = (total_salas + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar salas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar salas")
    
    
def get_detalle_sala(db: Session, id_sala: str):
    sql = text("SELECT * FROM detalle_sala WHERE id_sala = :id_sala")
    result = db.execute(sql, {"id_sala": id_sala}).fetchone()
    return result