from sqlalchemy import Integer,Column,ForeignKey, Enum # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from .base_class import Base
from enum import Enum as PyEnum
class Tipo_de_participante(PyEnum):
    ponente = "ponente"
    tutor = "tutor"
    evaluador = "evaluador"
    suplenteEvaluador = "suplenteEvaluador"
    suplentePonente = "suplentePonente"

class Participante_proyecto(Base):
    __tablename__ = 'participantes_proyecto'
    id_participante_proyecto = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_etapa = Column(Integer, ForeignKey("etapas.id_etapa"))
    id_proyecto = Column(Integer, ForeignKey('proyectos.id_proyecto') )
    id_proyecto_convocatoria = Column(Integer, ForeignKey('proyectos_convocatoria.id_proyecto_convocatoria'))
    tipo_usuario = Column(Enum(Tipo_de_participante))    
    
    usuario = relationship('Usuario', back_populates="participantes_proyectos")
    proyecto = relationship('Proyecto', back_populates="participantes_proyectos")
    etapa = relationship('Etapa', back_populates="participantes_proyectos")
    proyecto_convocatoria = relationship('Proyecto_convocatoria', back_populates="participantes_proyectos")