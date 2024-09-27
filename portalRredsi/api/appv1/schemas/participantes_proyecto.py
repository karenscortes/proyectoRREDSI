from pydantic import BaseModel

class participanteProyectoBase(BaseModel):
    id_usuario: int
    id_proyecto: int
    id_proyectos_convocatoria:int
    
    
    class Config:
        orm_mode = True
        
        
class participanteProyectoCreate(participanteProyectoBase):
    pass