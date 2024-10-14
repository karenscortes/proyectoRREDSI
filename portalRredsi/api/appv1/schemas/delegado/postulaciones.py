from pydantic import BaseModel
from typing import List, Optional

class applicationsResponse(BaseModel):
    id_convocatoria:int
    id_evaluador:int
    estado_postulacion:str
    etapa_virtual:bool
    etapa_presencial:bool
    jornada_manana:bool
    jornada_tarde:bool
    correo:str
    nombres:str
    apellidos:str
    celular:str
    nombre_institucion:str
    area_conocimiento:str
    otra_area:str

class PaginatedApplications(BaseModel):
    applications: List[applicationsResponse]
    total_pages: int
    current_page: int
    page_size: int

class certificatesResponse(BaseModel):
    id_titulo_academico:int
    nivel:str
    nombre_titulo:str
    url_titulo:str
    id_usuario:int

class CertificatesCreate(BaseModel):
    pregrado: Optional[str] = None
    especializacion: Optional[str] = None
    maestria: Optional[str] = None
    doctorado: Optional[str] = None
