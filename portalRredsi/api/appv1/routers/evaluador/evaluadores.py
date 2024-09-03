from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.etapa import EtapaBase
from db.database import get_db
from appv1.crud.proyectos import get_proyectos_por_etapa

router_evaluador = APIRouter()

@router_evaluador.get("/get-proyectos-por-etapa/", response_model=dict)
async def read_proyectos_por_etapa(
    nombre_etapa: EtapaBase,
    db: Session = Depends(get_db)
):
    proyectos = get_proyectos_por_etapa(db, nombre_etapa)
    if proyectos:
        return {"mensaje":"Proyectos obtenidos exitosamente"}


