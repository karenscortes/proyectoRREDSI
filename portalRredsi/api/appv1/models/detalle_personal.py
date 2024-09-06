import enum
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .base_class import Base

class Detalle_personal(Base):
    __tablename__ = 'detalles_personales'
    id_detalle_personal = Column(Integer, primary_key=True, autoincrement=True)
    id_tipo_documento = Column(Integer, ForeignKey('tipos_documento.id_tipo_documento'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_institucion = Column(Integer, ForeignKey('instituciones.id_institucion'))
    documento = Column(String(55))
    nombres = Column(String(25))
    apellidos = Column(String(25))
    celular = Column(String(10))
   
    tipo_documento = relationship("Tipo_documento",back_populates="detalles_personales")
    usuario = relationship("Usuario",back_populates="detalle_personal")
    institucion = relationship("Institucion",back_populates="detalles_personales")
    asistentes = relationship("Asistente", back_populates="detalle_personal")