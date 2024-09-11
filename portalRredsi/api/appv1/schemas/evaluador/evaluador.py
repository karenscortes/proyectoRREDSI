from typing import List,  Optional
from datetime import date, time
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
    estado_evaluacion: Optional[str] = None
    
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

class ProyectoConSalaSchema(BaseModel):
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
    numero_sala: str
    nombre_sala: str
    fecha: date  # Cambiado de str a date
    hora_inicio: str  # Cambiado de int a str para recibir la hora en formato 'HH:MM'
    hora_fin: str  # Cambiado de int a str para recibir la hora en formato 'HH:MM'


class PaginatedResponseHorario(BaseModel):
    data: List[ProyectoConSalaSchema]
    total_pages: int
