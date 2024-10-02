from typing import List
from pydantic import BaseModel

# Esquema de cada ítem dentro de una rúbrica calificada
class ItemRubrica(BaseModel):
    id_item_rubrica: int
    titulo_item: str
    item_componente: str
    valor_max: float
    calificacion: float
    observacion: str

    class Config:
        from_attributes = True  # Adaptado a Pydantic v2

# Esquema para la información del evaluador
class Evaluador(BaseModel):
    nombre_evaluador: str
    cedula_evaluador: str
    universidad_evaluador: str
    email_evaluador: str
    celular_evaluador: str

    class Config:
        from_attributes = True  # Adaptado a Pydantic v2

# Esquema para una rúbrica calificada, que incluye ítems y evaluador (sin etapa)
class RubricaCalificada(BaseModel):
    id_rubrica: int
    titulo_rubrica: str
    estado_proyecto: str
    puntaje_aprobacion: float
    items_rubrica: List[ItemRubrica]  # Lista de ítems calificados
    evaluador: Evaluador  # Información del evaluador

    class Config:
        from_attributes = True  # Adaptado a Pydantic v2

# Esquema principal que agrupa todo: proyecto, universidad, tutores, ponentes y las rúbricas calificadas
class ProyectoRubricasResponse(BaseModel):
    titulo_proyecto: str
    universidad_proyecto: str
    tutores: str
    ponentes: str
    rubricas_calificadas: List[RubricaCalificada]  # Lista de rúbricas calificadas

    class Config:
        from_attributes = True  # Adaptado a Pydantic v2
