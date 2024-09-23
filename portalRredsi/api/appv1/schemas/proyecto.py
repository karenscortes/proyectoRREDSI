import enum
from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

class EstadoProyectoEnum(str, enum.Enum):
    pendiente_virtual = "pendiente_virtual"
    asignado_virtual = "asignado_virtual"
    asignado = "asignado"
    pendiente = "pendiente"


class ProyectoBase(BaseModel):
    id_institucion: int
    id_modalidad:int
    id_area_conocimiento:int
    titulo: Annotated[str, constr(max_length=100)]
    programa_academico: Annotated[str, constr(max_length=50)]
    grupo_investigacion:Annotated[str, constr(max_length=50)]
    linea_investigacion:Annotated[str, constr(max_length=50)]
    nombre_semillero:Annotated[str, constr(max_length=50)]
  


class ProyectoCreate(ProyectoBase):
    pass

class ProyectoResponse(ProyectoBase):
    id_proyecto: int
    

class PaginatedProyectosResponse(BaseModel):
    proyectos: List[ProyectoResponse]
    total_pages: int
    current_page: int
    page_size: int
