
import enum
from typing import Annotated
from pydantic import BaseModel, StringConstraints

# class participante_tipo(enum.Enum):
#     ponente = "ponente"
#     tutor = "tutor"
#     suplente_evaluador = "suplente evaluador"
#     suplente_ponente = "suplente ponente"
#     evaluador = "evaluador"

class ProyectoEtapaUnoBase(BaseModel):
    id_participante_proyecto: int

class AsignarProyectoEtapaUno(BaseModel):
    id_datos_personales: int
    id_proyecto: int
    id_etapa: int
    id_proyecto_convocatoria: int
    tipo_participante : Annotated[str, StringConstraints(max_length=25)]
    