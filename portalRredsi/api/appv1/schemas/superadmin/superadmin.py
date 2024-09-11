from typing import Optional
from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

# Definición del esquema para el estado de los usuarios
class EstadoEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"

# Esquema de respuesta para los detalles completos de los administradores
class SuperAdminResponse(BaseModel):
    id_usuario: int
    id_rol: int
    documento: int
    nombres: str  
    apellidos: str  
    correo: EmailStr
    estado: str
    celular: Optional[str] = None
    direccion: Optional[str] = None 
    rol_nombre: str

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
