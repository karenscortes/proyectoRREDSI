from sqlalchemy import Column, Integer, Enum, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .base_class import Base
import enum

class Accion(enum.Enum):
    Insertar = "Insertar"
    Actualizar = "Actualizar"
    Eliminar = "Eliminar"

class Historial_admin(Base):
    __tablename__ = "historial_actividades_admin"

    id_actividad = Column(Integer, primary_key=True, autoincrement=True)
    accion = Column(Enum(Accion)) 
    id_modulo = Column(Integer, ForeignKey("modulos.id_modulo"))
    id_registro = Column(Integer)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    fecha = Column(TIMESTAMP, default=func.current_timestamp()) 

    modulo = relationship("Modulo")
    usuario = relationship("Usuario")