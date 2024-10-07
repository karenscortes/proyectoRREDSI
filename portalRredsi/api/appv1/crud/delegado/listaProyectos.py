from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

def get_all_projects(db: Session, nombre_etapa: str, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT DISTINCT 
                proyectos.id_proyecto,
                instituciones.nombre AS institucion,
                modalidades.nombre AS modalidad,
                proyectos.titulo,
                proyectos.estado_calificacion AS estado_calificacion
            FROM proyectos
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN etapas 
                ON participantes_proyecto.id_etapa = etapas.id_etapa 
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            LEFT JOIN respuestas_rubricas 
                ON proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria
            JOIN instituciones 
                ON proyectos.id_institucion = instituciones.id_institucion
            JOIN modalidades 
                ON proyectos.id_modalidad = modalidades.id_modalidad
            WHERE etapas.nombre = :nombre_etapa 
                AND convocatorias.estado = 'en curso'
            LIMIT :page_size OFFSET :offset
        """)
        
        params = {
            "nombre_etapa": nombre_etapa,
            "page_size": page_size,
            "offset": offset
        }
        
        result = db.execute(sql, params).mappings().all()
        
        count_sql = text("""
            SELECT COUNT(DISTINCT proyectos.id_proyecto)
            FROM proyectos
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN etapas 
                ON participantes_proyecto.id_etapa = etapas.id_etapa 
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            LEFT JOIN respuestas_rubricas 
                ON proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria
            WHERE etapas.nombre = :nombre_etapa 
                AND convocatorias.estado = 'en curso'
        """)
        
        total_proyectos = db.execute(count_sql, {"nombre_etapa": nombre_etapa}).scalar()
        
        total_pages = (total_proyectos + page_size - 1) // page_size
        
        return {
            "data": result,
            "total_pages": total_pages
        }
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por etapa: {e}")
        raise HTTPException(status_code=500, detail=f"Error al buscar proyectos por etapa {e}")
    
# Consulta para filtrar todos los proyectos por estado(calificado, pendiente) y por etapa
def get_projects_by_state(db: Session, nombre_etapa: str, estado_calificacion: str, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT DISTINCT 
                proyectos.id_proyecto,
                instituciones.nombre AS institucion,
                modalidades.nombre AS modalidad,
                proyectos.titulo,
                proyectos.estado_calificacion AS estado_calificacion
            FROM proyectos
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN etapas 
                ON participantes_proyecto.id_etapa = etapas.id_etapa 
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            LEFT JOIN respuestas_rubricas 
                ON proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria
            JOIN instituciones 
                ON proyectos.id_institucion = instituciones.id_institucion
            JOIN modalidades 
                ON proyectos.id_modalidad = modalidades.id_modalidad
            WHERE etapas.nombre = :nombre_etapa 
                AND convocatorias.estado = 'en curso'
                AND proyectos.estado_calificacion = :estado_calificacion
            LIMIT :page_size OFFSET :offset
        """)
        
        params = {
            "nombre_etapa": nombre_etapa,
            "estado_calificacion": estado_calificacion,
            "page_size": page_size,
            "offset": offset
        }
        
        result = db.execute(sql, params).mappings().all()
        
        count_sql = text("""
            SELECT COUNT(DISTINCT proyectos.id_proyecto)
            FROM proyectos
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN etapas 
                ON participantes_proyecto.id_etapa = etapas.id_etapa 
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            LEFT JOIN respuestas_rubricas 
                ON proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria
            WHERE etapas.nombre = :nombre_etapa 
                AND convocatorias.estado = 'en curso' 
                AND proyectos.estado_calificacion = :estado_calificacion 
        """)
        
        total_proyectos = db.execute(count_sql, {"nombre_etapa": nombre_etapa, "estado_calificacion": estado_calificacion}).scalar()
        
        total_pages = (total_proyectos + page_size - 1) // page_size
        
        return {
            "data": result,
            "total_pages": total_pages
        }
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por estado: {e}")
        raise HTTPException(status_code=500, detail=f"Error al buscar proyectos por estado")
    
