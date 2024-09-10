from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints, constr
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
    
    
class UserUpdate(BaseModel):
    nombres: Annotated[str, StringConstraints(max_length=25)]
    apellidos: Annotated[str, StringConstraints(max_length=25)]
    tipo_documento: Optional[int]  # ID del tipo de documento
    documento: Annotated[str, StringConstraints(max_length=55)]
    correo: Optional[EmailStr]
    clave: Optional[str]
    nueva_clave: Optional[str]
    id_institucion: Optional[int]  # ID de la institución educativa
    grupo_investigacion: Optional[str]
    nombre_semillero: Optional[str]
    titulo_pregrado: Optional[str]
    titulo_especializacion: Optional[str]
    titulo_maestria: Optional[str]
    titulo_doctorado: Optional[str]
    id_area_conocimiento: Optional[int]  # ID de la primera área de conocimiento
    otra_area_conocimiento: Optional[int]  # ID de la segunda área de conocimiento