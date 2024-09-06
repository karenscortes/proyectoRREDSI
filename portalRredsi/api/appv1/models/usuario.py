from enum import Enum as PyEnum #Enum de python
from sqlalchemy import Column, String, ForeignKey, Integer, Enum 
from sqlalchemy.orm import relationship
from .base_class import Base

class Estados(PyEnum):
    activo = "Activo"
    inactivo = "Inactivo"
    pendiente = "Pendiente"

class Usuario(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    id_rol = Column(Integer, ForeignKey('roles.id_rol'))
    correo = Column(String(70), unique=True)
    clave = Column(String(255))
    estado = Column(Enum(Estados), default=Estados.activo)
   
    rol = relationship("Rol", back_populates="usuarios")
    detalle_personal = relationship("Detalle_personal",back_populates="usuario")
    postulaciones_evaluadores = relationship("Postulacion_evaluador", back_populates="evaluador")
    salas = relationship("Sala", back_populates="usuario")
