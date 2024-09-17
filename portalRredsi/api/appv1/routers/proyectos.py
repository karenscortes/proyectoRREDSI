from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from appv1.crud.proyectos import create_project_sql, create_user_ponente_project, create_user_tutor_project
from appv1.schemas.proyecto import  ProyectoCreate
from appv1.schemas.usuario import UserCreate, UserResponse
from db.database import get_db
from appv1.crud.permissions import get_permissions

router_project = APIRouter()


@router_project.post("/create")
async def insert_project(
    project: ProyectoCreate, 
    usuario:UserCreate,
    db: Session = Depends(get_db)
    
):
    respuesta = create_project_sql(db,project )
    respuesta1=create_user_tutor_project(db,usuario )
    respuesta2=create_user_ponente_project(db,usuario )
    
    if respuesta:
        return {"mensaje":"Proyecto Ingresado exitosamente"}
        
