
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.delegado.detalleProyectos import  SalaConHorario, UrlPresentacionProyecto, UsuarioProyecto, AsistenciaEvento
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.detalleProyecto import get_asistentes_evento, get_datos_sala, get_evaluadores_por_etapa,  get_participantes_proyecto,  insertar_presentacion_proyecto, insertar_suplente_proyecto

router_detalle_proyecto = APIRouter()

#ruta para traer los evaluadores según etapa
@router_detalle_proyecto.get("/participantes-etapa/", response_model=List[UsuarioProyecto])
async def obtener_participantes_por_etapa(
    id_proyecto: int,
    id_etapa: int,
    db: Session = Depends(get_db)
):
    evaluadores = get_evaluadores_por_etapa(db, id_proyecto, id_etapa)
    if not evaluadores:
        raise HTTPException(status_code=404, detail="No se encontraron evaluadores para el proyecto")
    return evaluadores

#ruta para traer ponentes del proyecto
@router_detalle_proyecto.get("/ponentes-proyecto/", response_model=List[UsuarioProyecto])
async def obtener_participantes_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    ponentesProyecto = get_participantes_proyecto(db, id_proyecto)  
    if not ponentesProyecto:
        raise HTTPException(status_code=404, detail="No se encontraron evaluadores para el proyecto")
    return ponentesProyecto

#ruta para traer asistentes por convocatoria
@router_detalle_proyecto.get("/asistentes-evento/", response_model=List[AsistenciaEvento])
async def obtener_asistentes_evento(
    id_convocatoria: int,  
    db: Session = Depends(get_db)
):
    asistentesEvento = get_asistentes_evento(db, id_convocatoria)  
    if not asistentesEvento:
        raise HTTPException(status_code=404, detail="No se encontraron asistentes para este evento")
    return asistentesEvento

#ruta para insertar suplentes 
@router_detalle_proyecto.post("/insertar-suplentes/")
async def insertar_suplente(
    id_usuario: int,
    id_etapa: int,
    id_proyecto: int,
    id_proyectos_convocatoria: int,
    tipo_usuario: str,
    db: Session = Depends(get_db)    
):   
    try:
        insertar_suplente_proyecto(db,  id_usuario, id_etapa, id_proyecto, id_proyectos_convocatoria, tipo_usuario)
        return {"mensaje": "Suplente insertado correctamente"}
    except HTTPException as e:
        return {"mensaje": "Error al insertar suplente"}   

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


