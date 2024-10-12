from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.delegado.listaEvaluadores import EvaluatorsResponse, PaginatedUnassignedEvaluators
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.listaEvaluadores import get_all_evaluators, get_evaluator_by_document, get_evaluator_by_id, update_evaluator_status
from appv1.crud.permissions import get_permissions

router_evaluadores = APIRouter()
MODULE = 3

@router_evaluadores.get("/get-all-evaluators/", response_model=PaginatedUnassignedEvaluators)
async def read_all_evaluators(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    evaluadores,total_pages = get_all_evaluators(db, page, page_size)
    if len(evaluadores) == 0:
        raise HTTPException(status_code=404, detail="No hay Evaluadores")
    
    return {
        "evaluators": evaluadores,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }


@router_evaluadores.put("/update-evaluator-status/", response_model=dict)
def update_status(
    id_evaluador:int,
    estado: str,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if current_user.id_rol != 2 or not permisos.p_actualizar: 
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    verify_evaluator = get_evaluator_by_id(db, id_evaluador)
    if verify_evaluator is None:
        raise HTTPException(status_code=404, detail="Evaluador no encontrado")     
    updated= update_evaluator_status(db,id_evaluador,estado)
    if updated:
        return {"mensaje": "Estado de evaluador modificado con exito" }


@router_evaluadores.get("/get-evaluator-by-document/", response_model=List[EvaluatorsResponse])
async def read_evaluator_by_document(
    documento: str, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if current_user.documento != documento:  
        if not permisos.p_consultar:
            raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    evaluator = get_evaluator_by_document(db, documento)
    if evaluator is None:
        raise HTTPException(status_code=404, detail="Evaluador no encontrado")
    
    return evaluator