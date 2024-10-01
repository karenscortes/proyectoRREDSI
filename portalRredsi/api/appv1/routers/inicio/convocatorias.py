from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.inicio.convocatorias import ConvocatoriaResponse, PaginatedConvocatoriaResponse
from db.database import get_db
from appv1.crud.inicio.convocatorias import get_all_convocatorias, leer_convocatorias


router = APIRouter()

@router.get("/verconvocatorias", response_model=List[ConvocatoriaResponse])
async def get_convocatorias(
    db: Session = Depends(get_db)
):

    respuesta = leer_convocatorias(db)
    if len(respuesta)==0:
        raise HTTPException(status_code=404, detail="No hay convocatorias")
    
    return respuesta

# Obtener todos los administradores activos con paginación
@router.get("/verconvocatorias/", response_model=PaginatedConvocatoriaResponse)
async def read_all_convocatorias_by_page(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):
    
    convocatorias, total_pages = get_all_convocatorias(db, page, page_size)
    
    return {
        "convocatorias": convocatorias,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }