from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

def get_proyectos_por_etapa(db: Session, nombre_etapa: str, id_datos_personales: int):
    try:
        sql = text("""
            SELECT proyectos.* 
            FROM proyectos 
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN etapas 
                ON participantes_proyecto.id_etapa = etapas.id_etapa 
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            WHERE etapas.nombre = :nombre_etapa 
              AND participantes_proyecto.id_datos_personales = :id_datos_personales
              AND convocatorias.estado = 'en curso'
        """)
        
        result = db.execute(sql, {"nombre_etapa": nombre_etapa, "id_datos_personales": id_datos_personales}).fetchall()
        
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por etapa y convocatoria vigente: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos por etapa y convocatoria vigente")

def get_proyectos_asignados(db: Session, id_datos_personales: int):
    try:
        sql = text("""
            SELECT proyectos.* 
            FROM proyectos 
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            WHERE participantes_proyecto.id_datos_personales = :id_datos_personales
              AND convocatorias.estado = 'en curso'
        """)
        
        result = db.execute(sql, {"id_datos_personales": id_datos_personales}).fetchall()
        
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos asignados por convocatoria vigente: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos asignados por convocatoria vigente")
