from datetime import datetime
from pydantic import BaseModel


class AsistentesBase(BaseModel):
    id_asistente: int
    id_usuario: int
    asistencia: bool
    
class AsistenciaResponse(AsistentesBase):
    fecha: datetime
    url_comprobante_pago: str

class ConvocatoriaActual(BaseModel):
    id_convocatoria: int
    nombre:str
    fecha_inicio: datetime
    fecha_fin: datetime
    

