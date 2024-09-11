
from typing import Annotated
from pydantic import BaseModel, StringConstraints

class ProyectoEtapaUnoBase(BaseModel):
    id_participante_proyecto: int

class AsignarProyectoEtapaUno(BaseModel):
    id_usuario: int
    id_proyecto: int
    id_etapa: int
    id_proyecto_convocatoria: int
    
class PosibleEvaluadorEtapaVirtual():
    id_usuario: int
    documento: Annotated[str, StringConstraints(max_length=55)]
    nombres: Annotated[str, StringConstraints(max_length=25)]
    apellidos: Annotated[str, StringConstraints(max_length=25)]
    celular: Annotated[str, StringConstraints(max_length=10)]
    correo: Annotated[str, StringConstraints(max_length=70)]