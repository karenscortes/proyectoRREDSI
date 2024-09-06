from .base_class import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer, String # type: ignore

class Area_conocimiento(Base):
    __tablename__ = 'areas_conocimiento'
    id_area_conocimiento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(35))
    
    salas = relationship("Sala", back_populates="area_conocimiento")