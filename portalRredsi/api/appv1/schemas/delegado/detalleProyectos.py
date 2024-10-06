from datetime import date, timedelta
from typing import List, Optional
from pydantic import BaseModel

# Esquema básico del proyecto
class DetalleProyecto(BaseModel):
    id_proyecto: int
    institucion: str
    modalidad: str
    titulo: str
    url_propuesta_escrita: str
    estado_evaluacion: Optional[str] = None
    url_presentacion: Optional[str] = None

# Esquema para la sala y el horario del proyecto
class SalaConHorario(BaseModel):
    numero_sala: str
    fecha: date
    hora_inicio: timedelta 
    hora_fin: timedelta 

# Esquema para los usuarios asociados al proyecto (evaluador, ponente, suplente)
class UsuarioProyecto(BaseModel):
    id_usuario: int 
    nombres: str  
    apellidos: str
    id_rol: Optional[int] = None 
    id_etapa: Optional[int] = None


class ProyectoResponse(BaseModel):
    proyecto: DetalleProyecto 
    sala: SalaConHorario  
    participantes: List[UsuarioProyecto]  
    
class UrlPresentacionProyecto(BaseModel):
    id_presentacion: int
    id_proyecto: int
    url_presentacion: str
    


