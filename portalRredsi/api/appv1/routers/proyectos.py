
import os
import shutil
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from core.utils import save_file
from db.database import get_db
from appv1.crud.proyectos import insert_full_project, insert_user

router_project = APIRouter()

# Ruta para crear un proyecto completo y manejar la subida de archivos
@router_project.post("/projects/create", response_model=dict)
async def crear_proyecto_completo(
    id_institucion: int = Form(...),
    id_modalidad: int = Form(...),
    id_area_conocimiento: int = Form(...),
    titulo: str = Form(...),
    programa_academico: str = Form(...),
    grupo_investigacion: str = Form(...),
    linea_investigacion: str = Form(...),
    nombre_semillero: str = Form(...),
    tutor_id_tipo_documento: int = Form(...),
    tutor_documento: str = Form(...),
    tutor_nombres: str = Form(...),
    tutor_apellidos: str = Form(...),
    tutor_celular: str = Form(...),
    tutor_correo: str = Form(...),
    ponente1_id_tipo_documento: int = Form(...),
    ponente1_documento: str = Form(...),
    ponente1_nombres: str = Form(...),
    ponente1_apellidos: str = Form(...),
    ponente1_celular: str = Form(...),
    ponente1_correo: str = Form(...),
    ponente2_id_tipo_documento: Optional[int] = Form(None),
    ponente2_documento: Optional[str] = Form(None),
    ponente2_nombres: Optional[str] = Form(None),
    ponente2_apellidos: Optional[str] = Form(None),
    ponente2_celular: Optional[str] = Form(None),
    ponente2_correo: Optional[str] = Form(None),
    autores: List[str] = Form(...),  # Lista de autores
    propuesta_file: UploadFile = File(...),
    aval_file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """ Ruta para crear un proyecto completo, incluyendo tutor, ponentes, autores y la subida de archivos. """
    
    # Guardar los archivos de propuesta y aval
    propuesta_path = None
    aval_path = None
    
    if propuesta_file:
        # Guarda el archivo de propuesta
        try:
            propuesta_path = os.path.join("static/files", propuesta_file.filename)
            with open(propuesta_path, "wb") as buffer:
                shutil.copyfileobj(propuesta_file.file, buffer)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error al guardar la propuesta")

    if aval_file:
        # Guarda el archivo de aval
        try:
            aval_path = os.path.join("static/files", aval_file.filename)
            with open(aval_path, "wb") as buffer:
                shutil.copyfileobj(aval_file.file, buffer)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error al guardar el aval")

    # Datos del proyecto
    project_data = {
        "id_institucion": id_institucion,
        "id_modalidad": id_modalidad,
        "id_area_conocimiento": id_area_conocimiento,
        "titulo": titulo,
        "programa_academico": programa_academico,
        "grupo_investigacion": grupo_investigacion,
        "linea_investigacion": linea_investigacion,
        "nombre_semillero": nombre_semillero,
        "url_propuesta_escrita": propuesta_path,
        "url_aval": aval_path
    }

    # Datos del tutor
    tutor_data = {
        "id_tipo_documento": tutor_id_tipo_documento,
        "documento": tutor_documento,
        "nombres": tutor_nombres,
        "apellidos": tutor_apellidos,
        "celular": tutor_celular,
        "correo": tutor_correo
    }

    # Datos del ponente principal
    ponente_data = {
        "id_tipo_documento": ponente1_id_tipo_documento,
        "documento": ponente1_documento,
        "nombres": ponente1_nombres,
        "apellidos": ponente1_apellidos,
        "celular": ponente1_celular,
        "correo": ponente1_correo
    }

    # Datos del ponente opcional
    ponente_opcional_data = None
    if ponente2_documento:
        ponente_opcional_data = {
            "id_tipo_documento": ponente2_id_tipo_documento,
            "documento": ponente2_documento,
            "nombres": ponente2_nombres,
            "apellidos": ponente2_apellidos,
            "celular": ponente2_celular,
            "correo": ponente2_correo
        }

    # Lista de autores
    autores_data = [{"nombre": autor} for autor in autores]

    try:
        # Insertar tutor
        tutor_id = insert_user(db, tutor_data, rol=4)

        # Insertar ponente principal
        ponente_id = insert_user(db, ponente_data, rol=5)

        # Insertar ponente opcional si existe
        if ponente_opcional_data:
            ponente_opcional_id = insert_user(db, ponente_opcional_data, rol=5)

        # Llamar al CRUD para insertar todo el proyecto
        insert_full_project(db, project_data, tutor_data, ponente_data, autores_data, ponente_opcional_data)

        return {"mensaje": "Proyecto, tutor, ponentes y autores creados exitosamente"}
    
    except Exception as e:
        db.rollback()  # Realiza rollback si ocurre algún error
        raise HTTPException(status_code=500, detail=str(e))