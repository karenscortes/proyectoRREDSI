from pydantic import BaseModel
class ProyectoSchema(BaseModel):
    id_proyecto: int
    id_institucion: int 
    id_modalidad: int
    id_area_conocimiento: int
    titulo: str
    estado: str
    programa_academico: str
    grupo_investigacion: str
    linea_investigacion: str
    nombre_semillero: str
    url_propuesta_escrita: str
    url_poster: str
    url_aval: str

