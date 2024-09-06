from typing import Annotated, List
from pydantic import BaseModel, StringConstraints

from appv1.schemas.administrador.items_rubrica import ItemRubricaResponse


class RubricaBase(BaseModel):
    titulo: Annotated[str, StringConstraints(max_length=40)]
    id_etapa: int
    id_modalidad: int
    

class RubricaResponse(RubricaBase):
    id_rubrica: int
    items: List[ItemRubricaResponse]

    class Config:
        orm_mode = True 
    


