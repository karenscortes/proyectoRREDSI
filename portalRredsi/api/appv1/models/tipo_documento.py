from models.base_class import Base
from sqlalchemy import Column, Integer, String

class Tipo_documento(Base):
    __tablename__ = 'tipos_documento'
    id_tipo_documento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(10))
    