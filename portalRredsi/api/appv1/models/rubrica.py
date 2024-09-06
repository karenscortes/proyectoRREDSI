from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .base_class import Base

class Rubrica(Base):
    __tablename__ = 'rubricas'
    id_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(40))
    id_etapa = Column(Integer, ForeignKey('etapas.id_etapa'))
    id_modalidad = Column(Integer, ForeignKey('modalidades.id_modalidad'))

    etapa = relationship('Etapa', back_populates='rubricas')
    modalidad = relationship("Modalidad", back_populates='rubricas')
    itemsRubrica = relationship("Item_rubrica", back_populates='rubrica')
