from typing import Annotated, Optional
from pydantic import BaseModel, StringConstraints

from appv1.schemas.area_conocimiento import AreaConocimientoResponse
from appv1.schemas.institucion import InstitucionBase

class DetalleInstitucionalBase(BaseModel):
    id_usuario: int 
    institucion: InstitucionBase
    semillero: Annotated[str, StringConstraints(max_length=35)]
    grupo_investigacion: Annotated[str, StringConstraints(max_length=35)]
    primer_area: Optional[AreaConocimientoResponse] = None
    segunda_area: Optional[AreaConocimientoResponse] = None

    class Config:
        orm_mode = True 


class DetalleInstitucionalResponse(DetalleInstitucionalBase):
    id_detalle_institucional: int
    
class DetalleInstitucionalEditable(BaseModel):
    id_institucion: int
    semillero: Annotated[str, StringConstraints(max_length=35)]
    grupo_investigacion: Annotated[str, StringConstraints(max_length=35)]
    id_primera_area_conocimiento: int
    id_segunda_area_conocimiento: int
