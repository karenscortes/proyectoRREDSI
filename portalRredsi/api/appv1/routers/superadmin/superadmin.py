from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.superadmin.superadmin import get_all_admin, update_user_role
from appv1.schemas.superadmin.superadmin import SuperAdminResponse, UserRoleUpdateSchema
from db.database import get_db
from typing import List

router_superadmin = APIRouter()

@router_superadmin.get("/get-all-admin/", response_model=List[SuperAdminResponse])
async def read_all_admin(
    db: Session = Depends(get_db)
):
    administradores = get_all_admin(db)
    if not administradores:
        raise HTTPException(status_code=404, detail="Administradores no encontrados")
    return administradores

@router_superadmin.put("/update-role/", response_model=bool)
async def modify_user_role(user_role_update: UserRoleUpdateSchema, db: Session = Depends(get_db)):
    updated = update_user_role(db, user_id=user_role_update.user_id, new_role_id=user_role_update.new_role_id)
    if not updated:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el rol del usuario")
    return updated