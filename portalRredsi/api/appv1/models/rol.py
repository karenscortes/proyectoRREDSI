from sqlalchemy import Column, String, Integer
from models.base_class import Base

class Rol(Base):
    __tablename__ = 'roles'
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(35))