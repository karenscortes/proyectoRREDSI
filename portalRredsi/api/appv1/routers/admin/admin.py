from typing import List
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

# Crear etapa dentro de convocatoria
@router_admin.post("/crear-etapa/")
async def create_new_etapa(etapa: EtapaCreate, db: Session = Depends(get_db)):
    return create_etapa(db, etapa)

# Crear fase dentro de etapa
@router_admin.post("/crear-fase/")
async def create_new_fase(fase: FaseCreate, db: Session = Depends(get_db)):
    return create_fase(db, fase)

# Obtener fases por etapa
@router_admin.get("/fases/{id_etapa}/")
async def get_fases_for_etapa(id_etapa: int, db: Session = Depends(get_db)):
    return get_fases_by_etapa(db, id_etapa)

# Editar etapa
@router_admin.put("/edit-etapa/{id_etapa}/")
async def update_existing_etapa(id_etapa: int, etapa_update: EtapaUpdate, db: Session = Depends(get_db)):
    return update_etapa(db, id_etapa, etapa_update)

# Editar fase
@router_admin.put("/edit-fase/{id_fase}/")
async def update_existing_fase(id_fase: int, fase_update: FaseUpdate, db: Session = Depends(get_db)):
    return update_fase(db, id_fase, fase_update)


#Obtener todas las rubricas
@router_admin.get("/rubrics/", response_model=List[RubricaResponse])
async def consult_rubrics(db: Session = Depends(get_db)):
    existing_rubrics = get_all_rubricas(db)
    if existing_rubrics:
        return existing_rubrics
    else:
        return{
            'success': False,
            'message': 'Error',
        }
