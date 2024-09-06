from sqlalchemy import Integer, Column,ForeignKey,Date, Time
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from .base_class import Base


class Detalle_sala(Base):
    __tablename__ = "salas_asignadas"
    id_sala = Column(Integer, ForeignKey('salas.id_sala'))
    id_proyecto_convocatoria = Column(Integer, ForeignKey('proyectos_convocatoria.id_proyecto_convocatoria'))
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    
    __table_args__ = (
        PrimaryKeyConstraint('id_sala', 'id_proyecto_convocatoria'),
    )
    
    sala = relationship("Sala", back_populates="detalles_salas")
    proyecto_convocatoria = relationship("Proyecto_convocatoria", back_populates="detalles_salas")
    