from typing import Annotated
from pydantic import BaseModel, EmailStr
from datetime import datetime
import enum

class EstadosEnum(str, enum.Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    pendiente = "Pendiente"

class UserBase(BaseModel):
    correo: EmailStr
    id_rol: Annotated[str, "Identificador del rol"]

class UserCreate(UserBase):
    clave: Annotated[str, "Clave del usuario"]

class UserResponse(UserBase):
    user_id: str
    user_status: EstadosEnum = EstadosEnum.activo
    created_at: datetime
    updated_at: datetime
