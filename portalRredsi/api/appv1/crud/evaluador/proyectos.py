from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException
from datetime import timedelta

#Consulta para sacar los proyectos asignados a un evaluador por etapa (paginado)
def get_proyectos_por_etapa(db: Session, nombre_etapa: str, id_usuario: int, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT DISTINCT proyectos.*, rubricas_resultados.estado_proyecto AS estado_evaluacion
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
            SELECT DISTINCT proyectos.*, rubricas_resultados.estado_proyecto AS estado_evaluacion
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
            SELECT COUNT(DISTINCT proyectos.id_proyecto)
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
            SELECT DISTINCT proyectos.*, rubricas_resultados.estado_proyecto AS estado_evaluacion
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
            SELECT COUNT(DISTINCT proyectos.id_proyecto)
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


# Consulta para obtener el id_proyecto_convocatoria con el id_proyecto
def get_proyecto_convocatoria(db: Session, id_proyecto: int):
    try:
        sql_query = text(
            """
            SELECT proyectos_convocatoria.id_proyecto_convocatoria
            FROM proyectos_convocatoria
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            WHERE proyectos_convocatoria.id_proyecto = :id_proyecto
            AND convocatorias.estado = 'en curso'
            """
        )
        result = db.execute(sql_query, {"id_proyecto": id_proyecto}).fetchone()
        if result:
            return result[0]
        else:
            raise HTTPException(status_code=404, detail="No se encontró una convocatoria en curso para el proyecto.")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al consultar el proyecto convocatoria: {e}")
        raise HTTPException(status_code=500, detail="Error al consultar el proyecto convocatoria")
    
    
def insert_respuesta_rubrica(db: Session, id_item_rubrica: int, id_usuario: int, id_proyecto: int, observacion: str, calificacion: float, calificacion_final: float):
    try:
        # Obtener id_proyecto_convocatoria
        id_proyecto_convocatoria = get_proyecto_convocatoria(db, id_proyecto)
        
        if not id_proyecto_convocatoria:
            raise HTTPException(status_code=404, detail="No se encontró una convocatoria en curso para el proyecto.")
        
        # Verificar si ya existe un id_rubrica_resultado para este proyecto y usuario
        sql_check_rubrica_resultado = text(
            """
            SELECT rubricas_resultados.id_rubrica_resultado
            FROM rubricas_resultados
            JOIN respuestas_rubricas ON rubricas_resultados.id_rubrica_resultado = respuestas_rubricas.id_rubrica_resultado
            WHERE respuestas_rubricas.id_proyecto_convocatoria = :id_proyecto_convocatoria
            """
        )
        rubrica_resultado = db.execute(sql_check_rubrica_resultado, {
            "id_proyecto_convocatoria": id_proyecto_convocatoria,
            "id_usuario": id_usuario
        }).fetchone()

        if rubrica_resultado:
            id_rubrica_resultado = rubrica_resultado[0]
        else:
            # Inserción en rubricas_resultados
            sql_insert_rubrica_resultado = text(
                """
                INSERT INTO rubricas_resultados (estado_proyecto, puntaje_aprobacion)
                VALUES ('calificado', 0.0);
                """
            )
            db.execute(sql_insert_rubrica_resultado)

            # Obtener el último id insertado usando scalar()
            id_rubrica_resultado = db.execute(text("SELECT LAST_INSERT_ID();")).scalar()
        
    
        sql_insert_respuesta_rubrica = text(
            """
            INSERT INTO respuestas_rubricas (
                id_item_rubrica, id_rubrica_resultado, id_usuario, id_proyecto_convocatoria, observacion, calificacion
            ) 
            VALUES (
                :id_item_rubrica, :id_rubrica_resultado, :id_usuario, :id_proyecto_convocatoria, :observacion, :calificacion
            );
            """
        )
        params = {
            "id_item_rubrica": id_item_rubrica,
            "id_rubrica_resultado": id_rubrica_resultado,
            "id_usuario": id_usuario,
            "id_proyecto_convocatoria": id_proyecto_convocatoria,
            "observacion": observacion,
            "calificacion": calificacion
        }
        db.execute(sql_insert_respuesta_rubrica, params)

        sql_update_rubrica_resultado = text(
            """
            UPDATE rubricas_resultados
            SET puntaje_aprobacion = :calificacion_final,
            estado_proyecto = 'calificado'
            WHERE id_rubrica_resultado = :id_rubrica_resultado;
            """
        )
        db.execute(sql_update_rubrica_resultado, {
            "calificacion_final": calificacion_final,
            "id_rubrica_resultado": id_rubrica_resultado
        })

        db.commit()
        return {"message": "Respuesta de rúbrica registrada exitosamente."}

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al insertar respuesta de rúbrica: {e}")
        raise HTTPException(status_code=500, detail="Error al insertar respuesta de rúbrica")


def get_proyectos_etapa_presencial_con_horario(db: Session, id_usuario: int, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT DISTINCT proyectos.*, 
                   rubricas_resultados.estado_proyecto AS estado_evaluacion, 
                   salas.numero_sala, 
                   salas.nombre_sala, 
                   detalle_sala.fecha, 
                   detalle_sala.hora_inicio, 
                   detalle_sala.hora_fin
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
            LEFT JOIN detalle_sala 
                ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria
            LEFT JOIN salas 
                ON detalle_sala.id_sala = salas.id_sala
            WHERE etapas.nombre = 'Presencial'
              AND participantes_proyecto.id_usuario = :id_usuario
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
                AND respuestas_rubricas.id_usuario = :id_usuario
            LEFT JOIN rubricas_resultados 
                ON respuestas_rubricas.id_rubrica_resultado = rubricas_resultados.id_rubrica_resultado
            LEFT JOIN detalle_sala 
                ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria
            WHERE etapas.nombre = 'Presencial'
              AND participantes_proyecto.id_usuario = :id_usuario
              AND convocatorias.estado = 'en curso'
        """)
        
        total_proyectos = db.execute(count_sql, {"id_usuario": id_usuario}).scalar()
        
        total_pages = (total_proyectos + page_size - 1) // page_size
        
        return {
            "data": result,
            "total_pages": total_pages
        }
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por etapa: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos por etapa")
    


def convertir_timedelta_a_hora(timedelta_obj: timedelta) -> str:
    total_seconds = int(timedelta_obj.total_seconds())
    horas, minutos = divmod(total_seconds // 60, 60)
    return f"{horas:02}:{minutos:02}"




