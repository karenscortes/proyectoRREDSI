from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from appv1.crud.institucionEducativa import get_all_institucionEducativa
from appv1.schemas.institucionEducativa import institucionResponse
from sqlalchemy.orm import Session
from db.database import get_db

router_instituciones = APIRouter()
@router_instituciones.get("/get-all-instituciones/", response_model=List[institucionResponse])
async def read_all_instiruciones(
    db: Session = Depends(get_db),
):
    identificacion = get_all_institucionEducativa(db)
    if len(identificacion) == 0:
        raise HTTPException(status_code=404, detail="No hay tipo de instiruciones")
    
    return identificacion