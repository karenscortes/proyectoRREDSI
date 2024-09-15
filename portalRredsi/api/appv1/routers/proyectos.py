from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from appv1.crud.proyectos import create_project_sql
from appv1.routers.login import get_current_user
from appv1.schemas.proyecto import  ProyectoCreate
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.permissions import get_permissions

router_project = APIRouter()


@router_project.post("/create")
async def insert_user(
    project: ProyectoCreate, 
    db: Session = Depends(get_db)
    
):
    
    respuesta = create_project_sql(db,project )
    if respuesta:
        return {"mensaje":"Proyecto Ingresado exitosamente"}
        
