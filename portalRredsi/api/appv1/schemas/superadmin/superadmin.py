from typing import List, Optional
from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

# Definición del esquema para el estado de los usuarios
class EstadoEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"

# Esquema de respuesta para los detalles completos de los administradores
class AdminResponse(BaseModel):  # Cambié el nombre a algo más genérico
    id_usuario: int
    id_rol: int
    documento: int
    nombres: str  
    apellidos: str  
    correo: EmailStr
    estado: str
    celular: Optional[str] = None
    direccion: Optional[str] = None  # Puede quedar como opcional si planeas usarlo en el futuro
    rol_nombre: str

    class Config:
        orm_mode = True

# Esquema para paginacion de administradores
class PaginatedAdminsResponse(BaseModel):
    users: List[AdminResponse]
    total_pages: int
    current_page: int
    page_size: int

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
    correo: Optional[EmailStr] = None  # Incluyo el correo, ya que se devuelve en la consulta SQL

    class Config:
        orm_mode = True
