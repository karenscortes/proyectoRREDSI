from sqlalchemy import Integer,Column,ForeignKey, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from models.base_class import Base


class Proyecto_convocatoria(Base):
    __tablename__ = 'proyecto_convocatoria'
    id_proyecto_convocatoria = Column(Integer, primary_key=True, autoincrement=True)
    id_proyecto = Column(Integer, ForeignKey('proyecto.id_proyecto') )
    id_convocatoria = Column(Integer, ForeignKey('convocatoria.convocatoria') )
    
    proyecto = relationship('Proyecto')
    convocatoria = relationship('Convocatoria')