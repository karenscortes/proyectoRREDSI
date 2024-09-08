import enum
from .base_class import Base
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
    id_usuario = Column(Integer,ForeignKey('usuarios.id_usuario'))
    asistencia = Column(SmallInteger(), default=0)
    fecha = Column(TIMESTAMP)
    url_comprobante_pago = Column(String(255))
    
    usuario= relationship("Usuario", back_populates="asistentes")
