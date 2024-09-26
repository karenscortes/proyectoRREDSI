from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from appv1.crud.TipoDocumento import get_all_TipoIdentificacion
from appv1.schemas.Tipo_identificacion import TipoIdentificacionResponse
from sqlalchemy.orm import Session
from db.database import get_db

router_identificacion = APIRouter()
@router_identificacion.get("/get-all-identificacion/", response_model=List[TipoIdentificacionResponse])
async def read_all_documento(
    db: Session = Depends(get_db),
):
    identificacion = get_all_TipoIdentificacion(db)
    if len(identificacion) == 0:
        raise HTTPException(status_code=404, detail="No hay tipo de identificacion")
    
    return identificacion