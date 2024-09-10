from typing import List
from pydantic import BaseModel

class UnassignedProjects(BaseModel):
    titulo:str
    modalidad:str
    institucion:str
    area_conocimiento:str

class PaginatedUnassignedProjects(BaseModel):
    users: List[UnassignedProjects]
    total_pages: int
    current_page: int
    page_size: int

class AuthorsResponse(BaseModel):
    nombre:str