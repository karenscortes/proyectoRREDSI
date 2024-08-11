from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from models.base_class import Base

class Respuesta_rubricas(Base):
    __tablename__ = 'respuestas_rubricas'
    id_respuestas_rubrica = Column(Integer, primary_key=True, autoincrement=True)
    id_item_rubrica = Column(Integer, ForeignKey('items_rubrica.id_item_rubrica'))
    id_rubrica_resultado = Column(Integer, ForeignKey('rubricas_resultados.id_rubrica_resultado'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_proyecto_convocatoria = Column(Integer, ForeignKey('proyectos_convocatoria.id_proyecto_convocatoria'))
    observacion = Column(Text)
    calificacion = Column(Float(2,1))

    item_rubrica = relationship("Item_rubrica")
    rubrica_resultado = relationship("Rubrica_resultado")
    usuario = relationship("Usuario")
    proyecto_convocatoria = relationship("Proyecto_convocatoria")
