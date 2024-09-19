
from typing import Annotated
from pydantic import BaseModel, StringConstraints

class ProyectoEtapaUnoBase(BaseModel):
    id_participante_proyecto: int

class AsignarProyectoEtapaUno(BaseModel):
    id_usuario: int
    id_proyecto: int
    id_etapa: int
    id_proyecto_convocatoria: int
    