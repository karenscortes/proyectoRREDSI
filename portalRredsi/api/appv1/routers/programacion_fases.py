from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from appv1.crud.programacion_fases import get_phase_dates

router_fases = APIRouter()

@router_fases.get("/get-phase-dates/", response_model=List[dict])
async def read_phase_dates(db: Session = Depends(get_db)):
    phases = get_phase_dates(db)
    if not phases:
        raise HTTPException(status_code=404, detail="No se encontraron fases")
    
    return phases
