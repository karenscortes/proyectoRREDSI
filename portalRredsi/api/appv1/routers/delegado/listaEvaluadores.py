from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.listaEvaluadores import get_all_evaluators, get_id_rol, update_evaluator_status

router_evaluadores = APIRouter()
MODULE = 'usuarios'

@router_evaluadores.get("/get-all-evaluators/", response_model=List[UserResponse])
async def read_all_evaluators(
    db: Session = Depends(get_db)
    #current_user: UserResponse = Depends(get_current_user)
):
    # permisos = get_permissions(db, current_user.user_role, MODULE)
    # if not permisos.p_select:
    #     raise HTTPException(status_code=401, detail="Usuario no autorizado")
    id_rol = get_id_rol(db,'Evaluador')
    evaluadores = get_all_evaluators(db, id_rol)
    if len(evaluadores) == 0:
        raise HTTPException(status_code=404, detail="No hay Evaluadores")
    return evaluadores


@router_evaluadores.put("/update-evaluator-status/", response_model=dict)
def update_application_status(
    id_evaluador:str,
    estado: str,
    db: Session = Depends(get_db),
    #current_user: UserResponse = Depends(get_current_user)
):
    # permisos = get_permissions(db, current_user.user_role, MODULE)
    # if user_id != current_user.user_id:
    #     if not permisos.p_update:
    #         raise HTTPException(status_code=401, detail="Usuario no autorizado")

    # verify_evaluator = get_user_by_id(db, id_evaluador)
    # if verify_evaluator is None:
    #     raise HTTPException(status_code=404, detail="Evaluador no encontrado")     
    updated= update_evaluator_status(db,id_evaluador,estado)
    if updated:
        return {"mensaje": "Postulación procesada con exito" }
