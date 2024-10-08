from typing import Annotated, Optional
from pydantic import BaseModel, StringConstraints, condecimal 
class ItemRubrica(BaseModel):
    titulo: Annotated[str, StringConstraints(max_length=50)]
    componente: str
    valor_max: Annotated[float,condecimal(max_digits=2, decimal_places=1)]
    id_rubrica: int
    estado: Optional[str] = "activo"
    

class ItemRubricaResponse(ItemRubrica):
    id_item_rubrica: int

    class Config:
        orm_mode = True 

class ItemCreate(ItemRubrica):
    pass

class ItemUpdate(BaseModel):
    titulo: Optional[Annotated[str, StringConstraints(max_length=50)]] = None
    componente: Optional[str] = None
    valor_max: Optional[Annotated[float,condecimal(max_digits=2, decimal_places=1)]] = None
    class Config:
        orm_mode = True

class ItemUpdateStatus(BaseModel):
    estado: Optional[str] = "inactivo"