from models.base_class import Base
from sqlalchemy import Column,Integer, String # type: ignore

class Modalidad(Base):
    __tablename__ = 'modalidad'
    id_modalidad = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20))