from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.usuarios import create_user_sql
from appv1.schemas.usuario import  UserCreate
from db.database import get_db


router_user = APIRouter()
MODULE = 'usuarios'

@router_user.post("/create")
async def insert_user(
    user: UserCreate, 
    db: Session = Depends(get_db),
):

    respuesta = create_user_sql(db, user)
    if respuesta:
        return {"mensaje":"Usuario ingresado exitosamente"}
        
        