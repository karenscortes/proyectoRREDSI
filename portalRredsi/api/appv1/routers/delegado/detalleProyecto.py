
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.delegado.detalleProyectos import  ParticipanteProyectoS, SalaConHorario, UrlPresentacionProyecto, UsuarioProyecto, AsistenciaEvento
from appv1.schemas.evaluador.evaluador import CalificarProyectoRespuesta
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.detalleProyecto import get_asistentes_evento, get_datos_proyecto_calificado_completo_suplente, get_datos_sala, get_evaluadores_por_etapa, get_obtener_suplente_evaluador, get_obtener_suplentes,  get_participantes_proyecto,  insertar_presentacion_proyecto, insertar_suplente_proyecto
from appv1.crud.permissions import get_permissions

router_detalle_proyecto = APIRouter()

MODULE_PROYECTOS = 11

#ruta para traer los evaluadores según etapa
@router_detalle_proyecto.get("/participantes-etapa/", response_model=List[UsuarioProyecto])
async def obtener_participantes_por_etapa(
    id_proyecto: int,
    id_etapa: int,
    db: Session = Depends(get_db)
):
    evaluadores = get_evaluadores_por_etapa(db, id_proyecto, id_etapa)
    if not evaluadores:
        raise HTTPException(status_code=404, detail="No se encontraron evaluadores para el proyecto")
    return evaluadores

#ruta para traer ponentes del proyecto
@router_detalle_proyecto.get("/ponentes-proyecto/", response_model=List[UsuarioProyecto])
async def obtener_participantes_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    ponentesProyecto = get_participantes_proyecto(db, id_proyecto)  
    if not ponentesProyecto:
        raise HTTPException(status_code=404, detail="No se encontraron evaluadores para el proyecto")
    return ponentesProyecto

#ruta para traer asistentes por convocatoria
@router_detalle_proyecto.get("/asistentes-evento/", response_model=List[AsistenciaEvento])
async def obtener_asistentes_evento(
    id_convocatoria: int,  
    db: Session = Depends(get_db)
):
    asistentesEvento = get_asistentes_evento(db, id_convocatoria)  
    if not asistentesEvento:
        raise HTTPException(status_code=404, detail="No se encontraron asistentes para este evento")
    return asistentesEvento

#ruta para insertar suplentes 
@router_detalle_proyecto.post("/insertar-suplentes/")
async def insertar_suplente(
    id_suplente: int,
    id_etapa: int,
    id_proyecto: int,
    id_proyectos_convocatoria: int,
    tipo_usuario: str,
    id_evaluador: int,
    db: Session = Depends(get_db)    
):   
    try:
        insertar_suplente_proyecto(db, id_suplente, id_etapa, id_proyecto, id_proyectos_convocatoria, tipo_usuario, id_evaluador)
        return {"mensaje": "Suplente insertado correctamente"}
    except HTTPException as e:
        return {"mensaje": "Error al insertar suplente"}   

#ruta para obtener suplentes
@router_detalle_proyecto.get("/obtener-suplentes/", response_model=List[ParticipanteProyectoS])
async def obtener_suplente(
    id_proyecto: int,
    tipo_usuario: str,
    db: Session = Depends(get_db)
):
    infoSuplentes = get_obtener_suplentes(db, id_proyecto, tipo_usuario)
    if not infoSuplentes:
        raise HTTPException(status_code=404, detail="No se encontraron suplentes")
    return infoSuplentes

        

#ruta para traer datos de sala
@router_detalle_proyecto.get("/datos-sala-proyecto/", response_model=SalaConHorario)
async def obtener_datos_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    infoSala = get_datos_sala(db, id_proyecto)
    if not infoSala:
        raise HTTPException(status_code=404, detail="No se encontró información de sala para el proyecto")
    return infoSala

#ruta para traer suplente de evaluador
@router_detalle_proyecto.get("/suplente-evaluador/", response_model=dict)
async def obtener_suplentes_evalaudor(
    id_proyecto: int,
    id_evaluador: int,
    db: Session = Depends(get_db)
):
    suplenteEvaluador = get_obtener_suplente_evaluador(db, id_proyecto, id_evaluador)
    if not suplenteEvaluador:
        raise HTTPException(status_code=404, detail="No se encontraron suplentes agregados para evaluador")
    id_suplente = [dict(suplente) for suplente in suplenteEvaluador]
    return {"id_suplente":id_suplente}


#ruta para insertar url presentación proyecto
@router_detalle_proyecto.post("/insertar-url-presentacion/")
async def insertar_url_presentacion(
    id_proyecto: int,
    url_presentacion: str,
    db: Session = Depends(get_db)
):
    try:
        insertar_presentacion_proyecto(db, id_proyecto, url_presentacion)
        return {"mensaje": "URL de presentación insertada correctamente"}
    except HTTPException as e:
        return {"mensaje": "Error al insertar URL de presentación"}

# Ruta para obtener el detalle del proyecto calificado
@router_detalle_proyecto.get("/obtener-datos-del-proyecto-calificado-suplente/", response_model=CalificarProyectoRespuesta)
async def obtener_datos_del_proyecto_calificado(
    id_proyecto: int,
    id_usuario: int,
    nombre_etapa: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    proyecto = get_datos_proyecto_calificado_completo_suplente(db, id_proyecto, id_usuario, nombre_etapa)
    return proyecto
