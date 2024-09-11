from datetime import date
from typing import Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.models.convocatoria import Convocatoria
from appv1.models.etapa import Etapa
from appv1.models.fase import Fase
from appv1.models.programacion_fase import Programacion_fase
from appv1.models.sala import Sala
from appv1.models.usuario import Usuario
from appv1.schemas.admin.admin import EstadoDeConvocatoria

# Crear una nueva convocatoria
def create_convocatoria(db: Session, nombre: str, fecha_inicio: date, fecha_fin: date, estado: EstadoDeConvocatoria):
    convocatoria = Convocatoria(nombre=nombre, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, estado=estado)
    db.add(convocatoria)
    db.commit()
    return {"message": "Convocatoria creada exitosamente"}

# Crear una nueva etapa dentro de una convocatoria
def create_etapa(db: Session, nombre: str, id_convocatoria: int):
    
    convocatoria = db.query(Convocatoria).get(id_convocatoria)
    if not convocatoria:
        raise HTTPException(status_code=404, detail="Convocatoria no encontrada")
    
    etapa = Etapa(nombre=nombre, id_convocatoria=id_convocatoria)
    
    db.add(etapa)
    db.commit()
    db.refresh(etapa)
    return {"message": "Etapa creada exitosamente", "etapa_id": etapa.id_etapa}


# Crear una nueva fase dentro de una etapa
def create_fase(db: Session, nombre: str, id_etapa: int):
    # Verifica que la etapa existe
    etapa = db.query(Etapa).get(id_etapa)
    if not etapa:
        raise HTTPException(status_code=404, detail="Etapa no encontrada")

    # Crea la nueva fase
    fase = Fase(nombre=nombre, id_etapa=id_etapa)
    
    # Añade y guarda en la base de datos
    db.add(fase)
    db.commit()
    db.refresh(fase)  # Refresca el objeto fase con el ID generado
    return {"message": "Fase creada exitosamente", "fase_id": fase.id_fase}

# Traer fases por etapa
def get_fases_by_etapa(db: Session, id_etapa: int):
    # Verifica que la etapa exista
    etapa = db.query(Etapa).get(id_etapa)
    if not etapa:
        raise HTTPException(status_code=404, detail="Etapa no encontrada")
    
    # Obtiene todas las fases asociadas a la etapa
    fases = db.query(Fase).filter(Fase.id_etapa == id_etapa).all()
    return fases


# Editar una etapa
def update_etapa(db: Session, id_etapa: int, nombre: Optional[str] = None):
    # Verifica que la etapa exista
    etapa = db.query(Etapa).get(id_etapa)
    if not etapa:
        raise HTTPException(status_code=404, detail="Etapa no encontrada")

    # Actualiza los campos que sean provistos
    if nombre:
        etapa.nombre = nombre

    # Guarda los cambios en la base de datos
    db.commit()
    db.refresh(etapa)
    return etapa


# Editar una fase
def update_fase(db: Session, id_fase: int, nombre: Optional[str] = None):
    # Verifica que la fase exista
    fase = db.query(Fase).get(id_fase)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase no encontrada")

    # Actualiza los campos que sean provistos
    if nombre:
        fase.nombre = nombre

    # Guarda los cambios en la base de datos
    db.commit()
    db.refresh(fase)
    return fase

# Crear una nueva programación de fase
def create_programacion_fase(db: Session, id_fase: int, id_convocatoria: int, fecha_inicio: date, fecha_fin: date):
    programacion_fase = Programacion_fase(id_fase=id_fase, id_convocatoria=id_convocatoria, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
    db.add(programacion_fase)
    db.commit()
    return {"message": "Programación de fase creada exitosamente"}

# Crear una nueva sala
def create_sala(db: Session, id_usuario: int, area_conocimiento: int,  numero: str, nombre: str):
    sala = Sala(id_usuario=id_usuario, id_area_conocimiento=area_conocimiento, numero_sala=numero, nombre_sala=nombre)
    db.add(sala)
    db.commit()
    return {"message": "Sala creada exitosamente"}
