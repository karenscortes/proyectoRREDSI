from sqlalchemy import DECIMAL, Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from .base_class import Base

class Item_rubrica(Base):
    __tablename__ = 'items_rubrica'
    id_item_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    id_rubrica = Column(Integer, ForeignKey('rubricas.id_rubrica'))
    titulo = Column(Text)
    descripcion = Column(Text)
    valor_max = Column(DECIMAL(3,1))

    rubrica = relationship("Rubrica", back_populates='itemsRubrica')

