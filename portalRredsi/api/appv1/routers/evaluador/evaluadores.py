from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.evaluador.evaluador import PaginatedResponse, PostulacionEvaluadorCreate, RespuestaRubricaCreate
from db.database import get_db
from appv1.crud.evaluador.proyectos import create_postulacion_evaluador, get_current_convocatoria, get_proyectos_asignados, get_proyectos_por_estado, get_proyectos_por_etapa, insert_respuesta_rubrica

routerObtenerProyectos = APIRouter()
routerInsertarPostulacionEvaluador = APIRouter()
routerInsetarCalificacionRubrica = APIRouter()

#Ruta para obtener los proyectos asignados por etapa (Presencial/Virtual) paginados
@routerObtenerProyectos.get("/obtener-proyectos-por-etapa-paginados/", response_model=PaginatedResponse)
async def obtener_proyectos_por_etapa(
    nombre_etapa: str,
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    response = get_proyectos_por_etapa(db, nombre_etapa, id_usuario, page, page_size)
    return response


#Ruta para obtener los proyectos asignados por estado (calificado/pendiente) paginados
@routerObtenerProyectos.get("/obtener-proyectos-por-estado-paginados/", response_model=PaginatedResponse)
async def obtener_proyectos_por_estado(
    estado_evaluacion: str,
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    response = get_proyectos_por_estado(db, estado_evaluacion, id_usuario, page, page_size)
    return response


#Ruta para obtener los proyectos asignados
@routerObtenerProyectos.get("/obtener-proyectos-asignados-paginados/", response_model=PaginatedResponse)
async def obtener_proyectos_asignados(
    id_usuario: int,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    response = get_proyectos_asignados(db, id_usuario, page, page_size)
    return response


#Ruta para insertar la postulacion del evaluador
@routerInsertarPostulacionEvaluador.post("/insertar-postulacion-evaluador/")
async def insertar_postulacion_evaluador(
    postulacion: PostulacionEvaluadorCreate,
    db: Session = Depends(get_db),
):

    convocatoria_actual = get_current_convocatoria(db)
    
    if not convocatoria_actual:
        raise HTTPException(status_code=404, detail="No hay convocatorias en curso.")

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
    db: Session = Depends(get_db),
):

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