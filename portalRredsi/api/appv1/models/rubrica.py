from sqlalchemy import Column, String, ForeignKey, Integer, and_
from sqlalchemy.orm import relationship

from appv1.models.item_rubrica import Item_rubrica
from .base_class import Base

class Rubrica(Base):
    __tablename__ = 'rubricas'
    id_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(40))
    id_etapa = Column(Integer, ForeignKey('etapas.id_etapa'))
    id_modalidad = Column(Integer, ForeignKey('modalidades.id_modalidad'))

    etapa = relationship('Etapa', back_populates='rubricas')
    modalidad = relationship("Modalidad", back_populates='rubricas')
    items_rubrica = relationship("Item_rubrica", primaryjoin=and_(Item_rubrica.id_rubrica==id_rubrica,Item_rubrica.estado=="activo"), back_populates='rubrica')
    
