from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.evaluador.evaluador import ProyectoSchema
from db.database import get_db
from appv1.crud.evaluador.proyectos import get_proyectos_por_etapa

routerCalificarProyectos = APIRouter()

@routerCalificarProyectos.get("/get-proyectos-por-etapa/", response_model=List[ProyectoSchema])
async def read_proyectos_por_etapa(
    nombre_etapa: str,
    id_detalle_personal: int,
    db: Session = Depends(get_db),
):
    proyectos = get_proyectos_por_etapa(db, nombre_etapa, id_detalle_personal)
    return proyectos

