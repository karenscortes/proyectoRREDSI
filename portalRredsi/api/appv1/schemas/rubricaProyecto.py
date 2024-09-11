from pydantic import BaseModel
from typing import List

class ItemRubrica(BaseModel):
    id_item_rubrica: int
    titulo: str
    componente: str
    valor_max: float

class Rubrica(BaseModel):
    id_rubrica: int
    rubrica_titulo: str
    items: List[ItemRubrica]
