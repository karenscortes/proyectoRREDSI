from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from appv1.models import Usuario
from appv1.models.usuario import Estados

from appv1.schemas.superadmin.superadmin import EstadoEnum

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
            WHERE (usuarios.id_rol = 3 OR usuarios.id_rol = 2);
        """)
        total_admins = db.execute(count_sql).scalar()

        # Calcular el número total de páginas
        total_pages = (total_admins + page_size - 1) // page_size

        # Verificar si se encontraron administradores
        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron administradores activos")

        return result, total_pages

    except SQLAlchemyError as e:
        print(f"Error al buscar administradores y delegados: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar administradores y delegados")

# Actualizar el rol de un usuario si es un administrador/delegado
def update_user_role(db: Session, user_id: int, new_role_id: int):
    try:
        # Verificar si el usuario es un administrador o delegado activo
        sql_check = text("SELECT id_usuario, id_rol FROM usuarios WHERE id_usuario = :user_id AND (id_rol = 2 OR id_rol = 3)")
        params_check = {"user_id": user_id}
        user_to_update = db.execute(sql_check, params_check).fetchone()

        if not user_to_update:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        current_role_id = user_to_update[1]

        if current_role_id == new_role_id:
            raise HTTPException(status_code=400, detail="El usuario ya tiene el rol seleccionado")

        # Proceder con la actualización del rol
        sql_update = text("UPDATE usuarios SET id_rol = :new_role_id WHERE id_usuario = :user_id")
        params_update = {"new_role_id": new_role_id, "user_id": user_id}

        db.execute(sql_update, params_update)
        db.commit()
        return True  # Return a boolean value indicating success
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error
        print(f"Error al actualizar rol de usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar rol de usuario")


def cambiar_estado_usuario(db: Session, user_id: int):
    try:
        # Obtener el usuario por ID
        usuario = db.query(Usuario).filter(Usuario.id_usuario == user_id).first()

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Cambiar el estado de activo a inactivo o viceversa
        if usuario.estado == Estados.activo:
            nuevo_estado = Estados.inactivo
        elif usuario.estado == Estados.inactivo:
            nuevo_estado = Estados.activo
        else:
            raise HTTPException(status_code=400, detail="Estado del usuario inválido")

        # Asignar el nuevo estado al usuario
        usuario.estado = nuevo_estado

        # Guardar los cambios en la base de datos
        db.commit()
        db.refresh(usuario)  # Refrescar el objeto para reflejar los nuevos valores

        # Debug: Mostrar el nuevo estado para asegurarse de que se cambió
        print(f"Nuevo estado del usuario: {usuario.estado}")

        return {
            "message": f"El estado del usuario ha sido cambiado a {nuevo_estado.value}"
        }

    except Exception as e:
        # Manejo de excepciones en caso de error en la transacción
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al cambiar el estado del usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al cambiar el estado del usuario")


def get_activity_history_by_admin(db: Session, user_id: int, offset: int = 0, limit: int = 10):
    try:
        # Consulta SQL para obtener el historial de actividades por id_usuario con paginación
        sql = text("""
            SELECT 
                historial_actividades_admin.id_actividad,
                historial_actividades_admin.accion,
                historial_actividades_admin.fecha,
                historial_actividades_admin.id_modulo,   
                modulos.nombre AS modulo_nombre,
                historial_actividades_admin.id_registro,
                usuarios.id_usuario, 
                usuarios.correo 
            FROM historial_actividades_admin
            JOIN usuarios ON historial_actividades_admin.id_usuario = usuarios.id_usuario 
            JOIN modulos ON historial_actividades_admin.id_modulo = modulos.id_modulo
            WHERE usuarios.id_usuario = :user_id
            ORDER BY historial_actividades_admin.fecha DESC
            LIMIT :limit OFFSET :offset
        """)
        
        params = {"user_id": user_id, "limit": limit, "offset": offset}
        
        # Ejecutar la consulta
        result = db.execute(sql, params).fetchall()

        # Si no hay resultados, lanzar un error 404
        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron actividades para este administrador/delegado")
        
        # Retornar el resultado
        return result

    except SQLAlchemyError as e:
        # Manejo de errores de SQLAlchemy
        print(f"Error al buscar el historial de actividades: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar el historial de actividades")


