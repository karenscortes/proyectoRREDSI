from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.usuarios import get_user_by_email
from appv1.crud.ponente import create_user_ponente_project
from appv1.schemas.ponente import UserPonenteCreate
from db.database import get_db


router_userPonente = APIRouter()

@router_userPonente.post("/create")
async def insert_user(
    userPonente: UserPonenteCreate, 
    db: Session = Depends(get_db),
    
):

    respuesta = create_user_ponente_project(db, userPonente)
    if respuesta:
        return {"mensaje":"Usuario ingresado exitosamente"}
        
# Verificar si el email ya está registrado
    existing_user = get_user_by_email(db, userPonente.correo)
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    respuesta = create_user_ponente_project(db, userPonente)
    if respuesta:
        return {"mensaje":"usuario registrado con éxito"}