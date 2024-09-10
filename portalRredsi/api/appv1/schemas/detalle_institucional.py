from typing import Annotated
from pydantic import BaseModel, StringConstraints

class DetalleInstitucionalBase(BaseModel):
    id_usuario: int 
    id_institucion: int
    semillero: Annotated[str, StringConstraints(max_length=35)]
    grupo_investigacion: Annotated[str, StringConstraints(max_length=35)]
    id_primera_area_conocimiento: int
    id_segunda_area_conocimiento: int

    class Config:
        orm_mode = True 


class DetalleInstitucionalResponse(DetalleInstitucionalBase):
    id_detalle_institucional: int
    
    