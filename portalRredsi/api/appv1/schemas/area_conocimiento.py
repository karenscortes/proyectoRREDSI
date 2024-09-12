from pydantic import BaseModel

class AreaConocimientoBase(BaseModel):
    id_area_conocimiento: int 
    nombre: str
