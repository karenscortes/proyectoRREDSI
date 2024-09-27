from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

class modalidadResponse(BaseModel):
    id_modalidad: int
    nombre: Annotated[str, StringConstraints(max_length=20)]

