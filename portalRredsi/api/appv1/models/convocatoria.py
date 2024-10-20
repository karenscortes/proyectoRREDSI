from enum import Enum as PyEnum
from .base_class import Base
from sqlalchemy import DATE, Column, Integer, Enum, String
from sqlalchemy.orm import relationship

# Estado de convocatoria
class EstadoDeConvocatoria(PyEnum):
    en_curso = "en curso"  
    concluida = "concluida"
    por_publicar = "por publicar"

class Convocatoria(Base):
    __tablename__ = 'convocatorias'
    id_convocatoria = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(25))
    fecha_inicio = Column(DATE)
    fecha_fin= Column(DATE)
    estado = Column(Enum(EstadoDeConvocatoria, native_enum=False))

    programacion_fases = relationship("Programacion_fase", back_populates="convocatoria")
    postulaciones_evaluadores = relationship("Postulacion_evaluador", back_populates="convocatoria")
    proyectos_convocatorias = relationship("Proyecto_convocatoria", back_populates="convocatoria")
    asistentes = relationship("Asistente", back_populates="convocatoria")

