from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

from appv1.schemas.evaluador.evaluador import CalificarProyectoRespuesta, Componente
from appv1.crud.evaluador.proyectos import get_datos_calificados_rubrica, get_nombres_ponentes_proyecto


# Consultar los evaluadores de un proyecto
def get_evaluadores_por_etapa(db: Session, id_proyecto: int, id_etapa: int):
    try:
        sql = text("""
            SELECT DISTINCT usuarios.id_usuario, usuarios.nombres, usuarios.apellidos, participantes_proyecto.id_etapa, etapas.nombre
            FROM participantes_proyecto
            JOIN proyectos ON participantes_proyecto.id_proyecto = proyectos.id_proyecto
            JOIN etapas ON participantes_proyecto.id_etapa = etapas.id_etapa
            JOIN usuarios ON participantes_proyecto.id_usuario = usuarios.id_usuario
            JOIN respuestas_rubricas ON usuarios.id_usuario = respuestas_rubricas.id_usuario 
            WHERE participantes_proyecto.id_proyecto = :id_proyecto
            AND participantes_proyecto.id_etapa = :id_etapa
        """)
        result = db.execute(sql, {"id_proyecto": id_proyecto, "id_etapa": id_etapa}).mappings().all()
        return result
    except SQLAlchemyError as e:
        print(f"Error al ejecutar la consulta: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

    
# Consultar los ponentes de un proyecto

def get_participantes_proyecto(db: Session, id_proyecto: int):
    try:
        sql = text("""
            SELECT usuarios.id_usuario, usuarios.nombres, usuarios.apellidos, usuarios.id_rol
            FROM participantes_proyecto 
            JOIN proyectos ON participantes_proyecto.id_proyecto = proyectos.id_proyecto
            JOIN usuarios ON participantes_proyecto.id_usuario = usuarios.id_usuario 
            JOIN roles ON usuarios.id_rol = roles.id_rol
            WHERE participantes_proyecto.id_proyecto = :id_p
            AND roles.nombre = 'Ponente'
        """)
        result = db.execute(sql, {"id_p": id_proyecto}).mappings().all()
        return result
    except SQLAlchemyError as e:
        print(f"Error al ejecutar la consulta: {e}")
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

    
#Consultar datos sala pertenecientes a un proyecto
def get_datos_sala(db: Session, id_proyecto:int):
    try:
        sql = text("""SELECT salas.numero_sala, detalle_sala.fecha,  detalle_sala.hora_inicio, detalle_sala.hora_fin
            FROM salas
            JOIN detalle_sala ON salas.id_sala = detalle_sala.id_sala
            JOIN proyectos_convocatoria ON detalle_sala.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN proyectos ON proyectos_convocatoria.id_proyecto = proyectos.id_proyecto
            WHERE proyectos.id_proyecto = :id_proyecto;
        """)
        result = db.execute(sql, {"id_proyecto": id_proyecto}).mappings().first() 
        return result
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Datos de sala no encontrados")
        
#Consultar todos los asistentes de una convocatoria en curso
def get_asistentes_evento(db: Session, id_convocatoria: int):
    try:
        sql = text("""
            SELECT DISTINCT asistentes.id_asistente, asistentes.id_convocatoria, asistentes.asistencia, asistentes.fecha,usuarios.id_usuario, usuarios.nombres, usuarios.apellidos, usuarios.documento
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            JOIN convocatorias ON asistentes.id_convocatoria = convocatorias.id_convocatoria
            JOIN proyectos_convocatoria ON convocatorias.id_convocatoria = proyectos_convocatoria.id_convocatoria
            WHERE convocatorias.estado = 'en curso'
            AND asistentes.asistencia = 1
            AND asistentes.id_convocatoria = :id_convocatoria
        """)
        params = {
            "id_convocatoria": id_convocatoria, 
        }
        result = db.execute(sql, params).mappings().all()
        return result 
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail="Error al consultar los asistentes del evento")



#Insertar suplente
def insertar_suplente_proyecto(db: Session, id_suplente: int, id_etapa: int, id_proyecto: int, id_proyectos_convocatoria: int, tipo_usuario: str, id_evaluador: int):
    try:
        ##Consulta para insertar en participantes proyecto (suplente)
        sql = text("""
            INSERT INTO participantes_proyecto (id_usuario, id_etapa, id_proyecto, id_proyectos_convocatoria, tipo_usuario)
            VALUES (:id_suplente, :id_etapa, :id_proyecto, :id_proyectos_convocatoria, :tipo_usuario)
        """)
        params = {
            "id_suplente": id_suplente,
            "id_etapa": id_etapa,
            "id_proyecto": id_proyecto,
            "id_proyectos_convocatoria": id_proyectos_convocatoria,
            "tipo_usuario": tipo_usuario,
        }
        db.execute(sql, params)
        
        ##Insertar evaluador reemplazado 
        if(tipo_usuario == 'suplenteEvaluador'):
            sqlEvaluador = text("""
            INSERT INTO evaluador_suplente (id_evaluador, id_suplente, id_proyecto )
            VALUES (:id_evaluador, :id_suplente, :id_proyecto)
            """)
            paramsEvaluador = {
                "id_evaluador": id_evaluador,
                "id_suplente": id_suplente,
                "id_proyecto": id_proyecto,
            }
            db.execute(sqlEvaluador, paramsEvaluador)
            
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al registrar evaluador reemplazado")
    
def get_obtener_suplentes(db: Session, id_proyecto: int, tipo_usuario: str, ):
    try:
        sql = text("""
            SELECT usuarios.nombres, usuarios.apellidos, participantes_proyecto.id_usuario,
                participantes_proyecto.id_proyecto,
                participantes_proyecto.tipo_usuario  
            FROM participantes_proyecto
            JOIN usuarios ON participantes_proyecto.id_usuario = usuarios.id_usuario
            WHERE (participantes_proyecto.tipo_usuario = 'suplenteEvaluador' 
                OR participantes_proyecto.tipo_usuario = 'suplentePonente')
            AND participantes_proyecto.id_proyecto = :id_proyecto
        """)
        
        result = db.execute(sql,{ "id_proyecto": id_proyecto, "tipo_usuario": tipo_usuario}).fetchall()
        return result
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar suplentes")

def get_obtener_suplente_evaluador(db: Session, id_proyecto: int, id_evaluador: int):
    try:
        sql= text("""
            SELECT id_suplente FROM evaluador_suplente 
            WHERE id_evaluador = :id_evaluador  
            AND id_proyecto = :id_proyecto
        """)
        params = {
            "id_proyecto": id_proyecto,
            "id_evaluador": id_evaluador,
        }
        result = db.execute(sql,params).mappings().all()
        return result
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar suplentes")


# Actualizar o insertar presentacion del proyecto
def insertar_o_actualizar_presentacion(db: Session, id_proyecto: int, url_presentacion: str):
    try:
        # Verificar si ya existe una presentación para el proyecto
        sql_select = text("""
            SELECT id_presentacion
            FROM presentaciones_proyectos
            WHERE id_proyecto = :id_proy
        """)
        result = db.execute(sql_select, {"id_proy": id_proyecto}).fetchone()
        
        # Si existe, se actualiza; si no, se inserta una nueva presentación
        if result:
            sql_update = text("""
                UPDATE presentaciones_proyectos
                SET url_presentacion = :url
                WHERE id_proyecto = :id_proy
            """)
            db.execute(sql_update, {"id_proy": id_proyecto, "url": url_presentacion})
        else:
            sql_insert = text("""
                INSERT INTO presentaciones_proyectos (id_proyecto, url_presentacion)
                VALUES (:id_proy, :url)
            """)
            db.execute(sql_insert, {"id_proy": id_proyecto, "url": url_presentacion})

        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al insertar o actualizar la URL de presentación")


# Obtener los datos para calificar un proyecto
def get_datos_proyecto_calificado_completo_suplente(db: Session, id_proyecto: int, id_usuario: int, nombre_etapa: str):
    try:
        # Obtener los datos básicos del proyecto y del por suplente
        sql_query = text(""" 
            SELECT 
                proyectos.titulo AS titulo_proyecto,
                inst_proyecto.nombre AS universidad_proyecto,
                usuarios.nombres AS nombre_evaluador,
                usuarios.documento AS cedula_evaluador,
                usuarios.correo AS email_evaluador,
                usuarios.celular AS celular_evaluador
            FROM 
                proyectos
            JOIN 
                participantes_proyecto ON proyectos.id_proyecto = participantes_proyecto.id_proyecto
            JOIN 
                usuarios ON usuarios.id_usuario = participantes_proyecto.id_usuario
            JOIN 
                instituciones AS inst_proyecto ON proyectos.id_institucion = inst_proyecto.id_institucion
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
            universidad_evaluador= "",
            email_evaluador=result.email_evaluador,
            celular_evaluador=result.celular_evaluador,
            nombres_ponentes=nombres_ponentes,  
            componentes=componentes_rubrica  
        )

        return proyecto_respuesta

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al consultar los datos del proyecto")


