from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.superadmin.superadmin import get_all_admin
from appv1.schemas.usuario import UserResponse
from db.database import get_db

router_superadmin = APIRouter()

@router_superadmin.get("/get-all-admin/", response_model=List[UserResponse])
async def read_all_admin(
    db: Session = Depends(get_db)
):
    administradores = get_all_admin(db)
    if len(administradores) == 0:
        raise HTTPException(status_code=404, detail="Administradores no encontrados")
    return administradores

