from sqlalchemy import Integer, Column,ForeignKey,Date, Time
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from models.base_class import Base


class Sala_asignada(Base):
    __tablename__ = "sala_asignada"
    id_sala = Column(Integer, ForeignKey('sala.id_sala'))
    id_proyecto_convocatoria = Column(Integer, ForeignKey('proyecto_convocatoria.id_proyecto_convocatoria'))
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    
    _table_args_ = (
        PrimaryKeyConstraint('id_sala', 'id_proyecto_convocatoria'),
    )
    
    sala = relationship("Sala")
    proyecto_convocatoria = relationship("Proyecto_convocatoria")
    