from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from models.base_class import Base

class Item_rubrica(Base):
    __tablename__ = 'items_rubrica'
    id_item_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    id_rubrica = Column(Integer, ForeignKey('rubricas.id_rubrica'))
    componente = Column(Text)
    valor_max = Column(Float(2,1))

    rubrica = relationship("Rubrica")

