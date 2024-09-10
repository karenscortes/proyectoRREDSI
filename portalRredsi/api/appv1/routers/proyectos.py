from fastapi import APIRouter, Depends
from requests import Session
from appv1.crud.proyectos import create_project_sql
from appv1.schemas.proyecto import  ProyectoCreate
from db.database import get_db

router_project = APIRouter()
MODULE = 'proyectos'

@router_project.post("/create")
async def insert_user(
    project: ProyectoCreate, 
    db: Session = Depends(get_db),

    
):
    
    respuesta = create_project_sql(db,project )
    if respuesta:
        return {"mensaje":"Proyecto Ingresado exitosamente"}
        
