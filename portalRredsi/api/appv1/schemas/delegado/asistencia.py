from datetime import datetime
from pydantic import BaseModel


class AsistentesBase(BaseModel):
    id_asistente: int
    id_detalles_personales: int
    asistencia: bool
    
class AsistenciaResponse(AsistentesBase):
    tipo_asistente: str
    fecha: datetime
    url_comprobante_pago: str
