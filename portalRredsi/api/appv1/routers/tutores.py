from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.usuarios import  get_user_by_email
from appv1.schemas.tutor import UserTutorCreate
from db.database import get_db
from appv1.crud.tutor import create_user_tutor_project



router_userTutor = APIRouter()

@router_userTutor.post("/create")
async def insert_user(
    userTutor: UserTutorCreate, 
    db: Session = Depends(get_db),
    
):

    respuesta = create_user_tutor_project(db, userTutor)
    if respuesta:
        return {"mensaje":"Usuario ingresado exitosamente"}
        
# Verificar si el email ya está registrado
    existing_user = get_user_by_email(db, userTutor.correo)
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    respuesta = create_user_tutor_project(db, userTutor)
    if respuesta:
        return {"mensaje":"usuario registrado con éxito"}