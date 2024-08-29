import enum
from models.base_class import Base
from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey, SmallInteger, String, Enum
from sqlalchemy.orm import relationship 

class opciones_asistente(enum.Enum):  
    evaluador = "evaluador"
    delegado = "delegado"
    ponente = "ponente"
    externos = "externos"

class Asistente(Base):
    __tablename__ = 'asistentes'
    id_asistente = Column(Integer, primary_key=True, autoincrement=True)
    id_detalles_personales = Column(Integer, ForeignKey('Detalle_personal.id_detalles_personales'))
    asistencia = Column(SmallInteger(1), default=0)
    tipo_asistente = Column(Enum(opciones_asistente))
    fecha = Column(TIMESTAMP)
    url_comprobante_pago = Column(String(255))
    
    detalle_personal = relationship("Detalle_personal")
