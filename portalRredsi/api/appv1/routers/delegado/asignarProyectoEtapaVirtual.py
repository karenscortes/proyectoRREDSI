from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from appv1.schemas.delegado.asignacionProyectoEtapaVirtual import AsignarProyectoEtapaUno
from db.database import get_db
from appv1.crud.delegado.asignarProyectoEtapaVirtual import asignar_proyecto_etapa_virtual, get_convocatoria_actual_por_proyecto

router_proyecto_etapa_uno = APIRouter()

@router_proyecto_etapa_uno.post("/asignar-proyecto-etapa-uno")
async def asignar_proyecto_etapa_uno(
    asignacion: AsignarProyectoEtapaUno,
    db: Session = Depends(get_db)
):
    respuesta = asignar_proyecto_etapa_virtual(db, asignacion)
    if respuesta:
        return {"mensaje":f"Proyecto asignado a {asignacion.id_datos_personales} "}
    else:
        return {"mensaje":"El proyecto no se ha podido asignar con exito"}


@router_proyecto_etapa_uno.get("/obtener-proyecto-convocatoria", response_model=dict)
async def buscar_convocatoria_por_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db)
):
    proyecto_convocatoria = get_convocatoria_actual_por_proyecto(db, id_proyecto)
    
    if proyecto_convocatoria:
        return {
            "proyecto_convocatoria": proyecto_convocatoria._asdict()
        }
    else:
        return {"mensaje":"El proyecto no se ha podido encontrar en una convocatoria vigente."}
