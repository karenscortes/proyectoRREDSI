from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text


# Consultar los evaluadores de un proyecto
def get_participantes_proyecto(db: Session, id_proyecto: int, id_rol: int):
    try:
        sql = text("""SELECT usuarios.id_usuario, usuarios.nombres, usuarios.apellidos, usuarios.id_rol
                        FROM participantes_proyecto 
                        JOIN proyectos ON participantes_proyecto.id_proyecto = proyectos.id_proyecto
                        JOIN usuarios ON participantes_proyecto.id_usuario = usuarios.id_usuario 
                        JOIN roles ON usuarios.id_rol = roles.id_rol
                        WHERE participantes_proyecto.id_proyecto = :id_p
                        AND usuarios.id_rol = :id_rol
                    """)
        result = db.execute(sql, {"id_p": id_proyecto, "id_rol": id_rol}).mappings().all()
        return result
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Participantes proyecto no encontrados")
    
#Consultar datos sala pertenecientes a un proyecto
def get_datos_sala(db: Session, id_proyecto:int):
    try:
        sql = text("""SELECT salas.numero_sala, detalle_sala.fecha,  detalle_sala.hora_inicio, detalle_sala.hora_fin
            FROM salas
            JOIN detalle_sala ON salas.id_sala = detalle_sala.id_sala
            JOIN proyectos_convocatoria ON detalle_sala.id_proyecto_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria
            JOIN proyectos ON proyectos_convocatoria.id_proyecto = proyectos.id_proyecto
            WHERE proyectos.id_proyecto = :id_proyecto;
        """)
        result = db.execute(sql, {"id_proyecto": id_proyecto}).mappings().first() 
        return result
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Datos de sala no encontrados")
    
# def get_suplentes_sala(db:Session):
#     try:
#         sql = text("""SELECT """)
#     except SQLAlchemyError as e:
#         raise HTTPException(status_code=500, detail="Datos de sala no encontrados")
    
    
#Insertar presentacion del proyecto
def get_insertar_presentacion_proyecto(db: Session, id_proyecto: int):
    try:
        sql = text("""INSERT INTO presentaciones_proyectos (id_presentacion, id_proyecto, url_presentacion)
                VALUES :id_pres, :id_proy, :url""") 
        params = {
            "id_proy" : id_proyecto    
        }
        result = db.execute(db, params)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al insertar url de presentación")