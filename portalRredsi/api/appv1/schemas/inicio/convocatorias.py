from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints, constr
from datetime import date
import enum

class EstadosEnum(str, enum.Enum):
    en_curso = "en curso"
    concluida = "concluida"
    por_publicar = "por publicar"

class ConvocatoriaBase(BaseModel):
    nombre: Annotated[str, StringConstraints(max_length=25)]
    fecha_inicio:date
    fecha_fin:date 
    estado: EstadosEnum
    
    class Config:
        orm_mode = True
        
class ConvocatoriaResponse(ConvocatoriaBase):
    pass

# Esquema para la respuesta paginada
class PaginatedConvocatoriaResponse(BaseModel):
    convocatorias: List[ConvocatoriaBase]
    total_pages: int
    current_page: int
    page_size: int

    class Config:
        orm_mode = True

class ConvocatoriaUpdate(ConvocatoriaBase):
 
    documento: Optional[Annotated[str, StringConstraints(max_length=55)]] = None
    nombres: Optional[Annotated[str, StringConstraints(max_length=25)]] = None
    apellidos: Optional[Annotated[str, StringConstraints(max_length=25)]]= None
    celular: Optional[Annotated[str, StringConstraints(max_length=12)]]= None
    correo: Optional[EmailStr]= None 
            
class ConvocatoriaCreate(ConvocatoriaBase):
    id_tipo_documento: int
    clave: Annotated[str, "Clave del usuario"]

class PaginatedUsersResponse(BaseModel):
    total_pages: int
    current_page: int
    page_size: int