from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.area_conocimiento import AreaConocimientoResponse
from appv1.schemas.delegado.asignacionProyectoEtapaVirtual import AsignarProyectoEtapaUno
from appv1.schemas.institucion import InstitucionBase
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.asignarProyectoEtapaVirtual import asignar_proyecto_etapa_virtual, get_area_conocimiento_por_nombre, get_convocatoria_actual_por_proyecto, get_institucion_por_nombre, get_posibles_evaluadores_para_proyecto, update_estado_proyecto
from appv1.crud.permissions import get_permissions

router_proyecto_etapa_uno = APIRouter()

MODULE_AREAS_CONOCIMIENTO = 1
MODULE_INSTITUCIONES = 2
MODULE_USUARIOS= 3
MODULE_PROYECTOS= 11
MODULE_PARTICIPANTES_PROYECTO = 13

# RUTA PARA ASIGNAR UN PROYECTO A UN EVALUADOR EN LA ETAPA VIRTUAL
@router_proyecto_etapa_uno.post("/asignar-proyecto-etapa-uno/")
async def asignar_proyecto_etapa_uno(
    asignacion: AsignarProyectoEtapaUno,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PARTICIPANTES_PROYECTO)
    if not permisos.p_insertar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    respuesta = asignar_proyecto_etapa_virtual(db, asignacion)
    if respuesta:
        return {"mensaje": "Proyecto asignado con exito"}
    else:
        return {"mensaje":"El proyecto no se ha podido asignar con exito"}

# RUTA PARA OBTENER EL ID DE PROYECTO CONVOCATORIA LA QUE ESTE RELACIONADO UN PROYECTO
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

# RUTA PARA OBTENER UNA LISTA DE POSIBLES EVALUADORES PARA UN PROYECTO
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

# RUTA PARA OBTENER EL NOMBRE UNA AREA DE CONOCIMIENTO POR MEDIO DE SU ID 
@router_proyecto_etapa_uno.get("/get-id-area-conocimiento/", response_model=AreaConocimientoResponse)
async def read_datos_area_conocimiento(
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

# RUTA PARA OBTENER EL NOMBRE UNA INSTITUCION POR MEDIO DE SU ID 
@router_proyecto_etapa_uno.get("/get-id-institucion/", response_model=InstitucionBase)
async def read_datos_institucion(
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

# RUTA PARA ACTUALIZAR EL ESTADO DE UN PROYECTO CUANDO ES ASIGNADO 
@router_proyecto_etapa_uno.put("/update-estado-proyecto/")
async def read_update_estado_proyecto(
    id_proyecto: int,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    estado_actualizado = update_estado_proyecto(db,id_proyecto)
    if estado_actualizado != True:
        raise HTTPException(status_code=404, detail="Id proyecto no encontrado")
    
    return {"Mensaje": "Estado de proyecto actualizado correctamente"}