from typing import  List, Optional
from pydantic import BaseModel
from sqlalchemy import Enum


# Esquema para la respuesta de un proyecto
class ProyectoSchema(BaseModel):
    id_proyecto: int
    institucion: str 
    modalidad: str 
    titulo: str
    url_propuesta_escrita: str
    estado_calificacion: Optional[str] = None
    
# Esquema para la respuesta paginada de varios proyectos
class PaginatedResponse(BaseModel):
    data: List[ProyectoSchema]
    total_pages: int
