from typing import Annotated, List
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime
import enum

class EstadosEnum(str, enum.Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    pendiente = "Pendiente"

class UserBase(BaseModel):
    id_rol :int
    id_tipo_documento : int
    documento: Annotated[str, StringConstraints(max_length=55)]
    nombres: Annotated[str, StringConstraints(max_length=25)]
    apellidos: Annotated[str, StringConstraints(max_length=25)]
    celular: Annotated[str, StringConstraints(max_length=10)]
    correo: EmailStr
    estado: str

class UserCreate(UserBase):
    clave: Annotated[str, "Clave del usuario"]

class UserResponse(UserBase):
    id_usuario: str
    correo: EmailStr
    estado: EstadosEnum = EstadosEnum.activo
    id_rol :int
    
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
    