from sqlalchemy import Column, String, Integer
from .base_class import Base
from sqlalchemy.orm import relationship 

class Modulo(Base):
    __tablename__ = 'modulos'
    id_modulo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))

    permisos = relationship("Permiso", back_populates="modulo") 
    historial_actividades_admin = relationship("Historial_admin", back_populates="modulo")
    