from datetime import date
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class EstadoDeConvocatoria(str, Enum):
    en_curso = "en curso"
    concluida = "concluida"
    por_publicar = "por publicar"

class ConvocatoriaCreate(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_fin: date
    estado: EstadoDeConvocatoria  

class EtapaCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    id_convocatoria: int

class FaseCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    id_etapa: int

class EtapaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class FaseUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class ProgramacionFaseCreate(BaseModel):
    id_fase: int
    id_convocatoria: int
    fecha_inicio: date
    fecha_fin: date
