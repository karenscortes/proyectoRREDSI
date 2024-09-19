from typing import  Optional
from pydantic import BaseModel
from sqlalchemy import Enum


class ProyectoEstado(str, Enum):
    pendiente = 'pendiente'
    asignado = 'asignado'

class ProyectoBase(BaseModel):
    id_proyecto: int
    titulo: str
    estado: ProyectoEstado

class ProyectoResponse(ProyectoBase):
    nombre_institucion: str 
