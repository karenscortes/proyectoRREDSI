from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Todos los asistentes
def get_asistentes_por_convocatoria(db: Session, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        sql = text("""
            SELECT 
                asistentes.id_asistente, 
                asistentes.asistencia,
                detalles_personales.nombres, 
                detalles_personales.apellidos, 
                detalles_personales.documento, 
                instituciones.nombre
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            JOIN participantes_proyecto ON usuarios.id_usuario = participantes_proyecto.id_usuario
            JOIN proyectos_convocatoria ON participantes_proyecto.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            JOIN instituciones ON usuarios.id_usuario = detalles_institucionales.id_usuario
            WHERE convocatorias.estado = 'en curso'
            LIMIT :page_size OFFSET :offset;
        """)
        
        params = {
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql, params).mappings().all()

        # Consulta SQL para contar el número total de asistentes
        count_sql = text("""SELECT COUNT(*) FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuarios.id_usuario
            JOIN participantes_proyecto ON usuarios.id_usuario = participantes_proyecto.id_usuario
            JOIN proyectos_convocatoria ON participantes_proyecto.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            JOIN instituciones ON usuarios.id_usuario = detalles_institucionales.id_usuario
            WHERE convocatorias.estado = 'en curso' """)
        total_asistentes = db.execute(count_sql).scalar()

        # Calcular el número total de páginas
        total_pages = (total_asistentes + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar asistentes: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar asistentes")


# Asistentes por sala 
def get_asistentes_por_sala(db: Session, numero_sala: str, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        sql = text("""
            SELECT 
                asistentes.id_asistente, 
                asistentes.asistencia,
                usuarios.documento, 
                usuarios.nombres, 
                usuarios.apellidos, 
                instituciones.nombre
            FROM asistentes
            JOIN usuarios ON asistentes.id_usuario = usuario.id_usuario
            JOIN participantes_proyecto ON usuarios.id_usuario = participantes_proyecto.id_usuario
            JOIN proyectos_convocatoria ON participantes_proyecto.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            JOIN detalle_sala ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria
            JOIN salas ON detalle_sala.id_sala = salas.id_sala
            JOIN instituciones ON detalles_personales.id_institucion = instituciones.id_institucion
            WHERE convocatorias.estado = 'en curso'
            AND salas.numero_sala = :numero_sala
            LIMIT :page_size OFFSET :offset;
        """)

        params = {
            "numero_sala": numero_sala,
            "page_size": page_size,
            "offset": offset
        }
        
        result = db.execute(sql, params).mappings().all()

        # Consulta SQL para contar el número total de asistentes por sala
        count_sql = text("""SELECT COUNT(*)FROM FROM asistentes
            JOIN detalles_personales ON asistentes.id_detalles_personales = detalles_personales.id_detalle_personal
            JOIN participantes_proyecto ON detalles_personales.id_detalle_personal = participantes_proyecto.id_datos_personales
            JOIN proyectos_convocatoria ON participantes_proyecto.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            JOIN detalle_sala ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria
            JOIN salas ON detalle_sala.id_sala = salas.id_sala
            JOIN instituciones ON detalles_personales.id_institucion = instituciones.id_institucion
            WHERE convocatorias.estado = 'en curso'
            AND salas.numero_sala = :numero_sala""")

        total_asistentes = db.execute(count_sql, {"numero_sala": numero_sala}).scalar()
        total_pages = (total_asistentes + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar asistentes por sala: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar asistentes por sala")

    
# Asistentes por tipo (ponente, evaluador)

def get_asistentes_por_tipo(db: Session, tipo_asistente: str, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        sql= text("""
            SELECT
                asistentes.id_asistente, 
                asistentes.asistencia,
                asistentes.tipo_asistente,
                detalles_personales.nombres, 
                detalles_personales.apellidos, 
                detalles_personales.documento, 
                instituciones.nombre
            FROM asistentes
            JOIN detalles_personales ON asistentes.id_detalles_personales = detalles_personales.id_detalle_personal
            JOIN participantes_proyecto ON detalles_personales.id_detalle_personal = participantes_proyecto.id_datos_personales
            JOIN proyectos_convocatoria ON participantes_proyecto.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
            JOIN detalle_sala ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria
            JOIN salas ON detalle_sala.id_sala = salas.id_sala
            JOIN instituciones ON detalles_personales.id_institucion = instituciones.id_institucion
            WHERE asistentes.tipo_asistente IN ('ponente', 'evaluador')
            LIMIT :page_size OFFSET :offset;
            """)
        params = {
            "tipo_asistente": tipo_asistente,
            "page_size": page_size,
            "offset": offset
        }
    
    except SQLAlchemyError as e:
        print(f"Error al buscar asistentes por tipo: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar asistentes por tipo")
