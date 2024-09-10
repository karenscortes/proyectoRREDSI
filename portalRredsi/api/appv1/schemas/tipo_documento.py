from typing import Optional
from pydantic import BaseModel

class TipoDocumentoBase(BaseModel):
    nombre: str

class TipoDocumentoResponse(TipoDocumentoBase):
    id_tipo_documento: int
    class Config:
        orm_mode = True