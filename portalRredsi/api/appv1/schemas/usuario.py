from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
import enum

class EstadosEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"

class UserBase(BaseModel):
    id_rol :int
    id_tipo_documento: int 
    documento: Annotated[str, StringConstraints(max_length=55)]
    nombres: Annotated[str, StringConstraints(max_length=25)]
    apellidos: Annotated[str, StringConstraints(max_length=25)]
    celular: Annotated[str, StringConstraints(max_length=12)]
    correo: EmailStr 
    estado: Optional[EstadosEnum] = "activo"
    
    class Config:
        orm_mode = True
        
class UserResponse(UserBase):
    id_usuario: int

class UserUpdate(BaseModel):
    id_tipo_documento: Optional[int] = None
    documento: Optional[Annotated[str, StringConstraints(max_length=55)]] = None
    nombres: Optional[Annotated[str, StringConstraints(max_length=50)]] = None
    apellidos: Optional[Annotated[str, StringConstraints(max_length=50)]] = None
    celular: Optional[Annotated[str, StringConstraints(max_length=25)]] = None
    correo: Optional[EmailStr] = None
    clave: Optional[str] = None

            
class UserCreate(UserBase):
    id_tipo_documento: int
    clave: Annotated[str, "Clave del usuario"]

    
class PaginatedUsersResponse(BaseModel):
    users: List[UserResponse]
    total_pages: int
    current_page: int
    page_size: int

class UserLoggin(UserBase):
    id_usuario: int

class PermissionsRol(BaseModel):
    id_modulo: int
    p_consultar: bool

class ResponseLoggin(BaseModel):
    user: UserLoggin
    permisos: List[PermissionsRol]
    access_token: str

class ChangePassword(BaseModel):
    email: str
    new_password: str
    code: str
