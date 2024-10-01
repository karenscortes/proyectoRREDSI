from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from appv1.schemas.rubricasCalificadas import ProyectoRubricasResponse
from appv1.crud.rubricasCalificadas import get_rubricas_calificadas
from db.database import get_db

routerRubricasCalificadas = APIRouter()


@routerRubricasCalificadas.get("/proyectosConvocatorias/rubricas-calificadas/", response_model=ProyectoRubricasResponse)
def obtener_rubricas_calificadas(id_tutor: Optional[int] = None, id_proyecto: Optional[int] = None, db: Session = Depends(get_db)):
    return get_rubricas_calificadas(db, id_tutor, id_proyecto)