from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.area_conocimiento import AreaConocimientoResponse
from db.database import get_db
from appv1.crud.generales import get_areas_conocimiento

router_areas_conocimiento = APIRouter()

@router_areas_conocimiento.get("/get_areas_conocimiento/", response_model=List[AreaConocimientoResponse])
async def obtener_areas_conocimiento(
    db: Session = Depends(get_db)
):
    eventos = get_areas_conocimiento(db)
    if len(eventos) == 0:
        raise HTTPException(status_code=404, detail="areas no encontradas")
    return eventos