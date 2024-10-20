from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_class import Base

class Etapa(Base):
    __tablename__ = 'etapas'
    id_etapa = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)

    fases = relationship("Fase", back_populates="etapa")
    rubricas = relationship("Rubrica", back_populates="etapa")
    participantes_proyectos = relationship("Participante_proyecto", back_populates="etapa")