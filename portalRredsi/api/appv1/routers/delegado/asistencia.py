from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.delegado.asistencia import AsistenciaResponse
from db.database import get_db
from appv1.crud.delegado.asistencia import actualizar_asistencia, get_asistente_por_cedula, get_asistentes_por_convocatoria, get_asistentes_por_rol, get_asistentes_por_sala

router_asistencia = APIRouter()


@router_asistencia.get("/get-all-asistentes/", response_model=dict)
async def read_all_asistentes(
    page:int= 1, page_size:int = 10, db: Session = Depends(get_db)
):
    asistentes, total_pages = get_asistentes_por_convocatoria(db, page, page_size)
    if len(asistentes) == 0:
        raise HTTPException(status_code=404, detail="Asistentes no encontrados en esta convocatoria")
        
    asistentes_convocatoria = [dict(asistente) for asistente in asistentes]

    return {
        "asistentes": asistentes_convocatoria,
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


@router_asistencia.get("/get-asistentes-por-rol/{rol}", response_model=dict)
async def read_asistentes_por_rol(
    rol: str, 
    page: int = 1, 
    page_size: int = 10, 
    db: Session = Depends(get_db)
):
    asistentes, total_pages = get_asistentes_por_rol(db, rol, page, page_size)
    
    if len(asistentes) == 0:
        raise HTTPException(status_code=404, detail="Asistentes no encontrados para el rol especificado")
        
    asistentes_por_rol = [dict(asistente) for asistente in asistentes]

    return {
        "asistentes": asistentes_por_rol,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }

@router_asistencia.get("/get-asistente-por-cedula/{documento}", response_model=dict)
async def read_asistente_por_cedula(documento: str, db: Session = Depends(get_db)):
    asistente = get_asistente_por_cedula(db, documento)
    
    if not asistente:
        raise HTTPException(status_code=404, detail="Asistente no encontrado con el documento especificado")
    
    return asistente

@router_asistencia.put("/update-asistencia/", response_model=dict)
def update_asistencia_evento(
    id_asistencia:int,
    id_usuario:int,
    asistencia: int,
    db: Session = Depends(get_db),
):
    updated= actualizar_asistencia(db, id_asistencia, id_usuario, asistencia)
    if updated:
        return {"mensaje": "Asistencia actualizada con exito" }