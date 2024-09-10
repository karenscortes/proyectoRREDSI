from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime
import enum

from appv1.schemas.detalle_institucional import DetalleInstitucionalResponse

class EstadosEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"
    pendiente = "pendiente"

class UserBase(BaseModel):
    id_rol :int
    tipo_documento : int
    documento: Annotated[str, StringConstraints(max_length=55)]
    nombres: Annotated[str, StringConstraints(max_length=25)]
    apellidos: Annotated[str, StringConstraints(max_length=25)]
    celular: Annotated[str, StringConstraints(max_length=12)]
    correo: EmailStr
    estado: EstadosEnum
    detalles_institucionales: List[DetalleInstitucionalResponse]

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
    
    
class UsuarioUpdate(BaseModel):
    nombres: Optional[str]
    apellidos: Optional[str]
    correo: Optional[EmailStr]
    clave: Optional[str]

# Esquema para la actualización de detalles institucionales
class DetallesInstitucionalesUpdate(BaseModel):
    id_institucion: Optional[int]
    semillero: Optional[str]
    grupo_investigacion: Optional[str]
    id_primera_area_conocimiento: Optional[int]
    id_segunda_area_conocimiento: Optional[int]

# Esquema para la actualización de títulos académicos
class TituloAcademicoUpdate(BaseModel):
    nivel: str
    nombre_titulo: str
    url_titulo: Optional[str]
    
# Esquema completo de actualización de perfil
class PerfilUpdate(BaseModel):
    usuario: Optional[UsuarioUpdate]
    detalles_institucionales: Optional[DetallesInstitucionalesUpdate]
    titulos_academicos: Optional[list[TituloAcademicoUpdate]]