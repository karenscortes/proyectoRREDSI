from sqlalchemy.orm import Session
from sqlalchemy import text

def get_all_evaluators(db: Session):
    sql = text(
    """
        SELECT usuarios.id_usuario,
        usuarios.correo,
        usuarios.estado,
        usuarios.nombres,
        usuarios.apellidos,
        usuarios.celular,
        instituciones.nombre AS nombre_institucion,
        area1.nombre         AS area_conocimiento,
        area2.nombre         AS otra_area
        FROM usuarios
            INNER JOIN detalles_institucionales ON (usuarios.id_usuario = detalles_institucionales.id_usuario)
            INNER JOIN instituciones ON (detalles_institucionales.id_institucion = instituciones.id_institucion)
            LEFT JOIN areas_conocimiento area1 ON (detalles_institucionales.id_primera_area_conocimiento = area1.id_area_conocimiento)
            LEFT JOIN areas_conocimiento area2 ON (detalles_institucionales.id_segunda_area_conocimiento = area2.id_area_conocimiento)
        WHERE usuarios.id_rol  IN (
            SELECT id_rol
            FROM roles
            WHERE nombre = 'Evaluador'
		)

    """ 
    )
    result = db.execute(sql).fetchall()
    return result

def update_evaluator_status(db: Session, id_usuario:int, estado: str):
    sql = text("UPDATE usuarios SET estado = :estado WHERE id_usuario = :id_usuario")
    params = {
        "estado": estado,
        "id_usuario": id_usuario
    }
    db.execute(sql, params)
    db.commit()
    return True

def get_evaluator_by_document(db: Session, documento: str):
    sql = text(
    """
        SELECT usuarios.id_usuario,
        usuarios.correo,
        usuarios.estado,
        usuarios.nombres,
        usuarios.apellidos,
        usuarios.celular,
        instituciones.nombre AS nombre_institucion,
        area1.nombre         AS area_conocimiento,
        area2.nombre         AS otra_area
        FROM usuarios
            INNER JOIN detalles_institucionales ON (usuarios.id_usuario = detalles_institucionales.id_usuario)
            INNER JOIN instituciones ON (detalles_institucionales.id_institucion = instituciones.id_institucion)
            LEFT JOIN areas_conocimiento area1 ON (detalles_institucionales.id_primera_area_conocimiento = area1.id_area_conocimiento)
            LEFT JOIN areas_conocimiento area2 ON (detalles_institucionales.id_segunda_area_conocimiento = area2.id_area_conocimiento)
        WHERE usuarios.documento = :documento AND usuarios.id_rol IN (
            SELECT id_rol
            FROM roles
            WHERE nombre = 'Evaluador'
		)
    """
    )

    
    result = db.execute(sql, {"documento": documento}).fetchone()
    return result


