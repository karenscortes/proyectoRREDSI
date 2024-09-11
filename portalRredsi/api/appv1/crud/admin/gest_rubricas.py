from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from appv1.models.rubrica import Rubrica 
from appv1.models.item_rubrica import Item_rubrica
from appv1.schemas.administrador.items_rubrica import ItemCreate

def get_all_rubricas(db: Session):
    try:
        return  db.query(Rubrica).all()
    except SQLAlchemyError as e:
        print(f"Error al consultar las rubricas: {e}")
        raise HTTPException(status_code=500, detail=f"Error al consultar las rubricas{e}",)


def create_items(item: ItemCreate,db: Session):
    try:
        nuevo_item = Item_rubrica(
            id_rubrica = item.id_rubrica, 
            titulo = item.titulo, 
            componente = item.componente, 
            valor_max = item.valor_max,
        )
        db.add(nuevo_item)
        db.commit()
        return True
    except SQLAlchemyError as e:
        print(f"Error al consultar las rubricas: {e}")
        raise HTTPException(status_code=500, detail=f"Error al consultar las rubricas{e}",)