from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.usuario import UserResponse
from appv1.crud.usuarios import get_user_by_documento
from db.database import get_db

router_userId = APIRouter()

@router_userId.get("/user/", response_model=UserResponse)
async def get_user_by_document(
    documento: Annotated[str, "Documento del usuario"], 
    db: Session = Depends(get_db)
):
    # Llamamos a la función para buscar el usuario por el documento
    user = get_user_by_documento(db, documento)

    # Si no se encuentra el usuario, lanzamos una excepción
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Devolvemos la respuesta con el usuario encontrado
    return user
