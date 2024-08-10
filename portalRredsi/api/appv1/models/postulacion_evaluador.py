from models.base_class import Base
from sqlalchemy import DATE, Boolean, Column, Integer, ForeignKey, PrimaryKeyConstraint, String 
from sqlalchemy.orm import relationship # type: ignore


class Postulacion_evaluador(Base):
    __tablename__ = 'postulaciones_evaluadores'
    id_convocatoria = Column(Integer, primary_key=True)
    id_evaluador = Column(Integer, primary_key=True)
    etapa_virtual = Column(Boolean, default=True)
    etapa_presencial = Column(Boolean, default=True)
    jornada_manana = Column(Boolean, default=True)
    jornada_tarde = Column(Boolean, default=True)

    __table_args__ = (
        PrimaryKeyConstraint('id_convocatoria', 'id_evaluador'),
    )

    convocatoria = relationship("Convocatoria")
    usuario = relationship("Usuario")

