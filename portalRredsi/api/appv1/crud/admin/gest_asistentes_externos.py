import datetime
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from appv1.models.asistente import Asistente
from appv1.models.historial_actividades_admin import Historial_admin
from appv1.models.tipo_documento import Tipo_documento
from appv1.models.usuario import Usuario
from appv1.schemas.admin.attendees import UpdatedAttendee
from core.security import get_hashed_password
import random
import string

from core.utils import generate_user_id_int

def insert_user(db: Session, tipo_doc: int, num_doc:str, nombres: str, apellidos: str, correo: str, clave: str, telefono: str = None ):
    
    nuevo_usuario = Usuario(
        id_usuario = generate_user_id_int(),
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

        total_pages = (total_attendees + page_size - 1) // page_size
        return attendees, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar los asistentes: {e}")
        raise HTTPException(status_code=500, detail="Error. No hay integridad de datos")
    

def update_external_attendees(db: Session, usuario_id: int, newData: UpdatedAttendee):
    try:
        user = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
        attendee = db.query(Asistente).filter(Asistente.id_usuario == usuario_id).first()

        if user is None or attendee is None:
            raise HTTPException(status_code=404, detail="Item no encontrado")
        
        if(newData.nombres): 
            user.nombres = newData.nombres

        if(newData.apellidos):
            user.apellidos = newData.apellidos

        if(newData.correo):
            user.correo = newData.correo

        if(newData.url_comprobante_pago ): 
            attendee.url_comprobante_pago = newData.url_comprobante_pago


        db.commit() 
        db.refresh(user)
        db.refresh(attendee)
        return user, attendee

        
    except SQLAlchemyError as e:
        print(f"Error al actualizar asistente: {e}")
        raise HTTPException(status_code=500, detail=f"Error. No hay Integridad de datos",)
    
def get_attendee_by_document(db: Session, documento:str, page, page_size):
    try:
        offset = (page - 1) * page_size

        attendees = db.query(Asistente.url_comprobante_pago, Usuario.id_usuario, Usuario.documento, Usuario.nombres, Usuario.apellidos, Usuario.celular, Usuario.correo).join(Usuario).filter(Usuario.documento.like(f'{documento}%')).limit(page_size).offset(offset).all()

        
        if attendees is None:
            raise HTTPException(status_code=404, detail="No hay asistentes con ese documeto")
        
        total_coincidences = db.query(Usuario).join(Asistente).filter(Usuario.documento.like(f'{documento}%')).count()

        total_pages = (total_coincidences + page_size - 1) // page_size
        return attendees, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar el asistente por documento: {e}")
        raise HTTPException(status_code=500, detail="Error. No hay integridad de datos")

#Función para llamar procedimiento almacenado
def insertar_historial_admin(db: Session, servicio:str, modulo: int,registro:int, id_admin: int):
    try:
        nuevo_registro = Historial_admin(
            accion= servicio,
            id_modulo= modulo,
            id_registro=registro,
            id_usuario=id_admin,
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        db.add(nuevo_registro)
        db.commit()
    except SQLAlchemyError as e:
        print(f"Error al ejecutar el procedimiento insertar_acciones_admin: {e}")
        raise HTTPException(status_code=500, detail="Error al ejecutar el procedimiento.")