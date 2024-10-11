from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

class institucionResponse(BaseModel):
    id_institucion: int
    nombre: Annotated[str, StringConstraints(max_length=50)]

