from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.listaProyectos import get_all_projects
from appv1.crud.permissions import get_permissions

router_proyectos = APIRouter()


@router_proyectos.get("/get-lista-proyectos/", response_model=dict)
async def read_all_projects(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):

    proyectos, total_pages = get_all_projects(db, page=page, page_size=page_size)

    if len(proyectos) == 0:
        raise HTTPException(status_code=404, detail="Proyectos no encontrados")
    
    lista_proyectos = [dict(proyecto) for proyecto in proyectos]

    return {
        "proyectos": lista_proyectos,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }
