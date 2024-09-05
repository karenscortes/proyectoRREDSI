from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.postulaciones import get_all_applications, get_convocatoria

router_postulaciones = APIRouter()
MODULE = 'postulaciones_evaluadores'

@router_postulaciones.get("/get-all-applications/", response_model=List[UserResponse])
async def read_all_applications(
    db: Session = Depends(get_db)
    #current_user: UserResponse = Depends(get_current_user)
):
    # permisos = get_permissions(db, current_user.user_role, MODULE)
    # if not permisos.p_select:
    #     raise HTTPException(status_code=401, detail="Usuario no autorizado")
    id_convocatoria = get_convocatoria(db)
    usuarios = get_all_applications(db, id_convocatoria)
    if len(usuarios) == 0:
        raise HTTPException(status_code=404, detail="No hay usuarios")
    return usuarios

@router_postulaciones.put("/update-application-status/", response_model=dict)
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
    id_convocatoria = get_convocatoria(db)
    # verify_evaluator = get_user_by_id(db, id_evaluador)
    # if verify_evaluator is None:
    #     raise HTTPException(status_code=404, detail="Evaluador no encontrado")     
    updated= update_application_status(db, id_convocatoria, id_evaluador,estado)
    if updated:
        return {"mensaje": "Postulación procesada con exito" }
