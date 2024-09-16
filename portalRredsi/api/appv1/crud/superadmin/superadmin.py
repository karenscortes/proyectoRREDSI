from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

# Consultar administradores con paginación
def get_all_admins(db: Session, page: int = 1, page_size: int = 10):
    try:
        # Calcular el offset basado en el número de página y el tamaño de página
        offset = (page - 1) * page_size

        # Consulta SQL con paginación, incluyendo todos los campos requeridos
        sql = text("""
            SELECT
                usuarios.id_usuario,
                usuarios.id_rol,
                usuarios.documento,
                usuarios.nombres,  
                usuarios.apellidos,  
                usuarios.correo,
                usuarios.estado,
                usuarios.celular AS telefono,  
                NULL AS direccion,  
                roles.nombre AS rol_nombre
            FROM usuarios
            JOIN roles ON usuarios.id_rol = roles.id_rol
            WHERE (usuarios.id_rol = 3 OR usuarios.id_rol = 2)
            AND usuarios.estado = 'activo'
            LIMIT :page_size OFFSET :offset;
        """)
        params = {
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql, params).mappings().all()

        # Obtener el número total de administradores activos
        count_sql = text("""
            SELECT COUNT(usuarios.id_usuario)
            FROM usuarios
            WHERE usuarios.id_rol = 3
            AND usuarios.estado = 'activo';
        """)
        total_admins = db.execute(count_sql).scalar()

        # Calcular el número total de páginas
        total_pages = (total_admins + page_size - 1) // page_size

        # Verificar si se encontraron administradores
        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron administradores activos")

        return result, total_pages

    except SQLAlchemyError as e:
        print(f"Error al buscar administradores: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar administradores")

# Actualizar el rol de un usuario si es un administrador activo
def update_user_role(db: Session, user_id: int, new_role_id: int):
    try:
        # Verificar si el usuario es un administrador o delegado activo
        sql_check = text("SELECT id_usuario, id_rol FROM usuarios WHERE id_usuario = :user_id AND (id_rol = 2 OR id_rol = 3) AND estado = 'activo'")
        params_check = {"user_id": user_id}
        user_to_update = db.execute(sql_check, params_check).fetchone()

        if not user_to_update:
            raise HTTPException(status_code=404, detail="Usuario no encontrado o no es un administrador o delegado activo")

        current_role_id = user_to_update[1]

        if current_role_id == new_role_id:
            raise HTTPException(status_code=400, detail="El usuario ya tiene el rol seleccionado")

        # Proceder con la actualización del rol
        sql_update = text("UPDATE usuarios SET id_rol = :new_role_id WHERE id_usuario = :user_id AND estado = 'activo'")
        params_update = {"new_role_id": new_role_id, "user_id": user_id}

        db.execute(sql_update, params_update)
        db.commit()
        return True  # Return a boolean value indicating success
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
