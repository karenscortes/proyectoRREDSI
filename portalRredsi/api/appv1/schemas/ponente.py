from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints


class UserPonenteBase(BaseModel):
    id_tipo_documento: int 
    documento: Annotated[str, StringConstraints(max_length=55)]
    nombres: Annotated[str, StringConstraints(max_length=25)]
    apellidos: Annotated[str, StringConstraints(max_length=25)]
    celular: Annotated[str, StringConstraints(max_length=12)]
    correo: EmailStr 
    
    class Config:
        orm_mode = True
        
class UserPonenteResponse(UserPonenteBase):
    pass

            
class UserPonenteCreate(UserPonenteBase):
    id_tipo_documento: int

    