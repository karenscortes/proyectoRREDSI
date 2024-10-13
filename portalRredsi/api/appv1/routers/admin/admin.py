from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from appv1.crud.admin.gest_asistentes_externos import existing_attendee, existing_document, existing_email, generate_code, get_attendee_by_document, get_id_document_type, get_paginated_attendees, insert_attendee, insert_user, insertar_historial_admin, update_external_attendees
from appv1.crud.admin.gest_delegado import create_delegado, get_all_document,get_delegados_activos_paginated, get_delegados_by_document, get_user_email, update_status_delegate
from appv1.crud.admin.gest_rubricas import create_items,get_all_rubricas, update_items, update_status
from appv1.crud.admin.gest_rubricas import get_all_rubricas
from appv1.crud.admin.admin import crear_varias_programaciones_fases, create_convocatoria, create_sala, existe_convocatoria_en_curso, obtener_convocatoria_en_curso, update_sala
from appv1.models.programacion_fase import Programacion_fase
from appv1.routers.login import get_current_user
from appv1.schemas.admin.admin import ConvocatoriaCreate, ConvocatoriaResponse, CreateSala, ProgramacionFaseCreate, UpdateSala
from appv1.crud.admin.admin import create_convocatoria
from appv1.schemas.admin.attendees import PaginatedAttendees, UpdatedAttendee
from appv1.schemas.admin.delegado import DelegadoResponse, PaginatedDelegadoResponse
from appv1.schemas.admin.items_rubrica import ItemCreate, ItemUpdate, ItemUpdateStatus
from appv1.schemas.admin.rubrica import RubricaResponse
from appv1.schemas.tipo_documento import TipoDocumentoResponse
from appv1.schemas.usuario import UserCreate, UserResponse
from core.utils import save_file
from db.database import get_db
from appv1.crud.permissions import get_permissions
from appv1.crud.usuarios import get_user_by_documento
import pandas as pd

router_admin = APIRouter()

# Ruta para crear convocatorias 
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

    # Verificar si ya existe una convocatoria en curso usando count()
    if existe_convocatoria_en_curso(db):
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

@router_admin.get("/convocatoria-en-curso", response_model=ConvocatoriaResponse)
def get_convocatoria_en_curso(db: Session = Depends(get_db)):
    convocatoria = obtener_convocatoria_en_curso(db)
    if not convocatoria:
        raise HTTPException(status_code=404, detail="No hay convocatorias en curso")
    
    return convocatoria

@router_admin.post("/crear-programaciones-fases")
def create_programaciones_fases(
    programaciones_fases: List[ProgramacionFaseCreate], 
    db: Session = Depends(get_db),
):
    # 1. Verificar que existe una convocatoria en curso
    convocatoria_activa = existe_convocatoria_en_curso(db)
    
    if not convocatoria_activa:
        raise HTTPException(status_code=400, detail="No hay ninguna convocatoria en curso.")

    # 2. Obtener los detalles de la convocatoria en curso
    convocatoria_en_curso = get_convocatoria_en_curso(db)

    if not convocatoria_en_curso:
        raise HTTPException(status_code=500, detail="Error al obtener la convocatoria en curso.")

    programaciones_para_crear = []

    # Validar cada programación de fase
    for programacion_fase in programaciones_fases:
        # 3. Validar que la fecha de inicio sea antes que la fecha de fin
        if programacion_fase.fecha_inicio >= programacion_fase.fecha_fin:
            raise HTTPException(status_code=400, detail=f"La fecha de inicio debe ser anterior a la fecha de fin en la fase {programacion_fase.id_fase}")

        # 4. Validar que las fechas de la programación estén dentro del rango de las fechas de la convocatoria
        if programacion_fase.fecha_inicio < convocatoria_en_curso.fecha_inicio or programacion_fase.fecha_fin > convocatoria_en_curso.fecha_fin:
            raise HTTPException(status_code=400, detail=f"Las fechas de la fase {programacion_fase.id_fase} deben estar dentro del rango de las fechas de la convocatoria.")

        # 5. Verificar si ya existe una programación de la misma fase para la convocatoria
        programacion_existente = db.query(Programacion_fase).filter(
            Programacion_fase.id_fase == programacion_fase.id_fase,
            Programacion_fase.id_convocatoria == convocatoria_en_curso.id_convocatoria
        ).first()

        if programacion_existente:
            raise HTTPException(status_code=400, detail=f"La programación de la fase {programacion_fase.id_fase} ya existe para la convocatoria.")
        
        # Agregar a la lista de programaciones válidas
        programaciones_para_crear.append(programacion_fase)

    # 6. Crear todas las programaciones de fase si todo está en orden
    programaciones_creadas = crear_varias_programaciones_fases(db, programaciones_para_crear)
    
    return {
        "message": "Programaciones de fases creadas exitosamente", 
        "programaciones_creadas": programaciones_creadas
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
@router_admin.get("/delegates/{busqueda}/", response_model= DelegadoResponse)
def consult_by_document(
    busqueda: str, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 3
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    delegate = get_delegados_by_document(busqueda, db)

    if (delegate is None):
        raise HTTPException(status_code=404, detail="No se encontró un delegado con ese documento")

    return delegate

# Obtener tipos de documento
@router_admin.get("/all_type_documents/")
def consult_all_documents_types(
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
    MODULE = 3
    permisos = get_permissions(db, current_user.id_rol, MODULE)

    if permisos is None or not permisos.p_consultar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    documents_types = get_all_document(db)

    return documents_types

#Actualizar estado delegado 
@router_admin.put("/update-delegate-status/{id_delegate}/")
def update_delegate_status( 
    id_delegate: int,
    data: ItemUpdateStatus,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):  
    MODULE = 3  
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    if permisos is None or not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    delegate = update_status_delegate(id_delegate, data.estado, db)
    insertar_historial_admin(db,'Actualizar',MODULE,id_delegate,current_user.id_usuario)
    if delegate:    
        return{
            'success': True,
            'message': 'Se actualizo con éxito',
        }
    else:           
        return{
            'success': False,
            'message': 'Error al actualizar',
        }
        
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
    
    existing_user_email = get_user_email(db, user.correo)
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
            'data': new_item.id_item_rubrica,
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
    
# editar estado items 
@router_admin.put("/update-status-items/{id_item}/")
def update_status_item(
    data: ItemUpdateStatus,
    id_item:int, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
     
    MODULE = 10
    permisos = get_permissions(db, current_user.id_rol, MODULE)
    
    if permisos is None or not permisos.p_actualizar:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    
    item = update_status(id_item,data.estado,db)
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
        existing_user_email = existing_email(db,row['correo'])
        existing_user_doc = existing_document(db,row['documento'])

        usuario_id=None
        convocatoria= obtener_convocatoria_en_curso(db)

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

            usuario_id=asistente_externo.id_usuario
        else:
            #de lo contrario, se obtiene el id_usuario
            usuario_id=existing_user_doc[0]

        attendee = existing_attendee(db, usuario_id)

        # Si el asistente no se ha ingresado en la tabala asistencia en la convocatoria actual
        if(attendee is None):
            new_attendee = insert_attendee(
                db, 
                usuario_id, 
                row['url_comprobante_pago'],
                convocatoria.id_convocatoria
            )
            
            insertar_historial_admin(db,'Insertar',MODULE,new_attendee.id_asistente,current_user.id_usuario)
            return {"message": "File processed and data stored successfully.", "file_location": file_location}
        else:
            return{"mensaje": f"Ya se ingresó el asistente {attendee[0]} en esta convocatoria"}
            

            


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
