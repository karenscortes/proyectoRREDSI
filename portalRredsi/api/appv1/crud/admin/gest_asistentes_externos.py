import datetime
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.models.asistente import Asistente
from appv1.models.tipo_documento import Tipo_documento
from appv1.models.usuario import Usuario
from core.security import get_hashed_password
import random
import string

def insert_user(db: Session, tipo_doc: int, num_doc:str, nombres: str, apellidos: str, correo: str, clave: str, telefono: str = None ):
    # Crear un nuevo objeto Usuario
    nuevo_usuario = Usuario(
        id_rol=7,
        id_tipo_documento=tipo_doc,
        documento=num_doc, 
        nombres=nombres, 
        apellidos=apellidos, 
        celular=telefono, 
        correo=correo, 
        clave=get_hashed_password(clave), 
        estado='inactivo' 
    )

    db.add(nuevo_usuario)

    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


def generate_code(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def insert_attendee(db: Session, usuario_id: int, url_comprobante_pago: str):

    nuevo_comprobante = Asistente(
        id_usuario=usuario_id,
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        url_comprobante_pago=url_comprobante_pago
    )

    db.add(nuevo_comprobante)
    db.commit()
    db.refresh(nuevo_comprobante)
    return nuevo_comprobante

def get_id_document_type(db:Session, nombre:str):
    result = db.query(Tipo_documento).filter(Tipo_documento.nombre == nombre).first()
    if result is None:
         raise HTTPException(status_code=404, detail="No se ese tipo de documento")
    return result 

def get_paginated_attendees(db: Session, page, page_size):
    try:
        offset = (page - 1) * page_size
        attendees = db.query(Asistente.url_comprobante_pago, Usuario.id_usuario, Usuario.documento, Usuario.nombres, Usuario.apellidos, Usuario.celular, Usuario.correo).join(Usuario).limit(page_size).offset(offset).all()
        if attendees is None:
            raise HTTPException(status_code=404, detail="No hay asistentes")
        
        total_attendees = db.query(Asistente).count()

        # Calcular el número total de páginas
        total_pages = (total_attendees + page_size - 1) // page_size
        return attendees, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar los asistentes: {e}")
        raise HTTPException(status_code=500, detail="Error. No hay integridad de datos")

