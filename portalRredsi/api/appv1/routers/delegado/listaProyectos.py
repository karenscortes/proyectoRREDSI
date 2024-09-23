from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.delegado.listaProyectos import PaginatedResponse
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.permissions import get_permissions
from appv1.crud.delegado.listaProyectos import get_all_projects, get_projects_by_state


router_proyectos = APIRouter()

MODULE_PROYECTOS = 11

# Ruta para obtener los proyectos asignados por etapa (Presencial/Virtual) paginados
@router_proyectos.get("/obtener-proyectos-por-etapa-paginados/", response_model=PaginatedResponse)
async def obtener_proyectos_por_etapa(
    nombre_etapa: str,
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    response = get_all_projects(db, nombre_etapa, page, page_size)
    return response

# Ruta para obtener los proyectos estados (Pendientes/Calificados) paginados
@router_proyectos.get("/obtener-proyectos-por-estado/", response_model=PaginatedResponse)
async def obtener_proyectos_por_estado(
    estado_calificacion: str,
    nombre_etapa: str,
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),   
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado para utilizar este modulo")
    
    response = get_projects_by_state(db, nombre_etapa, estado_calificacion, page, page_size)
    return response