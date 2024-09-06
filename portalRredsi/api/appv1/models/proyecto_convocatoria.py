from sqlalchemy import Integer,Column,ForeignKey, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from .base_class import Base
from sqlalchemy.orm import relationship

class Proyecto_convocatoria(Base):
    __tablename__ = 'proyectos_convocatoria'
    id_proyecto_convocatoria = Column(Integer, primary_key=True, autoincrement=True)
    id_proyecto = Column(Integer, ForeignKey('proyectos.id_proyecto') )
    id_convocatoria = Column(Integer, ForeignKey('convocatorias.id_convocatoria') )
    
    proyecto = relationship('Proyecto', back_populates="proyectos_convocatorias")
    convocatoria = relationship('Convocatoria')
    detalles_salas = relationship("Detalle_sala", back_populates="proyecto_convocatoria")