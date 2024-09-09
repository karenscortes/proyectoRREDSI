from enum import Enum as PyEnum #Enum de python
from sqlalchemy import Column, String, ForeignKey, Integer, Enum 
from sqlalchemy.orm import relationship
from .base_class import Base

class Estados(PyEnum):
    activo = "Activo"
    inactivo = "Inactivo"
    pendiente = "Pendiente"

class Usuario(Base):
    _tablename_ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    id_rol = Column(Integer, ForeignKey('roles.id_rol'))
    id_tipo_documento = Column(Integer, ForeignKey('tipos_documento.id_tipo_documento'))
    documento = Column(String(55))
    nombres = Column(String(25))
    apellidos = Column(String(25))
    celular = Column(String(10))
    correo = Column(String(70), unique=True)
    clave = Column(String(255))
    estado = Column(Enum(Estados), default=Estados.activo)
   
    tipo_documento = relationship("Tipo_documento")
    rol = relationship("Rol")