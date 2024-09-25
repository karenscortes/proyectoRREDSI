from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.evaluador import create_evaluador_sql, get_user_by_email
from appv1.routers.login import get_current_user
from appv1.schemas.evaluador import EvaluadorCreate
from appv1.schemas.usuario import UserCreate, UserResponse, UserUpdate
from core.security import get_hashed_password
from db.database import get_db
from appv1.crud.permissions import get_permissions


router_evaluador = APIRouter()

@router_evaluador.post("/create")
async def insert_evaluador(
    evaluador: EvaluadorCreate, 
    db: Session = Depends(get_db),
    current_user : UserResponse =Depends(get_current_user)
    
):

    respuesta = create_evaluador_sql(db, evaluador)
    if respuesta:
        return {"mensaje":"Usuario ingresado exitosamente"}
        
# Verificar si el email ya está registrado
    existing_user = get_user_by_email(db, evaluador.correo)
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    respuesta = create_evaluador_sql(db, evaluador)
    if respuesta:
        return {"mensaje":"usuario registrado con éxito"}