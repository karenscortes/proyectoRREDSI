
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.delegado.detalleProyectos import  ProyectoResponse, SalaConHorario, UsuarioProyecto
from db.database import get_db
from appv1.crud.delegado.detalleProyecto import get_datos_sala, get_participantes_proyecto

router_detalle_proyecto = APIRouter()

@router_detalle_proyecto.get("/evaluadores-proyecto/", response_model=List[UsuarioProyecto])
async def obtener_evaluadores_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    evaluadores = get_participantes_proyecto(db, id_proyecto, id_rol=1)  
    if not evaluadores:
        raise HTTPException(status_code=404, detail="No se encontraron evaluadores para el proyecto")
    print(evaluadores)
    return [UsuarioProyecto(**evaluador) for evaluador in evaluadores]


@router_detalle_proyecto.get("/ponentes-proyecto/", response_model=List[UsuarioProyecto])
async def obtener_ponentes_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    ponentes = get_participantes_proyecto(db, id_proyecto, id_rol=5)  
    if not ponentes:
        raise HTTPException(status_code=404, detail="No se encontraron ponentes para el proyecto")
    return [UsuarioProyecto(**ponente) for ponente in ponentes]

@router_detalle_proyecto.get("/datos-sala-proyecto/", response_model=SalaConHorario)
async def obtener_datos_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    infoSala = get_datos_sala(db, id_proyecto)
    if not infoSala:
        raise HTTPException(status_code=404, detail="No se encontraron información de sala para el proyecto")
    return infoSala






