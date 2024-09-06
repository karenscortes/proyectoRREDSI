from pydantic import BaseModel

class applicationsResponse(BaseModel):
    id_convocatoria:int
    id_evaluador:int
    etapa_virtual:bool
    etapa_presencial:bool
    jornada_manana:bool
    jornada_tarde:bool
    correo:str
    nombres:str
    apellidos:str
    celular:str
    nombre_institucion:str
    area_conocimiento:str
    otra_area:str

class certificatesResponse(BaseModel):
    id_titulo_academico:int
    nivel:str
    nombre_titulo:str
    url_titulo:str
    id_usuario:int