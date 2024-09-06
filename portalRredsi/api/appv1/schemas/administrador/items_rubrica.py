from typing import Annotated
from pydantic import BaseModel, StringConstraints, condecimal

class ItemRubrica(BaseModel):
    titulo: Annotated[str, StringConstraints(max_length=50)]
    descripcion: str
    valor_max: Annotated[float,condecimal(max_digits=2, decimal_places=1)]
    

class ItemRubricaResponse(ItemRubrica):
    id_item_rubrica: int

    
    class Config:
        orm_mode = True 


class ItemCreate(ItemRubrica):
    pass
    