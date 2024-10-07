from pydantic import BaseModel
from typing import List, Optional

class ItemRubrica(BaseModel):
    id_item_rubrica: int
    titulo_item: str
    item_componente: Optional[str]
    valor_max: float
    calificacion: float
    observacion: Optional[str]

class RubricaCalificada(BaseModel):
    id_rubrica: int
    titulo_rubrica: str
    estado_proyecto: str
    puntaje_aprobacion: float
    items_rubrica: List[ItemRubrica]

class ProyectoRubricasResponse(BaseModel):
    titulo_proyecto: str
    universidad_proyecto: str
    tutores: Optional[str]
    ponentes: Optional[str]
    rubricas_calificadas: List[RubricaCalificada]
