from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from appv1.crud.superadmin.superadmin import (
    get_all_admins, 
    update_user_role, 
    get_activity_history_by_admin
)
from appv1.schemas.superadmin.superadmin import (
    PaginatedAdminResponse, 
    UserRoleUpdateSchema, 
    ActivityHistoryResponse
)
from db.database import get_db
from typing import List

router_superadmin = APIRouter()

# Obtener todos los administradores activos con paginación
@router_superadmin.get("/get-all-admins/", response_model=PaginatedAdminResponse)
async def read_all_admins_by_page(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):
    # Obtener administradores paginados
    admins, total_pages = get_all_admins(db, page, page_size)

    # Retornar la respuesta en la estructura del esquema
    return {
        "admins": admins,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }

# Modificar el rol de un usuario
@router_superadmin.put("/update-role/", response_model=bool)
async def modify_user_role(
    user_role_update: UserRoleUpdateSchema, 
    db: Session = Depends(get_db)
):
    # Actualizar rol
    updated = update_user_role(db, user_id=user_role_update.user_id, new_role_id=user_role_update.new_role_id)
    return updated

# Obtener el historial de actividades de un administrador
@router_superadmin.get("/get-activity-history/{user_id}/", response_model=List[ActivityHistoryResponse])
async def get_activity_history(
    user_id: int, 
    db: Session = Depends(get_db)
):
    # Obtener historial de actividades
    return get_activity_history_by_admin(db, user_id=user_id)

