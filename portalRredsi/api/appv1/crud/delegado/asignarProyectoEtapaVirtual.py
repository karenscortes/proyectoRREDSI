from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.delegado.asignacionProyectoEtapaVirtual import AsignarProyectoEtapaUno


def asignar_proyecto_etapa_virtual(db: Session, asignacion: AsignarProyectoEtapaUno ):
    try:
        sql = text("""INSERT INTO participantes_proyecto (id_usuario, id_proyecto, id_etapa, id_proyectos_convocatoria) 
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

def get_posibles_evaluadores_para_proyecto(db: Session, id_area_conocimiento: int, id_institucion: int):
    try:
        sql = text("""
            SELECT usuarios.id_usuario, usuarios.documento, usuarios.nombres, usuarios.apellidos, usuarios.celular, usuarios.correo 
            FROM detalles_institucionales 
            JOIN usuarios ON detalles_institucionales.id_usuario = usuarios.id_usuario
            WHERE detalles_institucionales.id_institucion != :id_i 
            AND (detalles_institucionales.id_primera_area_conocimiento = :id_ac OR detalles_institucionales.id_segunda_area_conocimiento = :id_ac)
            AND (usuarios.id_rol = 1 OR usuarios.id_rol = 2)
            AND usuarios.estado = 'activo'
        """)
        
        # Preparar los parámetros con comodines para LIKE
        params = {
            "id_ac": id_area_conocimiento,  # Incluir los comodines % aquí
            "id_i": id_institucion
        }
        result = db.execute(sql, params).fetchall()
        
        return result
    
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar evaluadores")
        raise HTTPException(status_code=204, detail="Error al buscar evaluadores")

def get_area_conocimiento_por_nombre(db: Session, nombre_area: str):
    try:
        sql = text("SELECT * FROM areas_conocimiento WHERE nombre like :nombre_area")
        result = db.execute(sql, {"nombre_area": nombre_area}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Area de conocimiento no se ha encontrado")
        raise HTTPException(status_code=204, detail="Area de conocimiento no se ha encontrado")
    
def get_institucion_por_nombre(db: Session, nombre_institucion: str):
    try:
        sql = text("SELECT * FROM instituciones WHERE nombre like :n_institucion")
        result = db.execute(sql, {"n_institucion": nombre_institucion}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Area de conocimiento no se ha encontrado")
        raise HTTPException(status_code=204, detail="Area de conocimiento no se ha encontrado")
    
def update_estado_proyecto(db: Session, id_proyecto:int):
    sql = text("UPDATE proyectos SET estado = 'asignado' WHERE id_proyecto = :id_proyecto")
    params = {
        "id_proyecto": id_proyecto
    }
    db.execute(sql, params)
    db.commit()
    return True