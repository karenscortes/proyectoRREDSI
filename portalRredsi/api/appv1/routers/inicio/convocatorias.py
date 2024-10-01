from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.inicio.convocatorias import PaginatedConvocatoriaResponse, PaginatedProgramacionFasesResponse
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.inicio.convocatorias import get_all_convocatorias, get_programacion_fases_activa
from appv1.crud.permissions import get_permissions

router = APIRouter()

# Obtener todas las convocatorias con paginación y protección
@router.get("/verconvocatorias/", response_model=PaginatedConvocatoriaResponse)
async def read_all_convocatorias_by_page(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 6
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    # Verificar permisos de consulta
    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    convocatorias, total_pages = get_all_convocatorias(db, page, page_size)

    return {
        "convocatorias": convocatorias,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }


@router.get("/programacion-fases-activa/", response_model=PaginatedProgramacionFasesResponse)
async def get_programacion_fases_activa_route(
    page: int = 1,
    page_size: int = 5,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    MODULE = 7
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    # Verificar permisos de consulta
    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    programacion_fases = get_programacion_fases_activa(db, page, page_size)

    return programacion_fases
