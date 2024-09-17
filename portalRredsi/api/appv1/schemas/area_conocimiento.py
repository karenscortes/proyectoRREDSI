from pydantic import BaseModel

class AreaConocimientoBase(BaseModel):
    nombre: str

class AreaConocimientoResponse(AreaConocimientoBase): 
    id_area_conocimiento: int 
    