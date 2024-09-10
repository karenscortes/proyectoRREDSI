from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.evento import EventoResponse
from db.database import get_db
from appv1.crud.eventos import get_eventos_activos

router_evento = APIRouter()

@router_evento.get("/get_eventos_activos/", response_model=List[EventoResponse])
async def read_all_events(
    db: Session = Depends(get_db)
):
    eventos = get_eventos_activos(db)
    if len(eventos) == 0:
        raise HTTPException(status_code=404, detail="Eventos no encontrados")
    return eventos