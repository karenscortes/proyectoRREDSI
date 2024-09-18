from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.delegado.salas import AsignarProyectoSala, DetalleSala, SalaBase, SalaResponse
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.salas import asignar_proyecto_a_sala, get_detalle_sala, get_ponentes_proyecto, get_salas_por_convocatoria, verificar_sala_asignada
from appv1.crud.permissions import get_permissions

router_sala = APIRouter()

# ID del modulo el cual quieren probar / validen en workbench los id en la tabla permisos
MODULE_USUARIOS= 3
MODULE_SALAS = 15
MODULE_DETALLE_SALA = 16

# RUTA PARA ASIGNAR PROYETCO ETAPA PRESENCIAL 
@router_sala.post("/asignar-proyecto-etapa-presencial/")
async def asignar_proyecto(
    asignacion: AsignarProyectoSala,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_DETALLE_SALA)
    
    if not permisos.p_insertar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    respuesta = asignar_proyecto_a_sala(db, asignacion)
    if respuesta:
        return {"mensaje":f"Proyecto asignado a sala {asignacion.id_sala} "}
    else:
        return {"mensaje":"El proyecto no se ha podido asignar"}

# RURA PARA OBTENER TODAS LAS SALAS QUE SE ENCUENTREN REGISTRADAS EN UNA CONVOCATORIA ACTIVA 
@router_sala.get("/get-salas-por-convocatoria/", response_model=dict)
async def read_all_salas_por_convocatoria(
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
    
):
    # Aqui tienen que consultar que permisos tiene asignados por rol :)
    permisos = get_permissions(db, current_user.id_rol, MODULE_SALAS)
    
    # Si no tiene permiso que necesita tira el mensaje de error
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    # si no imprime el resultado
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

# RUTA PARA OBTENER EL DETALLE DE UNA SALA 
@router_sala.get("/get-detalle-sala/", response_model=DetalleSala)
async def read_detalle_sala(
    id_sala: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_DETALLE_SALA)
    
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    sala_detalle = get_detalle_sala(db,id_sala)
    if len(sala_detalle) == 0:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    
    return sala_detalle

# RUTA PARA COMPROBAR SI UN DELEGADO TIENE ASIGNADA UNA SALA
@router_sala.get("/verificar-sala-asignada/", response_model=SalaBase)
async def read_sala_asignada(
    id_usuario: int,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_DETALLE_SALA)
    
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    sala_detalle = verificar_sala_asignada(db,id_usuario)
    if len(sala_detalle) == 0:
        raise HTTPException(status_code=404, detail="Sin sala asignada")

    return sala_detalle

# RUTA PARA OBTENER LOS PONENTES DE UN PROYECTO
@router_sala.get("/get-ponentes-proyecto/", response_model=dict)
async def read_sala_asignada(
    id_proyecto: int,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_USUARIOS)
    
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    ponentes = get_ponentes_proyecto(db,id_proyecto)
    if len(ponentes) == 0:
        raise HTTPException(status_code=404, detail="Sin ponentes asignados")

    ponentes_proyecto = [dict(ponente) for ponente in ponentes]
    
    return {"ponentes": ponentes_proyecto}