from .base_class import Base
from sqlalchemy import Column,Integer, String # type: ignore
from sqlalchemy.orm import relationship

class Modalidad(Base):
    __tablename__ = 'modalidades'
    id_modalidad = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20))

    rubricas = relationship('Rubrica', back_populates='modalidad')
    proyectos= relationship('Proyecto', back_populates='modalidad')