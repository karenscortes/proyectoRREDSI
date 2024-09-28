from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints

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

class UpdatedAttendee(BaseModel):
    nombres: Optional[Annotated[str, StringConstraints(max_length=25)]] = None
    apellidos: Optional[Annotated[str, StringConstraints(max_length=25)]] = None
    correo: Optional[EmailStr] = None
    celular: Optional[Annotated[str, StringConstraints(max_length=12)]] = None
    url_comprobante_pago: Optional[str] = None

    class Config:
        orm_mode = True