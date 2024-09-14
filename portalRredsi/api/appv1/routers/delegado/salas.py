from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.delegado.salas import AsignarProyectoSala, DetalleSala, SalaResponse
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.salas import asignar_proyecto_a_sala, get_detalle_sala, get_salas, get_salas_por_convocatoria
from appv1.crud.permissions import get_permissions

router_sala = APIRouter()

MODULE = 15

@router_sala.post("/asignar-proyecto-etapa-presencial/")
async def asignar_proyecto(asignacion: AsignarProyectoSala, db: Session = Depends(get_db)):
    respuesta = asignar_proyecto_a_sala(db, asignacion)
    if respuesta:
        return {"mensaje":f"Proyecto asignado a sala {asignacion.id_sala} "}
    else:
        return {"mensaje":"El proyecto no se ha podido asignar"}


@router_sala.get("/get-all-salas/", response_model=List[SalaResponse])
async def read_all_salas(
    db: Session = Depends(get_db)
):
    salas = get_salas(db)
    if len(salas) == 0:
        raise HTTPException(status_code=404, detail="Salas no encontradas")
    return salas

@router_sala.get("/get-salas-por-convocatoria/", response_model=dict)
async def read_all_salas_por_convocatoria(
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
    
):
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")

    salas, total_pages = get_salas_por_convocatoria(db, page, page_size)
    if len(salas) == 0:
        raise HTTPException(status_code=404, detail="Salas no encontradas")

    # Convertir cada fila en un diccionario
    salas_convocatoria = [dict(sala) for sala in salas]

    return {
        "salas": salas_convocatoria,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }


@router_sala.get("/get-detalle-sala/", response_model=DetalleSala)
async def read_detalle_sala(
    id_sala: str,
    db: Session = Depends(get_db),
):
    sala_detalle = get_detalle_sala(db,id_sala)
    if len(sala_detalle) == 0:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    
    return sala_detalle

# RUTAS SALAS />
