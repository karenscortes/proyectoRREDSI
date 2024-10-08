from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException
from datetime import timedelta
from appv1.schemas.evaluador.evaluador import CalificarProyectoRespuesta, Componente


# Consulta para obtener la etapa actual basada en la convocatoria en curso
def get_etapa_actual(db: Session):
    try:
        sql_query = text(
            """
            SELECT etapas.id_etapa, etapas.nombre
            FROM etapas
            JOIN fases ON etapas.id_etapa = fases.id_etapa
            JOIN programacion_fases ON fases.id_fase = programacion_fases.id_fase
            JOIN convocatorias ON programacion_fases.id_convocatoria = convocatorias.id_convocatoria
            WHERE convocatorias.estado = 'en curso'
            AND CURRENT_DATE BETWEEN programacion_fases.fecha_inicio AND programacion_fases.fecha_fin
            ORDER BY programacion_fases.fecha_inicio ASC
            LIMIT 1
            """
        )
        result = db.execute(sql_query).fetchone()
        if result:
            return {
                "id_etapa": str(result[0]),
                "nombre_etapa": result[1]
            }
        else:
            raise HTTPException(status_code=404, detail="No se encontró una etapa actual para la convocatoria en curso.")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al consultar la etapa actual: {e}")
        raise HTTPException(status_code=500, detail="Error al consultar la etapa actual")

# Consulta para sacar los proyectos asignados a un evaluador por etapa (paginado)
def get_proyectos_por_etapa(db: Session, nombre_etapa: str, id_usuario: int, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT DISTINCT 
                proyectos.id_proyecto,
                instituciones.nombre AS institucion,
                modalidades.nombre AS modalidad,
                areas_conocimiento.nombre AS area_conocimiento,
                proyectos.titulo,
                proyectos.estado_calificacion AS estado_evaluacion,
                proyectos.programa_academico,
                proyectos.grupo_investigacion,
                proyectos.linea_investigacion,
                proyectos.nombre_semillero,
                proyectos.url_propuesta_escrita,
                proyectos.url_aval
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
            JOIN instituciones 
                ON proyectos.id_institucion = instituciones.id_institucion
            JOIN modalidades 
                ON proyectos.id_modalidad = modalidades.id_modalidad
            JOIN areas_conocimiento 
                ON proyectos.id_area_conocimiento = areas_conocimiento.id_area_conocimiento
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

# Consulta para sacar los proyectos asignados a un evaluador por estado (paginado)
def get_proyectos_por_etapa_y_estado(db: Session, nombre_etapa: str, estado_calificacion: str, id_usuario: int, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT DISTINCT 
                proyectos.id_proyecto,
                instituciones.nombre AS institucion,
                modalidades.nombre AS modalidad,
                areas_conocimiento.nombre AS area_conocimiento,
                proyectos.titulo,
                proyectos.estado_calificacion AS estado_evaluacion,
                proyectos.programa_academico,
                proyectos.grupo_investigacion,
                proyectos.linea_investigacion,
                proyectos.nombre_semillero,
                proyectos.url_propuesta_escrita,
                proyectos.url_aval
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
            JOIN instituciones 
                ON proyectos.id_institucion = instituciones.id_institucion
            JOIN modalidades 
                ON proyectos.id_modalidad = modalidades.id_modalidad
            JOIN areas_conocimiento 
                ON proyectos.id_area_conocimiento = areas_conocimiento.id_area_conocimiento
            WHERE etapas.nombre = :nombre_etapa 
              AND participantes_proyecto.id_usuario = :id_usuario
              AND convocatorias.estado = 'en curso'
              AND proyectos.estado_calificacion = :estado_calificacion
            LIMIT :page_size OFFSET :offset
        """)
        
        params = {
            "nombre_etapa": nombre_etapa,
            "id_usuario": id_usuario,
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
                AND respuestas_rubricas.id_usuario = :id_usuario
            WHERE etapas.nombre = :nombre_etapa 
              AND participantes_proyecto.id_usuario = :id_usuario
              AND convocatorias.estado = 'en curso'
              AND proyectos.estado_calificacion = :estado_calificacion
        """)
        
        total_proyectos = db.execute(count_sql, {"nombre_etapa": nombre_etapa, "id_usuario": id_usuario, "estado_calificacion": estado_calificacion}).scalar()
        
        total_pages = (total_proyectos + page_size - 1) // page_size
        
        return {
            "data": result,
            "total_pages": total_pages
        }
    except SQLAlchemyError as e:
        print(f"Error al buscar proyectos por etapa y estado: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar proyectos por etapa y estado")

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
        print("Error al consultar el proyecto convocatoria")
        raise HTTPException(status_code=500, detail="Error al consultar el proyecto convocatoria")
    
# Inserción de las respuestas de un proyecto
def insert_respuesta_rubrica(db: Session, id_item_rubrica: int, id_usuario: int, id_proyecto: int, observacion: str, calificacion: float, calificacion_final: float, etapa_actual: str):
    try:
        # Obtener id_proyecto_convocatoria
        id_proyecto_convocatoria = get_proyecto_convocatoria(db, id_proyecto)
        
        if not id_proyecto_convocatoria:
            raise HTTPException(status_code=404, detail="No se encontró una convocatoria en curso para el proyecto.")
        
        # Verificar la modalidad del proyecto para determinar el puntaje mínimo de aprobación
        sql_get_modalidad = text(
            """
            SELECT id_modalidad
            FROM proyectos
            WHERE id_proyecto = :id_proyecto
            """
        )
        modalidad = db.execute(sql_get_modalidad, {"id_proyecto": id_proyecto}).scalar()
        
        if modalidad == '1':
            puntaje_minimo_aprobacion = 80
        else:
            puntaje_minimo_aprobacion = 75
        
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
            # Inserción en rubricas_resultados con estado 'reprobado' inicialmente
            sql_insert_rubrica_resultado = text(
                """
                INSERT INTO rubricas_resultados (estado_proyecto, puntaje_aprobacion)
                VALUES ('reprobado', 0.0);
                """
            )
            db.execute(sql_insert_rubrica_resultado)

            # Obtener el último id insertado usando scalar()
            id_rubrica_resultado = db.execute(text("SELECT LAST_INSERT_ID();")).scalar()
        
        # Inserción de la respuesta de rúbrica
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

        # Determinar si el proyecto aprueba o reprueba en función del puntaje final y modalidad
        estado_rubrica = 'aprobado' if calificacion_final >= puntaje_minimo_aprobacion else 'reprobado'

        # Actualización de rubricas_resultados con el estado final y el puntaje
        sql_update_rubrica_resultado = text(
            """
            UPDATE rubricas_resultados
            SET puntaje_aprobacion = :calificacion_final,
                estado_proyecto = :estado_rubrica
            WHERE id_rubrica_resultado = :id_rubrica_resultado;
            """
        )
        db.execute(sql_update_rubrica_resultado, {
            "calificacion_final": calificacion_final,
            "estado_rubrica": estado_rubrica,
            "id_rubrica_resultado": id_rubrica_resultado
        })

        # Verificar si hay otras respuestas en la etapa presencial
        if etapa_actual == 'Presencial':
            sql_check_otras_respuestas = text(
                """
                SELECT COUNT(*) FROM respuestas_rubricas
                JOIN items_rubrica ON respuestas_rubricas.id_item_rubrica = items_rubrica.id_item_rubrica
                JOIN rubricas on items_rubrica.id_rubrica = rubricas.id_rubrica
                WHERE respuestas_rubricas.id_proyecto_convocatoria = :id_proyecto_convocatoria
                AND respuestas_rubricas.id_usuario != :id_usuario
                AND rubricas.id_etapa = '1'
                """
            )
            otras_respuestas_count = db.execute(sql_check_otras_respuestas, {
                "id_proyecto_convocatoria": id_proyecto_convocatoria,
                "id_usuario": id_usuario
            }).scalar()

            if otras_respuestas_count > 0:
                # Si hay otras respuestas, el proyecto pasa a C_presencial
                nuevo_estado_calificacion = 'C_presencial'
            else:
                # Si no hay otras respuestas, queda en P_presencial
                nuevo_estado_calificacion = 'P_presencial'
        else:
            nuevo_estado_calificacion = 'C_virtual' if etapa_actual == 'Virtual' else 'C_presencial'

        # Actualización del estado_calificacion en la tabla proyectos
        sql_update_proyecto = text(
            """
            UPDATE proyectos
            SET estado_calificacion = :nuevo_estado_calificacion
            WHERE id_proyecto = :id_proyecto;
            """
        )
        db.execute(sql_update_proyecto, {
            "nuevo_estado_calificacion": nuevo_estado_calificacion,
            "id_proyecto": id_proyecto
        })

        db.commit()
        return {"message": "Respuesta de rúbrica registrada exitosamente."}

    except SQLAlchemyError as e:
        db.rollback()
        print("Error al insertar respuesta de rúbrica")

# Obtener los datos del proyecto con los datos de la sala    
def get_proyectos_etapa_presencial_con_horario(db: Session, id_usuario: int, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""
            SELECT DISTINCT proyectos.*, 
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
            LEFT JOIN detalle_sala 
                ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria
            LEFT JOIN salas 
                ON detalle_sala.id_sala = salas.id_sala
            WHERE etapas.nombre = 'Presencial'
              AND participantes_proyecto.id_usuario = :id_usuario
              AND convocatorias.estado = 'en curso'
            ORDER BY detalle_sala.fecha ASC, detalle_sala.hora_inicio ASC
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
        print("Error al buscar el horario de los proyectos")
        raise HTTPException(status_code=500, detail="Error al buscar el horario de los proyectos")
    
# Funcion para convetir la hora de la db a tiempo real
def convertir_timedelta_a_hora(timedelta_obj: timedelta) -> str:
    total_seconds = int(timedelta_obj.total_seconds())
    horas, minutos = divmod(total_seconds // 60, 60)
    return f"{horas:02}:{minutos:02}"

# Obtener los datos de la rubrica que fue asignada a un proyecto especifico
def get_datos_rubrica_proyecto(db: Session, id_proyecto: int, id_usuario: int, nombre_etapa: str):
    try:
        sql_query = text("""
            SELECT DISTINCT items_rubrica.* FROM items_rubrica
            JOIN rubricas ON items_rubrica.id_rubrica = rubricas.id_rubrica 
            JOIN participantes_proyecto ON rubricas.id_etapa = participantes_proyecto.id_etapa
            JOIN proyectos_convocatoria ON participantes_proyecto.id_proyecto = proyectos_convocatoria.id_proyecto         
            JOIN proyectos ON proyectos_convocatoria.id_proyecto = proyectos.id_proyecto
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            JOIN etapas ON rubricas.id_etapa = etapas.id_etapa    
            
            WHERE 
                participantes_proyecto.id_proyecto = :id_proyecto
                AND participantes_proyecto.id_usuario = :id_usuario
                AND rubricas.id_modalidad = proyectos.id_modalidad
                AND participantes_proyecto.id_etapa = rubricas.id_etapa
                AND convocatorias.estado = 'en curso'
                AND etapas.nombre = :nombre_etapa
                AND items_rubrica.estado = 'activo'

        """)
        params = {
            "id_proyecto": id_proyecto, 
            "id_usuario": id_usuario,
            "nombre_etapa": nombre_etapa
        }

        result = db.execute(sql_query,params).mappings().all()

        if len(result)==0:
            raise HTTPException(status_code=404, detail="Datos no encontrados")
        
        return result
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar la rubrica del proyecto")

# Obtener los nombres de los ponentes asignados a un proyecto y convocatoria en curso
def get_nombres_ponentes_proyecto(db: Session, id_proyecto: int):
    try:
        sql_query = text("""
            SELECT GROUP_CONCAT(ponente.nombres, ' ', ponente.apellidos SEPARATOR ', ') AS nombres_ponentes
            FROM participantes_proyecto
            JOIN usuarios AS ponente ON ponente.id_usuario = participantes_proyecto.id_usuario
            JOIN proyectos_convocatoria ON participantes_proyecto.id_proyecto = proyectos_convocatoria.id_proyecto
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            WHERE 
                participantes_proyecto.id_proyecto = :id_proyecto
                AND ponente.id_rol = 5
                AND convocatorias.estado = 'en curso'
        """)
        params = {
            "id_proyecto": id_proyecto
        }
        result = db.execute(sql_query, params).fetchone()

        # Verificar si se encontraron ponentes
        if not result or not result.nombres_ponentes:
            return "No se encontraron ponentes"

        return result.nombres_ponentes

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar los ponentes del proyecto:")

# Obtener los datos para calificar un proyecto
def get_datos_calificar_proyecto_completo(db: Session, id_proyecto: int, id_usuario: int, nombre_etapa: str):
    try:
        # Obtener los datos básicos del proyecto y del evaluador
        sql_query = text("""
            SELECT 
                proyectos.titulo AS titulo_proyecto,
                inst_proyecto.nombre AS universidad_proyecto,
                usuarios.nombres AS nombre_evaluador,
                usuarios.documento AS cedula_evaluador,
                inst_evaluador.nombre AS universidad_evaluador,
                usuarios.correo AS email_evaluador,
                usuarios.celular AS celular_evaluador
            FROM 
                proyectos
            JOIN 
                participantes_proyecto ON proyectos.id_proyecto = participantes_proyecto.id_proyecto
            JOIN 
                usuarios ON usuarios.id_usuario = participantes_proyecto.id_usuario
            JOIN 
                detalles_institucionales ON usuarios.id_usuario = detalles_institucionales.id_usuario
            JOIN 
                instituciones AS inst_proyecto ON proyectos.id_institucion = inst_proyecto.id_institucion
            JOIN 
                instituciones AS inst_evaluador ON detalles_institucionales.id_institucion = inst_evaluador.id_institucion
            WHERE 
                proyectos.id_proyecto = :id_proyecto
                AND usuarios.id_usuario = :id_usuario
        """)
        result = db.execute(sql_query, {"id_proyecto": id_proyecto, "id_usuario": id_usuario}).fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="Datos no encontrados")

        # Obtener los nombres de los ponentes asociados al proyecto
        nombres_ponentes = get_nombres_ponentes_proyecto(db, id_proyecto)

        # Obtener los datos de la rúbrica asociados al proyecto
        rubrica_result = get_datos_rubrica_proyecto(db, id_proyecto, id_usuario, nombre_etapa)
        
        componentes_rubrica = [
            Componente(
                id_item_rubrica=item['id_item_rubrica'],
                titulo=item['titulo'],
                descripcion=item['componente'],
                valor_maximo=item['valor_max']
            ) for item in rubrica_result
        ]

        # Crear la respuesta final incluyendo los datos del proyecto y la rúbrica
        proyecto_respuesta = CalificarProyectoRespuesta(
            titulo_proyecto=result.titulo_proyecto,
            universidad_proyecto=result.universidad_proyecto,
            nombre_evaluador=result.nombre_evaluador,
            cedula_evaluador=result.cedula_evaluador,
            universidad_evaluador=result.universidad_evaluador,
            email_evaluador=result.email_evaluador,
            celular_evaluador=result.celular_evaluador,
            nombres_ponentes=nombres_ponentes,  
            componentes=componentes_rubrica  
        )

        return proyecto_respuesta

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar los datos del proyecto")

# Obtener los datos calificados de la rúbrica para un proyecto
def get_datos_calificados_rubrica(db: Session, id_proyecto: int, id_usuario: int, nombre_etapa: str):
    try:
        # Obtener los datos calificados para el proyecto en la etapa proporcionada
        sql_query = text(""" 
            SELECT DISTINCT respuestas_rubricas.*, items_rubrica.titulo, items_rubrica.componente, items_rubrica.valor_max
            FROM respuestas_rubricas
            JOIN items_rubrica ON respuestas_rubricas.id_item_rubrica = items_rubrica.id_item_rubrica
            JOIN proyectos_convocatoria ON respuestas_rubricas.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            JOIN rubricas ON items_rubrica.id_rubrica = rubricas.id_rubrica
            JOIN etapas ON rubricas.id_etapa = etapas.id_etapa    
            WHERE 
                proyectos_convocatoria.id_proyecto = :id_proyecto
                AND respuestas_rubricas.id_usuario = :id_usuario
                AND convocatorias.estado = 'en curso'
                AND etapas.nombre = :nombre_etapa
        """)
        
        params = {
            "id_proyecto": id_proyecto,
            "id_usuario": id_usuario,
            "nombre_etapa": nombre_etapa
        }

        result = db.execute(sql_query, params).mappings().all()

        if len(result) == 0:
            raise HTTPException(status_code=404, detail="Datos calificados no encontrados")

        return result
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar los datos calificados del proyecto")

# Obtener los datos para calificar un proyecto
def get_datos_proyecto_calificado_completo(db: Session, id_proyecto: int, id_usuario: int, nombre_etapa: str):
    try:
        # Obtener los datos básicos del proyecto y del evaluador
        sql_query = text(""" 
            SELECT 
                proyectos.titulo AS titulo_proyecto,
                inst_proyecto.nombre AS universidad_proyecto,
                usuarios.nombres AS nombre_evaluador,
                usuarios.documento AS cedula_evaluador,
                inst_evaluador.nombre AS universidad_evaluador,
                usuarios.correo AS email_evaluador,
                usuarios.celular AS celular_evaluador
            FROM 
                proyectos
            JOIN 
                participantes_proyecto ON proyectos.id_proyecto = participantes_proyecto.id_proyecto
            JOIN 
                usuarios ON usuarios.id_usuario = participantes_proyecto.id_usuario
            JOIN 
                detalles_institucionales ON usuarios.id_usuario = detalles_institucionales.id_usuario
            JOIN 
                instituciones AS inst_proyecto ON proyectos.id_institucion = inst_proyecto.id_institucion
            JOIN 
                instituciones AS inst_evaluador ON detalles_institucionales.id_institucion = inst_evaluador.id_institucion
            WHERE 
                proyectos.id_proyecto = :id_proyecto
                AND usuarios.id_usuario = :id_usuario
        """)
        result = db.execute(sql_query, {"id_proyecto": id_proyecto, "id_usuario": id_usuario}).fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="Datos no encontrados")

        # Obtener los nombres de los ponentes asociados al proyecto
        nombres_ponentes = get_nombres_ponentes_proyecto(db, id_proyecto)

        # Obtener los datos de la rúbrica asociados al proyecto, incluyendo el nombre de la etapa
        rubrica_result = get_datos_calificados_rubrica(db, id_proyecto, id_usuario, nombre_etapa)
        
        componentes_rubrica = [
            Componente(
                id_item_rubrica=item['id_item_rubrica'],
                titulo=item['titulo'],
                descripcion=item['componente'],
                observaciones=item['observacion'],
                calificacion=item['calificacion'],
                valor_maximo=item['valor_max']
            ) for item in rubrica_result
        ]

        # Crear la respuesta final incluyendo los datos del proyecto y la rúbrica
        proyecto_respuesta = CalificarProyectoRespuesta(
            titulo_proyecto=result.titulo_proyecto,
            universidad_proyecto=result.universidad_proyecto,
            nombre_evaluador=result.nombre_evaluador,
            cedula_evaluador=result.cedula_evaluador,
            universidad_evaluador=result.universidad_evaluador,
            email_evaluador=result.email_evaluador,
            celular_evaluador=result.celular_evaluador,
            nombres_ponentes=nombres_ponentes,  
            componentes=componentes_rubrica  
        )

        return proyecto_respuesta

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar los datos del proyecto")

# Obtener los nombres de las fases y las fechas de la programación de una convocatoria en curso filtrando por etapa
def get_nombres_fases_y_fechas_programacion(db: Session, nombre_etapa: str) -> List[dict]:
    try:
        sql_query = text("""
            SELECT 
                fases.nombre AS nombre_fase,
                programacion_fases.fecha_inicio,
                programacion_fases.fecha_fin
            FROM programacion_fases
            JOIN convocatorias 
                ON programacion_fases.id_convocatoria = convocatorias.id_convocatoria
            JOIN fases 
                ON programacion_fases.id_fase = fases.id_fase
            JOIN etapas 
                ON fases.id_etapa = etapas.id_etapa 
            WHERE 
                convocatorias.estado = 'en curso'
                AND etapas.nombre = :nombre_etapa  
        """)
        
        # Ejecuta la consulta y pasa el parámetro de la etapa
        result = db.execute(sql_query, {"nombre_etapa": nombre_etapa}).fetchall()

        # Transformar el resultado en una lista de diccionarios
        programacion_fases = [
            {
                "nombre_fase": row[0],
                "fecha_inicio": row[1],
                "fecha_fin": row[2]
            }
            for row in result
        ]

        return programacion_fases

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar las fases junto a su programación")

# Obtener la información de la postulación del evaluador
def get_estado_postulacion_evaluador(db: Session, id_usuario: int):
    # Obtener la convocatoria actual
    convocatoria_actual = get_current_convocatoria(db)

    if not convocatoria_actual:
        raise HTTPException(status_code=404, detail="No se encontró ninguna convocatoria en curso")

    try:
        # Obtener el estado de la postulación
        sql_query = text(""" 
            SELECT estado_postulacion 
            FROM postulaciones_evaluadores 
            WHERE id_evaluador = :id_usuario 
            AND id_convocatoria = :convocatoria_actual
        """)
        result = db.execute(sql_query, {"id_usuario": id_usuario, "convocatoria_actual": convocatoria_actual}).fetchone()

        if not result:
            return {"estado_postulacion": 'sin postulacion'}

        # Acceder al primer valor de la tupla (estado_postulacion) usando el índice 0
        return {"estado_postulacion": result[0]}  # Aquí accedemos al valor de la primera columna

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al consultar la postulación del evaluador: {e}")

# Obtener la información institucional y académica del usuario
def get_informacion_institucional_academica(db: Session, id_usuario: int):
    try:
        # Consulta SQL para verificar si el usuario tiene registros en ambas tablas
        sql_query = text(""" 
            SELECT 
                (SELECT COUNT(*) FROM detalles_institucionales WHERE id_usuario = :id_usuario) AS existe_detalles_institucionales,
                (SELECT COUNT(*) FROM titulos_academicos WHERE id_usuario = :id_usuario) AS existe_titulos_academicos
        """)

        result = db.execute(sql_query, {"id_usuario": id_usuario}).fetchone()

        # Verificar si hay registros en ambas tablas
        existe_detalles_institucionales = result[0]
        existe_titulos_academicos = result[1]

        if existe_detalles_institucionales > 0 and existe_titulos_academicos > 0:
            return {"estado_institucional_academico": "con datos"}
        else:
            return {"estado_institucional_academico": "sin datos institucionales"}

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar la información institucional y académica")