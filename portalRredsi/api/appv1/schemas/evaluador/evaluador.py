from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

class ProyectoSchema(BaseModel):
    id_proyecto: int
    id_institucion: int 
    id_modalidad: int
    id_area_conocimiento: int
    titulo: str
    estado: str
    programa_academico: str
    grupo_investigacion: str
    linea_investigacion: str
    nombre_semillero: str
    url_propuesta_escrita: str
    url_aval: str
    estado_evaluacion: Optional[str] = None  # Campo opcional


class EstadoPostulacion(str, Enum):
    pendiente = 'pendiente'
    aceptada = 'aceptada'
    rechazada = 'rechazada'

class PostulacionEvaluadorSchema(BaseModel):
    id_convocatoria: int
    id_evaluador: int
    estado_postulacion: EstadoPostulacion 
    etapa_virtual:bool  # Solo acepta 0 o 1
    etapa_presencial:bool  # Solo acepta 0 o 1
    jornada_manana:bool  # Solo acepta 0 o 1
    jornada_tarde:bool  # Solo acepta 0 o 1

class PaginatedResponse(BaseModel):
    data: List[ProyectoSchema]
    total_pages: int

