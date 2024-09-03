from sqlalchemy import Integer, String, Column,ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base


class Sala(Base):
    __tablename__ = "salas"
    id_sala = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    area_conocimiento = Column(Integer, ForeignKey('areas_conocimiento.id_area_conocimiento'))
    numero_sala = Column(String(25))
    nombre_sala = Column(String(25))
    
    usuario = relationship("Usuario")
    area_conocimiento = relationship("Area_conocimiento")