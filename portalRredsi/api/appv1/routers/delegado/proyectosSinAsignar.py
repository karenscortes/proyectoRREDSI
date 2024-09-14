from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.delegado.proyectosSinAsignar import AuthorsResponse, PaginatedUnassignedProjects, UnassignedProjects
from db.database import get_db
from appv1.crud.delegado.proyectosSinAsignar import get_all_authors, get_unassigned_projects

router_proyectosSinAsignar = APIRouter()


@router_proyectosSinAsignar.get("/get-all-unassiggned-Projects/", response_model=PaginatedUnassignedProjects)
async def read_all_unassignedProjects(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
    #current_user: UserResponse = Depends(get_current_user)
):
    # permisos = get_permissions(db, current_user.user_role, MODULE)
    # if not permisos.p_select:
    #     raise HTTPException(status_code=401, detail="Usuario no autorizado")
    projects,total_pages = get_unassigned_projects(db, page, page_size)
    
    return {
        "projects": projects,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }

@router_proyectosSinAsignar.get("/get-all-authors",response_model=List[AuthorsResponse])
async def read_all_authors(
    id_proyecto:int,
    db: Session = Depends(get_db)
    #current_user: UserResponse = Depends(get_current_user)
):
    # permisos = get_permissions(db, current_user.user_role, MODULE)
    # if not permisos.p_select:
    #     raise HTTPException(status_code=401, detail="Usuario no autorizado")
    authors = get_all_authors(db, id_proyecto)
    if len(authors) == 0:
        raise HTTPException(status_code=404, detail="No hay autores")
    return authors