from pydantic import BaseModel

class InstitucionBase(BaseModel):
    id_institucion: int 
    nombre: str
