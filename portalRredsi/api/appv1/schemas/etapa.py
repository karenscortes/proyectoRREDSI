from pydantic import BaseModel

class EtapaBase(BaseModel):
    nombre: str

class EtapaResponse(EtapaBase):
    id_etapa: int
    class Config:
        orm_mode = True