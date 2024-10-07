from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text


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
def insertar_suplente_proyecto(db: Session, id_usuario: int, id_etapa: int, id_proyecto: int, id_proyectos_convocatoria: int, tipo_usuario: str):
    try:
        sql = text("""
            INSERT INTO participantes_proyecto (id_usuario, id_etapa, id_proyecto, id_proyectos_convocatoria, tipo_usuario)
            VALUES (:id_usuario, :id_etapa, :id_proyecto, :id_proyectos_convocatoria, :tipo_usuario)
        """)
        params = {
            "id_usuario": id_usuario,
            "id_etapa": id_etapa,
            "id_proyecto": id_proyecto,
            "id_proyectos_convocatoria": id_proyectos_convocatoria,
            "tipo_usuario": tipo_usuario,
        }
        db.execute(sql, params)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al registrar el suplente")


#Insertar presentacion del proyecto
def insertar_presentacion_proyecto(db: Session, id_proyecto: int, url_presentacion: str):
    try:
        sql = text("""
            INSERT INTO presentaciones_proyectos (id_proyecto, url_presentacion)
            VALUES (:id_proy, :url)
        """)
        params = {
            "id_proy": id_proyecto,
            "url": url_presentacion
        }
        
        db.execute(sql, params)
        db.commit() 
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail="Error al insertar URL de presentación")
