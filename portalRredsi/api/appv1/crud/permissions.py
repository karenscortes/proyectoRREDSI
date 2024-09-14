from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# consultar permisos de un rol por modulo
def get_permissions(db: Session, rol: int, module: int):
    try:
        sql = text("SELECT p_consultar, p_insertar, p_actualizar, p_eliminar FROM permisos WHERE id_rol = :rol AND id_modulo = :module")
        result = db.execute(sql, {"rol": rol, "module": module}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener permisos: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener permisos")

# consultar todos los permisos de un rol
def get_all_permissions(db: Session, rol: int):
    try:
        sql = text("SELECT id_modulo, p_consultar FROM permisos WHERE id_rol = :rol")
        result = db.execute(sql, {"rol": rol}).mappings().all()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener permisos: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener permisos")
