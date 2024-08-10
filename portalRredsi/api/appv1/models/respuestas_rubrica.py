from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from models.base_class import Base

class Respuesta_rubrica(Base):
    __tablename__ = 'respuestas_rubrica'
    id_respuestas_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    id_item_rubrica = Column(Integer, ForeignKey('item_rubrica.id_item_rubrica'))
    id_rubrica_resultado = Column(Integer, ForeignKey('rubrica_resultado.id_rubrica_resultado'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_proyecto_convocatoria = Column(Integer, ForeignKey('proyecto_convocatoria.id_proyecto_convocatoria'))
    observacion = Column(Text)
    calificacion = Column(Float(2,1))

    item_rubrica = relationship("Item_rubrica")
    rubrica_resultado = relationship("Rubrica_resultado")
    usuario = relationship("Usuario")
    proyecto_convocatoria = relationship("Proyecto_convocatoria")

