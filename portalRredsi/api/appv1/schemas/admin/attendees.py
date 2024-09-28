from typing import List
from pydantic import BaseModel, EmailStr

class AttendeesBase(BaseModel):
    id_usuario:int
    documento: str
    nombres:str
    apellidos:str
    celular: str
    correo: EmailStr 
    url_comprobante_pago:str

class PaginatedAttendees(BaseModel):
    attendees: List[AttendeesBase]
    total_pages: int
    current_page: int
    page_size: int

    class Config:
        orm_mode = True