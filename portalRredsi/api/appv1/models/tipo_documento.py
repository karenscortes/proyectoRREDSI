from models.base_class import Base
from sqlalchemy import Column, Integer, String

class tipo_documento(Base):
    __tablename__ = 'tipo_documento'
    id_tipo_documento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(10))
    