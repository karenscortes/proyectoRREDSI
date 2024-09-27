from datetime import date, timedelta
from typing import Annotated, Optional
from pydantic import BaseModel, StringConstraints


class SalaBase(BaseModel):
    id_sala: int
    numero_sala: Annotated[str, StringConstraints(max_length=25)]
    nombre_sala: Annotated[str, StringConstraints(max_length=25)]
    
class SalaResponse(SalaBase):
    id_usuario: int
    area_conocimiento: int

class AsignarProyectoSala(BaseModel):
    id_sala: int
    id_proyecto_convocatoria: int
    fecha: date
    hora_inicio: timedelta
    hora_fin: timedelta
    
class DetalleSala(AsignarProyectoSala):
    pass

class ProyectoResponse(BaseModel):
    id_proyecto: int
    id_institucion: int 
    id_modalidad: int
    id_area_conocimiento: int
    titulo: str
    programa_academico: str
    grupo_investigacion: str
    linea_investigacion: str
    nombre_semillero: str
    url_propuesta_escrita: str
    url_aval: str
    estado_calificacion: Optional[str] = None