from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.valeria_schemas.convocatorias import ConvocatoriaResponse
from db.database import get_db
from appv1.crud.permissions import get_permissions
from appv1.crud.valeria_crud.convocatorias import leer_convocatorias


router = APIRouter()

@router.get("/verconvocatorias", response_model=List[ConvocatoriaResponse])
async def get_convocatorias(
    db: Session = Depends(get_db)
):

    respuesta = leer_convocatorias(db)
    if len(respuesta)==0:
        raise HTTPException(status_code=404, detail="No hay convocatorias")
    
    return respuesta