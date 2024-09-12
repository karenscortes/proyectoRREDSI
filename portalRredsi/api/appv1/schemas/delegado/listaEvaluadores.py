from typing import List
from pydantic import BaseModel

class EvaluatorsResponse(BaseModel):
    id_usuario:int
    correo:str
    estado:str
    nombres:str
    apellidos:str
    celular:str
    nombre_institucion:str
    area_conocimiento:str
    otra_area:str
    
class PaginatedUnassignedEvaluators(BaseModel):
    evaluators: List[EvaluatorsResponse]
    total_pages: int
    current_page: int
    page_size: int