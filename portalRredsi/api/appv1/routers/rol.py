from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.rol import get_roles, get_rol
from appv1.schemas.rol import RolResponse
from db.database import get_db

router_rol = APIRouter()

@router_rol.get("/get-all-roles/", response_model=List[RolResponse])
async def read_all_roles(
    db: Session = Depends(get_db)
):
    roles = get_roles(db)
    if len(roles) == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return roles


@router_rol.get("/get-rol_by_id/", response_model=RolResponse)
async def read_rol(
    id:int,
    db: Session = Depends(get_db)
):
    rol = get_rol(db,id)
    if rol is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return rol
