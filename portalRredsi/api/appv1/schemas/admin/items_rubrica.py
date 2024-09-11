from typing import Annotated, Optional
from pydantic import BaseModel, StringConstraints, condecimal 
class ItemRubrica(BaseModel):
    titulo: Annotated[str, StringConstraints(max_length=50)]
    componente: str
    valor_max: Annotated[float,condecimal(max_digits=2, decimal_places=1)]
    id_rubrica: int
    

class ItemRubricaResponse(ItemRubrica):
    id_item_rubrica: int

    class Config:
        orm_mode = True 

class ItemCreate(ItemRubrica):
    pass

class ItemUpdate(BaseModel):
    titulo: Optional[Annotated[str, StringConstraints(max_length=50)]]
    componente: Optional[str]
    valor_max: Optional[Annotated[float,condecimal(max_digits=2, decimal_places=1)]]
    class Config:
        orm_mode = True