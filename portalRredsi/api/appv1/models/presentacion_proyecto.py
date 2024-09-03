from sqlalchemy import Integer, String, Column,ForeignKey, Text
from sqlalchemy.orm import relationship
from models.base_class import Base


class Presentacion_proyecto(Base):
    __tablename__ = "presentaciones_proyectos"
    id_presentacion = Column(Integer, primary_key=True, autoincrement=True)
    id_proyecto = Column(Integer, ForeignKey('proyectos.id_proyecto'))
    url_presentacion = Column(Text) 
    
    proyecto = relationship("Proyecto")
