from sqlalchemy.orm import Session
from sqlalchemy import text

def get_all_evaluators(db: Session,  id_rol:int):
    sql = text("SELECT usuarios.correo, usuarios.estado, detalles_personales.nombres,detalles_personales.apellidos, detalles_personales.celular,instituciones.nombre AS nombre_institucion, area1.nombre AS area_conocimiento, area2.nombre AS otra_area FROM usuarios INNER JOIN detalles_personales ON(usuarios.id_usuario = detalles_personales.id_usuario) INNER JOIN instituciones ON (detalles_personales.id_institucion = instituciones.id_institucion) LEFT JOIN areas_conocimiento area1 ON (detalles_personales.area_conocimiento = area1.id_area_conocimiento) LEFT JOIN areas_conocimiento area2 ON (detalles_personales.otra_area = area2.id_area_conocimiento) WHERE usuario.id_rol = :id_rol")
    result = db.execute(sql, {"id_rol": id_rol}).fetchall()
    return result

def get_id_rol(db:Session, nombre:str):
    sql = text("SELECT id_rol FROM roles WHERE nombre = :nombre")
    result = db.execute(sql, {"nombre": nombre}).fetchone()
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
    sql = text("SELECT usuarios.correo, usuarios.estado, detalles_personales.nombres,detalles_personales.apellidos, detalles_personales.celular,instituciones.nombre AS nombre_institucion, area1.nombre AS area_conocimiento, area2.nombre AS otra_area FROM usuarios INNER JOIN detalles_personales ON(usuarios.id_usuario = detalles_personales.id_usuario) INNER JOIN instituciones ON (detalles_personales.id_institucion = instituciones.id_institucion) LEFT JOIN areas_conocimiento area1 ON (detalles_personales.area_conocimiento = area1.id_area_conocimiento) LEFT JOIN areas_conocimiento area2 ON (detalles_personales.otra_area = area2.id_area_conocimiento) WHERE detalles_personales.documento = :documento")
    result = db.execute(sql, {"documento": documento}).fetchone()
    return result


