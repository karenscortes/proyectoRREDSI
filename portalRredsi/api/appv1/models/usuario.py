from enum import Enum as PyEnum #Enum de python
from sqlalchemy import Column, String, ForeignKey, Integer, Enum 
from sqlalchemy.orm import relationship
from .base_class import Base

class Estados(PyEnum):
    activo = "Activo"
    inactivo = "Inactivo"
    pendiente = "Pendiente"

class Usuario(Base):
    _tablename_ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    id_rol = Column(Integer, ForeignKey('roles.id_rol'))
    id_tipo_documento = Column(Integer, ForeignKey('tipos_documento.id_tipo_documento'))
    documento = Column(String(55), nullable=False, unique=True)
    nombres = Column(String(25))
    apellidos = Column(String(25))
    celular = Column(String(12), nullable=False, unique=True)
    correo = Column(String(70), unique=True)
    clave = Column(String(255))
    estado = Column(Enum(Estados), default=Estados.activo)
   
    tipo_documento = relationship("Tipo_documento", back_populates="usuarios")
    rol = relationship("Rol", back_populates="usuarios")
    postulaciones_evaluadores = relationship("Postulacion_evaluador", back_populates="evaluador")
    salas = relationship("Sala", back_populates="usuario")
    titulos_academicos = relationship("Titulo_academico", back_populates="usuario")
    detalles_institucionales = relationship("Detalle_institucional", back_populates="usuario")
    asistentes = relationship('Asistente', back_populates='usuario')
    participantes_proyectos = relationship('Participante_proyecto', back_populates="usuario")
    resp_rubricas = relationship("Respuesta_rubricas", back_populates="usuario")
    historial_actividades_admin = relationship("Historial_admin", back_populates="usuario")
