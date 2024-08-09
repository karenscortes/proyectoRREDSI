from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.base_class import Base

class Rubrica(Base):
    __tablename__ = 'rubrica'
    id_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(40))
    id_etapa = Column(Integer, ForeignKey('etapa.id_etapa'))
    id_modalidad = Column(Integer, ForeignKey('modalidad.id_modalidad'))

    etapa = relationship("Etapa")
    modalidad = relationship("Modalidad")
