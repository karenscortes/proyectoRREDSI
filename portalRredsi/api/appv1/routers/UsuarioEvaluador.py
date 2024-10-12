from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.UsuarioEvaluador import create_evaluador_sql, get_user_by_email, get_user_by_documento, get_user_by_celular
from appv1.schemas.UsuarioEvaluador import EvaluadorCreate
from db.database import get_db

router_evaluador = APIRouter()

@router_evaluador.post("/create")
async def insert_user(evaluador: EvaluadorCreate, db: Session = Depends(get_db)):

    # Verificar si el correo ya está registrado
    existing_user_by_email = get_user_by_email(db, evaluador.correo)
    if existing_user_by_email:
        raise HTTPException(status_code=400, detail="El correo ya está registrado, por favor inicie sesión")

    # Verificar si el documento ya está registrado
    existing_user_by_documento = get_user_by_documento(db, evaluador.documento)
    if existing_user_by_documento:
        raise HTTPException(status_code=400, detail="El número de documento ya está registrado")

    # Verificar si el número de celular ya está registrado
    existing_user_by_celular = get_user_by_celular(db, evaluador.celular)
    if existing_user_by_celular:
        raise HTTPException(status_code=400, detail="El número de celular ya está registrado")

    # Crear evaluador si no hay duplicados
    try:
        respuesta = create_evaluador_sql(db, evaluador)
        if respuesta:
            return {"mensaje": "Usuario ingresado exitosamente"}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")
