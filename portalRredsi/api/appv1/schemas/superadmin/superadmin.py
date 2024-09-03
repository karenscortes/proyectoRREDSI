from pydantic import BaseModel, EmailStr
from enum import Enum

class EstadoEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"

class SuperAdminResponse(BaseModel):
    id_usuario: int
    id_rol: int
    correo: EmailStr
    estado: EstadoEnum

    class Config:
        orm_mode = True

class UserRoleUpdateSchema(BaseModel):
    user_id: int
    new_role_id: int

    class Config:
        orm_mode = True        

