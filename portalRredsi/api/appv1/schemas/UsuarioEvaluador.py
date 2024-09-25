from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints

class EvaluadorBase(BaseModel):
    id_tipo_documento: int 
    documento: Annotated[str, StringConstraints(max_length=55)]
    nombres: Annotated[str, StringConstraints(max_length=25)]
    apellidos: Annotated[str, StringConstraints(max_length=25)]
    celular: Annotated[str, StringConstraints(max_length=12)]
    correo: EmailStr 
    
    class Config:
        orm_mode = True
        
        
class EvaluadorCreate(EvaluadorBase):
    id_tipo_documento: int
    clave: Annotated[str, "Clave del usuario"]