import enum
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.base_class import Base

class Niveles_academicos(enum.Enum):
    pregrado = "Pregrado"
    especializacion = "Especializacion"
    maestria = "Maestria"
    doctorado = "Doctorado"

class Titulo_academico(Base):
    __tablename__ = 'titulos_academicos'
    id_titulos_academicos = Column(Integer, primary_key=True, autoincrement=True)
    nivel = Column(enum.Enum(Niveles_academicos))
    nombre_titulo = Column(String(80))
    url_titulo = Column(String(255))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
   

    usuario = relationship("Usuario")