from .base_class import Base
from sqlalchemy import Column, Integer, ForeignKey, String 
from sqlalchemy.orm import relationship

class Etapa(Base):
    __tablename__ = 'etapas'
    id_etapa = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20))
   
    rubricas = relationship('Rubrica', back_populates='etapa')
    fases = relationship('Fase', back_populates="etapa")