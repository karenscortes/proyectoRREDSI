from collections import defaultdict
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from appv1.models.rubrica import Rubrica 
from appv1.models.item_rubrica import Item_rubrica

def get_all_rubricas(db: Session):
    try:
        return  db.query(Rubrica).all()
    except SQLAlchemyError as e:
        print(f"Error al consultar las rubricas: {e}")
        raise HTTPException(status_code=500, detail=f"Error al consultar las rubricas{e}",)

