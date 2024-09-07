from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException

#Consulta para sacar los proyectos asignados a un evaluador por etapa (paginado)
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
    
    
#Consulta para sacar los proyectos asignados a un evaluador por estado (paginado)
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


#Consulta para sacar los proyectos asignados a un evaluador (paginado)
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

# Consulta para obtener la convocatoria actual con estado 'en curso'
def get_current_convocatoria(db: Session):
    try:
        sql_query = text(
            "SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso' LIMIT 1;"
        )
        result = db.execute(sql_query).fetchone()
        if result:
            return result[0] 
        else:
            raise HTTPException(status_code=404, detail="No se encontró ninguna convocatoria en curso")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al consultar la convocatoria: {e}")
        raise HTTPException(status_code=500, detail="Error al consultar la convocatoria")
    

# Inserción en la tabla postulaciones_evaluadores
def create_postulacion_evaluador(db: Session, id_convocatoria: int, id_evaluador: int, etapa_virtual: int, etapa_presencial: int, jornada_manana: int, jornada_tarde: int):
    try:
        # Realizar el insert en la tabla postulaciones_evaluadores
        sql_query = text(
            """
            INSERT INTO postulaciones_evaluadores (
                id_convocatoria, id_evaluador, etapa_virtual, etapa_presencial, jornada_manana, jornada_tarde
            ) 
            VALUES (
                :convocatoria_id, :evaluador_id, :virtual, :presencial, :manana, :tarde
            );
            """
        )
        params = {
            "convocatoria_id": id_convocatoria,
            "evaluador_id": id_evaluador,
            "virtual": etapa_virtual,
            "presencial": etapa_presencial,
            "manana": jornada_manana,
            "tarde": jornada_tarde
        }
        db.execute(sql_query, params)
        db.commit()
        return True 
    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear la postulación: {e}")
        if 'Duplicate entry' in str(e.orig):
            raise HTTPException(status_code=400, detail="Ya existe una postulación para este evaluador y convocatoria")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad de datos")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear la postulación: {e}")
        raise HTTPException(status_code=500, detail="Error al crear la postulación")
