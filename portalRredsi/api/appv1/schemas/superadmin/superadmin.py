from typing import List, Optional
from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

# Definición del esquema para el estado de los usuarios
class EstadoEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"

# Esquema para los detalles completos de los administradores
class AdminResponse(BaseModel):
    id_usuario: int
    id_rol: int
    documento: str
    nombres: str  
    apellidos: str  
    correo: EmailStr
    estado: EstadoEnum  # Cambiado para usar el Enum
    telefono: Optional[str] = None
    direccion: Optional[str] = None 
    rol_nombre: str

    class Config:
        orm_mode = True

# Esquema para la respuesta paginada
class PaginatedAdminResponse(BaseModel):
    admins: List[AdminResponse]
    total_pages: int
    current_page: int
    page_size: int

    class Config:
        orm_mode = True

# Esquema de solicitud para actualizar el rol de un usuario
class UserRoleUpdateSchema(BaseModel):
    user_id: int
    new_role_id: int

    class Config:
        orm_mode = True

# Esquema para la respuesta de cambio de estado del usuario
class UserStatusUpdateResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True

# Esquema de respuesta para el historial de actividades
class ActivityHistoryResponse(BaseModel):
    id_actividad: int
    id_usuario: int
    accion: str  
    fecha: datetime
    correo: Optional[EmailStr] = None
    modulo_nombre: Optional[str] = None 

    class Config:
        orm_mode = True

# Esquema de respuesta para el historial de actividades paginado
class PaginatedActivityHistoryResponse(BaseModel):
    activities: List[ActivityHistoryResponse]  
    total_pages: int                          
    current_page: int                          
    page_size: int                          

    class Config:
        orm_mode = True


