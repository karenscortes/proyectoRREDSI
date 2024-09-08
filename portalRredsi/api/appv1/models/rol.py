from sqlalchemy import Column, String, Integer
from .base_class import Base
from sqlalchemy.orm import relationship

class Rol(Base):
    __tablename__ = 'roles'
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(35))

    usuarios = relationship('Usuario', back_populates="rol")
    permisos = relationship("Permiso", back_populates="rol") 