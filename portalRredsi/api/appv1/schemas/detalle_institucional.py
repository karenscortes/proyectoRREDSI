from typing import Annotated, Optional
from pydantic import BaseModel, StringConstraints

from appv1.schemas.area_conocimiento import AreaConocimientoResponse
from appv1.schemas.institucion import InstitucionBase

class DetalleInstitucionalBase(BaseModel):
    id_usuario: int 
    institucion: InstitucionBase
    semillero: Optional[Annotated[str, StringConstraints(max_length=35)]]=None
    grupo_investigacion: Annotated[str, StringConstraints(max_length=35)]
    primer_area: AreaConocimientoResponse
    segunda_area: AreaConocimientoResponse

    class Config:
        orm_mode = True 


class DetalleInstitucionalResponse(DetalleInstitucionalBase):
    id_detalle_institucional: int
    
class DetalleInstitucional(BaseModel):
    id_detalle_institucional:Optional[int] = None
    id_usuario:int
    id_institucion: int
    semillero:  Optional[Annotated[str, StringConstraints(max_length=35)]]=None
    grupo_investigacion: Annotated[str, StringConstraints(max_length=35)]
    id_primera_area_conocimiento: int
    id_segunda_area_conocimiento: int

class DetalleInstitucionalUpdate(BaseModel):
    id_usuario:Optional[int] = None
    id_institucion: Optional[int] = None
    grupo_investigacion: Optional[Annotated[str, StringConstraints(max_length=35)]] = None
    semillero:  Optional[Annotated[str, StringConstraints(max_length=35)]]=None
    id_primera_area_conocimiento:Optional[int] = None
    id_segunda_area_conocimiento:Optional[int] = None

