from datetime import date, timedelta
from typing import Annotated
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
