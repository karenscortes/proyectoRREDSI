from pydantic import BaseModel
from datetime import date

class EventoResponse(BaseModel):
    id_evento: int
    nombre: str
    fecha: date
    estado: str

    class Config:
        orm_mode = True
