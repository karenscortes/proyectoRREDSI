from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import text

def get_all_admin(db: Session):
    try:
        sql = text("SELECT id_usuario, id_rol, correo, estado FROM usuarios WHERE id_rol = 3")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar administradores: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar administradores")
    
def update_user_role(db: Session, user_id: int, new_role_id: int):
    try:
        sql = text("UPDATE usuarios SET id_rol = :new_role_id WHERE id_usuario = :user_id")
        params = {"new_role_id": new_role_id, "user_id": user_id}
        
        db.execute(sql, params)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error
        print(f"Error al actualizar rol de usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar rol de usuario")

