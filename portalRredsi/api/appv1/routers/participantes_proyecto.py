from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from appv1.schemas.participantes_proyecto import participanteProyectoCreate
from db.database import get_db
from appv1.crud.participantes_proyecto import create_participantes_proyecto



router_participante_proyecto = APIRouter()

@router_participante_proyecto.post("/create")
def add_participantes_proyectos(
    participantes_proyectos: participanteProyectoCreate,
    db: Session = Depends(get_db)
):
    respuesta= create_participantes_proyecto(db, participantes_proyectos)
    if respuesta:
        return {"mensaje":"Participante proyecto ingresado exitosamente"}

    respuesta = create_participantes_proyecto(db, participantes_proyectos)
    if respuesta:
        return {"mensaje":"Participante Proyecto registrado con éxito"}