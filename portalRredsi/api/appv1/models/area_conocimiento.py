
from models.base_class import Base
from sqlalchemy import Column,Integer, String # type: ignore

class Area_conocimiento(Base):
    __tablename__ = 'area_conocimiento'
    id_area_conocimiento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(35))
    