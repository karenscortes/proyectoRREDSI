from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.superadmin.superadmin import (
    get_all_admins, 
    update_user_role, 
    get_activity_history_by_admin
)
from appv1.schemas.superadmin.superadmin import (
    AdminResponse, 
    UserRoleUpdateSchema, 
    ActivityHistoryResponse
)
from db.database import get_db
from appv1.routers.login import get_current_user
from appv1.schemas.usuario import UserResponse  # Esquema del usuario autenticado
from appv1.crud.permissions import get_permissions  # Si usas permisos
from typing import List

router_superadmin = APIRouter()

# Definir el nombre del módulo (por ejemplo, "superadmin") para verificar permisos
MODULE = 3

# Obtener todos los administradores activos con paginación
@router_superadmin.get("/get-all-admins/", response_model=List[AdminResponse])
async def read_all_admins_by_page(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    # Verificar permisos
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if not permisos.p_select:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    # Obtener administradores paginados
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
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    # Verificar permisos
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if not permisos.p_update:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    # Actualizar rol
    updated = update_user_role(db, user_id=user_role_update.user_id, new_role_id=user_role_update.new_role_id)
    if not updated:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el rol del usuario")
    return updated

# Obtener el historial de actividades de un administrador
@router_superadmin.get("/get-activity-history/{user_id}/", response_model=List[ActivityHistoryResponse])
async def get_activity_history(
    user_id: int, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    # Verificar permisos
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if not permisos.p_select:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    # Obtener historial de actividades
    activity_history = get_activity_history_by_admin(db, user_id=user_id)
    if not activity_history:
        raise HTTPException(status_code=404, detail="No se encontró historial de actividades para este administrador")
    return activity_history
