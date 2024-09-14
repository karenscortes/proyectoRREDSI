from pydantic import BaseModel

class ModalidadBase(BaseModel):
    nombre: str

class ModalidadResponse(ModalidadBase):
    id_modalidad: int
    class Config:
        orm_mode = True