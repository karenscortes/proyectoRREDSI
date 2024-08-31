from sqlalchemy.orm import Session
from sqlalchemy import text

def get_roles(db: Session):
    sql = text("SELECT * FROM roles")
    result = db.execute(sql).fetchall()
    return result

def get_rol(db: Session, id_rol: str):
    sql = text("SELECT * FROM roles WHERE id_rol = :id_rol")
    result = db.execute(sql, {"id_rol": id_rol}).fetchone()
    return result