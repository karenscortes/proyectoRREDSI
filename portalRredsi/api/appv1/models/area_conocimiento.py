from .base_class import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer, String # type: ignore

class Area_conocimiento(Base):
    __tablename__ = 'areas_conocimiento'
    id_area_conocimiento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(35))
    
    salas = relationship("Sala", back_populates="area_conocimiento")
    proyectos = relationship("Proyecto", back_populates="area_conocimiento")
    detalles_institucionales_area1 = relationship("Detalle_institucional", 
    foreign_keys="Detalle_institucional.id_primera_area_conocimiento", back_populates="primer_area")
    detalles_institucionales_area2 = relationship("Detalle_institucional", 
    foreign_keys="Detalle_institucional.id_segunda_area_conocimiento", back_populates="segunda_area")