from typing import Dict
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.evaluador.evaluador import CalificarProyectoRespuesta, ListaDeProgramacionFases, PaginatedResponse, PaginatedResponseHorario, PostulacionEvaluadorCreate, RespuestaRubricaCreate
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.evaluador.proyectos import convertir_timedelta_a_hora, create_postulacion_evaluador, get_current_convocatoria, get_datos_calificar_proyecto_completo, get_datos_proyecto_calificado_completo, get_etapa_actual, get_nombres_fases_y_fechas_programacion, get_proyectos_etapa_presencial_con_horario, get_proyectos_por_etapa, get_proyectos_por_etapa_y_estado, insert_respuesta_rubrica
from appv1.crud.permissions import get_permissions

routerObtenerProyectos = APIRouter()
routerInsertarPostulacionEvaluador = APIRouter()
routerInsetarCalificacionRubrica = APIRouter()
routerObtenerHorarioEvaluador = APIRouter()
routerObtenerEtapaActual = APIRouter()
routerObtenerProgramacionFases = APIRouter()

# ID del modulo
MODULE_PROYECTOS = 11
MODULE_POSTULACIONES = 8
MODULE_RESPUESTAS_RUBRICAS = 14
MODULE_ETAPAS = 4
MODULE_PROGRAMACION_FASES = 7

# Ruta para obtener los proyectos asignados por etapa (Presencial/Virtual) paginados
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

# Ruta para obtener los proyectos asignados por estado (calificado/pendiente) y dependiendo de la etapa (Presencial/Virtual) paginados
@routerObtenerProyectos.get("/obtener-proyectos-por-etapa-y-estado/", response_model=PaginatedResponse)
async def obtener_proyectos_por_etapa_y_estado(
    nombre_etapa: str,
    estado_evaluacion: str,
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")

    response = get_proyectos_por_etapa_y_estado(db, nombre_etapa, estado_evaluacion, id_usuario, page, page_size)
    return response

# Ruta para insertar la postulacion del evaluador
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
    
# Ruta para insertar la calificacion de la rúbrica
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
        calificacion_final=respuesta.calificacion_final,
        etapa_actual=respuesta.etapa_actual
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
            proyecto_dict['hora_inicio'] = (
                convertir_timedelta_a_hora(proyecto_dict['hora_inicio'])
                if proyecto_dict['hora_inicio'] is not None else None
            )
            proyecto_dict['hora_fin'] = (
                convertir_timedelta_a_hora(proyecto_dict['hora_fin'])
                if proyecto_dict['hora_fin'] is not None else None
            )
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
    nombre_etapa: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROYECTOS)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    proyecto = get_datos_calificar_proyecto_completo(db, id_proyecto, id_usuario, nombre_etapa)
    return proyecto

# Ruta para obtener la etapa actual de la convocotaria en curso
@routerObtenerEtapaActual.get("/obtener-etapa-actual/", response_model=Dict[str, str])
async def obtener_etapa_actual(
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Verificar permisos (opcional)
    permisos = get_permissions(db, current_user.id_rol, MODULE_ETAPAS)  
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    etapa_actual = get_etapa_actual(db)
    return etapa_actual

# Ruta para obtener el detalle del proyecto calificado
@routerObtenerProyectos.get("/obtener-datos-del-proyecto-calificado/", response_model=CalificarProyectoRespuesta)
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
    
    proyecto = get_datos_proyecto_calificado_completo(db, id_proyecto, id_usuario, nombre_etapa)
    return proyecto

# Ruta para obtener las programaciones de las fases de la convocatoria en curso
@routerObtenerProgramacionFases.get("/obtener-programacion-fases/", response_model=ListaDeProgramacionFases)
async def obtener_programacion_fases(
    nombre_etapa: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Verificar permisos (opcional)
    permisos = get_permissions(db, current_user.id_rol, MODULE_PROGRAMACION_FASES)  
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="No está autorizado a utilizar este módulo")
    
    programacion_fases = get_nombres_fases_y_fechas_programacion(db, nombre_etapa)
    return {"data": programacion_fases}