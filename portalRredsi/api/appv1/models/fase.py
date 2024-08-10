from models.base_class import Base
from sqlalchemy import Column, Integer, ForeignKey, String 
from sqlalchemy.orm import relationship # type: ignore

class Fase(Base):
    __tablename__ = 'fases'
    id_fase = Column(Integer, primary_key=True, autoincrement=True)
    id_etapa = Column(Integer, ForeignKey('etapas.id_etapa'))    
    nombre = Column(String(30))
    etapa = relationship("Etapa")

   