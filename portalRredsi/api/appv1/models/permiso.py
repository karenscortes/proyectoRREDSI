from sqlalchemy import Column, Integer, Boolean, ForeignKey
from models.base_class import Base
from sqlalchemy.orm import relationship

class Permiso(Base):
    __tablename__ = 'permisos'
    id_modulo = Column(Integer, ForeignKey('modulos.id_modulo') , primary_key=True)
    id_rol = Column(Integer, ForeignKey('roles.id_rol') , primary_key=True)
    p_insertar = Column(Boolean, default=0)
    p_consultar = Column(Boolean, default=0)
    p_actualizar = Column(Boolean, default=0)
    p_eliminar = Column(Boolean, default=0)

    rol = relationship("Rol") 
    modulo = relationship("Modulo")