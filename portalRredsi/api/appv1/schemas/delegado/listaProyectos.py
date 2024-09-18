from datetime import date, timedelta
from typing import Annotated, Optional
from pydantic import BaseModel, StringConstraints

class ProyectoBase(BaseModel):
    id_proyecto: int
    titulo: str
    estado:str
    institucion:str

    
    
    
    
    



# CREATE TABLE proyectos (
#     id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
#     id_institucion INT,
#     id_modalidad INT,
#     id_area_conocimiento INT,
#     titulo VARCHAR(200),
#     estado ENUM('pendiente', 'asignado') NOT NULL,
#     programa_academico VARCHAR(50),
#     grupo_investigacion VARCHAR(50),
#     linea_investigacion VARCHAR(50),
#     nombre_semillero VARCHAR(50),
#     url_propuesta_escrita VARCHAR(255),
#     url_aval VARCHAR(255),
#     FOREIGN KEY (id_institucion) REFERENCES instituciones(id_institucion),
#     FOREIGN KEY (id_modalidad) REFERENCES modalidades(id_modalidad),
#     FOREIGN KEY (id_area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento)
# );