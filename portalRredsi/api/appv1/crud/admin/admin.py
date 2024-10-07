from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from appv1.models.area_conocimiento import Area_conocimiento
from appv1.models.convocatoria import Convocatoria
from appv1.models.programacion_fase import Programacion_fase
from appv1.models.sala import Sala
from appv1.schemas.admin.admin import ConvocatoriaResponse, EstadoDeConvocatoria, ProgramacionFaseResponse, UpdateSala
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import text

from appv1.crud.evaluador.proyectos import get_current_convocatoria

# Crear una convocatoria que devuelva su id 
def create_convocatoria(db: Session, nombre: str, fecha_inicio: date, fecha_fin: date, estado: EstadoDeConvocatoria):
    convocatoria = Convocatoria(
        nombre=nombre, 
        fecha_inicio=fecha_inicio, 
        fecha_fin=fecha_fin, 
        estado=estado
    )
    db.add(convocatoria)
    db.commit()
    db.refresh(convocatoria)  # Refresca para obtener el ID generado
    
    return ConvocatoriaResponse(
        id_convocatoria=convocatoria.id_convocatoria,
        nombre=convocatoria.nombre,
        fecha_inicio=convocatoria.fecha_inicio,
        fecha_fin=convocatoria.fecha_fin,
        estado=convocatoria.estado
    )

# Verificar convocatorias activa
def existe_convocatoria_en_curso(db: Session) -> bool:
    return db.query(Convocatoria).filter(Convocatoria.estado == EstadoDeConvocatoria.en_curso).count() > 0


# Consulta directa a la base de datos usando SQL crudo
def obtener_convocatoria_en_curso(db: Session):
    sql = text("SELECT * FROM convocatorias WHERE estado = 'en curso'")
    result = db.execute(sql).fetchone()
    
    if result:
        # Acceder a los valores por índice en lugar de por nombre
        return ConvocatoriaResponse(
            id_convocatoria=result[0],  
            nombre=result[1],           
            fecha_inicio=result[2],     
            fecha_fin=result[3],        
            estado=result[4]            
        )
    else:
        return None

# Crear programación de varias fases
def create_multiple_programaciones_fases(db: Session, programaciones_fases: list):
    programaciones_creadas = []

    for programacion in programaciones_fases:
        programacion_fase = Programacion_fase(
            id_fase=programacion.id_fase,
            id_convocatoria=programacion.id_convocatoria,
            fecha_inicio=programacion.fecha_inicio,
            fecha_fin=programacion.fecha_fin
        )
        db.add(programacion_fase)
        db.commit()
        db.refresh(programacion_fase)

        # Agregar la programación creada a la lista
        programaciones_creadas.append(
            ProgramacionFaseResponse(
                id_programacion_fase=programacion_fase.id_programacion_fase,
                id_fase=programacion_fase.id_fase,
                id_convocatoria=programacion_fase.id_convocatoria,
                fecha_inicio=programacion_fase.fecha_inicio,
                fecha_fin=programacion_fase.fecha_fin
            )
        )
    
    return programaciones_creadas

# Función que obtiene la convocatoria en curso
def get_convocatoria_en_curso(db: Session):
    return db.query(Convocatoria).filter(Convocatoria.estado == "en_curso").first()


# Crear una nueva sala
def create_sala(db: Session, id_usuario: int, area_conocimiento: int,  numero: str, nombre: str):
    try:
        sala = Sala(
            id_usuario=id_usuario, 
            id_area_conocimiento=area_conocimiento, 
            id_convocatoria=get_current_convocatoria(db),
            numero_sala=numero, 
            nombre_sala=nombre
        )
        db.add(sala)
        db.commit()
        db.refresh(sala)
        return sala
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear la sala")
    except SQLAlchemyError as e:
        print(f"Error al crear el item: {e}")
        raise HTTPException(status_code=500, detail=f"Error. No hay Integridad de datos",)
    

# Editar una sala
def update_sala( id_sala: int, new_sala: UpdateSala,db: Session):

    try:
        # Verifica que la sala exista
        sala = db.query(Sala).get(id_sala)
        if not sala:
            raise HTTPException(status_code=404, detail="Sala no encontrada")

        # Si se proporciona un área de conocimiento, obtén el objeto correspondiente
        if new_sala.area_conocimento:  # Corregido
            area = db.query(Area_conocimiento).get(new_sala.area_conocimento)
            if not area:
                raise HTTPException(status_code=404, detail="Área de conocimiento no encontrada")
                sala.area_conocimiento = area

        # Actualiza otros campos si se proporcionan
        if new_sala.nombre_sala:
            sala.nombre_sala = new_sala.nombre_sala
        if new_sala.numero_sala:
            sala.numero_sala = new_sala.numero_sala
        if new_sala.id_usuario:
            sala.id_usuario = new_sala.id_usuario

        try:
            # Guarda los cambios en la base de datos
            db.commit()
            db.refresh(sala)
            return sala
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar sala")
 
    except SQLAlchemyError as e:
        print(f"Error al actualizar sala: {e}")
        raise HTTPException(status_code=500, detail=f"Error. No hay Integridad de datos",)
    


