import enum
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .base_class import Base

class Detalle_institucional(Base):
    __tablename__ = 'detalles_institucionales'
    id_detalle_institucional = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_institucion = Column(Integer, ForeignKey('instituciones.id_institucion'))
    semillero = Column(String(35))
    grupo_investigacion = Column(String(35))
    id_primera_area_conocimiento = Column(Integer, ForeignKey('areas_conocimiento.id_area_conocimiento'))
    id_segunda_area_conocimiento = Column(Integer, ForeignKey('areas_conocimiento.id_area_conocimiento'))
   
    usuario = relationship("Usuario", back_populates="detalles_institucionales")
    institucion = relationship("Institucion", back_populates="detalles_institucionales")
    primer_area = relationship("Area_conocimiento", foreign_keys=[id_primera_area_conocimiento], back_populates="detalles_institucionales_area1")
    segunda_area = relationship("Area_conocimiento", foreign_keys=[id_segunda_area_conocimiento], back_populates="detalles_institucionales_area2")