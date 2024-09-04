from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.evaluador import ProyectoSchema
from db.database import get_db
from proyectos import get_proyectos_por_etapa

router_evaluador = APIRouter()

@router_evaluador.get("/get-proyectos-por-etapa/", response_model=List[ProyectoSchema])
async def read_proyectos_por_etapa(
    db: Session = Depends(get_db)
):
    proyectos = get_proyectos_por_etapa(db)
    
    return proyectos