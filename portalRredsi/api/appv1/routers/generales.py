from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.area_conocimiento import AreaConocimientoResponse
from appv1.schemas.delegado.salas import ProyectoResponse
from db.database import get_db
from appv1.crud.generales import get_areas_conocimiento, get_proyecto_by_id

router_consultas_generales = APIRouter()

# CONSULTAS QUE SE PUEDEN UTILIZAR EN VARIOS MODULOS 

@router_consultas_generales.get("/get_areas_conocimiento/", response_model=List[AreaConocimientoResponse])
async def obtener_areas_conocimiento(
    db: Session = Depends(get_db)
):
    areas_conocimiento = get_areas_conocimiento(db)
    if len(areas_conocimiento) == 0:
        raise HTTPException(status_code=404, detail="areas no encontradas")
    return areas_conocimiento

@router_consultas_generales.get("/get_proyecto_by_id/", response_model=ProyectoResponse)
async def obtener_proyecto_by_id(
    id_proyecto:int,
    db: Session = Depends(get_db)
):
    proyecto = get_proyecto_by_id(db,id_proyecto)
    if not proyecto:
        raise HTTPException(status_code=404, detail="proyecto no encontrado")
    return proyecto
