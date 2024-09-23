from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from requests import Session
from appv1.crud.proyectos import create_project_sql
from appv1.schemas.proyecto import  ProyectoCreate
from core.utils import save_file
from db.database import get_db

router_project = APIRouter()


@router_project.post("/create",response_model=dict)
async def insert_project(
    id_institucion: int = Form(...),
    id_modalidad: int = Form(...),
    id_area_conocimiento: int = Form(...),
    titulo: str = Form(...),
    programa_academico: str = Form(...),
    grupo_investigacion: str = Form(...),
    linea_investigacion: str = Form(...),
    nombre_semillero: str = Form(...),
    url_propuesta_escrita:UploadFile = File(...),
    url_aval:UploadFile = File(...),
    db: Session = Depends(get_db)
    
):
    try:
        file_url_propuesta = save_file(url_propuesta_escrita)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    try:
        file_url_aval = save_file(url_aval)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    
    project = ProyectoCreate(
        id_institucion = id_institucion,
        id_modalidad = id_modalidad,
        id_area_conocimiento = id_area_conocimiento,
        titulo= titulo,
        programa_academico = programa_academico,
        grupo_investigacion= grupo_investigacion,
        linea_investigacion= linea_investigacion,
        nombre_semillero= nombre_semillero
    )
    
    respuesta = create_project_sql(db,project,file_url_propuesta,file_url_aval)
    
    if respuesta:
        return {"mensaje":"Proyecto Ingresado exitosamente"}
        
