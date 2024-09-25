from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.UsuarioEvaluador import create_evaluador_sql
from appv1.crud.usuarios import get_user_by_email
from appv1.schemas.UsuarioEvaluador import EvaluadorCreate
from db.database import get_db


router_evaluador = APIRouter()

@router_evaluador.post("/create")
async def insert_user(
    evaluador: EvaluadorCreate, 
    db: Session = Depends(get_db),
    
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