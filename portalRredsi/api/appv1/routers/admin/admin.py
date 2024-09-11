from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from appv1.crud.admin.gest_delegado import create_delegados, get_delegados_activos, get_delegados_by_document
from appv1.crud.admin.gest_rubricas import create_items, delete_items, get_all_rubricas, update_items
from appv1.crud.admin.gest_delegado import get_delegados_activos
from appv1.crud.admin.gest_rubricas import get_all_rubricas
from appv1.crud.admin.admin import create_convocatoria, create_etapa, create_fase, create_sala, get_fases_by_etapa, update_etapa, update_fase, update_sala
from appv1.schemas.admin.admin import ConvocatoriaCreate, CreateSala, FaseUpdate
from appv1.crud.admin.admin import create_convocatoria, create_etapa, create_fase, get_fases_by_etapa, update_etapa, update_fase
from appv1.schemas.admin.delegado import DelegadoResponse
from appv1.schemas.admin.items_rubrica import ItemCreate, ItemUpdate
from appv1.schemas.admin.rubrica import RubricaResponse
from appv1.schemas.usuario import UserCreate
from db.database import get_db

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
async def consult_rubrics(db: Session = Depends(get_db)):
    existing_rubrics = get_all_rubricas(db)
    if existing_rubrics:
        return existing_rubrics
    else:
        return{
            'success': False,
            'message': 'Error',
        }

#Obtener delegados activos
@router_admin.get("/all-active-delegates/", response_model=List[DelegadoResponse])
async def consult_delegates(db: Session = Depends(get_db)):
    active_delegates = get_delegados_activos(db)
    if active_delegates:
        return active_delegates
    else:
        return{
            'success': False,
            'message': 'Error',
        }

#Obtener delegado por cedula
@router_admin.get("/delegates/{doc}/", response_model= DelegadoResponse)
def consult_by_document(document: str, db: Session = Depends(get_db)):
    delegates = get_delegados_by_document(document, db)
    if delegates:
        return delegates
    else:
        return{
            'success': False,
            'message': 'Error',
        }

#Crear delegado 
@router_admin.post("/create-delegates/")
def consult_by_document(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_delegados(user, db)
    if new_user:
        return print("Registrado con éxito")
    else: 
        return False

#Crear items
@router_admin.post("/create-items/")
def create_item_rubric(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = create_items(item, db)
    if new_item:
        return print("Registrado con éxito")
    else: 
        return False
    
#Editar items
@router_admin.post("/update-items/{id_item}/")
def update_item(id_item:int, item_nuevo: ItemUpdate, db: Session = Depends(get_db)):
    item = update_items(id_item,item_nuevo,db)
    if item:
        return print("update con éxito")
    else: 
        return False
    
#Eliminar items
@router_admin.post("/delete-items/{id_item}/")
def delete_item(id_item:int, db: Session = Depends(get_db)):
    item = delete_items(id_item,db)
    if item:
        return print("update con éxito")
    else: 
        return False
   
# Crear sala
@router_admin.post("/crear-sala")
def create_sala_admin(sala: CreateSala, db: Session = Depends(get_db)):
    return create_sala(db, sala.id_usuario, sala.area_conocimento, sala.numero_sala, sala.nombre_sala)

# Editar sala
@router_admin.put("/salas/{id_sala}")
def update_sala_admin(id_sala: int, id_usuario: Optional[int] = None, area_conocimiento: Optional[int] = None, nombre_sala: Optional[str] = None, numero_sala: Optional[str] = None, db: Session = Depends(get_db)):
    return update_sala(db, id_sala, id_usuario, area_conocimiento,nombre_sala,numero_sala)