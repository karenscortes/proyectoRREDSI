import enum
from models.base_class import Base
from sqlalchemy import DATE, Column, Integer, ForeignKey, String # type: ignore

class Tipo_de_convocatoria(enum.Enum):
    en_curso = "en curso"
    concluida= "concluida"
    por_publicar = "por publicar"

class Convocatoria(Base):
    __tablename__ = 'convocatorias'
    id_convocatoria = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(25))
    fecha_inicio = Column(DATE)
    fecha_fin= Column(DATE)
    tipo_de_convocatoria = Column(enum.Enum(Tipo_de_convocatoria))