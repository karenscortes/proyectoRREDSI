import enum
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.base_class import Base

class Estados(enum.Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    pendiente = "Pendiente"

class Usuario(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    id_rol = Column(Integer, ForeignKey('roles.id_rol'))
    correo = Column(String(70), unique=True)
    clave = Column(String(255))
    estado = Column(enum.Enum(Estados))
   

    rol = relationship("Rol")