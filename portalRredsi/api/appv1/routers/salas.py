from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.sala import AsignarProyectoSala, DetalleSala, SalaResponse
from db.database import get_db
from appv1.crud.salas import asignar_proyecto_a_sala, get_detalle_sala, get_salas, get_salas_por_convocatoria

router_delegado = APIRouter()


# < RUTAS SALAS

@router_delegado.post("/asignar-proyecto")
async def asignar_proyecto(asignacion: AsignarProyectoSala, db: Session = Depends(get_db)):
    respuesta = asignar_proyecto_a_sala(db, asignacion)
    if respuesta:
        return {"mensaje":f"Proyecto asignado a sala {asignacion.id_sala} "}
    else:
        return {"mensaje":"El proyecto no se ha podido asignar con exito"}


@router_delegado.get("/get-all-salas/", response_model=List[SalaResponse])
async def read_all_salas(
    db: Session = Depends(get_db)
):
    salas = get_salas(db)
    if len(salas) == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return salas

@router_delegado.get("/get-salas-por-convocatoria/", response_model=dict)
async def read_all_salas_por_categoria(
    db: Session = Depends(get_db)
):
    salas = get_salas_por_convocatoria(db)
    if len(salas) == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    response = {"salas": [sala._asdict() for sala in salas]}
    return response


@router_delegado.get("/get-detalle-sala/", response_model=DetalleSala)
async def read_detalle_sala(
    id_sala: str,
    db: Session = Depends(get_db),
):
    sala_detalle = get_detalle_sala(db,id_sala)
    if len(sala_detalle) == 0:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    
    return sala_detalle

# RUTAS SALAS />