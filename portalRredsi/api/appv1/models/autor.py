from models.base_class import Base
from sqlalchemy import Column, Integer, ForeignKey, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore

class Autor(Base):
    __tablename__ = 'autores'
    id_autor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    id_proyecto = Column(Integer, ForeignKey('proyectos.id_proyecto') )
    
    proyecto = relationship("Proyecto")