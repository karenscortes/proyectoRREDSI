from typing import Annotated
from pydantic import BaseModel, StringConstraints

class AutorBase(BaseModel):
    nombre: Annotated[str, StringConstraints(max_length=50)]
    id_proyecto:int

    class Config:
        orm_mode = True 
class AutorCreate(AutorBase):
    pass