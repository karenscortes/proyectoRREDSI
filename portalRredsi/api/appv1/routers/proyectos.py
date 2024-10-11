from fastapi import APIRouter, HTTPException, Depends, Form, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from typing import List, Optional

from appv1.crud.proyectos import create_full_project
from appv1.schemas.proyecto import AutorCreate, ProyectoResponse, ProyectoCreate, ParticipanteCreate
from db.database import get_db
from core.utils import save_file

router_project = APIRouter()

@router_project.post("/projects/create-project", response_model=ProyectoResponse)
def create_project(
    id_institucion: int = Form(...),
    id_modalidad: int = Form(...),
    id_area_conocimiento: int = Form(...),
    titulo: str = Form(...),
    programa_academico: str = Form(...),
    grupo_investigacion: Optional[str] = Form(None),
    linea_investigacion: Optional[str] = Form(None),
    nombre_semillero: Optional[str] = Form(None),
    url_propuesta_escrita: UploadFile = File(None),
    url_aval: UploadFile = File(None),
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
    autores: str = Form(...),  # Recibe los autores como una cadena
    db: Session = Depends(get_db)
):
    try:
        # Iniciar la transacción explícita
        with db.begin():
            # Guardar los archivos
            url_propuesta_escrita_path = save_file(url_propuesta_escrita) if url_propuesta_escrita else None
            url_aval_path = save_file(url_aval) if url_aval else None

            autores_lista = autores.split(",")  # Aquí se divide la cadena por comas

            # Preparar los datos del proyecto
            proyecto = ProyectoCreate(
                id_institucion=id_institucion,
                id_modalidad=id_modalidad,
                id_area_conocimiento=id_area_conocimiento,
                titulo=titulo,
                programa_academico=programa_academico,
                grupo_investigacion=grupo_investigacion,
                linea_investigacion=linea_investigacion,
                nombre_semillero=nombre_semillero,
                url_propuesta_escrita=url_propuesta_escrita_path,
                url_aval=url_aval_path,
                autores=[AutorCreate(nombre=autor.strip()) for autor in autores_lista]  # Creamos la lista de objetos AutorCreate
            )

            # Preparar los datos del tutor
            tutor = ParticipanteCreate(
                id_tipo_documento=tutor_id_tipo_documento,
                documento=tutor_documento,
                nombres=tutor_nombres,
                apellidos=tutor_apellidos,
                celular=tutor_celular,
                correo=tutor_correo
            )
            # Preparar el primer ponente
            ponente1 = ParticipanteCreate(
                id_tipo_documento=ponente1_id_tipo_documento,
                documento=ponente1_documento,
                nombres=ponente1_nombres,
                apellidos=ponente1_apellidos,
                celular=ponente1_celular,
                correo=ponente1_correo
            )

            # Preparar el segundo ponente (si se proporciona)
            ponente2 = None
            if ponente2_id_tipo_documento and ponente2_documento:
                ponente2 = ParticipanteCreate(
                    id_tipo_documento=ponente2_id_tipo_documento,
                    documento=ponente2_documento,
                    nombres=ponente2_nombres,
                    apellidos=ponente2_apellidos,
                    celular=ponente2_celular,
                    correo=ponente2_correo
                )

            # Llamar al CRUD para insertar el proyecto y manejar la lógica
            response = create_full_project(db, proyecto, tutor, ponente1, ponente2)

        # Si todo fue exitoso, se confirma la transacción automáticamente (db.commit() al final del with)

        # Retornar la respuesta con el ID del proyecto creado
        return ProyectoResponse(id_proyecto=response["project_id"], status="Proyecto creado con éxito")

    except (IntegrityError, SQLAlchemyError) as e:
        # En caso de error de integridad o SQL, se hará rollback automáticamente
        raise HTTPException(status_code=500, detail=f"Error {str(e)}")
    except Exception as e:
        # En caso de cualquier otro error, se hará rollback automáticamente
        raise HTTPException(status_code=500, detail=f"Error {str(e)}")
