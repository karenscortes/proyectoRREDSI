from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

# Consultar todos los administradores activos
def get_all_admin(db: Session):
    try:
        sql = text("SELECT id_usuario, id_rol, correo, estado FROM usuarios WHERE id_rol = 3 AND estado = 'activo'")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar administradores: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar administradores")

# Actualizar el rol de un usuario si es un administrador activo
def update_user_role(db: Session, user_id: int, new_role_id: int):
    try:
        # Verificar si el usuario es un administrador activo
        sql_check = text("SELECT id_usuario FROM usuarios WHERE id_usuario = :user_id AND id_rol = 3 AND estado = 'activo'")
        params_check = {"user_id": user_id}
        user_to_update = db.execute(sql_check, params_check).fetchone()

        if not user_to_update:
            raise HTTPException(status_code=404, detail="Usuario no encontrado o no es un administrador activo")

        # Proceder con la actualización del rol
        sql_update = text("UPDATE usuarios SET id_rol = :new_role_id WHERE id_usuario = :user_id AND estado = 'activo'")
        params_update = {"new_role_id": new_role_id, "user_id": user_id}

        db.execute(sql_update, params_update)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error
        print(f"Error al actualizar rol de usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar rol de usuario")

# Obtener historial de actividades por administrador (sin importar el estado)
def get_activity_history_by_admin(db: Session, user_id: int):
    try:
        sql = text("""
            SELECT actividades.id_actividad, actividades.descripcion, actividades.fecha, usuarios.id_usuario, usuarios.correo 
            FROM actividades 
            JOIN usuarios ON actividades.id_usuario = usuarios.id_usuario 
            WHERE usuarios.id_usuario = :user_id
        """)
        params = {"user_id": user_id}
        result = db.execute(sql, params).fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron actividades para este administrador")
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar el historial de actividades: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar el historial de actividades")