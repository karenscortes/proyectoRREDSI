from typing import List
from appv1.schemas.detalle_institucional import DetalleInstitucionalResponse
from appv1.schemas.titulo_academico import TituloAcademicoResponse
from appv1.schemas.usuario import UserResponse


class DelegadoResponse(UserResponse):
    detalles_institucionales: List[DetalleInstitucionalResponse]
    titulos_academicos: List[TituloAcademicoResponse]
    class Config:
        orm_mode = True


    