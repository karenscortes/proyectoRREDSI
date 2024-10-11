from datetime import date
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from appv1.schemas.delegado.asistencia import ConvocatoriaActual


def get_convocatoria_actual(db: Session):
    try:
        sql = text("SELECT * FROM convocatorias WHERE estado = 'en curso'")
        result = db.execute(sql).mappings().all()

        return [ConvocatoriaActual(**row) for row in result]
    except SQLAlchemyError as e:
        print(f"Error al obtener convocatorias: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener convocatorias")


# Todos los asistentes
def get_asistentes_por_convocatoria(db: Session, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        sql = text("""
            SELECT 
                asistentes.id_asistente, 
                asistentes.asistencia,
                asistentes.fecha,
                usuarios.id_usuario,
                usuarios.nombres, 
                usuarios.apellidos, 
                usuarios.documento 
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            LIMIT :page_size OFFSET :offset;
        """)
        
        params = {
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql, params).mappings().all()

        # Consulta SQL para contar el número total de asistentes
        count_sql = text("""SELECT COUNT(*)
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            """)
        
        total_asistentes = db.execute(count_sql).scalar()
        print("Total de asistentes:", total_asistentes)
        # Calcular el número total de páginas
        total_pages = (total_asistentes + page_size - 1) // page_size
        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar asistentes: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar asistentes")
    
# Asistentes por numero de sala    
def get_asistentes_por_sala(db: Session, numero_sala: str, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        sql = text("""
            SELECT  DISTINCT
                asistentes.id_asistente, 
                asistentes.asistencia,
                usuarios.id_usuario,
                usuarios.nombres, 
                usuarios.apellidos, 
                usuarios.documento
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            JOIN salas ON salas.id_usuario = usuarios.id_usuario
            JOIN detalles_institucionales ON asistentes.id_usuario = detalles_institucionales.id_usuario
            JOIN instituciones ON detalles_institucionales.id_institucion = instituciones.id_institucion
            JOIN convocatorias ON salas.id_convocatoria = convocatorias.id_convocatoria
            JOIN detalle_sala ON detalle_sala.id_sala = salas.id_sala
            JOIN proyectos_convocatoria ON detalle_sala.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN participantes_proyecto ON proyectos_convocatoria.id_proyecto_convocatoria = participantes_proyecto.id_proyectos_convocatoria
            WHERE salas.numero_sala = :numero_sala
            AND convocatorias.estado = 'en curso'
            LIMIT :page_size OFFSET :offset;
        """)
        params = {
            "numero_sala": numero_sala,
            "page_size": page_size,
            "offset": offset
        }
        
        result = db.execute(sql, params).mappings().all()
        # Consulta SQL para contar el número total de asistentes por sala
        count_sql = text("""SELECT COUNT(*)
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            JOIN salas ON salas.id_usuario = usuarios.id_usuario
            JOIN detalles_institucionales ON asistentes.id_usuario = detalles_institucionales.id_usuario
            JOIN instituciones ON detalles_institucionales.id_institucion = instituciones.id_institucion
            JOIN convocatorias ON salas.id_convocatoria = convocatorias.id_convocatoria
            JOIN detalle_sala ON detalle_sala.id_sala = salas.id_sala
            JOIN proyectos_convocatoria ON detalle_sala.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN participantes_proyecto ON proyectos_convocatoria.id_proyecto_convocatoria = participantes_proyecto.id_proyectos_convocatoria
            AND convocatorias.estado = 'en curso'""")

        total_asistentes = db.execute(count_sql, {"numero_sala": numero_sala}).scalar()
        total_pages = (total_asistentes + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar asistentes por sala: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar asistentes por sala")
    
# Asistentes por tipo (ponente, evaluador)
def get_asistentes_por_rol(db: Session, rol: str, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        sql = text("""
            SELECT 
                asistentes.id_asistente, 
                asistentes.asistencia,
                usuarios.id_usuario,
                usuarios.nombres, 
                usuarios.apellidos, 
                usuarios.documento, 
                roles.nombre AS rol
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            JOIN roles ON usuarios.id_rol = roles.id_rol
            WHERE roles.nombre = :rol
            LIMIT :page_size OFFSET :offset;
        """)
        params = {
            "rol": rol, 
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql, params).mappings().all()
        count_sql = text("""
            SELECT COUNT(*)
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            JOIN roles ON usuarios.id_rol = roles.id_rol
            WHERE roles.nombre = :rol;
        """)
        
        total_asistentes = db.execute(count_sql, {"rol": rol}).scalar()
        total_pages = (total_asistentes + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar asistentes: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar asistentes")

#Asistentes por cedula
def get_asistente_por_cedula(db: Session, documento: str):
    try:
        sql = text("""
            SELECT 
                asistentes.id_asistente, 
                asistentes.asistencia,
                usuarios.nombres, 
                usuarios.apellidos, 
                usuarios.documento, 
                instituciones.nombre AS institucion
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            JOIN participantes_proyecto ON usuarios.id_usuario = participantes_proyecto.id_usuario
            JOIN proyectos_convocatoria ON participantes_proyecto.id_proyectos_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            JOIN detalles_institucionales ON usuarios.id_usuario = detalles_institucionales.id_usuario
            JOIN instituciones ON detalles_institucionales.id_institucion = instituciones.id_institucion
            WHERE convocatorias.estado = 'en curso'
            AND usuarios.documento LIKE :documento
            
        """)
        params = {"documento": f"%{documento}%"}
        result = db.execute(sql, params).mappings().all()
        if not result:
            return None
        return dict(result)
    except SQLAlchemyError as e:
        print(f"Error al buscar asistente por documento: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar asistente")

#Actualizar check asistencia
def actualizar_asistencia(db: Session, id_asistente: int, id_usuario: int, asistencia: bool):
    sql = text("UPDATE asistentes SET asistencia = :asistencia WHERE id_asistente = :id_asistente AND id_usuario = :id_usuario")
    params = {
        "id_asistente": id_asistente,
        "id_usuario": id_usuario,
        "asistencia": asistencia
    }
    db.execute(sql, params)
    db.commit()
    return True

