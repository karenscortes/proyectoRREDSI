from typing import List
from pydantic import BaseModel

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
    estado_evaluacion: str

class PaginatedResponse(BaseModel):
    data: List[ProyectoSchema]
    total_pages: int

class PostulacionEvaluadorCreate(BaseModel):
    id_evaluador: int
    etapa_virtual: int
    etapa_presencial: int
    jornada_manana: int
    jornada_tarde: int

class RespuestaRubricaCreate(BaseModel):
    id_item_rubrica: int
    id_usuario: int
    id_proyecto: int
    observacion: str
    calificacion: float
    calificacion_final: float

