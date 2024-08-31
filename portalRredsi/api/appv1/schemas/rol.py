from typing import Optional
from pydantic import BaseModel

class RolBase(BaseModel):
    id_rol: Optional[int] = None
    nombre: str

class RolResponse(RolBase):
    pass