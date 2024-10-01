from typing import Annotated
from pydantic import BaseModel, StringConstraints

class AutorBase(BaseModel):
    nombre: Annotated[str, StringConstraints(max_length=50)]

    class Config:
        orm_mode = True 
class AutorCreate(AutorBase):
    pass