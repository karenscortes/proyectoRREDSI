from typing import Annotated
from pydantic import BaseModel, StringConstraints

class EtapaBase(BaseModel):
    nombre: Annotated[str, StringConstraints(max_length=20)]

