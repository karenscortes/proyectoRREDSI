from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.area_conocimiento import AreaConocimientoBase
from appv1.schemas.delegado.asignacionProyectoEtapaVirtual import AsignarProyectoEtapaUno, PosibleEvaluadorEtapaVirtual
from appv1.schemas.institucion import InstitucionBase
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.asignarProyectoEtapaVirtual import asignar_proyecto_etapa_virtual, get_area_conocimiento_por_nombre, get_convocatoria_actual_por_proyecto, get_institucion_por_nombre, get_posibles_evaluadores_para_proyecto
from appv1.crud.permissions import get_permissions

router_proyecto_etapa_uno = APIRouter()

MODULE_AREAS_CONOCIMIENTO = 1
MODULE_INSTITUCIONES = 2
MODULE_USUARIOS= 3
MODULE_PROYECTOS= 11


@router_proyecto_etapa_uno.post("/asignar-proyecto-etapa-uno/")
async def asignar_proyecto_etapa_uno(
    asignacion: AsignarProyectoEtapaUno,
    db: Session = Depends(get_db)
):
    respuesta = asignar_proyecto_etapa_virtual(db, asignacion)
    if respuesta:
        return {"mensaje": "Proyecto asignado con exito"}
    else:
        return {"mensaje":"El proyecto no se ha podido asignar con exito"}


@router_proyecto_etapa_uno.get("/obtener-proyecto-convocatoria/", response_model=dict)
async def buscar_convocatoria_por_proyecto(
    id_proyecto: int,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    proyecto_convocatoria = get_convocatoria_actual_por_proyecto(db, id_proyecto)
    
    if proyecto_convocatoria:
        return {
            "proyecto_convocatoria": proyecto_convocatoria._asdict()
        }
    else:
        return {"mensaje":"El proyecto no se ha podido encontrar en una convocatoria vigente."}

@router_proyecto_etapa_uno.get("/get-posibles-evaluadores/", response_model=dict)
async def read_posibles_evaluadores(
    area_conocimiento: int,
    id_institucion: int,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_USUARIOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    posibles_evaluadores = get_posibles_evaluadores_para_proyecto(db, area_conocimiento, id_institucion)

    if len(posibles_evaluadores) == 0:
        raise HTTPException(status_code=200, detail="No hay evaluadores disponibles")

    # Serialización manual
    evaluadores = [
        {
            "id": evaluador.id_usuario,
            "documento": evaluador.documento,
            "nombre": evaluador.nombres,
            "apellidos": evaluador.apellidos,
        }
        for evaluador in posibles_evaluadores
    ]

    return {
        "posibles_evaluadores": evaluadores
    }

@router_proyecto_etapa_uno.get("/get-id-area-conocimiento/", response_model=AreaConocimientoBase)
async def read_detalle_sala(
    nombre_area: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_AREAS_CONOCIMIENTO)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    area_conocimiento = get_area_conocimiento_por_nombre(db,nombre_area)
    if len(area_conocimiento) == 0:
        raise HTTPException(status_code=404, detail="Area de conocimiento no encontrada")
    
    return area_conocimiento

@router_proyecto_etapa_uno.get("/get-id-institucion/", response_model=InstitucionBase)
async def read_detalle_sala(
    nombre_institucion: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_INSTITUCIONES)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    area_conocimiento = get_institucion_por_nombre(db,nombre_institucion)
    if len(area_conocimiento) == 0:
        raise HTTPException(status_code=404, detail="Institucion no encontrada")
    
    return area_conocimiento