from pydantic import BaseModel
from typing import List, Optional


# Esquema para los participantes, que puede incluir tanto tutores como ponentes
class ParticipanteCreate(BaseModel):
    id_tipo_documento: int  # ID del tipo de documento (foráneo de tipos_documento)
    documento: str  # Documento de identidad del participante
    nombres: str  # Nombres del participante
    apellidos: str  # Apellidos del participante
    celular: str  # Número de celular del participante
    correo: str  # Correo electrónico del participante

# Esquema para los ponentes, reutilizando el esquema de participante
class PonenteCreate(ParticipanteCreate):
    # Hereda los mismos campos que ParticipanteCreate
    pass

# Esquema completo para la creación del proyecto
class AutorCreate(BaseModel):
    nombre: str

class ProyectoCreate(BaseModel):
    id_institucion: int
    id_modalidad: int
    id_area_conocimiento: int
    titulo: str
    programa_academico: str
    grupo_investigacion: Optional[str]
    linea_investigacion: Optional[str]
    nombre_semillero: Optional[str]
    url_propuesta_escrita: Optional[str]
    url_aval: Optional[str]
    autores: List[AutorCreate]
# Esquema para la creación de la convocatoria asociada al proyecto
class ProyectoConvocatoriaCreate(BaseModel):
    id_proyecto: int  # ID del proyecto (foráneo de proyectos)
    id_convocatoria: int  # ID de la convocatoria (foráneo de convocatorias)
class ProyectoResponse(BaseModel):
    id_proyecto: int
    status: str

    class Config:
        from_attributes = True  # Cambiado para Pydantic 2.x