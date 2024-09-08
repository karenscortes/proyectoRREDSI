from .base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Institucion(Base):
    __tablename__ = 'instituciones'
    id_institucion = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    
    proyectos = relationship("Proyecto", back_populates="institucion")
    detalles_institucionales = relationship("Detalle_institucional", back_populates="institucion")