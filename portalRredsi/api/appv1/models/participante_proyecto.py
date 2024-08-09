from sqlalchemy import Integer,Column,ForeignKey, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from models.base_class import Base
import enum

class Tipo_de_participante(enum.Enum):
    ponente = "ponente"
    tutor = "tutor"
    suplente = "suplente"
    evaluador = "evaluador"

class Participante_proyecto(Base):
    __tablename__ = 'participante_proyecto'
    id_participante_proyecto = Column(Integer, primary_key=True, autoincrement=True)
    id_datos_personales = Column(Integer, ForeignKey("detalle_personal.id_detalles_personales"))
    id_proyecto = Column(Integer, ForeignKey('proyecto.id_proyecto') )
    id_etapa = Column(Integer, ForeignKey("etapa.id_etapa"))
    id_proyecto_convocatoria = Column(Integer, ForeignKey('proyecto_convocatoria.id_proyecto_convocatoria') )
    tipo_participante = Column(enum.Enum(Tipo_de_participante))
    
    
    detalle_personal = relationship('Detalle_personal')
    proyecto = relationship('Proyecto')
    etapa = relationship('Etapa')
    proyecto_convocatoria = relationship('Proyecto_convocatoria')