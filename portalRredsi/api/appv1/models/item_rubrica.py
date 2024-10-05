from sqlalchemy import Column, Float, ForeignKey, Integer, Text,String,Enum
from sqlalchemy.orm import relationship
from .base_class import Base
import enum

class Estado(enum.Enum):
    activo = "activo"
    inactivo = "inactivo"

class Item_rubrica(Base):
    __tablename__ = 'items_rubrica'
    id_item_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    id_rubrica = Column(Integer, ForeignKey('rubricas.id_rubrica'))
    titulo = Column(String(50))
    componente= Column(Text)
    valor_max = Column(Float(2,1))
    estado = Column(Enum(Estado))

    rubrica = relationship("Rubrica", back_populates='items_rubrica')
    resp_rubricas = relationship("Respuesta_rubricas", back_populates="item_rubrica")
    
