from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.area_conocimiento import AreaConocimientoResponse
from appv1.schemas.delegado.salas import ProyectoResponse
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.generales import get_areas_conocimiento, get_cantidad_postulaciones, get_cantidad_proyectos_asignados, get_cantidad_proyectos_calificados, get_cantidad_proyectos_inscritos, get_proyecto_by_id
from appv1.crud.permissions import get_permissions

router_consultas_generales = APIRouter()

MODULE_PROYECTOS = 11
MODULE_POSTULACIONES_EVALUADORES = 8

# CONSULTAS QUE SE PUEDEN UTILIZAR EN VARIOS MODULOS 

# RUTA PARA OBTENER TODAS LAS AREAS DE CONOCIMIENTO 
@router_consultas_generales.get("/get_areas_conocimiento/", response_model=List[AreaConocimientoResponse])
async def obtener_areas_conocimiento(
    db: Session = Depends(get_db)
):
    areas_conocimiento = get_areas_conocimiento(db)
    if len(areas_conocimiento) == 0:
        raise HTTPException(status_code=404, detail="areas no encontradas")
    return areas_conocimiento

# RUTA PARA OBTENER LA INFORMACION DE UN PROYECTO POR SU ID 
@router_consultas_generales.get("/get_proyecto_by_id/", response_model=ProyectoResponse)
async def obtener_proyecto_by_id(
    id_proyecto:int,
    db: Session = Depends(get_db)
):
    proyecto = get_proyecto_by_id(db,id_proyecto)
    if not proyecto:
        raise HTTPException(status_code=404, detail="proyecto no encontrado")
    return proyecto

# RUTA PARA OBTENER LA CANTIDAD DE POSTULACIONES DE EVALUADORES EN UNA CONVOCATORIA ACTIVA 
@router_consultas_generales.get("/get_cantidad_postulaciones/")
async def obtener_cantidad_postulaciones(
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_POSTULACIONES_EVALUADORES)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    postulaciones = get_cantidad_postulaciones(db)
    return postulaciones

# RUTA PARA OBTENER LA CANTIDAD DE PROYECTOS ASIGNADOS EN UNA CONVOCATORIA ACTIVA 
@router_consultas_generales.get("/get_cantidad_proyectos_asignados/")
async def obtener_cantidad_proyectos_asignados(
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    proyectos_asignados = get_cantidad_proyectos_asignados(db)
    return proyectos_asignados


# RUTA PARA OBTENER LA CANTIDAD DE PROYECTOS INSCRITOS EN UNA CONVOCATORIA ACTIVA 
@router_consultas_generales.get("/get_cantidad_proyectos_inscritos/")
async def obtener_cantidad_proyectos_inscritos(
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    proyectos_inscritos = get_cantidad_proyectos_inscritos(db)
    return proyectos_inscritos

# RUTA PARA OBTENER LA CANTIDAD DE PROYECTOS INSCRITOS EN UNA CONVOCATORIA ACTIVA 
@router_consultas_generales.get("/get_cantidad_proyectos_calificados_por_etapa/")
async def obtener_cantidad_proyectos_calificados(
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    proyectos_calificados = get_cantidad_proyectos_calificados(db)
    return proyectos_calificados