# Crear un usuario
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.delegado.salas import AsignarProyectoSala

# ASIGNAR PROYECTO A SALA EN LA ETAPA PRESENCIAL 
def asignar_proyecto_a_sala(db: Session, asignacion: AsignarProyectoSala ):
    try:
        sql = text("""INSERT INTO detalle_sala (id_sala, id_proyecto_convocatoria, fecha, hora_inicio, hora_fin) 
                        VALUES (:id_sala, :id_proyecto_convocatoria, :fecha, :hora_inicio, :hora_fin)
                    """)
        
        params={
            "id_sala": asignacion.id_sala,
            "id_proyecto_convocatoria": asignacion.id_proyecto_convocatoria,
            "fecha": asignacion.fecha,
            "hora_inicio": asignacion.hora_inicio,
            "hora_fin": asignacion.hora_fin
        }
        result = db.execute(sql,params)
        db.commit()
        return result
    
    except IntegrityError as e:
        db.rollback()
        print(f"Error al asignar proyecto a sala: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID de proyecto ya esta asignado ")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al asignar proyecto")
        
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al asignar proyecto: {e}")
        raise HTTPException(status_code=500, detail="Error al asignar proyecto")
    
# OBTIENE LAS SALS QUE ESTEN REGISTRADAS EN UNA CONVOCATORIA ACTIVA 
def get_salas_por_convocatoria(db: Session, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        
        sql = text("""SELECT salas.*,areas_conocimiento.nombre AS nombre_area_conocimiento, usuarios.nombres AS nombres_delegado,usuarios.apellidos AS apellidos_delegado FROM salas
                        JOIN areas_conocimiento ON salas.id_area_conocimiento = areas_conocimiento.id_area_conocimiento
                        JOIN usuarios ON salas.id_usuario = usuarios.id_usuario
                        JOIN convocatorias ON salas.id_convocatoria = convocatorias.id_convocatoria 
                        WHERE convocatorias.estado = 'en curso' 
                        LIMIT :page_size OFFSET :offset 
                    """)
        
        params ={
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql,params).mappings().all()
        
        # Obtener el número total de usuarios
        count_sql = text("""SELECT COUNT(*) FROM salas 
                                JOIN convocatorias ON salas.id_convocatoria = convocatorias.id_convocatoria 
                                WHERE convocatorias.estado = 'en curso'
                            """)
        total_salas = db.execute(count_sql).scalar()

        # Calcular el número total de páginas
        total_pages = (total_salas + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al buscar salas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar salas")
    
# DETALLE DE UNA SALA POR ID
def get_detalle_sala(db: Session, id_sala: str):
    try:
        sql = text("SELECT * FROM detalle_sala WHERE id_sala = :id_sala")
        result = db.execute(sql, {"id_sala": id_sala}).fetchall()
        return result
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="La sala no se ha encontrado")

# VERIFICAR SI UNA SALA UN DELEGADO TIENE ASIGNADA UNA SALA
def verificar_sala_asignada(db: Session, id_usuario: int):
    try:
        sql = text("SELECT * FROM salas WHERE salas.id_usuario = :id_usuario")
        result = db.execute(sql, {"id_usuario": id_usuario}).fetchone()
        return result
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Delegado sin sala asignada")


# PROYECTOS SIN ASIGNAR EN LA ETAPA PRESENCIAL
def get_proyectos_sin_asignar_etapa_presencial(db: Session):
        try:

            sql = text(
            """
                    SELECT  DISTINCT proyectos.id_proyecto,
                                    proyectos.titulo,
                                    proyectos.id_institucion,
                                    areas_conocimiento.id_area_conocimiento
                    FROM proyectos
                            JOIN areas_conocimiento ON (proyectos.id_area_conocimiento = areas_conocimiento.id_area_conocimiento)
                            JOIN proyectos_convocatoria ON (proyectos.id_proyecto = proyectos_convocatoria.id_proyecto) 
                            JOIN participantes_proyecto ON (participantes_proyecto.id_proyectos_convocatoria = proyectos_convocatoria.id_proyecto_convocatoria)  
                            JOIN convocatorias ON (proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria)  
                            LEFT JOIN detalle_sala ON proyectos_convocatoria.id_proyecto_convocatoria = detalle_sala.id_proyecto_convocatoria     
                    WHERE proyectos.estado_asignacion= 'pendiente' 
                    AND convocatorias.estado = 'en curso' 
                    AND participantes_proyecto.id_etapa = 1
                    AND detalle_sala.id_proyecto_convocatoria IS NULL
            """
            )
            
            result = db.execute(sql).mappings().all()

            return result
        except SQLAlchemyError as e:
                print(f"Error al obtener proyectos no asignados: {e}")
                raise HTTPException(status_code=500, detail="Error al obtener todos los proyectos no asignados")

# Consultar los ponentes de un proyecto
def get_ponentes_proyecto(db: Session, id_proyecto: int):
    try:
        sql = text("""SELECT usuarios.id_usuario, usuarios.nombres, usuarios.apellidos 
                        FROM participantes_proyecto 
                        JOIN usuarios ON participantes_proyecto.id_usuario = usuarios.id_usuario  
                        WHERE participantes_proyecto.id_proyecto = :id_p
                        AND usuarios.id_rol NOT IN(1,2,3,4,6,7)
                    """)
        result = db.execute(sql, {"id_p": id_proyecto}).mappings().all()
        return result
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="La sala no se ha encontrado")

# CONSULTAR LOS POSIBLES EVALUADORES PARA UN PROYECTO EN ETAPA PRESENCIAL
def get_posibles_evaluadores_para_proyecto_etapa_presencial(db: Session, id_area_conocimiento: int, id_institucion: int):
    try:
    # Primera consulta que incluye las áreas de conocimiento
        sql_primaria = text("""
            SELECT postulaciones_evaluadores.*, usuarios.nombres AS nombre_evaluador, usuarios.apellidos AS apellidos_evaluador
            FROM postulaciones_evaluadores
            JOIN detalles_institucionales ON (postulaciones_evaluadores.id_evaluador = detalles_institucionales.id_usuario)
            JOIN usuarios ON detalles_institucionales.id_usuario = usuarios.id_usuario
            WHERE detalles_institucionales.id_institucion != :id_i 
            AND (detalles_institucionales.id_primera_area_conocimiento = :id_ac OR detalles_institucionales.id_segunda_area_conocimiento = :id_ac)
            AND (usuarios.id_rol = 1 OR usuarios.id_rol = 2)
            AND usuarios.estado = 'activo'
            AND postulaciones_evaluadores.estado_postulacion = 'aceptada'
            AND postulaciones_evaluadores.etapa_presencial = true
        """)
        
        params = {
            "id_ac": id_area_conocimiento, 
            "id_i": id_institucion
        }
        result = db.execute(sql_primaria, params).mappings().all()

        # Si la primera consulta no devuelve resultados, ejecutar la segunda sin áreas de conocimiento
        if not result:
            sql_secundaria = text("""
                SELECT postulaciones_evaluadores.*, usuarios.nombres AS nombre_evaluador, usuarios.apellidos AS apellidos_evaluador
                FROM postulaciones_evaluadores
                JOIN detalles_institucionales ON (postulaciones_evaluadores.id_evaluador = detalles_institucionales.id_usuario)
                JOIN usuarios ON detalles_institucionales.id_usuario = usuarios.id_usuario
                WHERE detalles_institucionales.id_institucion != :id_i
                AND (usuarios.id_rol = 1 OR usuarios.id_rol = 2)
                AND usuarios.estado = 'activo'
                AND postulaciones_evaluadores.estado_postulacion = 'aceptada'
                AND postulaciones_evaluadores.etapa_presencial = true
            """)
            # Ejecutar consulta secundaria sin filtrar por áreas de conocimiento
            result = db.execute(sql_secundaria, {"id_i": id_institucion}).mappings().all()
        
        return result
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar evaluadores")
        raise HTTPException(status_code=204, detail="Error al buscar evaluadores")
