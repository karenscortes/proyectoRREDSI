from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from appv1.crud.admin.gest_asistentes_externos import generate_code, get_attendee_by_document, get_id_document_type, get_paginated_attendees, insert_attendee, insert_user, insertar_historial_admin, update_external_attendees
from appv1.crud.admin.gest_delegado import create_delegado,get_delegados_activos_paginated, get_delegados_by_document
from appv1.crud.admin.gest_rubricas import create_items, delete_items, get_all_rubricas, update_items
from appv1.crud.admin.gest_rubricas import get_all_rubricas
from appv1.crud.admin.admin import create_convocatoria, create_programacion_fase, create_sala, update_sala
from appv1.models.convocatoria import Convocatoria
from appv1.models.programacion_fase import Programacion_fase
from appv1.routers.login import get_current_user
from appv1.schemas.admin.admin import ConvocatoriaCreate, CreateSala, EstadoDeConvocatoria, ProgramacionFaseCreate, UpdateSala
from appv1.crud.admin.admin import create_convocatoria
from appv1.schemas.admin.attendees import PaginatedAttendees, UpdatedAttendee
from appv1.schemas.admin.delegado import DelegadoResponse, PaginatedDelegadoResponse
from appv1.schemas.admin.items_rubrica import ItemCreate, ItemUpdate
from appv1.schemas.admin.rubrica import RubricaResponse
from appv1.schemas.usuario import UserCreate, UserResponse
from core.utils import save_file
from db.database import get_db
from appv1.crud.permissions import get_permissions
from appv1.crud.usuarios import get_user_by_documento, get_user_by_email
import pandas as pd

router_admin = APIRouter()

@router_admin.post("/crear-convocatoria")
def create_new_convocatoria(
    convocatoria: ConvocatoriaCreate, 
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(get_current_user)
):
    MODULE = 6  # Módulo para convocatorias
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    # Verificación de permisos
    if permisos is None or not permisos.p_insertar:  
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    # Verificar si ya existe una convocatoria en curso
    convocatoria_en_curso = db.query(Convocatoria).filter(Convocatoria.estado == EstadoDeConvocatoria.en_curso.value).first()
    print(f"Valor del estado: {EstadoDeConvocatoria.en_curso.value}")

    
    if convocatoria_en_curso:
        raise HTTPException(status_code=400, detail="Ya existe una convocatoria en curso.")

    # Crear la nueva convocatoria si no hay ninguna en curso
    convocatoria_created = create_convocatoria(
        db, convocatoria.nombre, convocatoria.fecha_inicio, 
        convocatoria.fecha_fin, convocatoria.estado
    )

    # Devolver el ID de la convocatoria creada
    return {
        "message": "Convocatoria creada exitosamente", 
        "id_convocatoria": convocatoria_created.id_convocatoria
    }




@router_admin.post("/crear-programacion-fase")
def create_new_programacion_fase(
    programacion_fase: ProgramacionFaseCreate, 
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(get_current_user)
):
    MODULE = 7  # Módulo para programación de fases
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    # Verificación de permisos
    if permisos is None or not permisos.p_insertar:  
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    # 1. Verificar que la convocatoria esté en curso
    convocatoria_en_curso = db.query(Convocatoria).filter(
        Convocatoria.id_convocatoria == programacion_fase.id_convocatoria,
        Convocatoria.estado == "en_curso"
    ).first()

    if not convocatoria_en_curso:
        raise HTTPException(status_code=400, detail="La convocatoria no está en curso o no existe.")

    # 2. Verificar si ya existe una programación de la misma fase para la convocatoria
    programacion_existente = db.query(Programacion_fase).filter(
        Programacion_fase.id_fase == programacion_fase.id_fase,
        Programacion_fase.id_convocatoria == programacion_fase.id_convocatoria
    ).first()

    if programacion_existente:
        raise HTTPException(status_code=400, detail="La programación de esta fase ya existe para la convocatoria.")

    # 3. Crear la programación de fase si todo está en orden
    programacion_fase_created = create_programacion_fase(
        db, 
        programacion_fase.id_fase, 
        programacion_fase.id_convocatoria, 
        programacion_fase.fecha_inicio, 
        programacion_fase.fecha_fin
    )
    
    return {
        "message": "Programación de fase creada exitosamente", 
        "id_programacion_fase": programacion_fase_created.id_programacion_fase
    }


# Obtener todas las rubricas
@router_admin.get("/all-rubrics/", response_model=List[RubricaResponse])
async def consult_rubrics(
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 9
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    existing_rubrics = get_all_rubricas(db)

    if len(existing_rubrics) == 0:
        raise HTTPException(status_code=404, detail="No hay rubricas")
    
    return existing_rubrics

# Obtener delegados activos(paginado)
@router_admin.get("/all-delegates/", response_model=PaginatedDelegadoResponse)
async def consult_delegates(
    db: Session = Depends(get_db),
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
):  
    MODULE = 3
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    users, total_pages = get_delegados_activos_paginated(db, page, page_size)

    if len(users) == 0:
        raise HTTPException(status_code=404, detail="No hay delegados")

    return {
        "users": users,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }

# Obtener delegado por documento
@router_admin.get("/delegates/{doc}/", response_model= DelegadoResponse)
def consult_by_document(
    document: str, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 3
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    delegate = get_delegados_by_document(document, db)

    if (delegate is None):
        raise HTTPException(status_code=404, detail="No se encontró un delegado con ese documento")

    return delegate

# Crear delegado 
@router_admin.post("/create-delegates/")
def create_delegates(
    user: UserCreate, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 3
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if(user.id_rol != 2):
        raise HTTPException(status_code=400, detail="El rol del usuario es incorrecto")
    
    if permisos is None or not permisos.p_insertar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    existing_user_email = get_user_by_email(db, user.correo)
    existing_user_doc = get_user_by_documento(db,user.documento) 
    if existing_user_email:
        raise HTTPException(status_code=400, detail="Ya se encuentra registrado un usuario con este email")
    
    if existing_user_doc: 
        raise HTTPException(status_code=400, detail="Ya se encuentra registrado un usuario con este documento")
    
    new_user = create_delegado(user, db)
    insertar_historial_admin(db,'Insertar',MODULE,new_user.id_usuario,current_user.id_usuario)
    if new_user:
        return{
            'success': True,
            'message': 'Registrado con éxito',
        }
    else: 
        return{
            'success': False,
            'message': 'Error, no se pudo registrar con éxito',
        }

# Crear items
@router_admin.post("/create-items/")
def create_item_rubric(
    item: ItemCreate, 
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 10
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_insertar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    new_item = create_items(item, db)
    insertar_historial_admin(db,'Insertar',MODULE,new_item.id_item_rubrica,current_user.id_usuario)
    if new_item:
        return{
            'success': True,
            'message': 'Registrado con éxito', 
            'data': item.id_item_rubrica,
        }
    else: 
        return{
            'success': False,
            'message': 'Error, no se pudo registrar con éxito',
        }
    
# Editar items
@router_admin.put("/update-items/{id_item}/")
def update_item(
    id_item:int, 
    item_nuevo: ItemUpdate, 
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 10
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    
    if permisos is None or not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    item = update_items(id_item,item_nuevo,db)
    insertar_historial_admin(db,'Actualizar',MODULE,id_item,current_user.id_usuario)
    if item:
        return{
            'success': True,
            'message': 'Se actualizo con éxito',
            'data': item,
        }
    else: 
        return{
            'success': False,
            'message': 'Error al actualizar',
        }
    
# Eliminar items
@router_admin.post("/delete-items/{id_item}/")
def delete_item(
    id_item:int, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
     
    MODULE = 10
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    
    if permisos is None or not permisos.p_eliminar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    item = delete_items(id_item,db)
    insertar_historial_admin(db,'Eliminar',MODULE,id_item,current_user.id_usuario)
    if item:
        return{
            'success': True,
            'message': 'Se elimino con éxito',
        }
    else: 
        return{
            'success': False,
            'message': 'Error al eliminar',
        }
   
# Crear sala
@router_admin.post("/crear-sala")
def create_sala_admin(
    sala: CreateSala, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),   
):
    MODULE = 15
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_insertar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    new_sala = create_sala(db, sala.id_usuario, sala.area_conocimento, sala.numero_sala, sala.nombre_sala)
    insertar_historial_admin(db,'Insertar',MODULE,new_sala.id_sala,current_user.id_usuario)
    if new_sala:
        return{
            'success': True,
            'message': 'Se agregó sala con éxito',
        }
    else: 
        return{
            'success': False,
            'message': 'Error al crear sala',
        }


# Editar sala
@router_admin.put("/salas/{id_sala}")
def update_sala_admin(
    id_sala: int,
    sala: UpdateSala,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    MODULE = 15
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    # Asumiendo que tienes una función para actualizar la sala en lugar de crearla
    updated_sala = update_sala(id_sala, sala,db )
    insertar_historial_admin(db,'Actualizar',MODULE,id_sala,current_user.id_usuario)
    if updated_sala:
        return {
            'success': True,
            'message': 'Se actualizó la sala con éxito',
        }
    else:
        return {
            'success': False,
            'message': 'Error al actualizar la sala',
        }

# Subir el archivo excel y procesar los datos
@router_admin.post("/upload-excel/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    
    MODULE = 12
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_insertar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    file_location = save_file(file)

    df = pd.read_excel(file_location)

    for index, row in df.iterrows():
        
        #Se comprueba que el asistente no se encuentre en la tabla usuarios
        existing_user_email = get_user_by_email(db,row['correo'])
        existing_user_doc = get_user_by_documento(db,row['documento'])

        id_asistente=None

        #Si no se encontró
        if existing_user_email is None and existing_user_doc is None:
            
            password = generate_code()
            id_tipo_doc = get_id_document_type(db,row['tipo_documento'])

            # se obtiene los datos de los campos indicados y se Insertan en la tabla 'usuarios'
            asistente_externo = insert_user(
                db=db,
                tipo_doc=id_tipo_doc.id_tipo_documento, 
                num_doc=row['documento'], 
                nombres=row['nombres'],
                apellidos=row['apellidos'],
                correo=row['correo'], 
                clave=password,
                telefono=row.get('celular', None)
            )

            id_asistente=asistente_externo.id_usuario
        else:
            #de lo contrario, se obtiene el id_usuario
            id_asistente=existing_user_doc[0]

        # Insertar comprobante_pago y demás datos en la tabala asistencia 
        new_attendee = insert_attendee(
            db, 
            id_asistente, 
            row['url_comprobante_pago']
        )

        insertar_historial_admin(db,'Insertar',MODULE,new_attendee.id_asistente,current_user.id_usuario)
    return {"message": "File processed and data stored successfully.", "file_location": file_location}


# Obtener asistentes paginados
@router_admin.get("/get-all-attendees/", response_model=PaginatedAttendees)
async def get_all_attendees(
    db: Session = Depends(get_db),
    page: int = 1,
    page_size: int = 10,
    current_user: UserResponse = Depends(get_current_user),
):  
    MODULE = 12
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    attendees, total_pages = get_paginated_attendees(db, page, page_size)

    if len(attendees) == 0:
        raise HTTPException(status_code=404, detail="No hay asistentes")

    return {
        "attendees": attendees,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }

# Editar asistente
@router_admin.put("/update-attendee/{id_usuario}/")
def update_attendee(
    id_usuario:int, 
    newData: UpdatedAttendee, 
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 12
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    
    if permisos is None or not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    user,attendee = update_external_attendees(db,id_usuario,newData)
    insertar_historial_admin(db,'Actualizar',MODULE,attendee.id_asistente,current_user.id_usuario)
    if user or attendee:
        return{
            'success': True,
            'message': 'Asistente actualizado con éxito',
            'usuario': user,
            'asistente': attendee,
        }
    else: 
        return{
            'success': False,
            'message': 'Error al actualizar',
        }
    
#Obtener asistente por documento
@router_admin.get("/get-attendee-by-document/", response_model=PaginatedAttendees)
async def get_attendee(
    documento: str,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(get_current_user),
):  
    MODULE = 12
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    attendees, total_pages = get_attendee_by_document(db, documento,page, page_size)

    return {
        "attendees": attendees,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }
