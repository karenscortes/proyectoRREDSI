import enum
from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

class EstadoProyectoEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"
    pendiente = "pendiente"

class PonenteBase(BaseModel):
    nombre: Annotated[str, constr(max_length=50)]
    apellido: Annotated[str, constr(max_length=50)]
    correo: EmailStr
    documento: Annotated[str, constr(max_length=20)]
    telefono: Annotated[str, constr(max_length=15)]

class TutorBase(BaseModel):
    nombre: Annotated[str, constr(max_length=50)]
    apellido: Annotated[str, constr(max_length=50)]
    correo: EmailStr
    documento: Annotated[str, constr(max_length=20)]
    telefono: Annotated[str, constr(max_length=15)]

class ProyectoBase(BaseModel):
    titulo: Annotated[str, constr(max_length=100)]
    descripcion: Annotated[str, constr(max_length=255)]
    fecha_inicio: datetime
    fecha_fin: Optional[datetime]
    estado: EstadoProyectoEnum

class ProyectoCreate(ProyectoBase):
    tutores: List[TutorBase]
    ponentes: List[PonenteBase]

class ProyectoResponse(ProyectoBase):
    id_proyecto: int
    tutores: List[TutorBase]
    ponentes: List[PonenteBase]

class PaginatedProyectosResponse(BaseModel):
    proyectos: List[ProyectoResponse]
    total_pages: int
    current_page: int
    page_size: int
