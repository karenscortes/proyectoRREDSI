from datetime import date
from pydantic import BaseModel
from typing import Optional
from enum import Enum

# Estado de convocatoria
class EstadoDeConvocatoria(str, Enum):
    en_curso = "en curso"
    concluida = "concluida"
    por_publicar = "por publicar"

# Schema para la creación de convocatorias
class ConvocatoriaCreate(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_fin: date
    estado: EstadoDeConvocatoria

# Schema para la respuesta al crear convocatorias (incluye ID)
class ConvocatoriaResponse(BaseModel):
    id_convocatoria: int
    nombre: str
    fecha_inicio: date
    fecha_fin: date
    estado: EstadoDeConvocatoria

    class Config:
        orm_mode = True

# Schema para la programación de fases
class ProgramacionFaseCreate(BaseModel):
    id_fase: int
    id_convocatoria: int
    fecha_inicio: date
    fecha_fin: date

    class Config:
        orm_mode = True

# Schema para la respuesta de la programación de fase
class ProgramacionFaseResponse(BaseModel):
    id_programacion_fase: int
    id_fase: int
    id_convocatoria: int
    fecha_inicio: date
    fecha_fin: date

    class Config:
        orm_mode = True

# Schema para crear una sala
class CreateSala(BaseModel):
    id_usuario: int
    area_conocimento: int
    numero_sala: str
    nombre_sala: str

# Schema para actualizar una sala
class UpdateSala(BaseModel):
    id_usuario: Optional[int] = None
    area_conocimento: Optional[int] = None
    numero_sala: Optional[str] = None
    nombre_sala: Optional[str] = None
