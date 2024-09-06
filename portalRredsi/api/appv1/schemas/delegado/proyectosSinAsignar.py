from pydantic import BaseModel

class UnassignedProjects(BaseModel):
    titulo:str
    modalidad:str
    institucion:str
    area_conocimiento:str

class AuthorsResponse(BaseModel):
    nombre:str