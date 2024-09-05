from sqlalchemy.orm import Session
from sqlalchemy import text

def get_all_applications(db: Session,  id_convocatoria:int):
    sql = text("SELECT postulaciones_evaluadores.*, usuarios.correo, detalles_personales.nombres,detalles_personales.apellidos, detalles_personales.celular,instituciones.nombre AS nombre_institucion, area1.nombre AS area_conocimiento, area2.nombre AS otra_area FROM postulaciones_evaluadores INNER JOIN usuarios ON(postulaciones_evaluadores.id_evaluador = usuarios.id_usuario) INNER JOIN detalles_personales ON(usuarios.id_usuario = detalles_personales.id_usuario) INNER JOIN instituciones ON (detalles_personales.id_institucion = instituciones.id_institucion) LEFT JOIN areas_conocimiento area1 ON (detalles_personales.area_conocimiento = area1.id_area_conocimiento) LEFT JOIN areas_conocimiento area2 ON (detalles_personales.otra_area = area2.id_area_conocimiento) WHERE postulaciones_evaluadores.id_convocatoria = :id_convocatoria AND postulaciones_evaluadores.estado ='pendiente'")
    result = db.execute(sql, {"id_convocatoria": id_convocatoria}).fetchall()
    return result

def update_application_status(db: Session,  id_convocatoria:int, id_evaluador:int, estado: str):
    sql = text("UPDATE postulaciones_evaluadores SET estado = :estado WHERE id_convocatoria = :id_convocatoria AND id_evaluador = :id_evaluador")
    params = {
        "estado": estado,
        "id_convocatoria": id_convocatoria,
        "id_evaluador": id_evaluador
    }
    db.execute(sql, params)
    db.commit()
    return True

def get_all_certificates(db: Session,  id_usuario:int):
    sql = text("SELECT * FROM titulos_academicos WHERE id_usuario = :id_usuario")
    result = db.execute(sql, {"id_usuario": id_usuario}).fetchall()
    return result

def get_convocatoria(db: Session):
    sql = text("SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso'")
    result = db.execute(sql).fetchone()
    return result
