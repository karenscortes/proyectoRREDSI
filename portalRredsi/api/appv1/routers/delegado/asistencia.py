from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.delegado.asistencia import AsistenciaResponse
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.asistencia import actualizar_asistencia, get_asistente_por_cedula, get_asistentes_por_convocatoria, get_asistentes_por_rol, get_asistentes_por_sala
from appv1.crud.permissions import get_permissions

router_asistencia = APIRouter()

MODULE = 12

#Ruta para traer todos los asistentes de una convocatoria en curso
@router_asistencia.get("/get-all-asistentes/", response_model=dict)
async def read_all_asistentes(
    page:int= 1,
    page_size:int = 10, 
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
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

#Ruta para traer todos los asistentes por sala de una convocatoria en curso
@router_asistencia.get("/get-asistentes-por-sala/", response_model=dict)
async def read_asistentes_por_sala(
    numero_sala: str,
    page: int = 1, 
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
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

#Ruta para actualizar asistencia
@router_asistencia.put("/update-asistencia/", response_model=dict)
def update_asistencia_evento(
    id_asistente: int,
    id_usuario: int,
    asistencia: bool,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    try:
        updated = actualizar_asistencia(db, id_asistente, id_usuario, asistencia)
        if updated:
            return {"mensaje": "Asistencia actualizada con éxito"}
        else:
            raise HTTPException(status_code=400, detail="No se pudo actualizar la asistencia")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

