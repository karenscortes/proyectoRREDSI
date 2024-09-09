from typing import Annotated, List
from pydantic import BaseModel, EmailStr
from datetime import datetime
import enum

class EstadosEnum(str, enum.Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    pendiente = "Pendiente"

class UserBase(BaseModel):
    correo: EmailStr
    id_rol: int

class UserCreate(UserBase):
    clave: Annotated[str, "Clave del usuario"]

class UserResponse(UserBase):
    user_id: str
    user_status: EstadosEnum = EstadosEnum.activo
    created_at: datetime
    updated_at: datetime

    
class PaginatedUsersResponse(BaseModel):
    users: List[UserResponse]
    total_pages: int
    current_page: int
    page_size: int

class UserLoggin(UserBase):
    user_id: str

class PermissionsRol(BaseModel):
    module_name: str
    p_select: bool

class ResponseLoggin(BaseModel):
    user: UserLoggin
    permissions: List[PermissionsRol]
    access_token: str

class ChangePassword(BaseModel):
    email: str
    new_password: str
    code: str
    