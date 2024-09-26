from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

class TipoIdentificacionResponse(BaseModel):
    id_tipo_documento: int
    nombre: Annotated[str, StringConstraints(max_length=10)]

