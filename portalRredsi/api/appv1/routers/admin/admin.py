import json
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.admin.gest_delegado import create_delegado,get_delegados_activos_paginated, get_delegados_by_document
from appv1.crud.admin.gest_rubricas import create_items, delete_items, get_all_rubricas, update_items
from appv1.crud.admin.gest_rubricas import get_all_rubricas
from appv1.crud.admin.admin import create_convocatoria, create_etapa, create_fase, create_sala, get_fases_by_etapa, update_etapa, update_fase, update_sala
from appv1.routers.login import get_current_user
from appv1.schemas.admin.admin import ConvocatoriaCreate, CreateSala, FaseUpdate
from appv1.crud.admin.admin import create_convocatoria, create_etapa, create_fase, get_fases_by_etapa, update_etapa, update_fase
from appv1.schemas.admin.delegado import DelegadoResponse, PaginatedDelegadoResponse
from appv1.schemas.admin.items_rubrica import ItemCreate, ItemUpdate
from appv1.schemas.admin.rubrica import RubricaResponse
from appv1.schemas.usuario import UserCreate, UserResponse
from db.database import get_db
from appv1.crud.permissions import get_permissions
from appv1.crud.usuarios import get_user_by_documento, get_user_by_email

router_admin = APIRouter()

# Crear convocatoria
@router_admin.post("/crear-convocatoria")
def create_new_convocatoria(convocatoria: ConvocatoriaCreate, db: Session = Depends(get_db)):
    return create_convocatoria(db, convocatoria.nombre, convocatoria.fecha_inicio, convocatoria.fecha_fin, convocatoria.estado)

# Endpoint para crear una nueva etapa
@router_admin.post("/convocatoria/{id_convocatoria}/etapas")
def add_etapa(id_convocatoria: int, nombre: str, db: Session = Depends(get_db)):
    return create_etapa(db, nombre, id_convocatoria)

# Endpoint para crear una nueva fase
@router_admin.post("/etapas/{id_etapa}/fases")
def add_fase(id_etapa: int, nombre: str, db: Session = Depends(get_db)):
    return create_fase(db, nombre, id_etapa)

# Endpoint para obtener fases por etapa
@router_admin.get("/etapas/{id_etapa}/fases")
def get_fases(id_etapa: int, db: Session = Depends(get_db)):
    return get_fases_by_etapa(db, id_etapa)

# Endpoint para editar una etapa
@router_admin.put("/etapas/{id_etapa}")
def modify_etapa(id_etapa: int, nombre: Optional[str] = None, db: Session = Depends(get_db)):
    return update_etapa(db, id_etapa, nombre)

# Editar fase
@router_admin.put("/edit-fase/{id_fase}/")
async def update_existing_fase(id_fase: int, fase_update: FaseUpdate, db: Session = Depends(get_db)):
    return update_fase(db, id_fase, fase_update)

# Endpoint para editar una fase
@router_admin.put("/fases/{id_fase}")
def modify_fase(id_fase: int, nombre: Optional[str] = None, db: Session = Depends(get_db)):
    return update_fase(db, id_fase, nombre)

#Obtener todas las rubricas
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

#Obtener delegados activos(paginado)
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

#Obtener delegado por documento
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

#Crear delegado 
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

#Crear items
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
    
    item = create_items(item, db)
    if item:
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
    
#Editar items
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
    
#Eliminar items
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
def update_sala_admin(id_sala: int, id_usuario: Optional[int] = None, area_conocimiento: Optional[int] = None, nombre_sala: Optional[str] = None, numero_sala: Optional[str] = None, db: Session = Depends(get_db)):
    return update_sala(db, id_sala, id_usuario, area_conocimiento,nombre_sala,numero_sala)