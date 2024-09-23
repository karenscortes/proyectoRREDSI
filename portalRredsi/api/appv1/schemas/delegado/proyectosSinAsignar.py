from datetime import date
from typing import List
from pydantic import BaseModel

class UnassignedProjects(BaseModel):
    id_proyecto:int
    titulo:str
    modalidad:str
    institucion:str
    area_conocimiento:str

class PaginatedUnassignedProjects(BaseModel):
    projects: List[UnassignedProjects]
    total_pages: int
    current_page: int
    page_size: int

class AuthorsResponse(BaseModel):
    nombre:str

class AssignmentVirtualStage(BaseModel):
    inicio_virtual: date
    fin_virtual: date

class AssignmentInPesonStage(BaseModel):
    inicio_presencial: date
    fin_presencial: date

class AssignmentDates(BaseModel):
    virtual_stage: AssignmentVirtualStage
    in_person_stage: AssignmentInPesonStage