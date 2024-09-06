from .base_class import Base
from sqlalchemy import DATE, Column, Integer, ForeignKey, String 
from sqlalchemy.orm import relationship # type: ignore

class Programacion_fase(Base):
    __tablename__ = 'programacion_fases'
    id_programacion_fase = Column(Integer, primary_key=True, autoincrement=True)
    id_fase = Column(Integer, ForeignKey('fases.id_fase')) 
    id_convocatoria = Column(Integer, ForeignKey('convocatorias.id_convocatoria'))
    fecha_inicio = Column(DATE)
    fecha_fin= Column(DATE)

    fase = relationship("Fase", back_populates="programacion_fases")
    convocatoria = relationship("Convocatoria", back_populates="programacion_fases")

