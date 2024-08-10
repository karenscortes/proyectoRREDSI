from models.base_class import Base
from sqlalchemy import Column, Integer, ForeignKey, String 

class Etapa(Base):
    __tablename__ = 'etapas'
    id_etapa = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20))
   