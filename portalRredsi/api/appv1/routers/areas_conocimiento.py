from typing import List
from fastapi import APIRouter, Depends, HTTPException
from appv1.crud.areaConocimiento import get_all_areasConocimiento
from appv1.schemas.area_conocimiento import AreaConocimientoResponse
from sqlalchemy.orm import Session
from db.database import get_db

router_areasConocimiento = APIRouter()
@router_areasConocimiento.get("/get-all-areasConocimiento/", response_model=List[AreaConocimientoResponse])
async def read_all_areasConocimiento(
    db: Session = Depends(get_db),
):
    identificacion = get_all_areasConocimiento(db)
    if len(identificacion) == 0:
        raise HTTPException(status_code=404, detail="No hay tipo de areas de conocimiento")
    
    return identificacion