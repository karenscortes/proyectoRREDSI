from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.superadmin.superadmin import (
    PaginatedAdminResponse, 
    UserRoleUpdateSchema, 
    ActivityHistoryResponse
)
from appv1.crud.superadmin.superadmin import (
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

# Obtener el historial de actividades de un administrador
@router_superadmin.get("/get-activity-history/{user_id}/", response_model=List[ActivityHistoryResponse])
async def get_activity_history(
    user_id: int, 
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_ACTIVIDADES)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    return get_activity_history_by_admin(db, user_id=user_id)
