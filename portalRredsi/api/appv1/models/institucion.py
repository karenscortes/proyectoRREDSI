from .base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Institucion(Base):
    __tablename__ = 'instituciones'
    id_institucion = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    
    detalles_personales = relationship("Detalle_personal",back_populates="institucion")
    proyectos = relationship("Proyecto", back_populates="institucion")