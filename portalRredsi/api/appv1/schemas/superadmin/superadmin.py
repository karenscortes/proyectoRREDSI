from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

# Definición del esquema para el estado de los usuarios
class EstadoEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"

# Esquema de respuesta para los detalles de los administradores
class SuperAdminResponse(BaseModel):
    id_usuario: int
    id_rol: int
    correo: EmailStr
    estado: EstadoEnum

    class Config:
        orm_mode = True

# Esquema de solicitud para actualizar el rol de un usuario
class UserRoleUpdateSchema(BaseModel):
    user_id: int
    new_role_id: int

    class Config:
        orm_mode = True

# Esquema de respuesta para el historial de actividades
class ActivityHistoryResponse(BaseModel):
    id_actividad: int
    id_usuario: int
    descripcion: str
    fecha: datetime

    class Config:
        orm_mode = True
