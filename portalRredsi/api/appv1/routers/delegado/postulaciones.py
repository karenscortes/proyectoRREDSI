from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.delegado.postulaciones import applicationsResponse, certificatesResponse
from db.database import get_db
from appv1.crud.delegado.postulaciones import get_all_applications, get_all_certificates, update_application_status

router_postulaciones = APIRouter()
MODULE = 'postulaciones_evaluadores'

@router_postulaciones.get("/get-all-applications/", response_model=List[applicationsResponse])
async def read_all_applications(
    db: Session = Depends(get_db)
    #current_user: UserResponse = Depends(get_current_user)
):
    # permisos = get_permissions(db, current_user.user_role, MODULE)
    # if not permisos.p_select:
    #     raise HTTPException(status_code=401, detail="Usuario no autorizado")
    applications = get_all_applications(db)
    if len(applications) == 0:
        raise HTTPException(status_code=404, detail="No hay postulaciones")
    return applications

@router_postulaciones.get("/get-all-certificates", response_model=List[certificatesResponse])
async def read_all_certificates(
    id_usuario:int,
    db: Session = Depends(get_db)
    #current_user: UserResponse = Depends(get_current_user)
):
    # permisos = get_permissions(db, current_user.user_role, MODULE)
    # if not permisos.p_select:
    #     raise HTTPException(status_code=401, detail="Usuario no autorizado")
    certificates = get_all_certificates(db, id_usuario)
    if len(certificates) == 0:
        raise HTTPException(status_code=404, detail="No hay titulos académicos")
    return certificates

@router_postulaciones.put("/update-application-status/", response_model=dict)
def update_status(
    id_evaluador:int,
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
    updated= update_application_status(db,id_evaluador,estado)
    if updated:
        return {"mensaje": "Postulación procesada con exito" }
