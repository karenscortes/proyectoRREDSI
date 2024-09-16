from typing import List,  Optional
from datetime import date, time
from pydantic import BaseModel

# Esquema para la respuesta de un proyecto
class ProyectoSchema(BaseModel):
    id_proyecto: int
    institucion: str 
    modalidad: str
    area_conocimiento: str
    titulo: str
    estado: str
    programa_academico: str
    grupo_investigacion: str
    linea_investigacion: str
    nombre_semillero: str
    url_propuesta_escrita: str
    url_aval: str
    estado_evaluacion: Optional[str] = None
    
# Esquema para la respuesta paginada de varios proyectos
class PaginatedResponse(BaseModel):
    data: List[ProyectoSchema]
    total_pages: int

# Esquema para crear la postulacion de un evaluador
class PostulacionEvaluadorCreate(BaseModel):
    id_evaluador: int
    etapa_virtual: int
    etapa_presencial: int
    jornada_manana: int
    jornada_tarde: int

# Esquema para la respuesta de la rubrica
class RespuestaRubricaCreate(BaseModel):
    id_item_rubrica: int
    id_usuario: int
    id_proyecto: int
    observacion: str
    calificacion: float
    calificacion_final: float

# Esquema para la respuesta de los proyectos que traen el horario de sala
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

# Esquema para la respuesta paginada de varios proyectos con el horario de la sala
class PaginatedResponseHorario(BaseModel):
    data: List[ProyectoConSalaSchema]
    total_pages: int

# Esquema para la respuesta de un componente de rubrica entero
class Componente(BaseModel):
    titulo: str
    descripcion: str
    valor_maximo: float
    calificacion: Optional[float] = None
    observaciones: Optional[str] = None

# Esquema para calificar un proyecto
class CalificarProyectoRespuesta(BaseModel):
    titulo_proyecto: str
    universidad_proyecto: str
    nombre_evaluador: str
    cedula_evaluador: str
    universidad_evaluador: str
    email_evaluador: str
    celular_evaluador: str
