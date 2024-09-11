from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from appv1.models.rubrica import Rubrica 
from appv1.models.item_rubrica import Item_rubrica
from appv1.schemas.admin.items_rubrica import ItemCreate, ItemUpdate
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def get_all_rubricas(db: Session):    
    try:
        result = db.query(Rubrica).all()
        if result is None:
            raise HTTPException(status_code=404, detail="No hay rúbricas registradas")
        return result 
    except SQLAlchemyError as e:
        db.rollback()
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
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos crear el item")
        
    except SQLAlchemyError as e:
        print(f"Error al consultar las rubricas: {e}")
        raise HTTPException(status_code=500, detail=f"Error al crear items{e}",)


def update_items(item_id: int, nuevo_item: ItemUpdate,db: Session):
    try:
        item_editar = db.query(Item_rubrica).filter(Item_rubrica.id_item_rubrica == item_id).first()
        if item_editar is None:
            raise HTTPException(status_code=404, detail="Sala no encontrada")
        
        if(nuevo_item.titulo): 
            item_editar.titulo = nuevo_item.titulo

        if(nuevo_item.componente):
            item_editar.componente = nuevo_item.componente

        if(nuevo_item.valor_max):
            item_editar.valor_max = nuevo_item.valor_max

        if(nuevo_item.valor_max and nuevo_item.componente and nuevo_item.titulo): 
            item_editar.titulo = nuevo_item.titulo
            item_editar.componente = nuevo_item.componente
            item_editar.valor_max = nuevo_item.valor_max

        try:
            db.commit() 
            db.refresh(item_editar)
            return item_editar
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar la sala")
        
    except SQLAlchemyError as e:
        print(f"Error al consultar las rubricas: {e}")
        raise HTTPException(status_code=500, detail=f"Error al consultar las rubricas{e}",)
    

def delete_items(id_item:int,db: Session):
    try:
        item = db.query(Item_rubrica).filter(Item_rubrica.id_item_rubrica == id_item).first()       
        if item is None:
            raise HTTPException(status_code=404, detail="Sala no encontrada")

        db.delete(item)
        db.commit()
        return True
    except SQLAlchemyError as e:
        print(f"Error al consultar las rubricas: {e}")
        raise HTTPException(status_code=500, detail=f"Error al consultar las rubricas{e}",)
    
