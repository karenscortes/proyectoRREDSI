from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.models.convocatoria import Convocatoria
from appv1.models.etapa import Etapa
from appv1.models.fase import Fase
from appv1.models.convocatoria import Tipo_de_convocatoria

# Crear una nueva convocatoria
def create_convocatoria(db: Session, nombre: str, fecha_inicio: date, fecha_fin: date, tipo_de_convocatoria: Tipo_de_convocatoria):
    convocatoria = Convocatoria(nombre=nombre, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, tipo_de_convocatoria=tipo_de_convocatoria)
    db.add(convocatoria)
    db.commit()
    return {"message": "Convocatoria creada exitosamente"}

# Crear una nueva etapa dentro de una convocatoria
def create_etapa(db: Session, nombre: str, id_convocatoria: int):
    etapa = Etapa(nombre=nombre)
    db.add(etapa)
    db.commit()
    return {"message": "Etapa creada exitosamente"}

# Crear una nueva fase dentro de una etapa
def create_fase(db: Session, nombre: str, id_etapa: int):
    fase = Fase(nombre=nombre, id_etapa=id_etapa)
    db.add(fase)
    db.commit()
    return {"message": "Fase creada exitosamente"}

# Traer fases por etapa
def get_fases_by_etapa(db: Session, id_etapa: int):
    fases = db.query(Fase).filter(Fase.id_etapa == id_etapa).all()
    if not fases:
        raise HTTPException(status_code=404, detail="Fases no encontradas para la etapa")
    return fases

# Editar una etapa
def update_etapa(db: Session, id_etapa: int, nombre: str = None):
    etapa = db.query(Etapa).get(id_etapa)
    if not etapa:
        raise HTTPException(status_code=404, detail="Etapa no encontrada")
    if nombre:
        etapa.nombre = nombre
    db.commit()
    return {"message": "Etapa actualizada exitosamente"}

# Editar una fase
def update_fase(db: Session, id_fase: int, nombre: str = None):
    fase = db.query(Fase).get(id_fase)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase no encontrada")
    if nombre:
        fase.nombre = nombre
    db.commit()
    return {"message": "Fase actualizada exitosamente"}

# Crear una nueva programación de fase
def create_programacion_fase(db: Session, id_fase: int, id_convocatoria: int, fecha_inicio: date, fecha_fin: date):
    programacion_fase = programacion_fase(id_fase=id_fase, id_convocatoria=id_convocatoria, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
    db.add(programacion_fase)
    db.commit()
    return {"message": "Programación de fase creada exitosamente"}