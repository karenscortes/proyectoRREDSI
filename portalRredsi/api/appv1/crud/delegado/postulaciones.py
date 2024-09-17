from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

def get_all_applications(db: Session, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        sql = text(
        """
        SELECT postulaciones_evaluadores.*,
        usuarios.correo,
        usuarios.nombres,
        usuarios.apellidos,
        usuarios.celular,
        instituciones.nombre AS nombre_institucion,
        area1.nombre         AS area_conocimiento,
        area2.nombre         AS otra_area
            FROM postulaciones_evaluadores
                INNER JOIN usuarios ON (postulaciones_evaluadores.id_evaluador = usuarios.id_usuario)
                INNER JOIN detalles_institucionales ON (usuarios.id_usuario = detalles_institucionales.id_usuario)
                INNER JOIN instituciones ON (detalles_institucionales.id_institucion = instituciones.id_institucion)
                LEFT JOIN areas_conocimiento area1 ON (detalles_institucionales.id_primera_area_conocimiento = area1.id_area_conocimiento)
                LEFT JOIN areas_conocimiento area2 ON (detalles_institucionales.id_segunda_area_conocimiento= area2.id_area_conocimiento)
            WHERE postulaciones_evaluadores.estado_postulacion = 'pendiente'
            AND postulaciones_evaluadores.id_convocatoria IN (
                SELECT id_convocatoria 
                FROM convocatorias 
                WHERE estado = 'en curso'
            )
            LIMIT :page_size OFFSET :offset
        """
        )

        params = {
            "page_size": page_size,
            "offset": offset
        }

        result = db.execute(sql, params).mappings().all()

        count_sql = text("SELECT COUNT(id_evaluador) AS cantidad_postulaciones FROM postulaciones_evaluadores WHERE id_convocatoria IN (SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso') AND estado_postulacion = 'pendiente'")

        total_postulaciones = db.execute(count_sql).scalar()

        total_pages = (total_postulaciones + page_size - 1) // page_size
        return result,total_pages
    
    except SQLAlchemyError as e:
        print(f"Error al obtener postulaciones de evaluadores: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener todas las postulaciones de evaluadores")


def update_application_status(db: Session, id_evaluador:int, estado: str):
    try:
        sql = text(
        """
            UPDATE postulaciones_evaluadores SET estado_postulacion = :estado 
            WHERE id_evaluador = :id_evaluador AND id_convocatoria IN (
                SELECT id_convocatoria 
                FROM convocatorias 
                WHERE estado = 'en curso'
            )
        """
        )

        params = {
            "estado": estado,
            "id_evaluador": id_evaluador
        }
        db.execute(sql, params)
        db.commit()
        return True
    except SQLAlchemyError as e:
        print(f"Error al actualizar estado de postulación: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar estado de postulación")

def get_certificates_by_id(db: Session,  id_usuario:int):
    try:
        sql = text("SELECT * FROM titulos_academicos WHERE id_usuario = :id_usuario")
        result = db.execute(sql, {"id_usuario": id_usuario}).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener titulos academicos por usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener titulos academicos por usuario")

