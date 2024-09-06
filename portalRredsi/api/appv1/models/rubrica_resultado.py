from sqlalchemy import Column, Float, Integer
from .base_class import Base

class Rubrica_resultado(Base):
    __tablename__ = 'rubricas_resultados'
    id_rubrica_resultado = Column(Integer, primary_key=True, autoincrement=True)
    puntaje_aprobacion =  Column(Float(2,1))

