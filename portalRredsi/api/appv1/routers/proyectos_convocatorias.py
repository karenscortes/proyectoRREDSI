from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from appv1.schemas.proyecto_convocatoria import ProyectoConvocatoriaCreate
from db.database import get_db
from appv1.crud.proyectos_convocatoria import create_proyecto_convocatoria



router_proyectoConvocatoria = APIRouter()

@router_proyectoConvocatoria.post("/create")
def add_proyecto_convocatoria(
    proyecto_convocatoria: ProyectoConvocatoriaCreate,
    db: Session = Depends(get_db)
):
    respuesta= create_proyecto_convocatoria(db, proyecto_convocatoria)
    if respuesta:
        return {"mensaje":"ProyectoConvocatoria ingresado exitosamente"}

    respuesta = create_proyecto_convocatoria(db, proyecto_convocatoria)
    if respuesta:
        return {"mensaje":"ProyectoConvocatoria registrado con éxito"}