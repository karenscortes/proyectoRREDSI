from typing import List, Optional
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


    