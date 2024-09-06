from sqlalchemy import Integer,Column,ForeignKey, Enum # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from .base_class import Base
from enum import Enum as PyEnum
class Tipo_de_participante(PyEnum):
    ponente = "ponente"
    tutor = "tutor"
    suplente = "suplente"
    evaluador = "evaluador"

class Participante_proyecto(Base):
    __tablename__ = 'participantes_proyecto'
    id_participante_proyecto = Column(Integer, primary_key=True, autoincrement=True)
    id_datos_personales = Column(Integer, ForeignKey("detalles_personales.id_detalle_personal"))
    id_proyecto = Column(Integer, ForeignKey('proyectos.id_proyecto') )
    id_etapa = Column(Integer, ForeignKey("etapas.id_etapa"))
    id_proyecto_convocatoria = Column(Integer, ForeignKey('proyectos_convocatoria.id_proyecto_convocatoria') )
    tipo_participante = Column(Enum(Tipo_de_participante))
    
    
    detalle_personal = relationship('Detalle_personal')
    proyecto = relationship('Proyecto')
    etapa = relationship('Etapa')
    proyecto_convocatoria = relationship('Proyecto_convocatoria')