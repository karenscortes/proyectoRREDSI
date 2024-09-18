from typing import List, Optional

from pydantic import BaseModel
from appv1.schemas.area_conocimiento import AreaConocimientoResponse
from appv1.schemas.detalle_institucional import DetalleInstitucionalResponse
from appv1.schemas.tipo_documento import TipoDocumentoResponse
from appv1.schemas.titulo_academico import TituloAcademicoResponse
from appv1.schemas.usuario import UserResponse

class DelegadoBase(UserResponse):
    tipo_documento : Optional[TipoDocumentoResponse] = None 
    
class DelegadoResponse(DelegadoBase):
    detalles_institucionales: List[DetalleInstitucionalResponse]
    titulos_academicos: List[TituloAcademicoResponse]
    class Config:
        orm_mode = True

class PaginatedDelegadoResponse(BaseModel):
    users: List[DelegadoResponse]
    total_pages: int
    current_page: int
    page_size: int
    class Config:
        orm_mode = True