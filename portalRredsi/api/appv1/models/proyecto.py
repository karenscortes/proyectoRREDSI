from sqlalchemy import Integer,Column,ForeignKey, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from models.base_class import Base

class Proyecto(Base):
    __tablename__ = 'proyecto'
    id_proyecto = Column(Integer, primary_key=True)
    id_institucion = Column(Integer, ForeignKey("institucion.id_institucion"))
    id_modalidad = Column(Integer, ForeignKey("modalidad.id_modalidad"))
    id_area_conocimiento = Column(Integer, ForeignKey("area_conocimiento.id_area_conocimiento"))
    titulo = Column(String(200))
    programa_academico = Column(String(50))
    grupo_investigacion = Column(String(50))
    linea_investigacion = Column(String(50))
    nombre_semillero = Column(String(50))
    url_propuesta_escrita = Column(String(255))
    url_poster = Column(String(255))
    url_aval = Column(String(255))
    
    institucion = relationship("Institucion")
    modalidad = relationship("Modalidad")
    area_conocimiento = relationship("Area_conocimiento")
    
    