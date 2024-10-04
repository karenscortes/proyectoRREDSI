from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.superadmin.superadmin import (
    PaginatedActivityHistoryResponse,
    PaginatedAdminResponse, 
    UserRoleUpdateSchema, 
    ActivityHistoryResponse,
    UserStatusUpdateResponse
)
from appv1.crud.superadmin.superadmin import (
    cambiar_estado_usuario,
    get_all_admins, 
    update_user_role, 
    get_activity_history_by_admin
)
from appv1.crud.permissions import get_permissions
from appv1.schemas.usuario import UserResponse
from db.database import get_db

router_superadmin = APIRouter()

# Definir correctamente los módulos
MODULE_ADMINISTRADORES = 3
MODULE_ACTIVIDADES = 18

# Obtener todos los administradores activos con paginación
@router_superadmin.get("/get-all-admins/", response_model=PaginatedAdminResponse)
async def read_all_admins_by_page(
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_ADMINISTRADORES)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")

    admins, total_pages = get_all_admins(db, page, page_size)
    
    return {
        "admins": admins,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }

@router_superadmin.put("/usuarios/{user_id}/estado", response_model=UserStatusUpdateResponse)
def cambiar_estado(user_id: int, db: Session = Depends(get_db)):
    
    resultado = cambiar_estado_usuario(db, user_id)

    if not resultado:
        raise HTTPException(status_code=400, detail="Error al cambiar el estado del usuario")

    # Devolvemos el esquema con la respuesta completa
    return UserStatusUpdateResponse(
        message=resultado["message"]
    )

# Modificar el rol de un usuario
@router_superadmin.put("/update-role/", response_model=bool)
async def modify_user_role(
    user_role_update: UserRoleUpdateSchema, 
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_ADMINISTRADORES)
    if not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    updated = update_user_role(db, user_id=user_role_update.user_id, new_role_id=user_role_update.new_role_id)
    return updated


# Traer paginas de historial de admin/delegado
@router_superadmin.get("/get-activity-history/{user_id}/", response_model=PaginatedActivityHistoryResponse)
async def get_activity_history(
    user_id: int, 
    page: int = 1,  
    page_size: int = 10,  
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_ACTIVIDADES)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    # Calcular offset
    offset = (page - 1) * page_size

    # Llamar al CRUD con limit y offset en lugar de page y page_size
    activities = get_activity_history_by_admin(db, user_id=user_id, offset=offset, limit=page_size)

    # Obtener el total de actividades para calcular total_pages
    total_activities = db.execute(text("""
        SELECT COUNT(*) FROM historial_actividades_admin
        WHERE id_usuario = :user_id
    """), {"user_id": user_id}).scalar()

    total_pages = (total_activities + page_size - 1) // page_size

    return {
        "activities": activities,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }


