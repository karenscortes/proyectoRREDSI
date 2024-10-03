
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.delegado.detalleProyectos import  SalaConHorario, UrlPresentacionProyecto, UsuarioProyecto
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.detalleProyecto import get_datos_sala, get_participantes_proyecto, insertar_presentacion_proyecto

router_detalle_proyecto = APIRouter()

#ruta para traer evaluadores del proyecto
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

#ruta para traer ponentes del proyecto
@router_detalle_proyecto.get("/ponentes-proyecto/", response_model=List[UsuarioProyecto])
async def obtener_ponentes_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    ponentes = get_participantes_proyecto(db, id_proyecto, id_rol=5)  
    if not ponentes:
        raise HTTPException(status_code=404, detail="No se encontraron ponentes para el proyecto")
    return [UsuarioProyecto(**ponente) for ponente in ponentes]

#ruta para traer datos de sala
@router_detalle_proyecto.get("/datos-sala-proyecto/", response_model=SalaConHorario)
async def obtener_datos_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    infoSala = get_datos_sala(db, id_proyecto)
    if not infoSala:
        raise HTTPException(status_code=404, detail="No se encontraron información de sala para el proyecto")
    return infoSala

#ruta para insertar url presentación proyecto
@router_detalle_proyecto.post("/insertar-url-presentacion/")
async def insertar_url_presentacion(
    id_proyecto: int,
    url_presentacion: str,
    db: Session = Depends(get_db)
):
    try:
        insertar_presentacion_proyecto(db, id_proyecto, url_presentacion)
        return {"mensaje": "URL de presentación insertada correctamente"}
    except HTTPException as e:
        return {"mensaje": "Error al insertar URL de presentación"}


