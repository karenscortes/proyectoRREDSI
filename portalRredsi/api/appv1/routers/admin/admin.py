from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from appv1.crud.admin.gest_rubricas import get_all_rubricas
from appv1.crud.admin.admin import create_convocatoria, create_etapa, create_fase, get_fases_by_etapa, update_etapa, update_fase
from appv1.schemas.admin.admin import ConvocatoriaCreate, EtapaCreate, FaseCreate, EtapaUpdate, FaseUpdate
from appv1.schemas.administrador.rubrica import RubricaResponse
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


# Endpoint para editar una fase
@router_admin.put("/fases/{id_fase}")
def modify_fase(id_fase: int, nombre: Optional[str] = None, db: Session = Depends(get_db)):
    return update_fase(db, id_fase, nombre)
