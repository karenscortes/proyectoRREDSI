from sqlalchemy.orm import Session
from sqlalchemy import text

def get_all_applications(db: Session):
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
    """
    )
    result = db.execute(sql).fetchall()
    return result

def update_application_status(db: Session, id_evaluador:int, estado: str):
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

def get_all_certificates(db: Session,  id_usuario:int):
    sql = text("SELECT * FROM titulos_academicos WHERE id_usuario = :id_usuario")
    result = db.execute(sql, {"id_usuario": id_usuario}).fetchall()
    return result

