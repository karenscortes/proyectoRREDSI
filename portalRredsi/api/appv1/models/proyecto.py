from sqlalchemy import Enum, Integer,Column,ForeignKey, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from enum import Enum as PyEnum #Enum de python
from .base_class import Base
class Estados(PyEnum):
    asignado = "asignado"
    pendiente = "pendiente"

class Proyecto(Base):
    __tablename__ = 'proyectos'
    id_proyecto = Column(Integer, primary_key=True)
    id_institucion = Column(Integer, ForeignKey("instituciones.id_institucion"))
    id_modalidad = Column(Integer, ForeignKey("modalidades.id_modalidad"))
    id_area_conocimiento = Column(Integer, ForeignKey("areas_conocimiento.id_area_conocimiento"))
    titulo = Column(String(200))
    estado = Column(Enum(Estados), default=Estados.pendiente, nullable=False)
    programa_academico = Column(String(50))
    grupo_investigacion = Column(String(50))
    linea_investigacion = Column(String(50))
    nombre_semillero = Column(String(50))
    url_propuesta_escrita = Column(String(255))
    url_aval = Column(String(255))
    
    institucion = relationship("Institucion", back_populates="proyectos")
    modalidad = relationship("Modalidad", back_populates="proyectos")
    area_conocimiento = relationship("Area_conocimiento", back_populates="proyectos")
    proyectos_convocatorias = relationship("Proyecto_convocatoria", back_populates="proyecto")
    presentaciones_proyectos = relationship("Presentacion_proyecto", back_populates="proyecto")
    autores = relationship("Autor", back_populates="proyecto")
    participantes_proyectos = relationship("Participante_proyecto", back_populates="proyecto")