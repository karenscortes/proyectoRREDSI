import enum
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.base_class import Base

class Detalle_personal(Base):
    __tablename__ = 'detalles_personales'
    id_detalle_personal = Column(Integer, primary_key=True, autoincrement=True)
    id_tipo_documento = Column(Integer, ForeignKey('tipos_documento.id_tipo_documento'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    documento = Column(String(55))
    nombres = Column(String(25))
    apellidos = Column(String(25))
    celular = Column(String(10))
    id_institucion = Column(Integer, ForeignKey('instituciones.id_institucion'))
   
    tipo_documento = relationship("Tipo_documento")
    usuario = relationship("Usuario")
    institucion = relationship("Institucion")