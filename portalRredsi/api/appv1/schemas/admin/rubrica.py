from typing import Annotated, List
from pydantic import BaseModel, StringConstraints

from appv1.schemas.admin.items_rubrica import ItemRubricaResponse


class RubricaBase(BaseModel):
    titulo: Annotated[str, StringConstraints(max_length=40)]
    id_etapa: int
    id_modalidad: int
    

class RubricaResponse(RubricaBase):
    id_rubrica: int
    items_rubrica: List[ItemRubricaResponse]

    class Config:
        orm_mode = True 
    


