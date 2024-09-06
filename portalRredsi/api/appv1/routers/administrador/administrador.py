from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.administrador.rubrica import RubricaResponse
from db.database import get_db
from appv1.crud.administrador.gest_rubricas import get_all_rubricas

router_admin = APIRouter()


@router_admin.get("/rubricas", response_model=List[RubricaResponse])
async def rubricas_existentes(db: Session = Depends(get_db)):
    rubricas_existentes = get_all_rubricas(db)
    print(rubricas_existentes)
    if rubricas_existentes:
        return rubricas_existentes
    else:
        return{
            'success': False,
            'message': 'Error',
        }


