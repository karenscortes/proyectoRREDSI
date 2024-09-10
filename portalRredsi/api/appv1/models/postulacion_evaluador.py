from .base_class import Base
from sqlalchemy import Boolean, Column, Enum, Integer, ForeignKey, PrimaryKeyConstraint
from enum import Enum as PyEnum #Enum de python
from sqlalchemy.orm import relationship # type: ignore

class Estados(PyEnum):
    aceptada = "aceptada"
    rechazada = "rechazada"
    pendiente = "pendiente"


class Postulacion_evaluador(Base):
    __tablename__ = 'postulaciones_evaluadores'
    id_convocatoria = Column(Integer,ForeignKey('convocatorias.id_convocatoria'))
    id_evaluador = Column(Integer, ForeignKey('usuarios.id_usuario'))
    estado = Column(Enum(Estados), default=Estados.pendiente)
    etapa_virtual = Column(Boolean, default=True)
    etapa_presencial = Column(Boolean, default=True)
    jornada_manana = Column(Boolean, default=True)
    jornada_tarde = Column(Boolean, default=True)

    __table_args__ = (
        PrimaryKeyConstraint('id_convocatoria', 'id_evaluador'),
    )

    convocatoria = relationship("Convocatoria", back_populates="postulaciones_evaluadores")
    evaluador = relationship("Usuario", back_populates="postulaciones_evaluadores")


