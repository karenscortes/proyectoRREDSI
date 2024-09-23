from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from appv1.schemas.autores import AutorCreate
from appv1.crud.autor import create_autor_sql
from db.database import get_db


router_autor = APIRouter()
@router_autor.post("/create")
async def insert_autor(
    autor: AutorCreate, 
    db: Session = Depends(get_db),
    
):

    respuesta = create_autor_sql(db, autor)
    if respuesta:
        return {"mensaje":"Autor ingresado exitosamente"}