from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
import enum
from appv1.schemas.tipo_documento import TipoDocumentoResponse

class EstadosEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"
    pendiente = "pendiente"

class UserBase(BaseModel):
    id_rol :int
    tipo_documento : Optional[TipoDocumentoResponse] = None 
    documento: Annotated[str, StringConstraints(max_length=55)]
    nombres: Annotated[str, StringConstraints(max_length=25)]
    apellidos: Annotated[str, StringConstraints(max_length=25)]
    celular: Annotated[str, StringConstraints(max_length=12)]
    correo: EmailStr
    estado: EstadosEnum
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    clave: Annotated[str, "Clave del usuario"]

class UserResponse(UserBase):
    id_usuario: int
    
class PaginatedUsersResponse(BaseModel):
    users: List[UserResponse]
    total_pages: int
    current_page: int
    page_size: int

class UserLoggin(UserBase):
    id_usuario: int

class PermissionsRol(BaseModel):
    module_name: str
    p_select: bool

class ResponseLoggin(BaseModel):
    user: UserLoggin
    # permissions: List[PermissionsRol]
    access_token: str

class ChangePassword(BaseModel):
    email: str
    new_password: str
    code: str
    