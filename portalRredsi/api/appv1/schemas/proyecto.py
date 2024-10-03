import enum
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr

class EstadoProyectoEnum(str, enum.Enum):
    pendiente_virtual = "pendiente_virtual"
    asignado_virtual = "asignado_virtual"
    asignado = "asignado"
    pendiente = "pendiente"

class UsuarioBase(BaseModel):
    id_tipo_documento: int
    documento: str
    nombres: str
    apellidos: str
    celular: str
    correo: EmailStr

class TutorCreate(UsuarioBase):
    pass

class PonenteCreate(UsuarioBase):
    pass

class AutorCreate(BaseModel):
    nombre: str

class ProyectoBase(BaseModel):
    id_institucion: int
    id_modalidad: int
    id_area_conocimiento: int
    titulo: str
    programa_academico: str
    grupo_investigacion: str
    linea_investigacion: str
    nombre_semillero: str

class ProyectoCreate(ProyectoBase):
    tutor: TutorCreate
    ponente1: PonenteCreate
    ponente2: Optional[PonenteCreate] = None
    autores: List[AutorCreate] = []
