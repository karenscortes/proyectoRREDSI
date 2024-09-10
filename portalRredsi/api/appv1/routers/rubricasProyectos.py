from fastapi import APIRouter, FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional

app = FastAPI()
router_rubrica = APIRouter()
MODULE = 'rubricas'

@router_rubrica.get("/rubricas/", response_model=List[dict])
def get_rubricas(tutor_id: int, proyecto_id:int, db: Session):
    if tutor_id is None and proyecto_id is None:
        raise HTTPException(status_code=400, detail="Debe proporcionar el ID del tutor o el ID del proyecto.")
    
    try:
        if tutor_id is not None:
            sql = text("""
                SELECT r.id_rubrica, r.titulo AS rubrica_titulo, 
                       i.id_item_rubrica, i.titulo AS item_titulo, i.componente, i.valor_max
                FROM rubricas r
                JOIN items_rubrica i ON r.id_rubrica = i.id_rubrica
                JOIN participantes_proyecto pp ON pp.id_proyecto = r.id_proyecto
                WHERE pp.id_usuario = :tutor_id AND i.titulo IS NOT NULL AND i.componente IS NOT NULL
            """)
            result = db.execute(sql, {"tutor_id": tutor_id}).fetchall()
        elif proyecto_id is not None:
            sql = text("""
                SELECT r.id_rubrica, r.titulo AS rubrica_titulo, 
                       i.id_item_rubrica, i.titulo AS item_titulo, i.componente, i.valor_max
                FROM rubricas r
                JOIN items_rubrica i ON r.id_rubrica = i.id_rubrica
                JOIN proyectos p ON p.id_proyecto = r.id_proyecto
                WHERE p.id_proyecto = :proyecto_id AND i.titulo IS NOT NULL AND i.componente IS NOT NULL
            """)
            result = db.execute(sql, {"proyecto_id": proyecto_id}).fetchall()

        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron rúbricas.")
        
        return result

    except SQLAlchemyError as e:
        print(f"Error al buscar rúbricas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar rúbricas.")