from sqlalchemy import Column, Float, ForeignKey, Integer, Text,String
from sqlalchemy.orm import relationship
from .base_class import Base

class Item_rubrica(Base):
    __tablename__ = 'items_rubrica'
    id_item_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    id_rubrica = Column(Integer, ForeignKey('rubricas.id_rubrica'))
    titulo = Column(String(50))
    descripcion = Column(Text)
    valor_max = Column(Float(2,1))

    rubrica = relationship("Rubrica", back_populates='items_rubrica')
    respuestas_rubricas = relationship("Respuesta_rubricas", back_populates="item_rubrica")
    
