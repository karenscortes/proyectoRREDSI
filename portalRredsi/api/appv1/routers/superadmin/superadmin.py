from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.superadmin.superadmin import get_all_admins, update_user_role, get_activity_history_by_admin
from appv1.schemas.superadmin.superadmin import SuperAdminResponse, UserRoleUpdateSchema, ActivityHistoryResponse
from db.database import get_db
from typing import List

router_superadmin = APIRouter()

# Obtener todos los administradores activos
@router_superadmin.get("/get-all-admin/", response_model=List[SuperAdminResponse])
async def read_all_admin(
    db: Session = Depends(get_db)
):
    administradores = get_all_admins(db)
    if not administradores:
        raise HTTPException(status_code=404, detail="Administradores no encontrados")
    return administradores

# Modificar el rol de un usuario
@router_superadmin.put("/update-role/", response_model=bool)
async def modify_user_role(user_role_update: UserRoleUpdateSchema, db: Session = Depends(get_db)):
    updated = update_user_role(db, user_id=user_role_update.user_id, new_role_id=user_role_update.new_role_id)
    if not updated:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el rol del usuario")
    return updated

# Obtener el historial de actividades de un administrador
@router_superadmin.get("/get-activity-history/{user_id}/", response_model=List[ActivityHistoryResponse])
async def get_activity_history(user_id: int, db: Session = Depends(get_db)):
    activity_history = get_activity_history_by_admin(db, user_id=user_id)
    if not activity_history:
        raise HTTPException(status_code=404, detail="No se encontró historial de actividades para este administrador")
    return activity_history
