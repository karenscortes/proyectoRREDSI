from .base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Tipo_documento(Base):
    __tablename__ = 'tipos_documento'
    id_tipo_documento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(25))
    
    usuarios = relationship("Usuario",back_populates="tipo_documento")