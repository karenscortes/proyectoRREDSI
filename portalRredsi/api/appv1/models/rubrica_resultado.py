from sqlalchemy import Column, Enum, Float, Integer
from .base_class import Base
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship

class Estados(PyEnum):
    pendiente = "pendiente"
    calificado = "calificado"

class Rubrica_resultado(Base):
    __tablename__ = 'rubricas_resultados'
    id_rubrica_resultado = Column(Integer, primary_key=True, autoincrement=True)
    estado = Column(Enum(Estados), default=Estados.pendiente, nullable=False)
    puntaje_aprobacion =  Column(Float(2,1))

    resp_rubricas = relationship("Respuesta_rubricas", back_populates="rubrica_resultado")