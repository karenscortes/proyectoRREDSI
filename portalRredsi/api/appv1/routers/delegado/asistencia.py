from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.delegado.asistencia import AsistenciaResponse
from db.database import get_db
from appv1.crud.delegado.asistencia import get_asistentes_por_convocatoria, get_asistentes_por_sala

router_asistencia = APIRouter()


@router_asistencia.get("/get-all-asistentes/", response_model=dict)
async def read_all_asistentes(
    page:int= 1, page_size:int = 10, db: Session = Depends(get_db)
):
    asistentes, total_pages = get_asistentes_por_convocatoria(db, page, page_size)
    if len(asistentes) == 0:
        raise HTTPException(status_code=404, detail="Asistentes no encontrados")
        
    asistentes_convocatoria = [dict(asistente) for asistente in asistentes]

    return {
        "salas": asistentes_convocatoria,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }


@router_asistencia.get("/get-asistentes-por-sala/{numero_sala}", response_model=dict)
async def read_asistentes_por_sala(
    numero_sala: str, page: int = 1, page_size: int = 10, db: Session = Depends(get_db)
):
    asistentes, total_pages = get_asistentes_por_sala(db, numero_sala, page, page_size)
    if len(asistentes) == 0:
        raise HTTPException(status_code=404, detail="Asistentes no encontrados para esta sala")
        
    asistentes_por_sala = [dict(asistente) for asistente in asistentes]

    return {
        "asistentes": asistentes_por_sala,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }
