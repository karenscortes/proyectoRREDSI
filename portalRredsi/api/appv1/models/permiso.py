from sqlalchemy import Column, Integer, Boolean, ForeignKey,PrimaryKeyConstraint
from .base_class import Base
from sqlalchemy.orm import relationship

class Permiso(Base):
    __tablename__ = 'permisos'
    id_modulo = Column(Integer, ForeignKey('modulos.id_modulo'))
    id_rol = Column(Integer, ForeignKey('roles.id_rol'))
    p_insertar = Column(Boolean, default=0)
    p_consultar = Column(Boolean, default=0)
    p_actualizar = Column(Boolean, default=0)
    p_eliminar = Column(Boolean, default=0)

    __table_args__ = (
        PrimaryKeyConstraint('id_modulo', 'id_rol'),
    )

    rol = relationship("Rol", back_populates="permisos") 
    modulo = relationship("Modulo", back_populates="permisos")