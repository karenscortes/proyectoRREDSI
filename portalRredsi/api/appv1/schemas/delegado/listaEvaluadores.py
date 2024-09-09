from pydantic import BaseModel

class EvaluatorsResponse(BaseModel):
    id_usuario:int
    correo:str
    estado:str
    nombres:str
    apellidos:str
    celular:str
    nombre_institucion:str
    area_conocimiento:str
    otra_area:str