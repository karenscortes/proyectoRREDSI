from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional

# Modelo para los ítems de la rúbrica
class ItemRubrica(BaseModel):
    id_item_rubrica: int
    titulo_item: str
    item_componente: str
    valor_max: float
    calificacion: float
    observacion: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

# Modelo para la Etapa
class Etapa(BaseModel):
    nombre_etapa: str
    tipo_etapa: str

    model_config = ConfigDict(from_attributes=True)

# Modelo para el Evaluador
class Evaluador(BaseModel):
    nombre_evaluador: str
    cedula_evaluador: str
    universidad_evaluador: str
    email_evaluador: str
    celular_evaluador: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

# Modelo para la Rúbrica Calificada
class RubricaCalificada(BaseModel):
    id_rubrica: int
    titulo_rubrica: str
    estado_proyecto: str
    puntaje_aprobacion: float
    items_rubrica: List[ItemRubrica]
    etapa: Etapa
    evaluador: Evaluador

    model_config = ConfigDict(from_attributes=True)

# Modelo para la respuesta final del proyecto con rúbricas calificadas
class ProyectoRubricasResponse(BaseModel):
    titulo_proyecto: str
    universidad_proyecto: str
    tutores: Optional[str] = None
    ponentes: Optional[str] = None
    rubricas_calificadas: List[RubricaCalificada]

    model_config = ConfigDict(from_attributes=True)
