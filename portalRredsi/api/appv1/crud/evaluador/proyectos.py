from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

def get_proyectos_por_etapa(db: Session, nombre_etapa: str, id_usuario: int, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT proyectos.*, rubricas_resultados.estado_proyecto AS estado_evaluacion
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
                AND respuestas_rubricas.id_usuario = :id_usuario
            LEFT JOIN rubricas_resultados 
                ON respuestas_rubricas.id_rubrica_resultado = rubricas_resultados.id_rubrica_resultado
            WHERE etapas.nombre = :nombre_etapa 
              AND participantes_proyecto.id_usuario = :id_usuario
              AND convocatorias.estado = 'en curso'
            LIMIT :page_size OFFSET :offset
        """)
        
        params = {
            "nombre_etapa": nombre_etapa,
            "id_usuario": id_usuario,
            "page_size": page_size,
            "offset": offset
        }
        
        result = db.execute(sql, params).mappings().all()
        
        count_sql = text("""
            SELECT COUNT(*)
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
                AND respuestas_rubricas.id_usuario = :id_usuario
            LEFT JOIN rubricas_resultados 
                ON respuestas_rubricas.id_rubrica_resultado = rubricas_resultados.id_rubrica_resultado
            WHERE etapas.nombre = :nombre_etapa 
              AND participantes_proyecto.id_usuario = :id_usuario
              AND convocatorias.estado = 'en curso'
        """)
        
        total_proyectos = db.execute(count_sql, {"nombre_etapa": nombre_etapa, "id_usuario": id_usuario}).scalar()
        
        total_pages = (total_proyectos + page_size - 1) // page_size
        
        return {
            "data": result,
            "total_pages": total_pages
        }
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por etapa: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos por etapa")


    

def get_proyectos_por_estado(db: Session, estado_evaluacion: str, id_usuario: int, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT proyectos.*, rubricas_resultados.estado_proyecto AS estado_evaluacion
            FROM proyectos
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            LEFT JOIN respuestas_rubricas 
                ON proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria
                AND respuestas_rubricas.id_usuario = :id_usuario
            LEFT JOIN rubricas_resultados 
                ON respuestas_rubricas.id_rubrica_resultado = rubricas_resultados.id_rubrica_resultado
            WHERE participantes_proyecto.id_usuario = :id_usuario
              AND rubricas_resultados.estado_proyecto = :estado_evaluacion
              AND convocatorias.estado = 'en curso'
            LIMIT :page_size OFFSET :offset
        """)
        
        params = {
            "estado_evaluacion": estado_evaluacion,
            "id_usuario": id_usuario,
            "page_size": page_size,
            "offset": offset
        }
        
        result = db.execute(sql, params).mappings().all()
        
        count_sql = text("""
            SELECT COUNT(*)
            FROM proyectos
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            LEFT JOIN respuestas_rubricas 
                ON proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria
                AND respuestas_rubricas.id_usuario = :id_usuario
            LEFT JOIN rubricas_resultados 
                ON respuestas_rubricas.id_rubrica_resultado = rubricas_resultados.id_rubrica_resultado
            WHERE participantes_proyecto.id_usuario = :id_usuario
              AND rubricas_resultados.estado_proyecto = :estado_evaluacion
              AND convocatorias.estado = 'en curso'
        """)
        
        total_proyectos = db.execute(count_sql, {"estado_evaluacion": estado_evaluacion, "id_usuario": id_usuario}).scalar()
        
        total_pages = (total_proyectos + page_size - 1) // page_size
        
        return {
            "data": result,
            "total_pages": total_pages
        }
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por estado de evaluación: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos por estado de evaluación")



def get_proyectos_asignados(db: Session, id_usuario: int, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT proyectos.*, rubricas_resultados.estado_proyecto AS estado_evaluacion
            FROM proyectos
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            LEFT JOIN respuestas_rubricas 
                ON proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria
                AND respuestas_rubricas.id_usuario = :id_usuario
            LEFT JOIN rubricas_resultados 
                ON respuestas_rubricas.id_rubrica_resultado = rubricas_resultados.id_rubrica_resultado
            WHERE participantes_proyecto.id_usuario = :id_usuario
              AND convocatorias.estado = 'en curso'
            LIMIT :page_size OFFSET :offset
        """)
        
        params = {
            "id_usuario": id_usuario,
            "page_size": page_size,
            "offset": offset
        }
        
        result = db.execute(sql, params).mappings().all()
        
        count_sql = text("""
            SELECT COUNT(*)
            FROM proyectos
            JOIN participantes_proyecto 
                ON proyectos.id_proyecto = participantes_proyecto.id_proyecto  
            JOIN proyectos_convocatoria 
                ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto 
            JOIN convocatorias 
                ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            WHERE participantes_proyecto.id_usuario = :id_usuario
              AND convocatorias.estado = 'en curso'
        """)
        
        total_proyectos = db.execute(count_sql, {"id_usuario": id_usuario}).scalar()
        
        total_pages = (total_proyectos + page_size - 1) // page_size
        
        return {
            "data": result,
            "total_pages": total_pages
        }
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos asignados: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos asignados")



