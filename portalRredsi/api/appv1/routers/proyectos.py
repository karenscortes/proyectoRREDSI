from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from core.utils import save_file, generate_project_id
from db.database import get_db
from appv1.schemas.proyecto import ProyectoCreate
from appv1.schemas.tutor import UserTutorCreate
from appv1.schemas.ponente import UserPonenteCreate
from appv1.crud.proyectos import insert_full_project

router_project = APIRouter()

@router_project.post("/projects/create", response_model=dict)
async def create_project(
    # Datos del proyecto
    id_institucion: int = Form(...),  # Recibe directamente el ID de la institución educativa
    programa_academico: str = Form(...),
    grupo_investigacion: str = Form(...),
    linea_investigacion: str = Form(...),
    modalidad: int = Form(...),
    titulo: str = Form(...),
    propuesta_escrita: UploadFile = File(...),
    area_conocimiento: int = Form(...),
    aval: UploadFile = File(...),
    # Datos del tutor
    tipo_documento_tutor: int = Form(...),
    documento_tutor: str = Form(...),
    nombres_tutor: str = Form(...),
    apellidos_tutor: str = Form(...),
    celular_tutor: str = Form(...),
    correo_tutor: str = Form(...),
    # Datos del primer ponente
    tipo_documento_ponente1: int = Form(...),
    documento_ponente1: str = Form(...),
    nombres_ponente1: str = Form(...),
    apellidos_ponente1: str = Form(...),
    celular_ponente1: str = Form(...),
    correo_ponente1: str = Form(...),
    # Datos del ponente opcional (opcional)
    tipo_documento_ponente_opcional: int = Form(None),
    documento_ponente_opcional: str = Form(None),
    nombres_ponente_opcional: str = Form(None),
    apellidos_ponente_opcional: str = Form(None),
    celular_ponente_opcional: str = Form(None),
    correo_ponente_opcional: str = Form(None),
    # Autores
    autores: list[str] = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # 1. Guardar los archivos y obtener sus URLs
        propuesta_url = save_file(propuesta_escrita)
        aval_url = save_file(aval)

        # 2. Crear el proyecto
        project_data = ProyectoCreate(
            id_institucion=id_institucion,
            id_modalidad=modalidad,
            id_area_conocimiento=area_conocimiento,
            titulo=titulo,
            programa_academico=programa_academico,
            grupo_investigacion=grupo_investigacion,
            linea_investigacion=linea_investigacion,
            url_propuesta_escrita=propuesta_url,
            url_aval=aval_url,
            autores=autores
        )

        # 3. Crear el tutor
        tutor_data = UserTutorCreate(
            id_tipo_documento=tipo_documento_tutor,
            documento=documento_tutor,
            nombres=nombres_tutor,
            apellidos=apellidos_tutor,
            celular=celular_tutor,
            correo=correo_tutor
        )

        # 4. Crear el primer ponente
        ponente_data = UserPonenteCreate(
            id_tipo_documento=tipo_documento_ponente1,
            documento=documento_ponente1,
            nombres=nombres_ponente1,
            apellidos=apellidos_ponente1,
            celular=celular_ponente1,
            correo=correo_ponente1
        )

        # 5. Verificar si los datos del ponente opcional están completos y son válidos
        ponente_opcional = None
        if documento_ponente_opcional and nombres_ponente_opcional and correo_ponente_opcional:
            if "@" not in correo_ponente_opcional:
                raise HTTPException(status_code=400, detail="El correo del ponente opcional no es válido")

            ponente_opcional = UserPonenteCreate(
                id_tipo_documento=tipo_documento_ponente_opcional,
                documento=documento_ponente_opcional,
                nombres=nombres_ponente_opcional,
                apellidos=apellidos_ponente_opcional,
                celular=celular_ponente_opcional,
                correo=correo_ponente_opcional
            )

        # 6. Insertar todos los datos del proyecto
        result = insert_full_project(db, project_data, tutor_data, ponente_data, ponente_opcional)

        return {"mensaje": "Proyecto y participantes registrados exitosamente", "id_proyecto": result["id_proyecto"]}

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad: " + str(e))
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error en la base de datos: " + str(e))
