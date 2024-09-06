from sqlalchemy import Integer, String, Column,ForeignKey
from sqlalchemy.orm import relationship
from .base_class import Base


class Sala(Base):
    __tablename__ = "salas"
    id_sala = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_area_conocimiento = Column(Integer, ForeignKey('areas_conocimiento.id_area_conocimiento'))
    numero_sala = Column(String(25))
    nombre_sala = Column(String(25))
    
    usuario = relationship("Usuario", back_populates="salas")
    area_conocimiento = relationship("Area_conocimiento", back_populates="salas")
    detalles_salas = relationship("Detalle_sala", back_populates="sala")