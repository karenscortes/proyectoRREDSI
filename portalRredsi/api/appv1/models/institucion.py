from models.base_class import Base
from sqlalchemy import Column, Integer, String

class Institucion(Base):
    __tablename__ = 'instituciones'
    id_institucion = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    