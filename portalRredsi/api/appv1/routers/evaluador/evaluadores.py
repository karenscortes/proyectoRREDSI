from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.evaluador.evaluador import CalificarProyectoRespuesta, PaginatedResponse, PaginatedResponseHorario, PostulacionEvaluadorCreate, RespuestaRubricaCreate
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.evaluador.proyectos import convertir_timedelta_a_hora, create_postulacion_evaluador, get_current_convocatoria, get_datos_calificar_proyecto, get_datos_rubrica_proyecto, get_proyectos_asignados, get_proyectos_etapa_presencial_con_horario, get_proyectos_por_estado, get_proyectos_por_etapa, insert_respuesta_rubrica
from appv1.crud.permissions import get_permissions

routerObtenerProyectos = APIRouter()
routerInsertarPostulacionEvaluador = APIRouter()
routerInsetarCalificacionRubrica = APIRouter()
routerObtenerHorarioEvaluador = APIRouter()

# ID del modulo
MODULE_PROYECTOS = 11
MODULE_POSTULACIONES = 8
MODULE_RESPUESTAS_RUBRICAS = 14

#Ruta para obtener los proyectos asignados por etapa (Presencial/Virtual) paginados
@routerObtenerProyectos.get("/obtener-proyectos-por-etapa-paginados/", response_model=PaginatedResponse)
async def obtener_proyectos_por_etapa(
    nombre_etapa: str,
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    response = get_proyectos_por_etapa(db, nombre_etapa, id_usuario, page, page_size)
    return response

#Ruta para obtener los proyectos asignados por estado (calificado/pendiente) paginados
@routerObtenerProyectos.get("/obtener-proyectos-por-estado-paginados/", response_model=PaginatedResponse)
async def obtener_proyectos_por_estado(
    estado_evaluacion: str,
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")

    response = get_proyectos_por_estado(db, estado_evaluacion, id_usuario, page, page_size)
    return response

#Ruta para obtener los proyectos asignados (Tanto virtuales como presenciales)
@routerObtenerProyectos.get("/obtener-proyectos-asignados-paginados/", response_model=PaginatedResponse)
async def obtener_proyectos_asignados(
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    response = get_proyectos_asignados(db, id_usuario, page, page_size)
    return response

#Ruta para insertar la postulacion del evaluador
@routerInsertarPostulacionEvaluador.post("/insertar-postulacion-evaluador/")
async def insertar_postulacion_evaluador(
    postulacion: PostulacionEvaluadorCreate,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    convocatoria_actual = get_current_convocatoria(db)
    
    if not convocatoria_actual:
        raise HTTPException(status_code=404, detail="No hay convocatorias en curso.")
    
    permisos = get_permissions(db, current_user.id_rol, MODULE_POSTULACIONES)
    if not permisos.p_insertar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    response = create_postulacion_evaluador(
        db=db,
        id_convocatoria=convocatoria_actual,
        id_evaluador=postulacion.id_evaluador,
        etapa_virtual=postulacion.etapa_virtual,
        etapa_presencial=postulacion.etapa_presencial,
        jornada_manana=postulacion.jornada_manana,
        jornada_tarde=postulacion.jornada_tarde
    )
    
    if response:
        return {"message": "Postulación registrada exitosamente."}
    else:
        raise HTTPException(status_code=500, detail="Error al registrar la postulación.")
    
#Ruta para insertar la calificacion de la rúbrica
@routerInsetarCalificacionRubrica.post("/insertar-calificacion-rubrica/")
async def insertar_calificacion_proyecto(
    respuesta: RespuestaRubricaCreate,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    permisos = get_permissions(db, current_user.id_rol, MODULE_RESPUESTAS_RUBRICAS)
    if not permisos.p_insertar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")

    response = insert_respuesta_rubrica(
        db=db,
        id_item_rubrica=respuesta.id_item_rubrica,
        id_usuario=respuesta.id_usuario,
        id_proyecto=respuesta.id_proyecto,
        observacion=respuesta.observacion,
        calificacion=respuesta.calificacion,
        calificacion_final=respuesta.calificacion_final
    )
        
    if response:
        return {"message": "Respuesta de rúbrica registrada exitosamente."}
    else:
        raise HTTPException(status_code=500, detail="Error al registrar la calificación.")
    
# Ruta para obtener los proyectos asignados en la etapa presencial con horario
@routerObtenerHorarioEvaluador.get("/obtener-horario-evaluador/", response_model=PaginatedResponseHorario)
async def obtener_horario_evaluador(
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este modulo")
    
    try:
        response = get_proyectos_etapa_presencial_con_horario(db, id_usuario, page, page_size)
        
        # Convertir RowMapping a diccionario y aplicar la conversión de hora
        proyectos = []
        for proyecto in response["data"]:
            proyecto_dict = dict(proyecto)  # Convertir RowMapping a dict
            proyecto_dict['hora_inicio'] = convertir_timedelta_a_hora(proyecto_dict['hora_inicio'])
            proyecto_dict['hora_fin'] = convertir_timedelta_a_hora(proyecto_dict['hora_fin'])
            proyectos.append(proyecto_dict)
        
        # Devolver el resultado con los proyectos actualizados
        return {"data": proyectos, "total_pages": response["total_pages"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el horario: {str(e)}")

# Ruta para obtener el detalle del proyecto y evaluador para calificar un proyecto
@routerObtenerProyectos.get("/obtener-datos-para-calificar-proyecto/", response_model=CalificarProyectoRespuesta)
async def obtener_datos_para_calificar_proyecto(
    id_proyecto: int,
    id_usuario: int,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    proyecto = get_datos_calificar_proyecto(db, id_proyecto, id_usuario)
    return proyecto

# Ruta para obtener el detalle del proyecto y evaluador para calificar un proyecto
@routerObtenerProyectos.get("/obtener-items-rubricas-proyecto/", response_model=dict)
async def obtener_items_rubricas_proyecto(
    id_proyecto: int,
    id_usuario: int,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_RESPUESTAS_RUBRICAS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    items_rubrica_proyecto = get_datos_rubrica_proyecto(db, id_proyecto, id_usuario)

    items_rubrica = [dict(item) for item in items_rubrica_proyecto]

    return {
        "items_rubrica": items_rubrica,
    }


