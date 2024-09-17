from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.usuarios import create_user_sql,  get_user_by_email, get_user_by_id,update_user_profile
from appv1.routers.login import get_current_user
from appv1.schemas.usuario import UserCreate, UserResponse, UserUpdate
from db.database import get_db
from appv1.crud.permissions import get_permissions


router_user = APIRouter()
MODULE = 3

@router_user.post("/create")
async def insert_user(
    user: UserCreate, 
    db: Session = Depends(get_db),
    current_user : UserResponse =Depends(get_current_user)
    
):

    respuesta = create_user_sql(db, user)
    if respuesta:
        return {"mensaje":"Usuario ingresado exitosamente"}
        
# Verificar si el email ya está registrado
    existing_user = get_user_by_email(db, user.correo)
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    respuesta = create_user_sql(db, user)
    if respuesta:
        return {"mensaje":"usuario registrado con éxito"}
    
@router_user.put("/update/", response_model=dict)
def update_user_by_id(
    user_id: int, 
    user: UserUpdate,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
        
    verify_user = get_user_by_id(db, user_id)
    if verify_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    verify_new_email = get_user_by_email(db, user.correo)
    if verify_new_email:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    db_user = update_user_profile(db, user_id, user)
    if db_user:
        return {"mensaje": "registro actualizado con éxito" }