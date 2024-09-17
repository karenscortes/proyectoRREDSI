from typing import Annotated
from pydantic import BaseModel, StringConstraints
import enum

class NivelEnum(str, enum.Enum):
    pregrado = "pregrado"
    maestria = "maestria"
    especializacion = "especializacion"
    doctorado = "doctorado"


class TituloAcademicoBase(BaseModel):
    nivel: NivelEnum
    nombre_titulo: Annotated[str, StringConstraints(max_length=80)]
    url_titulo: Annotated[str, StringConstraints(max_length=255)]
    class Config:
        orm_mode = True 

class TituloAcademicoResponse(TituloAcademicoBase):
    id_titulo_academico: int


    
    