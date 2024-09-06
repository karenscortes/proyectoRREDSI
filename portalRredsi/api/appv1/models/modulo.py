from sqlalchemy import Column, String, Integer
from .base_class import Base

class Modulo(Base):
    __tablename__ = 'modulos'
    id_modulo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))