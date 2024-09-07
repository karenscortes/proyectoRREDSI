from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from appv1.schemas.evaluador.evaluador import PaginatedResponse
from db.database import get_db
from appv1.crud.evaluador.proyectos import get_proyectos_asignados, get_proyectos_por_estado, get_proyectos_por_etapa

routerCalificarProyectos = APIRouter()

@routerCalificarProyectos.get("/get-proyectos-por-etapa-paginados/", response_model=PaginatedResponse)
async def read_proyectos_por_etapa(
    nombre_etapa: str,
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    response = get_proyectos_por_etapa(db, nombre_etapa, id_usuario, page, page_size)
    return response

@routerCalificarProyectos.get("/get-proyectos-por-estado-paginados/", response_model=PaginatedResponse)
async def read_proyectos_por_estado(
    estado_evaluacion: str,
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    response = get_proyectos_por_estado(db, estado_evaluacion, id_usuario, page, page_size)
    return response

@routerCalificarProyectos.get("/get-proyectos-asignados-paginados/", response_model=PaginatedResponse)
async def read_proyectos_asignados(
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    response = get_proyectos_asignados(db, id_usuario, page, page_size)
    return response
