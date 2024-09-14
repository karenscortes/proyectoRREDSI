from typing import Annotated, List
from pydantic import BaseModel, StringConstraints

from appv1.schemas.admin.items_rubrica import ItemRubricaResponse
from appv1.schemas.etapa import EtapaResponse
from appv1.schemas.modalidad import ModalidadResponse


class RubricaBase(BaseModel):
    titulo: Annotated[str, StringConstraints(max_length=40)]
    etapa: EtapaResponse
    modalidad: ModalidadResponse
    

class RubricaResponse(RubricaBase):
    id_rubrica: int
    items_rubrica: List[ItemRubricaResponse]

    class Config:
        orm_mode = True 
    


