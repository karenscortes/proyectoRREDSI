from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from appv1.crud.modalidad import get_all_modalidades
from appv1.schemas.modalidades import modalidadResponse
from sqlalchemy.orm import Session
from db.database import get_db

router_modalidades = APIRouter()
@router_modalidades.get("/get-all-modalidades/", response_model=List[modalidadResponse])
async def read_all_modalidades(
    db: Session = Depends(get_db),
):
    identificacion = get_all_modalidades(db)
    if len(identificacion) == 0:
        raise HTTPException(status_code=404, detail="No hay tipo de modalidades")
    
    return identificacion